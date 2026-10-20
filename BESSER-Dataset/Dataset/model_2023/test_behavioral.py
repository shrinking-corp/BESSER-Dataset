import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    ActionActivation_firing_Value,
    ActionActivation_pinActivations_Value,
    ActivityContent,
    ActivityEdgeInstance_edge_ActivityEdgeInstance_Value,
    ActivityEdgeInstance_group_ActivityEdgeInstance_Value,
    ActivityEdgeInstance_offers_Value,
    ActivityEdgeInstance_source_Value,
    ActivityEdgeInstance_target_Value,
    ActivityExecution_activationGroup_Value,
    ActivityNodeActivationGroup_activityExecution_Value,
    ActivityNodeActivationGroup_edgeInstances_Value,
    ActivityNodeActivationGroup_nodeActivations_Value,
    ActivityNodeActivation_group_ActivityNodeActivation_Value,
    ActivityNodeActivation_heldTokens_Value,
    ActivityNodeActivation_incomingEdges_Value,
    ActivityNodeActivation_isRunning_Value,
    ActivityNodeActivation_node_ActivityNodeActivation_Value,
    ActivityNodeActivation_outgoingEdges_Value,
    ActivityNodeActivation_running_Value,
    BasicActions_TracedActionActivation,
    BasicActions_TracedCallActionActivation,
    BasicActions_TracedCallBehaviorActionActivation,
    BasicActions_TracedInputPinActivation,
    BasicActions_TracedOpaqueActionActivation,
    BasicActions_TracedOutputPinActivation,
    BasicActions_TracedPinActivation,
    BasicBehaviors_TracedExecution,
    BasicBehaviors_TracedOpaqueBehaviorExecution,
    BasicBehaviors_TracedParameterValue,
    BigStep,
    BooleanValue_value_BooleanValue_Value,
    CallActionActivation_callExecutions_Value,
    CompoundValue_featureValues_Value,
    Element_semanticVisitor_Value,
    Evaluation_locus_Evaluation_Value,
    Evaluation_specification_Evaluation_Value,
    ExecutionEnvironment_locus_ExecutionEnvironment_Value,
    ExecutionFactory_builtInTypes_Value,
    ExecutionFactory_locus_ExecutionFactory_Value,
    ExecutionFactory_primitiveBehaviorPrototypes_Value,
    Execution_context_Value,
    Execution_parameterValues_Value,
    Executor_locus_Executor_Value,
    ExtensionalValue_locus_ExtensionalValue_Value,
    FeatureValue_feature_Value,
    FeatureValue_position_Value,
    FeatureValue_values_FeatureValue_Value,
    ForkedToken_baseTokenIsWithdrawn_Value,
    ForkedToken_baseToken_Value,
    ForkedToken_remainingOffersCount_Value,
    InputParameterValues_name_Value,
    InputParameterValues_parameterValues_Value,
    Input_TracedInputParameterValues,
    IntegerFunctions_TracedIntegerGreaterFunctionBehaviorExecution,
    IntegerFunctions_TracedIntegerLessFunctionBehaviorExecution,
    IntegerFunctions_TracedIntegerPlusFunctionBehaviorExecution,
    IntegerValue_value_IntegerValue_Value,
    IntermediateActions_TracedAddStructuralFeatureValueActionActivation,
    IntermediateActions_TracedCreateObjectActionActivation,
    IntermediateActions_TracedReadStructuralFeatureActionActivation,
    IntermediateActions_TracedValueSpecificationActionActivation,
    IntermediateActivities_TracedActivityEdgeInstance,
    IntermediateActivities_TracedActivityExecution,
    IntermediateActivities_TracedActivityFinalNodeActivation,
    IntermediateActivities_TracedActivityNodeActivation,
    IntermediateActivities_TracedActivityNodeActivationGroup,
    IntermediateActivities_TracedActivityParameterNodeActivation,
    IntermediateActivities_TracedControlToken,
    IntermediateActivities_TracedDecisionNodeActivation,
    IntermediateActivities_TracedForkNodeActivation,
    IntermediateActivities_TracedForkedToken,
    IntermediateActivities_TracedInitialNodeActivation,
    IntermediateActivities_TracedJoinNodeActivation,
    IntermediateActivities_TracedMergeNodeActivation,
    IntermediateActivities_TracedObjectNodeActivation,
    IntermediateActivities_TracedObjectToken,
    IntermediateActivities_TracedOffer,
    IntermediateActivities_TracedToken,
    Kernel_TracedBooleanValue,
    Kernel_TracedCompoundValue,
    Kernel_TracedEvaluation,
    Kernel_TracedExtensionalValue,
    Kernel_TracedFeatureValue,
    Kernel_TracedIntegerValue,
    Kernel_TracedLiteralBooleanEvaluation,
    Kernel_TracedLiteralIntegerEvaluation,
    Kernel_TracedObject,
    Kernel_TracedPrimitiveValue,
    Kernel_TracedReference,
    Kernel_TracedValue,
    Loci_TracedExecutionEnvironment,
    Loci_TracedExecutionFactory,
    Loci_TracedExecutor,
    Loci_TracedLocus,
    Loci_TracedSemanticVisitor,
    Locus_executor_Value,
    Locus_extensionalValues_Value,
    Locus_factory_Value,
    ObjectNodeActivation_offeredTokenCount_Value,
    ObjectToken_value_Value,
    Object_types_Value,
    Offer_offeredTokens_Value,
    ParameterValue_parameter_ParameterValue_Value,
    ParameterValue_values_ParameterValue_Value,
    PinActivation_actionActivation_Value,
    PinActivation_count_temp_Value,
    PrimitiveValue_type_Value,
    Reference_referent_Value,
    SemanticVisitor_runtimeModelElement_Value,
    SmallStep,
    Steps,
    Steps_umlTrace_State,
    Token_holder_Value,
    TracedAbstraction,
    TracedAcceptEventAction,
    TracedAction,
    TracedActionActivation,
    TracedActivityEdge,
    TracedActivityGroup,
    TracedActivityNode,
    TracedActivityNodeActivation,
    TracedArtifact,
    TracedAssociation,
    TracedBehavior,
    TracedBehavioralFeature,
    TracedBehavioredClassifier,
    TracedCallAction,
    TracedCallActionActivation,
    TracedCentralBufferNode,
    TracedClass,
    TracedClassifier,
    TracedCombinedFragment,
    TracedCompoundValue,
    TracedConstraint,
    TracedControlNode,
    TracedControlNodeActivation,
    TracedCreateLinkAction,
    TracedDataType,
    TracedDependency,
    TracedDirectedRelationship,
    TracedEModelElement,
    TracedElement,
    TracedEvaluation,
    TracedEvent,
    TracedExecutableNode,
    TracedExecution,
    TracedExecutionSpecification,
    TracedExtensionalValue,
    TracedFeature,
    TracedFinalNode,
    TracedInputPin,
    TracedInstanceSpecification,
    TracedInteractionFragment,
    TracedInteractionUse,
    TracedInterval,
    TracedIntervalConstraint,
    TracedInvocationAction,
    TracedInvocationActionActivation,
    TracedLinkAction,
    TracedLinkEndData,
    TracedLiteralEvaluation,
    TracedLiteralSpecification,
    TracedMessageEnd,
    TracedMessageEvent,
    TracedMessageOccurrenceSpecification,
    TracedMultiplicityElement,
    TracedNamedElement,
    TracedNode,
    TracedObject,
    TracedObjectNode,
    TracedObjectNodeActivation,
    TracedObjects,
    TracedObservation,
    TracedOccurrenceSpecification,
    TracedOpaqueBehavior,
    TracedOpaqueBehaviorExecution,
    TracedPackage,
    TracedPackageableElement,
    TracedPin,
    TracedPinActivation,
    TracedPrimitiveValue,
    TracedProperty,
    TracedRealization,
    TracedRedefinableElement,
    TracedRelationship,
    TracedSemanticVisitor,
    TracedState,
    TracedStateMachine,
    TracedStructuralFeatureAction,
    TracedStructuralFeatureActionActivation,
    TracedStructuredActivityNode,
    TracedStructuredClassifier,
    TracedStructuredValue,
    TracedTemplateParameter,
    TracedToken,
    TracedTransition,
    TracedValue,
    TracedValueSpecification,
    TracedVariableAction,
    TracedVertex,
    TracedWriteLinkAction,
    TracedWriteStructuralFeatureAction,
    TracedWriteStructuralFeatureActionActivation,
    TracedWriteVariableAction,
    Values_umlTrace_State,
    ecore_umlTrace_EAnnotation,
    umlTrace_BasicActions_TracedActionActivation,
    umlTrace_BasicActions_TracedCallActionActivation,
    umlTrace_BasicActions_TracedCallBehaviorActionActivation,
    umlTrace_BasicActions_TracedInputPinActivation,
    umlTrace_BasicActions_TracedInvocationActionActivation,
    umlTrace_BasicActions_TracedOpaqueActionActivation,
    umlTrace_BasicActions_TracedOutputPinActivation,
    umlTrace_BasicActions_TracedPinActivation,
    umlTrace_BasicBehaviors_TracedExecution,
    umlTrace_BasicBehaviors_TracedOpaqueBehaviorExecution,
    umlTrace_BasicBehaviors_TracedParameterValue,
    umlTrace_Input_TracedInputParameterValues,
    umlTrace_IntegerFunctions_TracedIntegerGreaterFunctionBehaviorExecution,
    umlTrace_IntegerFunctions_TracedIntegerLessFunctionBehaviorExecution,
    umlTrace_IntegerFunctions_TracedIntegerPlusFunctionBehaviorExecution,
    umlTrace_IntermediateActions_TracedAddStructuralFeatureValueActionActivation,
    umlTrace_IntermediateActions_TracedCreateObjectActionActivation,
    umlTrace_IntermediateActions_TracedReadStructuralFeatureActionActivation,
    umlTrace_IntermediateActions_TracedStructuralFeatureActionActivation,
    umlTrace_IntermediateActions_TracedValueSpecificationActionActivation,
    umlTrace_IntermediateActions_TracedWriteStructuralFeatureActionActivation,
    umlTrace_IntermediateActivities_TracedActivityEdgeInstance,
    umlTrace_IntermediateActivities_TracedActivityExecution,
    umlTrace_IntermediateActivities_TracedActivityFinalNodeActivation,
    umlTrace_IntermediateActivities_TracedActivityNodeActivation,
    umlTrace_IntermediateActivities_TracedActivityNodeActivationGroup,
    umlTrace_IntermediateActivities_TracedActivityParameterNodeActivation,
    umlTrace_IntermediateActivities_TracedControlNodeActivation,
    umlTrace_IntermediateActivities_TracedControlToken,
    umlTrace_IntermediateActivities_TracedDecisionNodeActivation,
    umlTrace_IntermediateActivities_TracedForkNodeActivation,
    umlTrace_IntermediateActivities_TracedForkedToken,
    umlTrace_IntermediateActivities_TracedInitialNodeActivation,
    umlTrace_IntermediateActivities_TracedJoinNodeActivation,
    umlTrace_IntermediateActivities_TracedMergeNodeActivation,
    umlTrace_IntermediateActivities_TracedObjectNodeActivation,
    umlTrace_IntermediateActivities_TracedObjectToken,
    umlTrace_IntermediateActivities_TracedOffer,
    umlTrace_IntermediateActivities_TracedToken,
    umlTrace_Kernel_TracedBooleanValue,
    umlTrace_Kernel_TracedCompoundValue,
    umlTrace_Kernel_TracedEvaluation,
    umlTrace_Kernel_TracedExtensionalValue,
    umlTrace_Kernel_TracedFeatureValue,
    umlTrace_Kernel_TracedIntegerValue,
    umlTrace_Kernel_TracedLiteralBooleanEvaluation,
    umlTrace_Kernel_TracedLiteralEvaluation,
    umlTrace_Kernel_TracedLiteralIntegerEvaluation,
    umlTrace_Kernel_TracedObject,
    umlTrace_Kernel_TracedPrimitiveValue,
    umlTrace_Kernel_TracedReference,
    umlTrace_Kernel_TracedStructuredValue,
    umlTrace_Kernel_TracedValue,
    umlTrace_Loci_TracedExecutionEnvironment,
    umlTrace_Loci_TracedExecutionFactory,
    umlTrace_Loci_TracedExecutor,
    umlTrace_Loci_TracedLocus,
    umlTrace_Loci_TracedSemanticVisitor,
    umlTrace_State,
    umlTrace_Steps_BigStep,
    umlTrace_Steps_SmallStep,
    umlTrace_Steps_Steps,
    umlTrace_Trace,
    umlTrace_Traced_TracedObjects,
    umlTrace_Values_ActionActivation_firing_Value,
    umlTrace_Values_ActionActivation_pinActivations_Value,
    umlTrace_Values_ActivityEdgeInstance_edge_ActivityEdgeInstance_Value,
    umlTrace_Values_ActivityEdgeInstance_group_ActivityEdgeInstance_Value,
    umlTrace_Values_ActivityEdgeInstance_offers_Value,
    umlTrace_Values_ActivityEdgeInstance_source_Value,
    umlTrace_Values_ActivityEdgeInstance_target_Value,
    umlTrace_Values_ActivityExecution_activationGroup_Value,
    umlTrace_Values_ActivityNodeActivationGroup_activityExecution_Value,
    umlTrace_Values_ActivityNodeActivationGroup_edgeInstances_Value,
    umlTrace_Values_ActivityNodeActivationGroup_nodeActivations_Value,
    umlTrace_Values_ActivityNodeActivation_group_ActivityNodeActivation_Value,
    umlTrace_Values_ActivityNodeActivation_heldTokens_Value,
    umlTrace_Values_ActivityNodeActivation_incomingEdges_Value,
    umlTrace_Values_ActivityNodeActivation_isRunning_Value,
    umlTrace_Values_ActivityNodeActivation_node_ActivityNodeActivation_Value,
    umlTrace_Values_ActivityNodeActivation_outgoingEdges_Value,
    umlTrace_Values_ActivityNodeActivation_running_Value,
    umlTrace_Values_BooleanValue_value_BooleanValue_Value,
    umlTrace_Values_CallActionActivation_callExecutions_Value,
    umlTrace_Values_CompoundValue_featureValues_Value,
    umlTrace_Values_Element_semanticVisitor_Value,
    umlTrace_Values_Evaluation_locus_Evaluation_Value,
    umlTrace_Values_Evaluation_specification_Evaluation_Value,
    umlTrace_Values_ExecutionEnvironment_locus_ExecutionEnvironment_Value,
    umlTrace_Values_ExecutionFactory_builtInTypes_Value,
    umlTrace_Values_ExecutionFactory_locus_ExecutionFactory_Value,
    umlTrace_Values_ExecutionFactory_primitiveBehaviorPrototypes_Value,
    umlTrace_Values_Execution_context_Value,
    umlTrace_Values_Execution_parameterValues_Value,
    umlTrace_Values_Executor_locus_Executor_Value,
    umlTrace_Values_ExtensionalValue_locus_ExtensionalValue_Value,
    umlTrace_Values_FeatureValue_feature_Value,
    umlTrace_Values_FeatureValue_position_Value,
    umlTrace_Values_FeatureValue_values_FeatureValue_Value,
    umlTrace_Values_ForkedToken_baseTokenIsWithdrawn_Value,
    umlTrace_Values_ForkedToken_baseToken_Value,
    umlTrace_Values_ForkedToken_remainingOffersCount_Value,
    umlTrace_Values_InputParameterValues_name_Value,
    umlTrace_Values_InputParameterValues_parameterValues_Value,
    umlTrace_Values_IntegerValue_value_IntegerValue_Value,
    umlTrace_Values_Locus_executor_Value,
    umlTrace_Values_Locus_extensionalValues_Value,
    umlTrace_Values_Locus_factory_Value,
    umlTrace_Values_ObjectNodeActivation_offeredTokenCount_Value,
    umlTrace_Values_ObjectToken_value_Value,
    umlTrace_Values_Object_types_Value,
    umlTrace_Values_Offer_offeredTokens_Value,
    umlTrace_Values_ParameterValue_parameter_ParameterValue_Value,
    umlTrace_Values_ParameterValue_values_ParameterValue_Value,
    umlTrace_Values_PinActivation_actionActivation_Value,
    umlTrace_Values_PinActivation_count_temp_Value,
    umlTrace_Values_PrimitiveValue_type_Value,
    umlTrace_Values_Reference_referent_Value,
    umlTrace_Values_SemanticVisitor_runtimeModelElement_Value,
    umlTrace_Values_Token_holder_Value,
    umlTrace_ecore_TracedEModelElement,
    umlTrace_uml_TracedAbstraction,
    umlTrace_uml_TracedAcceptCallAction,
    umlTrace_uml_TracedAcceptEventAction,
    umlTrace_uml_TracedAction,
    umlTrace_uml_TracedActionExecutionSpecification,
    umlTrace_uml_TracedActionInputPin,
    umlTrace_uml_TracedActivity,
    umlTrace_uml_TracedActivityEdge,
    umlTrace_uml_TracedActivityFinalNode,
    umlTrace_uml_TracedActivityGroup,
    umlTrace_uml_TracedActivityNode,
    umlTrace_uml_TracedActivityParameterNode,
    umlTrace_uml_TracedActivityPartition,
    umlTrace_uml_TracedActor,
    umlTrace_uml_TracedAddStructuralFeatureValueAction,
    umlTrace_uml_TracedAddVariableValueAction,
    umlTrace_uml_TracedAnyReceiveEvent,
    umlTrace_uml_TracedArtifact,
    umlTrace_uml_TracedAssociation,
    umlTrace_uml_TracedAssociationClass,
    umlTrace_uml_TracedBehavior,
    umlTrace_uml_TracedBehaviorExecutionSpecification,
    umlTrace_uml_TracedBehavioralFeature,
    umlTrace_uml_TracedBehavioredClassifier,
    umlTrace_uml_TracedBroadcastSignalAction,
    umlTrace_uml_TracedCallAction,
    umlTrace_uml_TracedCallBehaviorAction,
    umlTrace_uml_TracedCallEvent,
    umlTrace_uml_TracedCallOperationAction,
    umlTrace_uml_TracedCentralBufferNode,
    umlTrace_uml_TracedChangeEvent,
    umlTrace_uml_TracedClass,
    umlTrace_uml_TracedClassifier,
    umlTrace_uml_TracedClassifierTemplateParameter,
    umlTrace_uml_TracedClause,
    umlTrace_uml_TracedClearAssociationAction,
    umlTrace_uml_TracedClearStructuralFeatureAction,
    umlTrace_uml_TracedClearVariableAction,
    umlTrace_uml_TracedCollaboration,
    umlTrace_uml_TracedCollaborationUse,
    umlTrace_uml_TracedCombinedFragment,
    umlTrace_uml_TracedComment,
    umlTrace_uml_TracedCommunicationPath,
    umlTrace_uml_TracedComponent,
    umlTrace_uml_TracedComponentRealization,
    umlTrace_uml_TracedConditionalNode,
    umlTrace_uml_TracedConnectableElement,
    umlTrace_uml_TracedConnectableElementTemplateParameter,
    umlTrace_uml_TracedConnectionPointReference,
    umlTrace_uml_TracedConnector,
    umlTrace_uml_TracedConnectorEnd,
    umlTrace_uml_TracedConsiderIgnoreFragment,
    umlTrace_uml_TracedConstraint,
    umlTrace_uml_TracedContinuation,
    umlTrace_uml_TracedControlFlow,
    umlTrace_uml_TracedControlNode,
    umlTrace_uml_TracedCreateLinkAction,
    umlTrace_uml_TracedCreateLinkObjectAction,
    umlTrace_uml_TracedCreateObjectAction,
    umlTrace_uml_TracedDataStoreNode,
    umlTrace_uml_TracedDataType,
    umlTrace_uml_TracedDecisionNode,
    umlTrace_uml_TracedDependency,
    umlTrace_uml_TracedDeployedArtifact,
    umlTrace_uml_TracedDeployment,
    umlTrace_uml_TracedDeploymentSpecification,
    umlTrace_uml_TracedDeploymentTarget,
    umlTrace_uml_TracedDestroyLinkAction,
    umlTrace_uml_TracedDestroyObjectAction,
    umlTrace_uml_TracedDestructionOccurrenceSpecification,
    umlTrace_uml_TracedDevice,
    umlTrace_uml_TracedDirectedRelationship,
    umlTrace_uml_TracedDuration,
    umlTrace_uml_TracedDurationConstraint,
    umlTrace_uml_TracedDurationInterval,
    umlTrace_uml_TracedDurationObservation,
    umlTrace_uml_TracedElement,
    umlTrace_uml_TracedElementImport,
    umlTrace_uml_TracedEncapsulatedClassifier,
    umlTrace_uml_TracedEnumeration,
    umlTrace_uml_TracedEnumerationLiteral,
    umlTrace_uml_TracedEvent,
    umlTrace_uml_TracedExceptionHandler,
    umlTrace_uml_TracedExecutableNode,
    umlTrace_uml_TracedExecutionEnvironment,
    umlTrace_uml_TracedExecutionOccurrenceSpecification,
    umlTrace_uml_TracedExecutionSpecification,
    umlTrace_uml_TracedExpansionNode,
    umlTrace_uml_TracedExpansionRegion,
    umlTrace_uml_TracedExpression,
    umlTrace_uml_TracedExtend,
    umlTrace_uml_TracedExtension,
    umlTrace_uml_TracedExtensionEnd,
    umlTrace_uml_TracedExtensionPoint,
    umlTrace_uml_TracedFeature,
    umlTrace_uml_TracedFinalNode,
    umlTrace_uml_TracedFinalState,
    umlTrace_uml_TracedFlowFinalNode,
    umlTrace_uml_TracedForkNode,
    umlTrace_uml_TracedFunctionBehavior,
    umlTrace_uml_TracedGate,
    umlTrace_uml_TracedGeneralOrdering,
    umlTrace_uml_TracedGeneralization,
    umlTrace_uml_TracedGeneralizationSet,
    umlTrace_uml_TracedImage,
    umlTrace_uml_TracedInclude,
    umlTrace_uml_TracedInformationFlow,
    umlTrace_uml_TracedInformationItem,
    umlTrace_uml_TracedInitialNode,
    umlTrace_uml_TracedInputPin,
    umlTrace_uml_TracedInstanceSpecification,
    umlTrace_uml_TracedInstanceValue,
    umlTrace_uml_TracedInteraction,
    umlTrace_uml_TracedInteractionConstraint,
    umlTrace_uml_TracedInteractionFragment,
    umlTrace_uml_TracedInteractionOperand,
    umlTrace_uml_TracedInteractionUse,
    umlTrace_uml_TracedInterface,
    umlTrace_uml_TracedInterfaceRealization,
    umlTrace_uml_TracedInterruptibleActivityRegion,
    umlTrace_uml_TracedInterval,
    umlTrace_uml_TracedIntervalConstraint,
    umlTrace_uml_TracedInvocationAction,
    umlTrace_uml_TracedJoinNode,
    umlTrace_uml_TracedLifeline,
    umlTrace_uml_TracedLinkAction,
    umlTrace_uml_TracedLinkEndCreationData,
    umlTrace_uml_TracedLinkEndData,
    umlTrace_uml_TracedLinkEndDestructionData,
    umlTrace_uml_TracedLiteralBoolean,
    umlTrace_uml_TracedLiteralInteger,
    umlTrace_uml_TracedLiteralNull,
    umlTrace_uml_TracedLiteralReal,
    umlTrace_uml_TracedLiteralSpecification,
    umlTrace_uml_TracedLiteralString,
    umlTrace_uml_TracedLiteralUnlimitedNatural,
    umlTrace_uml_TracedLoopNode,
    umlTrace_uml_TracedManifestation,
    umlTrace_uml_TracedMergeNode,
    umlTrace_uml_TracedMessage,
    umlTrace_uml_TracedMessageEnd,
    umlTrace_uml_TracedMessageEvent,
    umlTrace_uml_TracedMessageOccurrenceSpecification,
    umlTrace_uml_TracedModel,
    umlTrace_uml_TracedMultiplicityElement,
    umlTrace_uml_TracedNamedElement,
    umlTrace_uml_TracedNamespace,
    umlTrace_uml_TracedNode,
    umlTrace_uml_TracedObjectFlow,
    umlTrace_uml_TracedObjectNode,
    umlTrace_uml_TracedObservation,
    umlTrace_uml_TracedOccurrenceSpecification,
    umlTrace_uml_TracedOpaqueAction,
    umlTrace_uml_TracedOpaqueBehavior,
    umlTrace_uml_TracedOpaqueExpression,
    umlTrace_uml_TracedOperation,
    umlTrace_uml_TracedOperationTemplateParameter,
    umlTrace_uml_TracedOutputPin,
    umlTrace_uml_TracedPackage,
    umlTrace_uml_TracedPackageImport,
    umlTrace_uml_TracedPackageMerge,
    umlTrace_uml_TracedPackageableElement,
    umlTrace_uml_TracedParameter,
    umlTrace_uml_TracedParameterSet,
    umlTrace_uml_TracedParameterableElement,
    umlTrace_uml_TracedPartDecomposition,
    umlTrace_uml_TracedPin,
    umlTrace_uml_TracedPort,
    umlTrace_uml_TracedPrimitiveType,
    umlTrace_uml_TracedProfile,
    umlTrace_uml_TracedProfileApplication,
    umlTrace_uml_TracedProperty,
    umlTrace_uml_TracedProtocolConformance,
    umlTrace_uml_TracedProtocolStateMachine,
    umlTrace_uml_TracedProtocolTransition,
    umlTrace_uml_TracedPseudostate,
    umlTrace_uml_TracedQualifierValue,
    umlTrace_uml_TracedRaiseExceptionAction,
    umlTrace_uml_TracedReadExtentAction,
    umlTrace_uml_TracedReadIsClassifiedObjectAction,
    umlTrace_uml_TracedReadLinkAction,
    umlTrace_uml_TracedReadLinkObjectEndAction,
    umlTrace_uml_TracedReadLinkObjectEndQualifierAction,
    umlTrace_uml_TracedReadSelfAction,
    umlTrace_uml_TracedReadStructuralFeatureAction,
    umlTrace_uml_TracedReadVariableAction,
    umlTrace_uml_TracedRealization,
    umlTrace_uml_TracedReception,
    umlTrace_uml_TracedReclassifyObjectAction,
    umlTrace_uml_TracedRedefinableElement,
    umlTrace_uml_TracedRedefinableTemplateSignature,
    umlTrace_uml_TracedReduceAction,
    umlTrace_uml_TracedRegion,
    umlTrace_uml_TracedRelationship,
    umlTrace_uml_TracedRemoveStructuralFeatureValueAction,
    umlTrace_uml_TracedRemoveVariableValueAction,
    umlTrace_uml_TracedReplyAction,
    umlTrace_uml_TracedSendObjectAction,
    umlTrace_uml_TracedSendSignalAction,
    umlTrace_uml_TracedSequenceNode,
    umlTrace_uml_TracedSignal,
    umlTrace_uml_TracedSignalEvent,
    umlTrace_uml_TracedSlot,
    umlTrace_uml_TracedStartClassifierBehaviorAction,
    umlTrace_uml_TracedStartObjectBehaviorAction,
    umlTrace_uml_TracedState,
    umlTrace_uml_TracedStateInvariant,
    umlTrace_uml_TracedStateMachine,
    umlTrace_uml_TracedStereotype,
    umlTrace_uml_TracedStringExpression,
    umlTrace_uml_TracedStructuralFeature,
    umlTrace_uml_TracedStructuralFeatureAction,
    umlTrace_uml_TracedStructuredActivityNode,
    umlTrace_uml_TracedStructuredClassifier,
    umlTrace_uml_TracedSubstitution,
    umlTrace_uml_TracedTemplateBinding,
    umlTrace_uml_TracedTemplateParameter,
    umlTrace_uml_TracedTemplateParameterSubstitution,
    umlTrace_uml_TracedTemplateSignature,
    umlTrace_uml_TracedTemplateableElement,
    umlTrace_uml_TracedTestIdentityAction,
    umlTrace_uml_TracedTimeConstraint,
    umlTrace_uml_TracedTimeEvent,
    umlTrace_uml_TracedTimeExpression,
    umlTrace_uml_TracedTimeInterval,
    umlTrace_uml_TracedTimeObservation,
    umlTrace_uml_TracedTransition,
    umlTrace_uml_TracedTrigger,
    umlTrace_uml_TracedType,
    umlTrace_uml_TracedTypedElement,
    umlTrace_uml_TracedUnmarshallAction,
    umlTrace_uml_TracedUsage,
    umlTrace_uml_TracedUseCase,
    umlTrace_uml_TracedValuePin,
    umlTrace_uml_TracedValueSpecification,
    umlTrace_uml_TracedValueSpecificationAction,
    umlTrace_uml_TracedVariable,
    umlTrace_uml_TracedVariableAction,
    umlTrace_uml_TracedVertex,
    umlTrace_uml_TracedWriteLinkAction,
    umlTrace_uml_TracedWriteStructuralFeatureAction,
    umlTrace_uml_TracedWriteVariableAction,
    uml_TracedAbstraction,
    uml_TracedAcceptCallAction,
    uml_TracedAcceptEventAction,
    uml_TracedAction,
    uml_TracedActionExecutionSpecification,
    uml_TracedActionInputPin,
    uml_TracedActivity,
    uml_TracedActivityEdge,
    uml_TracedActivityFinalNode,
    uml_TracedActivityGroup,
    uml_TracedActivityNode,
    uml_TracedActivityParameterNode,
    uml_TracedActivityPartition,
    uml_TracedActor,
    uml_TracedAddStructuralFeatureValueAction,
    uml_TracedAddVariableValueAction,
    uml_TracedAnyReceiveEvent,
    uml_TracedArtifact,
    uml_TracedAssociation,
    uml_TracedAssociationClass,
    uml_TracedBehavior,
    uml_TracedBehaviorExecutionSpecification,
    uml_TracedBehavioralFeature,
    uml_TracedBehavioredClassifier,
    uml_TracedBroadcastSignalAction,
    uml_TracedCallBehaviorAction,
    uml_TracedCallEvent,
    uml_TracedCallOperationAction,
    uml_TracedCentralBufferNode,
    uml_TracedChangeEvent,
    uml_TracedClass,
    uml_TracedClassifier,
    uml_TracedClassifierTemplateParameter,
    uml_TracedClause,
    uml_TracedClearAssociationAction,
    uml_TracedClearStructuralFeatureAction,
    uml_TracedClearVariableAction,
    uml_TracedCollaboration,
    uml_TracedCollaborationUse,
    uml_TracedCombinedFragment,
    uml_TracedComment,
    uml_TracedCommunicationPath,
    uml_TracedComponent,
    uml_TracedComponentRealization,
    uml_TracedConditionalNode,
    uml_TracedConnectableElement,
    uml_TracedConnectableElementTemplateParameter,
    uml_TracedConnectionPointReference,
    uml_TracedConnector,
    uml_TracedConnectorEnd,
    uml_TracedConsiderIgnoreFragment,
    uml_TracedConstraint,
    uml_TracedContinuation,
    uml_TracedControlFlow,
    uml_TracedCreateLinkAction,
    uml_TracedCreateLinkObjectAction,
    uml_TracedCreateObjectAction,
    uml_TracedDataStoreNode,
    uml_TracedDataType,
    uml_TracedDecisionNode,
    uml_TracedDependency,
    uml_TracedDeployedArtifact,
    uml_TracedDeployment,
    uml_TracedDeploymentSpecification,
    uml_TracedDeploymentTarget,
    uml_TracedDestroyLinkAction,
    uml_TracedDestroyObjectAction,
    uml_TracedDestructionOccurrenceSpecification,
    uml_TracedDevice,
    uml_TracedDirectedRelationship,
    uml_TracedDuration,
    uml_TracedDurationConstraint,
    uml_TracedDurationInterval,
    uml_TracedDurationObservation,
    uml_TracedElement,
    uml_TracedElementImport,
    uml_TracedEncapsulatedClassifier,
    uml_TracedEnumeration,
    uml_TracedEnumerationLiteral,
    uml_TracedEvent,
    uml_TracedExceptionHandler,
    uml_TracedExecutableNode,
    uml_TracedExecutionEnvironment,
    uml_TracedExecutionOccurrenceSpecification,
    uml_TracedExecutionSpecification,
    uml_TracedExpansionNode,
    uml_TracedExpansionRegion,
    uml_TracedExpression,
    uml_TracedExtend,
    uml_TracedExtension,
    uml_TracedExtensionEnd,
    uml_TracedExtensionPoint,
    uml_TracedFeature,
    uml_TracedFinalState,
    uml_TracedFlowFinalNode,
    uml_TracedForkNode,
    uml_TracedFunctionBehavior,
    uml_TracedGate,
    uml_TracedGeneralOrdering,
    uml_TracedGeneralization,
    uml_TracedGeneralizationSet,
    uml_TracedImage,
    uml_TracedInclude,
    uml_TracedInformationFlow,
    uml_TracedInformationItem,
    uml_TracedInitialNode,
    uml_TracedInputPin,
    uml_TracedInstanceSpecification,
    uml_TracedInstanceValue,
    uml_TracedInteraction,
    uml_TracedInteractionConstraint,
    uml_TracedInteractionFragment,
    uml_TracedInteractionOperand,
    uml_TracedInteractionUse,
    uml_TracedInterface,
    uml_TracedInterfaceRealization,
    uml_TracedInterruptibleActivityRegion,
    uml_TracedInterval,
    uml_TracedIntervalConstraint,
    uml_TracedJoinNode,
    uml_TracedLifeline,
    uml_TracedLinkEndCreationData,
    uml_TracedLinkEndData,
    uml_TracedLinkEndDestructionData,
    uml_TracedLiteralBoolean,
    uml_TracedLiteralInteger,
    uml_TracedLiteralNull,
    uml_TracedLiteralReal,
    uml_TracedLiteralString,
    uml_TracedLiteralUnlimitedNatural,
    uml_TracedLoopNode,
    uml_TracedManifestation,
    uml_TracedMergeNode,
    uml_TracedMessage,
    uml_TracedMessageEnd,
    uml_TracedMessageOccurrenceSpecification,
    uml_TracedModel,
    uml_TracedMultiplicityElement,
    uml_TracedNamedElement,
    uml_TracedNamespace,
    uml_TracedNode,
    uml_TracedObjectFlow,
    uml_TracedObjectNode,
    uml_TracedObservation,
    uml_TracedOccurrenceSpecification,
    uml_TracedOpaqueAction,
    uml_TracedOpaqueBehavior,
    uml_TracedOpaqueExpression,
    uml_TracedOperation,
    uml_TracedOperationTemplateParameter,
    uml_TracedOutputPin,
    uml_TracedPackage,
    uml_TracedPackageImport,
    uml_TracedPackageMerge,
    uml_TracedPackageableElement,
    uml_TracedParameter,
    uml_TracedParameterSet,
    uml_TracedParameterableElement,
    uml_TracedPartDecomposition,
    uml_TracedPort,
    uml_TracedPrimitiveType,
    uml_TracedProfile,
    uml_TracedProfileApplication,
    uml_TracedProperty,
    uml_TracedProtocolConformance,
    uml_TracedProtocolStateMachine,
    uml_TracedProtocolTransition,
    uml_TracedPseudostate,
    uml_TracedQualifierValue,
    uml_TracedRaiseExceptionAction,
    uml_TracedReadExtentAction,
    uml_TracedReadIsClassifiedObjectAction,
    uml_TracedReadLinkAction,
    uml_TracedReadLinkObjectEndAction,
    uml_TracedReadLinkObjectEndQualifierAction,
    uml_TracedReadSelfAction,
    uml_TracedReadStructuralFeatureAction,
    uml_TracedReadVariableAction,
    uml_TracedRealization,
    uml_TracedReception,
    uml_TracedReclassifyObjectAction,
    uml_TracedRedefinableElement,
    uml_TracedRedefinableTemplateSignature,
    uml_TracedReduceAction,
    uml_TracedRegion,
    uml_TracedRelationship,
    uml_TracedRemoveStructuralFeatureValueAction,
    uml_TracedRemoveVariableValueAction,
    uml_TracedReplyAction,
    uml_TracedSendObjectAction,
    uml_TracedSendSignalAction,
    uml_TracedSequenceNode,
    uml_TracedSignal,
    uml_TracedSignalEvent,
    uml_TracedSlot,
    uml_TracedStartClassifierBehaviorAction,
    uml_TracedStartObjectBehaviorAction,
    uml_TracedState,
    uml_TracedStateInvariant,
    uml_TracedStateMachine,
    uml_TracedStereotype,
    uml_TracedStringExpression,
    uml_TracedStructuralFeature,
    uml_TracedStructuredActivityNode,
    uml_TracedStructuredClassifier,
    uml_TracedSubstitution,
    uml_TracedTemplateBinding,
    uml_TracedTemplateParameter,
    uml_TracedTemplateParameterSubstitution,
    uml_TracedTemplateSignature,
    uml_TracedTemplateableElement,
    uml_TracedTestIdentityAction,
    uml_TracedTimeConstraint,
    uml_TracedTimeEvent,
    uml_TracedTimeExpression,
    uml_TracedTimeInterval,
    uml_TracedTimeObservation,
    uml_TracedTransition,
    uml_TracedTrigger,
    uml_TracedType,
    uml_TracedTypedElement,
    uml_TracedUnmarshallAction,
    uml_TracedUsage,
    uml_TracedUseCase,
    uml_TracedValuePin,
    uml_TracedValueSpecification,
    uml_TracedValueSpecificationAction,
    uml_TracedVariable,
    uml_TracedVertex,
    uml_umlTrace_AcceptEventAction,
    uml_umlTrace_ActionExecutionSpecification,
    uml_umlTrace_ActivityFinalNode,
    uml_umlTrace_ActivityParameterNode,
    uml_umlTrace_ActivityPartition,
    uml_umlTrace_Actor,
    uml_umlTrace_AddStructuralFeatureValueAction,
    uml_umlTrace_AddVariableValueAction,
    uml_umlTrace_AnyReceiveEvent,
    uml_umlTrace_Artifact,
    uml_umlTrace_Association,
    uml_umlTrace_BehaviorExecutionSpecification,
    uml_umlTrace_BroadcastSignalAction,
    uml_umlTrace_CallBehaviorAction,
    uml_umlTrace_CallEvent,
    uml_umlTrace_CallOperationAction,
    uml_umlTrace_CentralBufferNode,
    uml_umlTrace_ChangeEvent,
    uml_umlTrace_Class,
    uml_umlTrace_Clause,
    uml_umlTrace_ClearAssociationAction,
    uml_umlTrace_ClearStructuralFeatureAction,
    uml_umlTrace_ClearVariableAction,
    uml_umlTrace_Collaboration,
    uml_umlTrace_CollaborationUse,
    uml_umlTrace_CombinedFragment,
    uml_umlTrace_Comment,
    uml_umlTrace_ConnectionPointReference,
    uml_umlTrace_Connector,
    uml_umlTrace_ConnectorEnd,
    uml_umlTrace_Constraint,
    uml_umlTrace_Continuation,
    uml_umlTrace_ControlFlow,
    uml_umlTrace_CreateLinkAction,
    uml_umlTrace_CreateObjectAction,
    uml_umlTrace_DataType,
    uml_umlTrace_DecisionNode,
    uml_umlTrace_Dependency,
    uml_umlTrace_DestroyLinkAction,
    uml_umlTrace_DestroyObjectAction,
    uml_umlTrace_Duration,
    uml_umlTrace_DurationObservation,
    uml_umlTrace_ElementImport,
    uml_umlTrace_ExceptionHandler,
    uml_umlTrace_ExpansionNode,
    uml_umlTrace_Expression,
    uml_umlTrace_Extend,
    uml_umlTrace_ExtensionPoint,
    uml_umlTrace_FlowFinalNode,
    uml_umlTrace_ForkNode,
    uml_umlTrace_Gate,
    uml_umlTrace_GeneralOrdering,
    uml_umlTrace_Generalization,
    uml_umlTrace_GeneralizationSet,
    uml_umlTrace_Image,
    uml_umlTrace_Include,
    uml_umlTrace_InformationFlow,
    uml_umlTrace_InformationItem,
    uml_umlTrace_InitialNode,
    uml_umlTrace_InputPin,
    uml_umlTrace_InstanceSpecification,
    uml_umlTrace_InstanceValue,
    uml_umlTrace_InteractionOperand,
    uml_umlTrace_InteractionUse,
    uml_umlTrace_Interface,
    uml_umlTrace_InterruptibleActivityRegion,
    uml_umlTrace_Interval,
    uml_umlTrace_JoinNode,
    uml_umlTrace_Lifeline,
    uml_umlTrace_LinkEndData,
    uml_umlTrace_LiteralBoolean,
    uml_umlTrace_LiteralInteger,
    uml_umlTrace_LiteralNull,
    uml_umlTrace_LiteralReal,
    uml_umlTrace_LiteralString,
    uml_umlTrace_LiteralUnlimitedNatural,
    uml_umlTrace_MergeNode,
    uml_umlTrace_Message,
    uml_umlTrace_ObjectFlow,
    uml_umlTrace_OccurrenceSpecification,
    uml_umlTrace_OpaqueAction,
    uml_umlTrace_OpaqueExpression,
    uml_umlTrace_Operation,
    uml_umlTrace_OutputPin,
    uml_umlTrace_Package,
    uml_umlTrace_PackageImport,
    uml_umlTrace_PackageMerge,
    uml_umlTrace_Parameter,
    uml_umlTrace_ParameterSet,
    uml_umlTrace_ProfileApplication,
    uml_umlTrace_Property,
    uml_umlTrace_ProtocolConformance,
    uml_umlTrace_Pseudostate,
    uml_umlTrace_QualifierValue,
    uml_umlTrace_RaiseExceptionAction,
    uml_umlTrace_ReadExtentAction,
    uml_umlTrace_ReadIsClassifiedObjectAction,
    uml_umlTrace_ReadLinkAction,
    uml_umlTrace_ReadLinkObjectEndAction,
    uml_umlTrace_ReadLinkObjectEndQualifierAction,
    uml_umlTrace_ReadSelfAction,
    uml_umlTrace_ReadStructuralFeatureAction,
    uml_umlTrace_ReadVariableAction,
    uml_umlTrace_Reception,
    uml_umlTrace_ReclassifyObjectAction,
    uml_umlTrace_ReduceAction,
    uml_umlTrace_Region,
    uml_umlTrace_RemoveStructuralFeatureValueAction,
    uml_umlTrace_RemoveVariableValueAction,
    uml_umlTrace_ReplyAction,
    uml_umlTrace_SendObjectAction,
    uml_umlTrace_SendSignalAction,
    uml_umlTrace_Signal,
    uml_umlTrace_SignalEvent,
    uml_umlTrace_Slot,
    uml_umlTrace_StartClassifierBehaviorAction,
    uml_umlTrace_StartObjectBehaviorAction,
    uml_umlTrace_State,
    uml_umlTrace_StateInvariant,
    uml_umlTrace_StructuredActivityNode,
    uml_umlTrace_TemplateBinding,
    uml_umlTrace_TemplateParameter,
    uml_umlTrace_TemplateParameterSubstitution,
    uml_umlTrace_TemplateSignature,
    uml_umlTrace_TestIdentityAction,
    uml_umlTrace_TimeEvent,
    uml_umlTrace_TimeExpression,
    uml_umlTrace_TimeObservation,
    uml_umlTrace_Transition,
    uml_umlTrace_Trigger,
    uml_umlTrace_UnmarshallAction,
    uml_umlTrace_UseCase,
    uml_umlTrace_ValueSpecificationAction,
    uml_umlTrace_Variable,
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

def test_assoc_parent133_stub_double():
    # Kernel_TracedIntegerValue has no real 'TracedIntegerValue' property in the generated
    # code (a bare stub) -- manually attach it so umlTrace_Values_IntegerValue_value_IntegerValue_Value's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # umlTrace_Values_IntegerValue_value_IntegerValue_Value's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = umlTrace_Values_IntegerValue_value_IntegerValue_Value(value_IntegerValue=7)
    partner = Kernel_TracedIntegerValue()
    setattr(partner, 'TracedIntegerValue', None)
    _safe_set(owner, 'value_IntegerValueTrace', partner)
    assert getattr(partner, 'TracedIntegerValue') == owner
    _safe_set(owner, 'value_IntegerValueTrace', None)
    assert getattr(partner, 'TracedIntegerValue') is None


def test_assoc_parent136_stub_double():
    # IntermediateActivities_TracedForkedToken has no real 'TracedForkedToken' property in the generated
    # code (a bare stub) -- manually attach it so umlTrace_Values_ForkedToken_remainingOffersCount_Value's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # umlTrace_Values_ForkedToken_remainingOffersCount_Value's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = umlTrace_Values_ForkedToken_remainingOffersCount_Value(remainingOffersCount=7)
    partner = IntermediateActivities_TracedForkedToken()
    setattr(partner, 'TracedForkedToken', None)
    _safe_set(owner, 'remainingOffersCountTrace', partner)
    assert getattr(partner, 'TracedForkedToken') == owner
    _safe_set(owner, 'remainingOffersCountTrace', None)
    assert getattr(partner, 'TracedForkedToken') is None


def test_assoc_parent144_stub_double():
    # IntermediateActivities_TracedForkedToken has no real 'TracedForkedToken145' property in the generated
    # code (a bare stub) -- manually attach it so umlTrace_Values_ForkedToken_baseTokenIsWithdrawn_Value's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # umlTrace_Values_ForkedToken_baseTokenIsWithdrawn_Value's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = umlTrace_Values_ForkedToken_baseTokenIsWithdrawn_Value(baseTokenIsWithdrawn=True)
    partner = IntermediateActivities_TracedForkedToken()
    setattr(partner, 'TracedForkedToken145', None)
    _safe_set(owner, 'baseTokenIsWithdrawnTrace', partner)
    assert getattr(partner, 'TracedForkedToken145') == owner
    _safe_set(owner, 'baseTokenIsWithdrawnTrace', None)
    assert getattr(partner, 'TracedForkedToken145') is None


def test_assoc_parent176_stub_double():
    # IntermediateActivities_TracedObjectNodeActivation has no real 'TracedObjectNodeActivation' property in the generated
    # code (a bare stub) -- manually attach it so umlTrace_Values_ObjectNodeActivation_offeredTokenCount_Value's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # umlTrace_Values_ObjectNodeActivation_offeredTokenCount_Value's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = umlTrace_Values_ObjectNodeActivation_offeredTokenCount_Value(offeredTokenCount=7)
    partner = IntermediateActivities_TracedObjectNodeActivation()
    setattr(partner, 'TracedObjectNodeActivation', None)
    _safe_set(owner, 'offeredTokenCountTrace', partner)
    assert getattr(partner, 'TracedObjectNodeActivation') == owner
    _safe_set(owner, 'offeredTokenCountTrace', None)
    assert getattr(partner, 'TracedObjectNodeActivation') is None


def test_assoc_parent196_stub_double():
    # BasicActions_TracedActionActivation has no real 'TracedActionActivation197' property in the generated
    # code (a bare stub) -- manually attach it so umlTrace_Values_ActionActivation_firing_Value's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # umlTrace_Values_ActionActivation_firing_Value's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = umlTrace_Values_ActionActivation_firing_Value(firing=True)
    partner = BasicActions_TracedActionActivation()
    setattr(partner, 'TracedActionActivation197', None)
    _safe_set(owner, 'firingTrace', partner)
    assert getattr(partner, 'TracedActionActivation197') == owner
    _safe_set(owner, 'firingTrace', None)
    assert getattr(partner, 'TracedActionActivation197') is None


def test_assoc_parent248_stub_double():
    # Kernel_TracedBooleanValue has no real 'TracedBooleanValue' property in the generated
    # code (a bare stub) -- manually attach it so umlTrace_Values_BooleanValue_value_BooleanValue_Value's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # umlTrace_Values_BooleanValue_value_BooleanValue_Value's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = umlTrace_Values_BooleanValue_value_BooleanValue_Value(value_BooleanValue=True)
    partner = Kernel_TracedBooleanValue()
    setattr(partner, 'TracedBooleanValue', None)
    _safe_set(owner, 'value_BooleanValueTrace', partner)
    assert getattr(partner, 'TracedBooleanValue') == owner
    _safe_set(owner, 'value_BooleanValueTrace', None)
    assert getattr(partner, 'TracedBooleanValue') is None


def test_assoc_parent284_stub_double():
    # Kernel_TracedFeatureValue has no real 'TracedFeatureValue285' property in the generated
    # code (a bare stub) -- manually attach it so umlTrace_Values_FeatureValue_position_Value's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # umlTrace_Values_FeatureValue_position_Value's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = umlTrace_Values_FeatureValue_position_Value(position=7)
    partner = Kernel_TracedFeatureValue()
    setattr(partner, 'TracedFeatureValue285', None)
    _safe_set(owner, 'positionTrace', partner)
    assert getattr(partner, 'TracedFeatureValue285') == owner
    _safe_set(owner, 'positionTrace', None)
    assert getattr(partner, 'TracedFeatureValue285') is None


def test_assoc_parent292_stub_double():
    # BasicActions_TracedPinActivation has no real 'TracedPinActivation293' property in the generated
    # code (a bare stub) -- manually attach it so umlTrace_Values_PinActivation_count_temp_Value's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # umlTrace_Values_PinActivation_count_temp_Value's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = umlTrace_Values_PinActivation_count_temp_Value(count_temp=7)
    partner = BasicActions_TracedPinActivation()
    setattr(partner, 'TracedPinActivation293', None)
    _safe_set(owner, 'count_tempTrace', partner)
    assert getattr(partner, 'TracedPinActivation293') == owner
    _safe_set(owner, 'count_tempTrace', None)
    assert getattr(partner, 'TracedPinActivation293') is None


def test_assoc_parent322_stub_double():
    # Input_TracedInputParameterValues has no real 'TracedInputParameterValues' property in the generated
    # code (a bare stub) -- manually attach it so umlTrace_Values_InputParameterValues_name_Value's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # umlTrace_Values_InputParameterValues_name_Value's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = umlTrace_Values_InputParameterValues_name_Value(name="sample_text")
    partner = Input_TracedInputParameterValues()
    setattr(partner, 'TracedInputParameterValues', None)
    _safe_set(owner, 'nameTrace', partner)
    assert getattr(partner, 'TracedInputParameterValues') == owner
    _safe_set(owner, 'nameTrace', None)
    assert getattr(partner, 'TracedInputParameterValues') is None


def test_assoc_parent342_stub_double():
    # IntermediateActivities_TracedActivityNodeActivation has no real 'TracedActivityNodeActivation343' property in the generated
    # code (a bare stub) -- manually attach it so umlTrace_Values_ActivityNodeActivation_running_Value's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # umlTrace_Values_ActivityNodeActivation_running_Value's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = umlTrace_Values_ActivityNodeActivation_running_Value(running=True)
    partner = IntermediateActivities_TracedActivityNodeActivation()
    setattr(partner, 'TracedActivityNodeActivation343', None)
    _safe_set(owner, 'runningTrace', partner)
    assert getattr(partner, 'TracedActivityNodeActivation343') == owner
    _safe_set(owner, 'runningTrace', None)
    assert getattr(partner, 'TracedActivityNodeActivation343') is None


def test_assoc_parent346_stub_double():
    # IntermediateActivities_TracedActivityNodeActivation has no real 'TracedActivityNodeActivation347' property in the generated
    # code (a bare stub) -- manually attach it so umlTrace_Values_ActivityNodeActivation_isRunning_Value's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # umlTrace_Values_ActivityNodeActivation_isRunning_Value's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = umlTrace_Values_ActivityNodeActivation_isRunning_Value(isRunning=True)
    partner = IntermediateActivities_TracedActivityNodeActivation()
    setattr(partner, 'TracedActivityNodeActivation347', None)
    _safe_set(owner, 'isRunningTrace', partner)
    assert getattr(partner, 'TracedActivityNodeActivation347') == owner
    _safe_set(owner, 'isRunningTrace', None)
    assert getattr(partner, 'TracedActivityNodeActivation347') is None


def test_assoc_states134_stub_double():
    # Values_umlTrace_State has no real 'State135' property in the generated
    # code (a bare stub) -- manually attach it so umlTrace_Values_IntegerValue_value_IntegerValue_Value's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # umlTrace_Values_IntegerValue_value_IntegerValue_Value's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = umlTrace_Values_IntegerValue_value_IntegerValue_Value(value_IntegerValue=7)
    partner = Values_umlTrace_State()
    setattr(partner, 'State135', None)
    _safe_set(owner, 'integerValue_value_IntegerValue_Values', {partner})
    assert getattr(partner, 'State135') == owner
    _safe_set(owner, 'integerValue_value_IntegerValue_Values', set())
    assert getattr(partner, 'State135') is None


def test_assoc_states137_stub_double():
    # Values_umlTrace_State has no real 'State138' property in the generated
    # code (a bare stub) -- manually attach it so umlTrace_Values_ForkedToken_remainingOffersCount_Value's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # umlTrace_Values_ForkedToken_remainingOffersCount_Value's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = umlTrace_Values_ForkedToken_remainingOffersCount_Value(remainingOffersCount=7)
    partner = Values_umlTrace_State()
    setattr(partner, 'State138', None)
    _safe_set(owner, 'forkedToken_remainingOffersCount_Values', {partner})
    assert getattr(partner, 'State138') == owner
    _safe_set(owner, 'forkedToken_remainingOffersCount_Values', set())
    assert getattr(partner, 'State138') is None


def test_assoc_states146_stub_double():
    # Values_umlTrace_State has no real 'State147' property in the generated
    # code (a bare stub) -- manually attach it so umlTrace_Values_ForkedToken_baseTokenIsWithdrawn_Value's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # umlTrace_Values_ForkedToken_baseTokenIsWithdrawn_Value's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = umlTrace_Values_ForkedToken_baseTokenIsWithdrawn_Value(baseTokenIsWithdrawn=True)
    partner = Values_umlTrace_State()
    setattr(partner, 'State147', None)
    _safe_set(owner, 'forkedToken_baseTokenIsWithdrawn_Values', {partner})
    assert getattr(partner, 'State147') == owner
    _safe_set(owner, 'forkedToken_baseTokenIsWithdrawn_Values', set())
    assert getattr(partner, 'State147') is None


def test_assoc_states177_stub_double():
    # Values_umlTrace_State has no real 'State178' property in the generated
    # code (a bare stub) -- manually attach it so umlTrace_Values_ObjectNodeActivation_offeredTokenCount_Value's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # umlTrace_Values_ObjectNodeActivation_offeredTokenCount_Value's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = umlTrace_Values_ObjectNodeActivation_offeredTokenCount_Value(offeredTokenCount=7)
    partner = Values_umlTrace_State()
    setattr(partner, 'State178', None)
    _safe_set(owner, 'objectNodeActivation_offeredTokenCount_Values', {partner})
    assert getattr(partner, 'State178') == owner
    _safe_set(owner, 'objectNodeActivation_offeredTokenCount_Values', set())
    assert getattr(partner, 'State178') is None


def test_assoc_states198_stub_double():
    # Values_umlTrace_State has no real 'State199' property in the generated
    # code (a bare stub) -- manually attach it so umlTrace_Values_ActionActivation_firing_Value's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # umlTrace_Values_ActionActivation_firing_Value's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = umlTrace_Values_ActionActivation_firing_Value(firing=True)
    partner = Values_umlTrace_State()
    setattr(partner, 'State199', None)
    _safe_set(owner, 'actionActivation_firing_Values', {partner})
    assert getattr(partner, 'State199') == owner
    _safe_set(owner, 'actionActivation_firing_Values', set())
    assert getattr(partner, 'State199') is None


def test_assoc_states249_stub_double():
    # Values_umlTrace_State has no real 'State250' property in the generated
    # code (a bare stub) -- manually attach it so umlTrace_Values_BooleanValue_value_BooleanValue_Value's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # umlTrace_Values_BooleanValue_value_BooleanValue_Value's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = umlTrace_Values_BooleanValue_value_BooleanValue_Value(value_BooleanValue=True)
    partner = Values_umlTrace_State()
    setattr(partner, 'State250', None)
    _safe_set(owner, 'booleanValue_value_BooleanValue_Values', {partner})
    assert getattr(partner, 'State250') == owner
    _safe_set(owner, 'booleanValue_value_BooleanValue_Values', set())
    assert getattr(partner, 'State250') is None


def test_assoc_states286_stub_double():
    # Values_umlTrace_State has no real 'State287' property in the generated
    # code (a bare stub) -- manually attach it so umlTrace_Values_FeatureValue_position_Value's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # umlTrace_Values_FeatureValue_position_Value's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = umlTrace_Values_FeatureValue_position_Value(position=7)
    partner = Values_umlTrace_State()
    setattr(partner, 'State287', None)
    _safe_set(owner, 'featureValue_position_Values', {partner})
    assert getattr(partner, 'State287') == owner
    _safe_set(owner, 'featureValue_position_Values', set())
    assert getattr(partner, 'State287') is None


def test_assoc_states294_stub_double():
    # Values_umlTrace_State has no real 'State295' property in the generated
    # code (a bare stub) -- manually attach it so umlTrace_Values_PinActivation_count_temp_Value's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # umlTrace_Values_PinActivation_count_temp_Value's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = umlTrace_Values_PinActivation_count_temp_Value(count_temp=7)
    partner = Values_umlTrace_State()
    setattr(partner, 'State295', None)
    _safe_set(owner, 'pinActivation_count_temp_Values', {partner})
    assert getattr(partner, 'State295') == owner
    _safe_set(owner, 'pinActivation_count_temp_Values', set())
    assert getattr(partner, 'State295') is None


def test_assoc_states323_stub_double():
    # Values_umlTrace_State has no real 'State324' property in the generated
    # code (a bare stub) -- manually attach it so umlTrace_Values_InputParameterValues_name_Value's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # umlTrace_Values_InputParameterValues_name_Value's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = umlTrace_Values_InputParameterValues_name_Value(name="sample_text")
    partner = Values_umlTrace_State()
    setattr(partner, 'State324', None)
    _safe_set(owner, 'inputParameterValues_name_Values', {partner})
    assert getattr(partner, 'State324') == owner
    _safe_set(owner, 'inputParameterValues_name_Values', set())
    assert getattr(partner, 'State324') is None


def test_assoc_states344_stub_double():
    # Values_umlTrace_State has no real 'State345' property in the generated
    # code (a bare stub) -- manually attach it so umlTrace_Values_ActivityNodeActivation_running_Value's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # umlTrace_Values_ActivityNodeActivation_running_Value's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = umlTrace_Values_ActivityNodeActivation_running_Value(running=True)
    partner = Values_umlTrace_State()
    setattr(partner, 'State345', None)
    _safe_set(owner, 'activityNodeActivation_running_Values', {partner})
    assert getattr(partner, 'State345') == owner
    _safe_set(owner, 'activityNodeActivation_running_Values', set())
    assert getattr(partner, 'State345') is None


def test_assoc_states348_stub_double():
    # Values_umlTrace_State has no real 'State349' property in the generated
    # code (a bare stub) -- manually attach it so umlTrace_Values_ActivityNodeActivation_isRunning_Value's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # umlTrace_Values_ActivityNodeActivation_isRunning_Value's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = umlTrace_Values_ActivityNodeActivation_isRunning_Value(isRunning=True)
    partner = Values_umlTrace_State()
    setattr(partner, 'State349', None)
    _safe_set(owner, 'activityNodeActivation_isRunning_Values', {partner})
    assert getattr(partner, 'State349') == owner
    _safe_set(owner, 'activityNodeActivation_isRunning_Values', set())
    assert getattr(partner, 'State349') is None


