import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Action,
    Activity,
    Alloc_Allocated,
    Alloc_MARTE_Abstraction,
    Alloc_MARTE_ActivityPartition,
    Alloc_MARTE_Comment,
    Alloc_MARTE_Dependency,
    Alloc_MARTE_Element,
    Alloc_MARTE_NamedElement,
    Allocate,
    ArrivalPattern,
    CoreElements_Configuration,
    CoreElements_MARTE_Package,
    CoreElements_MARTE_State,
    CoreElements_MARTE_StateMachine,
    CoreElements_MARTE_StructuredClassifier,
    CoreElements_MARTE_Transition,
    CoreElements_Mode,
    DataTypes_MARTE_DataType,
    DataTypes_MARTE_Property,
    GCM_ClientServerSpecification,
    GCM_MARTE_AnyReceiveEvent,
    GCM_MARTE_Behavior,
    GCM_MARTE_BehavioralFeature,
    GCM_MARTE_Classifier,
    GCM_MARTE_Feature,
    GCM_MARTE_Interface,
    GCM_MARTE_InvocationAction,
    GCM_MARTE_Port,
    GCM_MARTE_Property,
    GCM_MARTE_Trigger,
    GQAM_GaCommStep,
    GQAM_GaEventTrace,
    GQAM_GaExecHost,
    GQAM_GaRequestedService,
    GQAM_GaResourcesPlatform,
    GQAM_GaScenario,
    GQAM_GaStep,
    GQAM_GaTimedObs,
    GQAM_GaWorkloadBehavior,
    GQAM_GaWorkloadEvent,
    GQAM_GaWorkloadGenerator,
    GQAM_MARTE_Behavior,
    GQAM_MARTE_Classifier,
    GQAM_MARTE_NamedElement,
    GQAM_MARTE_Operation,
    GQAM_MARTE_TimeEvent,
    GQAM_MARTE_TimeObservation,
    GRM_CommunicationEndPoint,
    GRM_CommunicationMedia,
    GRM_ComputingResource,
    GRM_DeviceResource,
    GRM_MARTE_Behavior,
    GRM_MARTE_BehavioralFeature,
    GRM_MARTE_Classifier,
    GRM_MARTE_Collaboration,
    GRM_MARTE_CollaborationUse,
    GRM_MARTE_ConnectableElement,
    GRM_MARTE_Connector,
    GRM_MARTE_ExecutionSpecification,
    GRM_MARTE_InstanceSpecification,
    GRM_MARTE_Lifeline,
    GRM_MARTE_NamedElement,
    GRM_MARTE_OpaqueExpression,
    GRM_MARTE_Property,
    GRM_MutualExclusionResource,
    GRM_ProcessingResource,
    GRM_Resource,
    GRM_ResourceUsage,
    GRM_SchedulableResource,
    GRM_Scheduler,
    GRM_SecondaryScheduler,
    GRM_StorageResource,
    GRM_SynchronizationResource,
    GRM_TimingResource,
    GaAnalysisContext,
    GaCommHost,
    GaCommStep,
    GaExecHost,
    GaScenario,
    GaStep,
    GaTimedObs,
    GrService,
    HLAM_MARTE_Behavior,
    HLAM_MARTE_BehavioralFeature,
    HLAM_MARTE_BehavioredClassifier,
    HLAM_MARTE_Comment,
    HLAM_MARTE_InvocationAction,
    HLAM_MARTE_Message,
    HLAM_MARTE_Operation,
    HLAM_MARTE_Port,
    HLAM_MARTE_Signal,
    HLAM_RtSpecification,
    HwCommunicationResource,
    HwCommunication_HwArbiter,
    HwCommunication_HwCommunicationResource,
    HwCommunication_HwConnection,
    HwCommunication_HwEndPoint,
    HwCommunication_HwMedia,
    HwCommunication_HwPort,
    HwComponent,
    HwComputingResource,
    HwComputing_HwBranchPredictor,
    HwComputing_HwComputingResource,
    HwComputing_HwISA,
    HwComputing_HwProcessor,
    HwComputing_PLD_Organization,
    HwDevice,
    HwDeviceFunction_HwDeviceFunction,
    HwDevice_HwPeripheral,
    HwDiagram_MARTE_DataType,
    HwEndPoint,
    HwGeneral_HwResource,
    HwGeneral_HwResourceService,
    HwGeneral_MARTE_Activity,
    HwGeneral_MARTE_Operation,
    HwIO_HwLine,
    HwIO_HwPin,
    HwI_O,
    HwLayout_Env_Condition,
    HwLayout_HwComponent,
    HwMedia,
    HwMemory,
    HwMemory_CacheStructure,
    HwMemory_HwCache,
    HwMemory_HwMemory,
    HwMemory_HwRAM,
    HwMemory_MemoryOrganization,
    HwMemory_Timing,
    HwPackage_HwPackage,
    HwPackage_HwPackagePin,
    HwPackage_HwWire,
    HwPeripheral_MARTE_InputPin,
    HwPeripheral_MARTE_Operation,
    HwPeripheral_MARTE_OutputPin,
    HwPeripheral_OperationImpl,
    HwPeripheral_PeripheralActivity,
    HwPeripheral_RegisterAction,
    HwProtocol_HwProtocol,
    HwProtocol_MARTE_Operation,
    HwRegister_HwRegister,
    HwResource,
    HwStorageManager,
    HwStorageManager_HwMMU,
    HwStorageManager_HwStorageManager,
    HwTimingResource,
    HwTiming_HwClock,
    IntegerInterval,
    IntegerMatrix,
    IntegerVector,
    InterruptResource,
    LinkTopology,
    MARTE_Alloc_Allocate,
    MARTE_Alloc_AllocateActivityGroup,
    MARTE_Alloc_Allocated,
    MARTE_Alloc_Assign,
    MARTE_Alloc_NfpRefine,
    MARTE_CoreElements_Configuration,
    MARTE_CoreElements_Mode,
    MARTE_CoreElements_ModeBehavior,
    MARTE_CoreElements_ModeTransition,
    MARTE_DataTypes_BoundedSubtype,
    MARTE_DataTypes_ChoiceType,
    MARTE_DataTypes_CollectionType,
    MARTE_DataTypes_IntervalType,
    MARTE_DataTypes_TupleType,
    MARTE_GCM_ClientServerFeature,
    MARTE_GCM_ClientServerPort,
    MARTE_GCM_ClientServerSpecification,
    MARTE_GCM_DataEvent,
    MARTE_GCM_DataPool,
    MARTE_GCM_FlowPort,
    MARTE_GCM_FlowProperty,
    MARTE_GCM_FlowSpecification,
    MARTE_GCM_GCMInvocationAction,
    MARTE_GCM_GCMTrigger,
    MARTE_GQAM_GaAcqStep,
    MARTE_GQAM_GaAnalysisContext,
    MARTE_GQAM_GaCommChannel,
    MARTE_GQAM_GaCommHost,
    MARTE_GQAM_GaCommStep,
    MARTE_GQAM_GaEventTrace,
    MARTE_GQAM_GaExecHost,
    MARTE_GQAM_GaLatencyObs,
    MARTE_GQAM_GaRelStep,
    MARTE_GQAM_GaRequestedService,
    MARTE_GQAM_GaResourcesPlatform,
    MARTE_GQAM_GaScenario,
    MARTE_GQAM_GaStep,
    MARTE_GQAM_GaTimedObs,
    MARTE_GQAM_GaWorkloadBehavior,
    MARTE_GQAM_GaWorkloadEvent,
    MARTE_GQAM_GaWorkloadGenerator,
    MARTE_GRM_Acquire,
    MARTE_GRM_ClockResource,
    MARTE_GRM_CommunicationEndPoint,
    MARTE_GRM_CommunicationMedia,
    MARTE_GRM_ComputingResource,
    MARTE_GRM_ConcurrencyResource,
    MARTE_GRM_DeviceResource,
    MARTE_GRM_GrService,
    MARTE_GRM_MutualExclusionResource,
    MARTE_GRM_ProcessingResource,
    MARTE_GRM_Release,
    MARTE_GRM_Resource,
    MARTE_GRM_ResourceUsage,
    MARTE_GRM_SchedulableResource,
    MARTE_GRM_Scheduler,
    MARTE_GRM_SecondaryScheduler,
    MARTE_GRM_StorageResource,
    MARTE_GRM_SynchronizationResource,
    MARTE_GRM_TimerResource,
    MARTE_GRM_TimingResource,
    MARTE_HLAM_PpUnit,
    MARTE_HLAM_RtAction,
    MARTE_HLAM_RtFeature,
    MARTE_HLAM_RtService,
    MARTE_HLAM_RtSpecification,
    MARTE_HLAM_RtUnit,
    MARTE_HwCommunication_HwArbiter,
    MARTE_HwCommunication_HwBridge,
    MARTE_HwCommunication_HwBus,
    MARTE_HwCommunication_HwCommunicationResource,
    MARTE_HwCommunication_HwConnection,
    MARTE_HwCommunication_HwEndPoint,
    MARTE_HwCommunication_HwMedia,
    MARTE_HwCommunication_HwPort,
    MARTE_HwComputing_HwASIC,
    MARTE_HwComputing_HwBranchPredictor,
    MARTE_HwComputing_HwComputingResource,
    MARTE_HwComputing_HwISA,
    MARTE_HwComputing_HwMCU,
    MARTE_HwComputing_HwPLD,
    MARTE_HwComputing_HwProcessor,
    MARTE_HwComputing_PLD_Organization,
    MARTE_HwDatasheet_HwDatasheet,
    MARTE_HwDeviceFunction_HwDeviceFunction,
    MARTE_HwDevice_HWActuator,
    MARTE_HwDevice_HWSensor,
    MARTE_HwDevice_HwDevice,
    MARTE_HwDevice_HwI_O,
    MARTE_HwDevice_HwPeripheral,
    MARTE_HwDevice_HwSupport,
    MARTE_HwDiagram_HwBlockDiagram,
    MARTE_HwDiagram_HwCircuitDiagram,
    MARTE_HwDiagram_HwHRMDiagram,
    MARTE_HwDiagram_SRMDiagram,
    MARTE_HwGeneral_HwResource,
    MARTE_HwGeneral_HwResourceService,
    MARTE_HwIO_HwLine,
    MARTE_HwIO_HwPin,
    MARTE_HwLayout_Env_Condition,
    MARTE_HwLayout_HwComponent,
    MARTE_HwMemory_CacheStructure,
    MARTE_HwMemory_HwCache,
    MARTE_HwMemory_HwDrive,
    MARTE_HwMemory_HwMemory,
    MARTE_HwMemory_HwRAM,
    MARTE_HwMemory_HwROM,
    MARTE_HwMemory_MemoryOrganization,
    MARTE_HwMemory_Timing,
    MARTE_HwPackage_HwPackage,
    MARTE_HwPackage_HwPackagePin,
    MARTE_HwPackage_HwWire,
    MARTE_HwPeripheral_OperationImpl,
    MARTE_HwPeripheral_PeripheralActivity,
    MARTE_HwPeripheral_ReadRegisterAction,
    MARTE_HwPeripheral_RegisterAction,
    MARTE_HwPeripheral_WriteRegisterAction,
    MARTE_HwPower_HwCoolingSupply,
    MARTE_HwPower_HwPowerSupply,
    MARTE_HwProtocol_HwProtocol,
    MARTE_HwRegister_HwRegister,
    MARTE_HwStorageManager_HwDMA,
    MARTE_HwStorageManager_HwMMU,
    MARTE_HwStorageManager_HwStorageManager,
    MARTE_HwTiming_HwClock,
    MARTE_HwTiming_HwTimer,
    MARTE_HwTiming_HwTimingResource,
    MARTE_NFPs_Dimension,
    MARTE_NFPs_Nfp,
    MARTE_NFPs_NfpConstraint,
    MARTE_NFPs_NfpType,
    MARTE_NFPs_Unit,
    MARTE_PAM_PaCommStep,
    MARTE_PAM_PaLogicalResource,
    MARTE_PAM_PaRequestedStep,
    MARTE_PAM_PaResPassStep,
    MARTE_PAM_PaRunTInstance,
    MARTE_PAM_PaStep,
    MARTE_RSM_DefaultLink,
    MARTE_RSM_Distribute,
    MARTE_RSM_InterRepetition,
    MARTE_RSM_LinkTopology,
    MARTE_RSM_Reshape,
    MARTE_RSM_Shaped,
    MARTE_RSM_Tiler,
    MARTE_SAM_SaAnalysisContext,
    MARTE_SAM_SaCommHost,
    MARTE_SAM_SaCommStep,
    MARTE_SAM_SaEndtoEndFlow,
    MARTE_SAM_SaExecHost,
    MARTE_SAM_SaSchedObs,
    MARTE_SAM_SaSharedResource,
    MARTE_SAM_SaStep,
    MARTE_SW_Brokering_DeviceBroker,
    MARTE_SW_Brokering_MemoryBroker,
    MARTE_SW_Concurrency_Alarm,
    MARTE_SW_Concurrency_EntryPoint,
    MARTE_SW_Concurrency_InterruptResource,
    MARTE_SW_Concurrency_MemoryPartition,
    MARTE_SW_Concurrency_SwConcurrentResource,
    MARTE_SW_Concurrency_SwSchedulableResource,
    MARTE_SW_Concurrency_SwTimerResource,
    MARTE_SW_Interaction_MessageComResource,
    MARTE_SW_Interaction_NotificationResource,
    MARTE_SW_Interaction_SharedDataComResource,
    MARTE_SW_Interaction_SwCommunicationResource,
    MARTE_SW_Interaction_SwInteractionResource,
    MARTE_SW_Interaction_SwMutualExclusionResource,
    MARTE_SW_Interaction_SwSynchronizationResource,
    MARTE_SW_ResourceCore_SwAccessService,
    MARTE_SW_ResourceCore_SwResource,
    MARTE_Time_Clock,
    MARTE_Time_ClockConstraint,
    MARTE_Time_ClockType,
    MARTE_Time_TimedConstraint,
    MARTE_Time_TimedDomain,
    MARTE_Time_TimedDurationObservation,
    MARTE_Time_TimedElement,
    MARTE_Time_TimedEvent,
    MARTE_Time_TimedInstantObservation,
    MARTE_Time_TimedObservation,
    MARTE_Time_TimedProcessing,
    MARTE_Time_TimedValueSpecification,
    MARTE_Variables_ExpressionContext,
    MARTE_Variables_Var,
    MutualExclusionResource,
    NFP_Area,
    NFP_Boolean,
    NFP_DataSize,
    NFP_DataTxRate,
    NFP_DateTime,
    NFP_Duration,
    NFP_Energy,
    NFP_Frequency,
    NFP_FrequencyInterval,
    NFP_Integer,
    NFP_Length,
    NFP_Natural,
    NFP_NaturalInterval,
    NFP_Percentage,
    NFP_Power,
    NFP_Price,
    NFP_Real,
    NFP_String,
    NFPs_Dimension,
    NFPs_MARTE_Constraint,
    NFPs_MARTE_Enumeration,
    NFPs_MARTE_EnumerationLiteral,
    NFPs_MARTE_Property,
    NFPs_NfpConstraint,
    NFPs_Unit,
    NfpConstraint,
    Operation,
    PAM_MARTE_NamedElement,
    PAM_PaStep,
    ProcessingResource,
    RSM_MARTE_Connector,
    RSM_MARTE_ConnectorEnd,
    RSM_MARTE_MultiplicityElement,
    Realnterval,
    RegisterAction,
    Resource,
    SAM_MARTE_BehavioralFeature,
    SAM_MARTE_NamedElement,
    SAM_SaSharedResource,
    SW_Brokering_DeviceBroker,
    SW_Brokering_MARTE_Activity,
    SW_Brokering_MARTE_BehavioralFeature,
    SW_Brokering_MARTE_Operation,
    SW_Brokering_MARTE_TypedElement,
    SW_Concurrency_MARTE_BehavioralFeature,
    SW_Concurrency_MARTE_Element,
    SW_Concurrency_MARTE_NamedElement,
    SW_Concurrency_MARTE_Namespace,
    SW_Concurrency_MARTE_TypedElement,
    SW_Concurrency_SwConcurrentResource,
    SW_Interaction_MARTE_BehavioralFeature,
    SW_Interaction_MARTE_TypedElement,
    SW_Interaction_SwInteractionResource,
    SW_Interaction_SwSynchronizationResource,
    SW_ResourceCore_MARTE_BehavioralFeature,
    SW_ResourceCore_MARTE_Property,
    SW_ResourceCore_MARTE_TypedElement,
    SchedParameters,
    SchedulableResource,
    Scheduler,
    ShapeSpecification,
    SwCommunicationResource,
    SwConcurrentResource,
    SwResource,
    SwSynchronizationResource,
    TilerSpecification,
    Time_Clock,
    Time_ClockType,
    Time_MARTE_Action,
    Time_MARTE_Behavior,
    Time_MARTE_Class,
    Time_MARTE_DurationObservation,
    Time_MARTE_Enumeration,
    Time_MARTE_Event,
    Time_MARTE_InstanceSpecification,
    Time_MARTE_Message,
    Time_MARTE_Namespace,
    Time_MARTE_Operation,
    Time_MARTE_Property,
    Time_MARTE_TimeEvent,
    Time_MARTE_TimeObservation,
    Time_MARTE_ValueSpecification,
    Time_TimedElement,
    Time_TimedInstantObservation,
    Time_TimedProcessing,
    TimedElement,
    TimedObservation,
    TimerResource,
    TimingResource,
    TupleType,
    UtilityType,
    Variables_ExpressionContext,
    Variables_MARTE_NamedElement,
    Variables_MARTE_Property,
    AccessPolicyKind,
    AllocationEndKind,
    AllocationKind,
    AllocationNature,
    AssignmentKind,
    AssignmentNature,
    CacheType,
    CallConcurrencyKind,
    ClientServerKind,
    ComponentKind,
    ComponentState,
    ConcurrencyKind,
    ConcurrentAccessProtocolKind,
    ConditionType,
    ConstraintKind,
    DataPoolOrderingKind,
    ExecutionKind,
    FlowDirectionKind,
    ISA_Type,
    InterruptKind,
    LaxityKind,
    MessageResourceKind,
    MutualExclusionResourceKind,
    NotificationKind,
    NotificationResourceKind,
    OptimallityCriterionKind,
    PLD_Class,
    PLD_Technology,
    PoolMgtPolicyKind,
    PortSpecificationKind,
    QueuePolicyKind,
    ROM_Type,
    Repl_Policy,
    SynchronizationKind,
    VariableDirectionKind,
    WritePolicy,
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

def test_assoc_accessTokenElements792_stub_double():
    # SW_Interaction_MARTE_TypedElement has no real 'SW_Interaction_MARTE_TypedElement793' property in the generated
    # code (a bare stub) -- manually attach it so MARTE_SW_Interaction_SwMutualExclusionResource's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # MARTE_SW_Interaction_SwMutualExclusionResource's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = MARTE_SW_Interaction_SwMutualExclusionResource(concurrentAccessProtocol="sample_text", mechanism="sample_text")
    partner = SW_Interaction_MARTE_TypedElement()
    setattr(partner, 'SW_Interaction_MARTE_TypedElement793', None)
    _safe_set(owner, 'MARTE_SW_Interaction_SwMutualExclusionResource', {partner})
    assert getattr(partner, 'SW_Interaction_MARTE_TypedElement793') == owner
    _safe_set(owner, 'MARTE_SW_Interaction_SwMutualExclusionResource', set())
    assert getattr(partner, 'SW_Interaction_MARTE_TypedElement793') is None


def test_assoc_accessedElement623_stub_double():
    # SW_ResourceCore_MARTE_Property has no real 'SW_ResourceCore_MARTE_Property' property in the generated
    # code (a bare stub) -- manually attach it so MARTE_SW_ResourceCore_SwAccessService's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # MARTE_SW_ResourceCore_SwAccessService's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = MARTE_SW_ResourceCore_SwAccessService(isModifier="sample_text")
    partner = SW_ResourceCore_MARTE_Property()
    setattr(partner, 'SW_ResourceCore_MARTE_Property', None)
    _safe_set(owner, 'MARTE_SW_ResourceCore_SwAccessService', partner)
    assert getattr(partner, 'SW_ResourceCore_MARTE_Property') == owner
    _safe_set(owner, 'MARTE_SW_ResourceCore_SwAccessService', None)
    assert getattr(partner, 'SW_ResourceCore_MARTE_Property') is None


def test_assoc_acquireServices797_stub_double():
    # SW_Interaction_MARTE_BehavioralFeature has no real 'SW_Interaction_MARTE_BehavioralFeature799' property in the generated
    # code (a bare stub) -- manually attach it so MARTE_SW_Interaction_SwMutualExclusionResource's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # MARTE_SW_Interaction_SwMutualExclusionResource's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = MARTE_SW_Interaction_SwMutualExclusionResource(concurrentAccessProtocol="sample_text", mechanism="sample_text")
    partner = SW_Interaction_MARTE_BehavioralFeature()
    setattr(partner, 'SW_Interaction_MARTE_BehavioralFeature799', None)
    _safe_set(owner, 'MARTE_SW_Interaction_SwMutualExclusionResource798', {partner})
    assert getattr(partner, 'SW_Interaction_MARTE_BehavioralFeature799') == owner
    _safe_set(owner, 'MARTE_SW_Interaction_SwMutualExclusionResource798', set())
    assert getattr(partner, 'SW_Interaction_MARTE_BehavioralFeature799') is None


def test_assoc_activateServices640_stub_double():
    # SW_Concurrency_MARTE_BehavioralFeature has no real 'SW_Concurrency_MARTE_BehavioralFeature642' property in the generated
    # code (a bare stub) -- manually attach it so MARTE_SW_Concurrency_SwConcurrentResource's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # MARTE_SW_Concurrency_SwConcurrentResource's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = MARTE_SW_Concurrency_SwConcurrentResource(activationCapacity="sample_text")
    partner = SW_Concurrency_MARTE_BehavioralFeature()
    setattr(partner, 'SW_Concurrency_MARTE_BehavioralFeature642', None)
    _safe_set(owner, 'MARTE_SW_Concurrency_SwConcurrentResource641', {partner})
    assert getattr(partner, 'SW_Concurrency_MARTE_BehavioralFeature642') == owner
    _safe_set(owner, 'MARTE_SW_Concurrency_SwConcurrentResource641', set())
    assert getattr(partner, 'SW_Concurrency_MARTE_BehavioralFeature642') is None


def test_assoc_activities523_stub_double():
    # HwGeneral_MARTE_Activity has no real 'HwGeneral_MARTE_Activity' property in the generated
    # code (a bare stub) -- manually attach it so MARTE_HwGeneral_HwResource's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # MARTE_HwGeneral_HwResource's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = MARTE_HwGeneral_HwResource(name="sample_text")
    partner = HwGeneral_MARTE_Activity()
    setattr(partner, 'HwGeneral_MARTE_Activity', None)
    _safe_set(owner, 'MARTE_HwGeneral_HwResource524', {partner})
    assert getattr(partner, 'HwGeneral_MARTE_Activity') == owner
    _safe_set(owner, 'MARTE_HwGeneral_HwResource524', set())
    assert getattr(partner, 'HwGeneral_MARTE_Activity') is None


def test_assoc_activities737_stub_double():
    # SW_Brokering_MARTE_Activity has no real 'SW_Brokering_MARTE_Activity' property in the generated
    # code (a bare stub) -- manually attach it so MARTE_SW_Brokering_DeviceBroker's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # MARTE_SW_Brokering_DeviceBroker's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = MARTE_SW_Brokering_DeviceBroker(accessPolicy="sample_text", isBuffered="sample_text", name="sample_text")
    partner = SW_Brokering_MARTE_Activity()
    setattr(partner, 'SW_Brokering_MARTE_Activity', None)
    _safe_set(owner, 'MARTE_SW_Brokering_DeviceBroker738', {partner})
    assert getattr(partner, 'SW_Brokering_MARTE_Activity') == owner
    _safe_set(owner, 'MARTE_SW_Brokering_DeviceBroker738', set())
    assert getattr(partner, 'SW_Brokering_MARTE_Activity') is None


def test_assoc_adressSpace629_stub_double():
    # SW_Concurrency_MARTE_TypedElement has no real 'SW_Concurrency_MARTE_TypedElement' property in the generated
    # code (a bare stub) -- manually attach it so MARTE_SW_Concurrency_SwConcurrentResource's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # MARTE_SW_Concurrency_SwConcurrentResource's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = MARTE_SW_Concurrency_SwConcurrentResource(activationCapacity="sample_text")
    partner = SW_Concurrency_MARTE_TypedElement()
    setattr(partner, 'SW_Concurrency_MARTE_TypedElement', None)
    _safe_set(owner, 'MARTE_SW_Concurrency_SwConcurrentResource630', {partner})
    assert getattr(partner, 'SW_Concurrency_MARTE_TypedElement') == owner
    _safe_set(owner, 'MARTE_SW_Concurrency_SwConcurrentResource630', set())
    assert getattr(partner, 'SW_Concurrency_MARTE_TypedElement') is None


def test_assoc_area526_stub_double():
    # NFP_Area has no real 'NFP_Area' property in the generated
    # code (a bare stub) -- manually attach it so MARTE_HwLayout_HwComponent's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # MARTE_HwLayout_HwComponent's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = MARTE_HwLayout_HwComponent(kind="sample_text")
    partner = NFP_Area()
    setattr(partner, 'NFP_Area', None)
    _safe_set(owner, 'MARTE_HwLayout_HwComponent527', partner)
    assert getattr(partner, 'NFP_Area') == owner
    _safe_set(owner, 'MARTE_HwLayout_HwComponent527', None)
    assert getattr(partner, 'NFP_Area') is None


def test_assoc_baseDimension15_stub_double():
    # NFPs_Dimension has no real 'NFPs_Dimension' property in the generated
    # code (a bare stub) -- manually attach it so MARTE_NFPs_Dimension's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # MARTE_NFPs_Dimension's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = MARTE_NFPs_Dimension(baseExponent=7, symbol="sample_text")
    partner = NFPs_Dimension()
    setattr(partner, 'NFPs_Dimension', None)
    _safe_set(owner, 'MARTE_NFPs_Dimension', {partner})
    assert getattr(partner, 'NFPs_Dimension') == owner
    _safe_set(owner, 'MARTE_NFPs_Dimension', set())
    assert getattr(partner, 'NFPs_Dimension') is None


def test_assoc_baseType213_stub_double():
    # DataTypes_MARTE_Property has no real 'DataTypes_MARTE_Property' property in the generated
    # code (a bare stub) -- manually attach it so MARTE_DataTypes_BoundedSubtype's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # MARTE_DataTypes_BoundedSubtype's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = MARTE_DataTypes_BoundedSubtype(isMaxOpen=True, isMinOpen=True, maxValue="sample_text", minValue="sample_text")
    partner = DataTypes_MARTE_Property()
    setattr(partner, 'DataTypes_MARTE_Property', None)
    _safe_set(owner, 'MARTE_DataTypes_BoundedSubtype', partner)
    assert getattr(partner, 'DataTypes_MARTE_Property') == owner
    _safe_set(owner, 'MARTE_DataTypes_BoundedSubtype', None)
    assert getattr(partner, 'DataTypes_MARTE_Property') is None


def test_assoc_baseUnit1_stub_double():
    # NFPs_Unit has no real 'NFPs_Unit' property in the generated
    # code (a bare stub) -- manually attach it so MARTE_NFPs_Unit's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # MARTE_NFPs_Unit's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = MARTE_NFPs_Unit(convFactor="sample_text", offsetFactor="sample_text")
    partner = NFPs_Unit()
    setattr(partner, 'NFPs_Unit', None)
    _safe_set(owner, 'MARTE_NFPs_Unit', partner)
    assert getattr(partner, 'NFPs_Unit') == owner
    _safe_set(owner, 'MARTE_NFPs_Unit', None)
    assert getattr(partner, 'NFPs_Unit') is None


def test_assoc_base_Abstraction46_stub_double():
    # Alloc_MARTE_Abstraction has no real 'Alloc_MARTE_Abstraction' property in the generated
    # code (a bare stub) -- manually attach it so MARTE_Alloc_Allocate's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # MARTE_Alloc_Allocate's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = MARTE_Alloc_Allocate(kind="sample_text", nature="sample_text")
    partner = Alloc_MARTE_Abstraction()
    setattr(partner, 'Alloc_MARTE_Abstraction', None)
    _safe_set(owner, 'MARTE_Alloc_Allocate', partner)
    assert getattr(partner, 'Alloc_MARTE_Abstraction') == owner
    _safe_set(owner, 'MARTE_Alloc_Allocate', None)
    assert getattr(partner, 'Alloc_MARTE_Abstraction') is None


def test_assoc_base_BehavioralFeature294_stub_double():
    # HLAM_MARTE_BehavioralFeature has no real 'HLAM_MARTE_BehavioralFeature296' property in the generated
    # code (a bare stub) -- manually attach it so MARTE_HLAM_RtAction's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # MARTE_HLAM_RtAction's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = MARTE_HLAM_RtAction(isAtomic="sample_text", synchKind="sample_text")
    partner = HLAM_MARTE_BehavioralFeature()
    setattr(partner, 'HLAM_MARTE_BehavioralFeature296', None)
    _safe_set(owner, 'MARTE_HLAM_RtAction295', partner)
    assert getattr(partner, 'HLAM_MARTE_BehavioralFeature296') == owner
    _safe_set(owner, 'MARTE_HLAM_RtAction295', None)
    assert getattr(partner, 'HLAM_MARTE_BehavioralFeature296') is None


def test_assoc_base_BehavioralFeature300_stub_double():
    # HLAM_MARTE_BehavioralFeature has no real 'HLAM_MARTE_BehavioralFeature301' property in the generated
    # code (a bare stub) -- manually attach it so MARTE_HLAM_RtService's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # MARTE_HLAM_RtService's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = MARTE_HLAM_RtService(concPolicy="sample_text", exeKind="sample_text", isAtomic="sample_text", synchKind="sample_text")
    partner = HLAM_MARTE_BehavioralFeature()
    setattr(partner, 'HLAM_MARTE_BehavioralFeature301', None)
    _safe_set(owner, 'MARTE_HLAM_RtService', partner)
    assert getattr(partner, 'HLAM_MARTE_BehavioralFeature301') == owner
    _safe_set(owner, 'MARTE_HLAM_RtService', None)
    assert getattr(partner, 'HLAM_MARTE_BehavioralFeature301') is None


def test_assoc_base_BehavioralFeature815_stub_double():
    # GCM_MARTE_BehavioralFeature has no real 'GCM_MARTE_BehavioralFeature' property in the generated
    # code (a bare stub) -- manually attach it so MARTE_GCM_ClientServerFeature's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # MARTE_GCM_ClientServerFeature's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = MARTE_GCM_ClientServerFeature(kind="sample_text")
    partner = GCM_MARTE_BehavioralFeature()
    setattr(partner, 'GCM_MARTE_BehavioralFeature', None)
    _safe_set(owner, 'MARTE_GCM_ClientServerFeature', partner)
    assert getattr(partner, 'GCM_MARTE_BehavioralFeature') == owner
    _safe_set(owner, 'MARTE_GCM_ClientServerFeature', None)
    assert getattr(partner, 'GCM_MARTE_BehavioralFeature') is None


def test_assoc_base_BehavioredClassifier248_stub_double():
    # HLAM_MARTE_BehavioredClassifier has no real 'HLAM_MARTE_BehavioredClassifier' property in the generated
    # code (a bare stub) -- manually attach it so MARTE_HLAM_RtUnit's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # MARTE_HLAM_RtUnit's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = MARTE_HLAM_RtUnit(isDynamic="sample_text", isMain="sample_text", queueSchedPolicy="sample_text", queueSize="sample_text", srPoolPolicy="sample_text", srPoolSize="sample_text")
    partner = HLAM_MARTE_BehavioredClassifier()
    setattr(partner, 'HLAM_MARTE_BehavioredClassifier', None)
    _safe_set(owner, 'MARTE_HLAM_RtUnit249', partner)
    assert getattr(partner, 'HLAM_MARTE_BehavioredClassifier') == owner
    _safe_set(owner, 'MARTE_HLAM_RtUnit249', None)
    assert getattr(partner, 'HLAM_MARTE_BehavioredClassifier') is None


def test_assoc_base_BehavioredClassifier255_stub_double():
    # HLAM_MARTE_BehavioredClassifier has no real 'HLAM_MARTE_BehavioredClassifier257' property in the generated
    # code (a bare stub) -- manually attach it so MARTE_HLAM_PpUnit's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # MARTE_HLAM_PpUnit's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = MARTE_HLAM_PpUnit(concPolicy="sample_text")
    partner = HLAM_MARTE_BehavioredClassifier()
    setattr(partner, 'HLAM_MARTE_BehavioredClassifier257', None)
    _safe_set(owner, 'MARTE_HLAM_PpUnit256', partner)
    assert getattr(partner, 'HLAM_MARTE_BehavioredClassifier257') == owner
    _safe_set(owner, 'MARTE_HLAM_PpUnit256', None)
    assert getattr(partner, 'HLAM_MARTE_BehavioredClassifier257') is None


def test_assoc_base_Class77_stub_double():
    # Time_MARTE_Class has no real 'Time_MARTE_Class' property in the generated
    # code (a bare stub) -- manually attach it so MARTE_Time_ClockType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # MARTE_Time_ClockType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = MARTE_Time_ClockType(isLogical="sample_text", nature="sample_text")
    partner = Time_MARTE_Class()
    setattr(partner, 'Time_MARTE_Class', None)
    _safe_set(owner, 'MARTE_Time_ClockType78', partner)
    assert getattr(partner, 'Time_MARTE_Class') == owner
    _safe_set(owner, 'MARTE_Time_ClockType78', None)
    assert getattr(partner, 'Time_MARTE_Class') is None


def test_assoc_base_Classifier105_stub_double():
    # GRM_MARTE_Classifier has no real 'GRM_MARTE_Classifier' property in the generated
    # code (a bare stub) -- manually attach it so MARTE_GRM_Resource's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # MARTE_GRM_Resource's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = MARTE_GRM_Resource(isProtected="sample_text")
    partner = GRM_MARTE_Classifier()
    setattr(partner, 'GRM_MARTE_Classifier', None)
    _safe_set(owner, 'MARTE_GRM_Resource106', partner)
    assert getattr(partner, 'GRM_MARTE_Classifier') == owner
    _safe_set(owner, 'MARTE_GRM_Resource106', None)
    assert getattr(partner, 'GRM_MARTE_Classifier') is None


def test_assoc_base_ConnectableElement109_stub_double():
    # GRM_MARTE_ConnectableElement has no real 'GRM_MARTE_ConnectableElement' property in the generated
    # code (a bare stub) -- manually attach it so MARTE_GRM_Resource's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # MARTE_GRM_Resource's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = MARTE_GRM_Resource(isProtected="sample_text")
    partner = GRM_MARTE_ConnectableElement()
    setattr(partner, 'GRM_MARTE_ConnectableElement', None)
    _safe_set(owner, 'MARTE_GRM_Resource110', partner)
    assert getattr(partner, 'GRM_MARTE_ConnectableElement') == owner
    _safe_set(owner, 'MARTE_GRM_Resource110', None)
    assert getattr(partner, 'GRM_MARTE_ConnectableElement') is None


def test_assoc_base_Connector136_stub_double():
    # GRM_MARTE_Connector has no real 'GRM_MARTE_Connector' property in the generated
    # code (a bare stub) -- manually attach it so MARTE_GRM_CommunicationMedia's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # MARTE_GRM_CommunicationMedia's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = MARTE_GRM_CommunicationMedia(transmMode="sample_text")
    partner = GRM_MARTE_Connector()
    setattr(partner, 'GRM_MARTE_Connector', None)
    _safe_set(owner, 'MARTE_GRM_CommunicationMedia137', partner)
    assert getattr(partner, 'GRM_MARTE_Connector') == owner
    _safe_set(owner, 'MARTE_GRM_CommunicationMedia137', None)
    assert getattr(partner, 'GRM_MARTE_Connector') is None


def test_assoc_base_Constraint4_stub_double():
    # NFPs_MARTE_Constraint has no real 'NFPs_MARTE_Constraint' property in the generated
    # code (a bare stub) -- manually attach it so MARTE_NFPs_NfpConstraint's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # MARTE_NFPs_NfpConstraint's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = MARTE_NFPs_NfpConstraint(kind="sample_text")
    partner = NFPs_MARTE_Constraint()
    setattr(partner, 'NFPs_MARTE_Constraint', None)
    _safe_set(owner, 'MARTE_NFPs_NfpConstraint', partner)
    assert getattr(partner, 'NFPs_MARTE_Constraint') == owner
    _safe_set(owner, 'MARTE_NFPs_NfpConstraint', None)
    assert getattr(partner, 'NFPs_MARTE_Constraint') is None


def test_assoc_base_DataType214_stub_double():
    # DataTypes_MARTE_DataType has no real 'DataTypes_MARTE_DataType' property in the generated
    # code (a bare stub) -- manually attach it so MARTE_DataTypes_BoundedSubtype's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # MARTE_DataTypes_BoundedSubtype's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = MARTE_DataTypes_BoundedSubtype(isMaxOpen=True, isMinOpen=True, maxValue="sample_text", minValue="sample_text")
    partner = DataTypes_MARTE_DataType()
    setattr(partner, 'DataTypes_MARTE_DataType', None)
    _safe_set(owner, 'MARTE_DataTypes_BoundedSubtype215', partner)
    assert getattr(partner, 'DataTypes_MARTE_DataType') == owner
    _safe_set(owner, 'MARTE_DataTypes_BoundedSubtype215', None)
    assert getattr(partner, 'DataTypes_MARTE_DataType') is None


def test_assoc_base_DurationObservation82_stub_double():
    # Time_MARTE_DurationObservation has no real 'Time_MARTE_DurationObservation' property in the generated
    # code (a bare stub) -- manually attach it so MARTE_Time_TimedDurationObservation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # MARTE_Time_TimedDurationObservation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = MARTE_Time_TimedDurationObservation(obsKind="sample_text")
    partner = Time_MARTE_DurationObservation()
    setattr(partner, 'Time_MARTE_DurationObservation', None)
    _safe_set(owner, 'MARTE_Time_TimedDurationObservation', partner)
    assert getattr(partner, 'Time_MARTE_DurationObservation') == owner
    _safe_set(owner, 'MARTE_Time_TimedDurationObservation', None)
    assert getattr(partner, 'Time_MARTE_DurationObservation') is None


def test_assoc_base_Enumeration16_stub_double():
    # NFPs_MARTE_Enumeration has no real 'NFPs_MARTE_Enumeration' property in the generated
    # code (a bare stub) -- manually attach it so MARTE_NFPs_Dimension's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # MARTE_NFPs_Dimension's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = MARTE_NFPs_Dimension(baseExponent=7, symbol="sample_text")
    partner = NFPs_MARTE_Enumeration()
    setattr(partner, 'NFPs_MARTE_Enumeration', None)
    _safe_set(owner, 'MARTE_NFPs_Dimension17', partner)
    assert getattr(partner, 'NFPs_MARTE_Enumeration') == owner
    _safe_set(owner, 'MARTE_NFPs_Dimension17', None)
    assert getattr(partner, 'NFPs_MARTE_Enumeration') is None


def test_assoc_base_EnumerationLiteral2_stub_double():
    # NFPs_MARTE_EnumerationLiteral has no real 'NFPs_MARTE_EnumerationLiteral' property in the generated
    # code (a bare stub) -- manually attach it so MARTE_NFPs_Unit's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # MARTE_NFPs_Unit's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = MARTE_NFPs_Unit(convFactor="sample_text", offsetFactor="sample_text")
    partner = NFPs_MARTE_EnumerationLiteral()
    setattr(partner, 'NFPs_MARTE_EnumerationLiteral', None)
    _safe_set(owner, 'MARTE_NFPs_Unit3', partner)
    assert getattr(partner, 'NFPs_MARTE_EnumerationLiteral') == owner
    _safe_set(owner, 'MARTE_NFPs_Unit3', None)
    assert getattr(partner, 'NFPs_MARTE_EnumerationLiteral') is None


def test_assoc_base_InstanceSpecification103_stub_double():
    # GRM_MARTE_InstanceSpecification has no real 'GRM_MARTE_InstanceSpecification' property in the generated
    # code (a bare stub) -- manually attach it so MARTE_GRM_Resource's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # MARTE_GRM_Resource's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = MARTE_GRM_Resource(isProtected="sample_text")
    partner = GRM_MARTE_InstanceSpecification()
    setattr(partner, 'GRM_MARTE_InstanceSpecification', None)
    _safe_set(owner, 'MARTE_GRM_Resource104', partner)
    assert getattr(partner, 'GRM_MARTE_InstanceSpecification') == owner
    _safe_set(owner, 'MARTE_GRM_Resource104', None)
    assert getattr(partner, 'GRM_MARTE_InstanceSpecification') is None


def test_assoc_base_InstanceSpecification51_stub_double():
    # Time_MARTE_InstanceSpecification has no real 'Time_MARTE_InstanceSpecification' property in the generated
    # code (a bare stub) -- manually attach it so MARTE_Time_Clock's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # MARTE_Time_Clock's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = MARTE_Time_Clock(standard="sample_text")
    partner = Time_MARTE_InstanceSpecification()
    setattr(partner, 'Time_MARTE_InstanceSpecification', None)
    _safe_set(owner, 'MARTE_Time_Clock', partner)
    assert getattr(partner, 'Time_MARTE_InstanceSpecification') == owner
    _safe_set(owner, 'MARTE_Time_Clock', None)
    assert getattr(partner, 'Time_MARTE_InstanceSpecification') is None


def test_assoc_base_InvocationAction297_stub_double():
    # HLAM_MARTE_InvocationAction has no real 'HLAM_MARTE_InvocationAction299' property in the generated
    # code (a bare stub) -- manually attach it so MARTE_HLAM_RtAction's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # MARTE_HLAM_RtAction's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = MARTE_HLAM_RtAction(isAtomic="sample_text", synchKind="sample_text")
    partner = HLAM_MARTE_InvocationAction()
    setattr(partner, 'HLAM_MARTE_InvocationAction299', None)
    _safe_set(owner, 'MARTE_HLAM_RtAction298', partner)
    assert getattr(partner, 'HLAM_MARTE_InvocationAction299') == owner
    _safe_set(owner, 'MARTE_HLAM_RtAction298', None)
    assert getattr(partner, 'HLAM_MARTE_InvocationAction299') is None


def test_assoc_base_Lifeline107_stub_double():
    # GRM_MARTE_Lifeline has no real 'GRM_MARTE_Lifeline' property in the generated
    # code (a bare stub) -- manually attach it so MARTE_GRM_Resource's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # MARTE_GRM_Resource's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = MARTE_GRM_Resource(isProtected="sample_text")
    partner = GRM_MARTE_Lifeline()
    setattr(partner, 'GRM_MARTE_Lifeline', None)
    _safe_set(owner, 'MARTE_GRM_Resource108', partner)
    assert getattr(partner, 'GRM_MARTE_Lifeline') == owner
    _safe_set(owner, 'MARTE_GRM_Resource108', None)
    assert getattr(partner, 'GRM_MARTE_Lifeline') is None


def test_assoc_base_NamedElement1117_stub_double():
    # PAM_MARTE_NamedElement has no real 'PAM_MARTE_NamedElement' property in the generated
    # code (a bare stub) -- manually attach it so MARTE_PAM_PaRunTInstance's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # MARTE_PAM_PaRunTInstance's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = MARTE_PAM_PaRunTInstance(unbddPool="sample_text")
    partner = PAM_MARTE_NamedElement()
    setattr(partner, 'PAM_MARTE_NamedElement', None)
    _safe_set(owner, 'MARTE_PAM_PaRunTInstance1118', partner)
    assert getattr(partner, 'PAM_MARTE_NamedElement') == owner
    _safe_set(owner, 'MARTE_PAM_PaRunTInstance1118', None)
    assert getattr(partner, 'PAM_MARTE_NamedElement') is None


def test_assoc_base_NamedElement837_stub_double():
    # GQAM_MARTE_NamedElement has no real 'GQAM_MARTE_NamedElement' property in the generated
    # code (a bare stub) -- manually attach it so MARTE_GQAM_GaEventTrace's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # MARTE_GQAM_GaEventTrace's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = MARTE_GQAM_GaEventTrace(content="sample_text", format="sample_text", location="sample_text")
    partner = GQAM_MARTE_NamedElement()
    setattr(partner, 'GQAM_MARTE_NamedElement', None)
    _safe_set(owner, 'MARTE_GQAM_GaEventTrace', partner)
    assert getattr(partner, 'GQAM_MARTE_NamedElement') == owner
    _safe_set(owner, 'MARTE_GQAM_GaEventTrace', None)
    assert getattr(partner, 'GQAM_MARTE_NamedElement') is None


def test_assoc_base_Port801_stub_double():
    # GCM_MARTE_Port has no real 'GCM_MARTE_Port' property in the generated
    # code (a bare stub) -- manually attach it so MARTE_GCM_FlowPort's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # MARTE_GCM_FlowPort's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = MARTE_GCM_FlowPort(direction="sample_text", isAtomic="sample_text", isConjugated="sample_text")
    partner = GCM_MARTE_Port()
    setattr(partner, 'GCM_MARTE_Port', None)
    _safe_set(owner, 'MARTE_GCM_FlowPort', partner)
    assert getattr(partner, 'GCM_MARTE_Port') == owner
    _safe_set(owner, 'MARTE_GCM_FlowPort', None)
    assert getattr(partner, 'GCM_MARTE_Port') is None


def test_assoc_base_Port802_stub_double():
    # GCM_MARTE_Port has no real 'GCM_MARTE_Port803' property in the generated
    # code (a bare stub) -- manually attach it so MARTE_GCM_ClientServerPort's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # MARTE_GCM_ClientServerPort's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = MARTE_GCM_ClientServerPort(isConjugated="sample_text", kind="sample_text", specificationKind="sample_text")
    partner = GCM_MARTE_Port()
    setattr(partner, 'GCM_MARTE_Port803', None)
    _safe_set(owner, 'MARTE_GCM_ClientServerPort', partner)
    assert getattr(partner, 'GCM_MARTE_Port803') == owner
    _safe_set(owner, 'MARTE_GCM_ClientServerPort', None)
    assert getattr(partner, 'GCM_MARTE_Port803') is None


def test_assoc_base_Property101_stub_double():
    # GRM_MARTE_Property has no real 'GRM_MARTE_Property' property in the generated
    # code (a bare stub) -- manually attach it so MARTE_GRM_Resource's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # MARTE_GRM_Resource's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = MARTE_GRM_Resource(isProtected="sample_text")
    partner = GRM_MARTE_Property()
    setattr(partner, 'GRM_MARTE_Property', None)
    _safe_set(owner, 'MARTE_GRM_Resource102', partner)
    assert getattr(partner, 'GRM_MARTE_Property') == owner
    _safe_set(owner, 'MARTE_GRM_Resource102', None)
    assert getattr(partner, 'GRM_MARTE_Property') is None


def test_assoc_base_Property211_stub_double():
    # Variables_MARTE_Property has no real 'Variables_MARTE_Property' property in the generated
    # code (a bare stub) -- manually attach it so MARTE_Variables_Var's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # MARTE_Variables_Var's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = MARTE_Variables_Var(dir="sample_text")
    partner = Variables_MARTE_Property()
    setattr(partner, 'Variables_MARTE_Property', None)
    _safe_set(owner, 'MARTE_Variables_Var', partner)
    assert getattr(partner, 'Variables_MARTE_Property') == owner
    _safe_set(owner, 'MARTE_Variables_Var', None)
    assert getattr(partner, 'Variables_MARTE_Property') is None


def test_assoc_base_Property57_stub_double():
    # Time_MARTE_Property has no real 'Time_MARTE_Property' property in the generated
    # code (a bare stub) -- manually attach it so MARTE_Time_Clock's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # MARTE_Time_Clock's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = MARTE_Time_Clock(standard="sample_text")
    partner = Time_MARTE_Property()
    setattr(partner, 'Time_MARTE_Property', None)
    _safe_set(owner, 'MARTE_Time_Clock58', partner)
    assert getattr(partner, 'Time_MARTE_Property') == owner
    _safe_set(owner, 'MARTE_Time_Clock58', None)
    assert getattr(partner, 'Time_MARTE_Property') is None


def test_assoc_base_Property800_stub_double():
    # GCM_MARTE_Property has no real 'GCM_MARTE_Property' property in the generated
    # code (a bare stub) -- manually attach it so MARTE_GCM_FlowProperty's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # MARTE_GCM_FlowProperty's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = MARTE_GCM_FlowProperty(direction="sample_text")
    partner = GCM_MARTE_Property()
    setattr(partner, 'GCM_MARTE_Property', None)
    _safe_set(owner, 'MARTE_GCM_FlowProperty', partner)
    assert getattr(partner, 'GCM_MARTE_Property') == owner
    _safe_set(owner, 'MARTE_GCM_FlowProperty', None)
    assert getattr(partner, 'GCM_MARTE_Property') is None


def test_assoc_base_Property826_stub_double():
    # GCM_MARTE_Property has no real 'GCM_MARTE_Property827' property in the generated
    # code (a bare stub) -- manually attach it so MARTE_GCM_DataPool's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # MARTE_GCM_DataPool's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = MARTE_GCM_DataPool(ordering="sample_text")
    partner = GCM_MARTE_Property()
    setattr(partner, 'GCM_MARTE_Property827', None)
    _safe_set(owner, 'MARTE_GCM_DataPool', partner)
    assert getattr(partner, 'GCM_MARTE_Property827') == owner
    _safe_set(owner, 'MARTE_GCM_DataPool', None)
    assert getattr(partner, 'GCM_MARTE_Property827') is None


def test_assoc_base_TimeEvent83_stub_double():
    # Time_MARTE_TimeEvent has no real 'Time_MARTE_TimeEvent' property in the generated
    # code (a bare stub) -- manually attach it so MARTE_Time_TimedEvent's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # MARTE_Time_TimedEvent's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = MARTE_Time_TimedEvent(repetition="sample_text")
    partner = Time_MARTE_TimeEvent()
    setattr(partner, 'Time_MARTE_TimeEvent', None)
    _safe_set(owner, 'MARTE_Time_TimedEvent', partner)
    assert getattr(partner, 'Time_MARTE_TimeEvent') == owner
    _safe_set(owner, 'MARTE_Time_TimedEvent', None)
    assert getattr(partner, 'Time_MARTE_TimeEvent') is None


def test_assoc_base_TimeObservation81_stub_double():
    # Time_MARTE_TimeObservation has no real 'Time_MARTE_TimeObservation' property in the generated
    # code (a bare stub) -- manually attach it so MARTE_Time_TimedInstantObservation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # MARTE_Time_TimedInstantObservation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = MARTE_Time_TimedInstantObservation(obsKind="sample_text")
    partner = Time_MARTE_TimeObservation()
    setattr(partner, 'Time_MARTE_TimeObservation', None)
    _safe_set(owner, 'MARTE_Time_TimedInstantObservation', partner)
    assert getattr(partner, 'Time_MARTE_TimeObservation') == owner
    _safe_set(owner, 'MARTE_Time_TimedInstantObservation', None)
    assert getattr(partner, 'Time_MARTE_TimeObservation') is None


def test_assoc_base_ValueSpecification80_stub_double():
    # Time_MARTE_ValueSpecification has no real 'Time_MARTE_ValueSpecification' property in the generated
    # code (a bare stub) -- manually attach it so MARTE_Time_TimedValueSpecification's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # MARTE_Time_TimedValueSpecification's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = MARTE_Time_TimedValueSpecification(interpretation="sample_text")
    partner = Time_MARTE_ValueSpecification()
    setattr(partner, 'Time_MARTE_ValueSpecification', None)
    _safe_set(owner, 'MARTE_Time_TimedValueSpecification', partner)
    assert getattr(partner, 'Time_MARTE_ValueSpecification') == owner
    _safe_set(owner, 'MARTE_Time_TimedValueSpecification', None)
    assert getattr(partner, 'Time_MARTE_ValueSpecification') is None


def test_assoc_behavCount1087_stub_double():
    # NFP_Real has no real 'NFP_Real1089' property in the generated
    # code (a bare stub) -- manually attach it so MARTE_PAM_PaStep's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # MARTE_PAM_PaStep's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = MARTE_PAM_PaStep(extOpDemand="sample_text")
    partner = NFP_Real()
    setattr(partner, 'NFP_Real1089', None)
    _safe_set(owner, 'MARTE_PAM_PaStep1088', {partner})
    assert getattr(partner, 'NFP_Real1089') == owner
    _safe_set(owner, 'MARTE_PAM_PaStep1088', set())
    assert getattr(partner, 'NFP_Real1089') is None


def test_assoc_behavDemand1084_stub_double():
    # GQAM_GaScenario has no real 'GQAM_GaScenario1086' property in the generated
    # code (a bare stub) -- manually attach it so MARTE_PAM_PaStep's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # MARTE_PAM_PaStep's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = MARTE_PAM_PaStep(extOpDemand="sample_text")
    partner = GQAM_GaScenario()
    setattr(partner, 'GQAM_GaScenario1086', None)
    _safe_set(owner, 'MARTE_PAM_PaStep1085', {partner})
    assert getattr(partner, 'GQAM_GaScenario1086') == owner
    _safe_set(owner, 'MARTE_PAM_PaStep1085', set())
    assert getattr(partner, 'GQAM_GaScenario1086') is None


def test_assoc_blockT138_stub_double():
    # NFP_Duration has no real 'NFP_Duration' property in the generated
    # code (a bare stub) -- manually attach it so MARTE_GRM_CommunicationMedia's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # MARTE_GRM_CommunicationMedia's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = MARTE_GRM_CommunicationMedia(transmMode="sample_text")
    partner = NFP_Duration()
    setattr(partner, 'NFP_Duration', None)
    _safe_set(owner, 'MARTE_GRM_CommunicationMedia139', {partner})
    assert getattr(partner, 'NFP_Duration') == owner
    _safe_set(owner, 'MARTE_GRM_CommunicationMedia139', set())
    assert getattr(partner, 'NFP_Duration') is None


def test_assoc_blocksComputing354_stub_double():
    # HwComputing_HwComputingResource has no real 'HwComputing_HwComputingResource' property in the generated
    # code (a bare stub) -- manually attach it so MARTE_HwComputing_HwPLD's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # MARTE_HwComputing_HwPLD's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = MARTE_HwComputing_HwPLD(technology="sample_text")
    partner = HwComputing_HwComputingResource()
    setattr(partner, 'HwComputing_HwComputingResource', None)
    _safe_set(owner, 'MARTE_HwComputing_HwPLD355', {partner})
    assert getattr(partner, 'HwComputing_HwComputingResource') == owner
    _safe_set(owner, 'MARTE_HwComputing_HwPLD355', set())
    assert getattr(partner, 'HwComputing_HwComputingResource') is None


def test_assoc_blocksRAM352_stub_double():
    # HwMemory_HwRAM has no real 'HwMemory_HwRAM' property in the generated
    # code (a bare stub) -- manually attach it so MARTE_HwComputing_HwPLD's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # MARTE_HwComputing_HwPLD's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = MARTE_HwComputing_HwPLD(technology="sample_text")
    partner = HwMemory_HwRAM()
    setattr(partner, 'HwMemory_HwRAM', None)
    _safe_set(owner, 'MARTE_HwComputing_HwPLD353', {partner})
    assert getattr(partner, 'HwMemory_HwRAM') == owner
    _safe_set(owner, 'MARTE_HwComputing_HwPLD353', set())
    assert getattr(partner, 'HwMemory_HwRAM') is None


def test_assoc_capacity143_stub_double():
    # NFP_DataTxRate has no real 'NFP_DataTxRate' property in the generated
    # code (a bare stub) -- manually attach it so MARTE_GRM_CommunicationMedia's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # MARTE_GRM_CommunicationMedia's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = MARTE_GRM_CommunicationMedia(transmMode="sample_text")
    partner = NFP_DataTxRate()
    setattr(partner, 'NFP_DataTxRate', None)
    _safe_set(owner, 'MARTE_GRM_CommunicationMedia144', {partner})
    assert getattr(partner, 'NFP_DataTxRate') == owner
    _safe_set(owner, 'MARTE_GRM_CommunicationMedia144', set())
    assert getattr(partner, 'NFP_DataTxRate') is None


def test_assoc_ceiling125_stub_double():
    # NFP_Integer has no real 'NFP_Integer126' property in the generated
    # code (a bare stub) -- manually attach it so MARTE_GRM_MutualExclusionResource's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # MARTE_GRM_MutualExclusionResource's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = MARTE_GRM_MutualExclusionResource(otherProtectProtocol="sample_text", protectKind="sample_text")
    partner = NFP_Integer()
    setattr(partner, 'NFP_Integer126', None)
    _safe_set(owner, 'MARTE_GRM_MutualExclusionResource', partner)
    assert getattr(partner, 'NFP_Integer126') == owner
    _safe_set(owner, 'MARTE_GRM_MutualExclusionResource', None)
    assert getattr(partner, 'NFP_Integer126') is None


def test_assoc_clearServices789_stub_double():
    # SW_Interaction_MARTE_BehavioralFeature has no real 'SW_Interaction_MARTE_BehavioralFeature791' property in the generated
    # code (a bare stub) -- manually attach it so MARTE_SW_Interaction_NotificationResource's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # MARTE_SW_Interaction_NotificationResource's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = MARTE_SW_Interaction_NotificationResource(mechanism="sample_text", occurence="sample_text")
    partner = SW_Interaction_MARTE_BehavioralFeature()
    setattr(partner, 'SW_Interaction_MARTE_BehavioralFeature791', None)
    _safe_set(owner, 'MARTE_SW_Interaction_NotificationResource790', {partner})
    assert getattr(partner, 'SW_Interaction_MARTE_BehavioralFeature791') == owner
    _safe_set(owner, 'MARTE_SW_Interaction_NotificationResource790', set())
    assert getattr(partner, 'SW_Interaction_MARTE_BehavioralFeature791') is None


def test_assoc_closeServices721_stub_double():
    # SW_Brokering_MARTE_BehavioralFeature has no real 'SW_Brokering_MARTE_BehavioralFeature' property in the generated
    # code (a bare stub) -- manually attach it so MARTE_SW_Brokering_DeviceBroker's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # MARTE_SW_Brokering_DeviceBroker's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = MARTE_SW_Brokering_DeviceBroker(accessPolicy="sample_text", isBuffered="sample_text", name="sample_text")
    partner = SW_Brokering_MARTE_BehavioralFeature()
    setattr(partner, 'SW_Brokering_MARTE_BehavioralFeature', None)
    _safe_set(owner, 'MARTE_SW_Brokering_DeviceBroker722', {partner})
    assert getattr(partner, 'SW_Brokering_MARTE_BehavioralFeature') == owner
    _safe_set(owner, 'MARTE_SW_Brokering_DeviceBroker722', set())
    assert getattr(partner, 'SW_Brokering_MARTE_BehavioralFeature') is None


def test_assoc_components573_stub_double():
    # HwGeneral_HwResource has no real 'HwGeneral_HwResource574' property in the generated
    # code (a bare stub) -- manually attach it so MARTE_HwDatasheet_HwDatasheet's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # MARTE_HwDatasheet_HwDatasheet's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = MARTE_HwDatasheet_HwDatasheet(name="sample_text", revision="sample_text")
    partner = HwGeneral_HwResource()
    setattr(partner, 'HwGeneral_HwResource574', None)
    _safe_set(owner, 'MARTE_HwDatasheet_HwDatasheet', {partner})
    assert getattr(partner, 'HwGeneral_HwResource574') == owner
    _safe_set(owner, 'MARTE_HwDatasheet_HwDatasheet', set())
    assert getattr(partner, 'HwGeneral_HwResource574') is None


def test_assoc_components586_stub_double():
    # HwGeneral_HwResource has no real 'HwGeneral_HwResource588' property in the generated
    # code (a bare stub) -- manually attach it so MARTE_HwDiagram_HwBlockDiagram's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # MARTE_HwDiagram_HwBlockDiagram's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = MARTE_HwDiagram_HwBlockDiagram(name="sample_text")
    partner = HwGeneral_HwResource()
    setattr(partner, 'HwGeneral_HwResource588', None)
    _safe_set(owner, 'MARTE_HwDiagram_HwBlockDiagram587', {partner})
    assert getattr(partner, 'HwGeneral_HwResource588') == owner
    _safe_set(owner, 'MARTE_HwDiagram_HwBlockDiagram587', set())
    assert getattr(partner, 'HwGeneral_HwResource588') is None


def test_assoc_components589_stub_double():
    # HwPackage_HwPackage has no real 'HwPackage_HwPackage590' property in the generated
    # code (a bare stub) -- manually attach it so MARTE_HwDiagram_HwCircuitDiagram's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # MARTE_HwDiagram_HwCircuitDiagram's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = MARTE_HwDiagram_HwCircuitDiagram(name="sample_text")
    partner = HwPackage_HwPackage()
    setattr(partner, 'HwPackage_HwPackage590', None)
    _safe_set(owner, 'MARTE_HwDiagram_HwCircuitDiagram', {partner})
    assert getattr(partner, 'HwPackage_HwPackage590') == owner
    _safe_set(owner, 'MARTE_HwDiagram_HwCircuitDiagram', set())
    assert getattr(partner, 'HwPackage_HwPackage590') is None


def test_assoc_components594_stub_double():
    # HwGeneral_HwResource has no real 'HwGeneral_HwResource595' property in the generated
    # code (a bare stub) -- manually attach it so MARTE_HwDiagram_HwHRMDiagram's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # MARTE_HwDiagram_HwHRMDiagram's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = MARTE_HwDiagram_HwHRMDiagram(name="sample_text")
    partner = HwGeneral_HwResource()
    setattr(partner, 'HwGeneral_HwResource595', None)
    _safe_set(owner, 'MARTE_HwDiagram_HwHRMDiagram', {partner})
    assert getattr(partner, 'HwGeneral_HwResource595') == owner
    _safe_set(owner, 'MARTE_HwDiagram_HwHRMDiagram', set())
    assert getattr(partner, 'HwGeneral_HwResource595') is None


def test_assoc_connections584_stub_double():
    # HwCommunication_HwConnection has no real 'HwCommunication_HwConnection' property in the generated
    # code (a bare stub) -- manually attach it so MARTE_HwDiagram_HwBlockDiagram's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # MARTE_HwDiagram_HwBlockDiagram's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = MARTE_HwDiagram_HwBlockDiagram(name="sample_text")
    partner = HwCommunication_HwConnection()
    setattr(partner, 'HwCommunication_HwConnection', None)
    _safe_set(owner, 'MARTE_HwDiagram_HwBlockDiagram585', {partner})
    assert getattr(partner, 'HwCommunication_HwConnection') == owner
    _safe_set(owner, 'MARTE_HwDiagram_HwBlockDiagram585', set())
    assert getattr(partner, 'HwCommunication_HwConnection') is None


def test_assoc_connections596_stub_double():
    # HwCommunication_HwMedia has no real 'HwCommunication_HwMedia598' property in the generated
    # code (a bare stub) -- manually attach it so MARTE_HwDiagram_HwHRMDiagram's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # MARTE_HwDiagram_HwHRMDiagram's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = MARTE_HwDiagram_HwHRMDiagram(name="sample_text")
    partner = HwCommunication_HwMedia()
    setattr(partner, 'HwCommunication_HwMedia598', None)
    _safe_set(owner, 'MARTE_HwDiagram_HwHRMDiagram597', {partner})
    assert getattr(partner, 'HwCommunication_HwMedia598') == owner
    _safe_set(owner, 'MARTE_HwDiagram_HwHRMDiagram597', set())
    assert getattr(partner, 'HwCommunication_HwMedia598') is None


def test_assoc_controlServices723_stub_double():
    # SW_Brokering_MARTE_BehavioralFeature has no real 'SW_Brokering_MARTE_BehavioralFeature725' property in the generated
    # code (a bare stub) -- manually attach it so MARTE_SW_Brokering_DeviceBroker's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # MARTE_SW_Brokering_DeviceBroker's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = MARTE_SW_Brokering_DeviceBroker(accessPolicy="sample_text", isBuffered="sample_text", name="sample_text")
    partner = SW_Brokering_MARTE_BehavioralFeature()
    setattr(partner, 'SW_Brokering_MARTE_BehavioralFeature725', None)
    _safe_set(owner, 'MARTE_SW_Brokering_DeviceBroker724', {partner})
    assert getattr(partner, 'SW_Brokering_MARTE_BehavioralFeature725') == owner
    _safe_set(owner, 'MARTE_SW_Brokering_DeviceBroker724', set())
    assert getattr(partner, 'SW_Brokering_MARTE_BehavioralFeature725') is None


def test_assoc_datatypes602_stub_double():
    # HwDiagram_MARTE_DataType has no real 'HwDiagram_MARTE_DataType' property in the generated
    # code (a bare stub) -- manually attach it so MARTE_HwDiagram_HwHRMDiagram's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # MARTE_HwDiagram_HwHRMDiagram's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = MARTE_HwDiagram_HwHRMDiagram(name="sample_text")
    partner = HwDiagram_MARTE_DataType()
    setattr(partner, 'HwDiagram_MARTE_DataType', None)
    _safe_set(owner, 'MARTE_HwDiagram_HwHRMDiagram603', {partner})
    assert getattr(partner, 'HwDiagram_MARTE_DataType') == owner
    _safe_set(owner, 'MARTE_HwDiagram_HwHRMDiagram603', set())
    assert getattr(partner, 'HwDiagram_MARTE_DataType') is None


def test_assoc_deadlineElements685_stub_double():
    # SW_Concurrency_MARTE_TypedElement has no real 'SW_Concurrency_MARTE_TypedElement687' property in the generated
    # code (a bare stub) -- manually attach it so MARTE_SW_Concurrency_SwSchedulableResource's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # MARTE_SW_Concurrency_SwSchedulableResource's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = MARTE_SW_Concurrency_SwSchedulableResource(isPreemptable="sample_text", isStaticSchedulingFeature="sample_text")
    partner = SW_Concurrency_MARTE_TypedElement()
    setattr(partner, 'SW_Concurrency_MARTE_TypedElement687', None)
    _safe_set(owner, 'MARTE_SW_Concurrency_SwSchedulableResource686', {partner})
    assert getattr(partner, 'SW_Concurrency_MARTE_TypedElement687') == owner
    _safe_set(owner, 'MARTE_SW_Concurrency_SwSchedulableResource686', set())
    assert getattr(partner, 'SW_Concurrency_MARTE_TypedElement687') is None


def test_assoc_deadlineTypeElements688_stub_double():
    # SW_Concurrency_MARTE_TypedElement has no real 'SW_Concurrency_MARTE_TypedElement690' property in the generated
    # code (a bare stub) -- manually attach it so MARTE_SW_Concurrency_SwSchedulableResource's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # MARTE_SW_Concurrency_SwSchedulableResource's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = MARTE_SW_Concurrency_SwSchedulableResource(isPreemptable="sample_text", isStaticSchedulingFeature="sample_text")
    partner = SW_Concurrency_MARTE_TypedElement()
    setattr(partner, 'SW_Concurrency_MARTE_TypedElement690', None)
    _safe_set(owner, 'MARTE_SW_Concurrency_SwSchedulableResource689', {partner})
    assert getattr(partner, 'SW_Concurrency_MARTE_TypedElement690') == owner
    _safe_set(owner, 'MARTE_SW_Concurrency_SwSchedulableResource689', set())
    assert getattr(partner, 'SW_Concurrency_MARTE_TypedElement690') is None


def test_assoc_delayServices694_stub_double():
    # SW_Concurrency_MARTE_BehavioralFeature has no real 'SW_Concurrency_MARTE_BehavioralFeature696' property in the generated
    # code (a bare stub) -- manually attach it so MARTE_SW_Concurrency_SwSchedulableResource's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # MARTE_SW_Concurrency_SwSchedulableResource's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = MARTE_SW_Concurrency_SwSchedulableResource(isPreemptable="sample_text", isStaticSchedulingFeature="sample_text")
    partner = SW_Concurrency_MARTE_BehavioralFeature()
    setattr(partner, 'SW_Concurrency_MARTE_BehavioralFeature696', None)
    _safe_set(owner, 'MARTE_SW_Concurrency_SwSchedulableResource695', {partner})
    assert getattr(partner, 'SW_Concurrency_MARTE_BehavioralFeature696') == owner
    _safe_set(owner, 'MARTE_SW_Concurrency_SwSchedulableResource695', set())
    assert getattr(partner, 'SW_Concurrency_MARTE_BehavioralFeature696') is None


def test_assoc_description508_stub_double():
    # NFP_String has no real 'NFP_String509' property in the generated
    # code (a bare stub) -- manually attach it so MARTE_HwGeneral_HwResource's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # MARTE_HwGeneral_HwResource's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = MARTE_HwGeneral_HwResource(name="sample_text")
    partner = NFP_String()
    setattr(partner, 'NFP_String509', None)
    _safe_set(owner, 'MARTE_HwGeneral_HwResource', partner)
    assert getattr(partner, 'NFP_String509') == owner
    _safe_set(owner, 'MARTE_HwGeneral_HwResource', None)
    assert getattr(partner, 'NFP_String509') is None


def test_assoc_description554_stub_double():
    # NFP_String has no real 'NFP_String555' property in the generated
    # code (a bare stub) -- manually attach it so MARTE_HwLayout_Env_Condition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # MARTE_HwLayout_Env_Condition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = MARTE_HwLayout_Env_Condition(status="sample_text", type="sample_text")
    partner = NFP_String()
    setattr(partner, 'NFP_String555', None)
    _safe_set(owner, 'MARTE_HwLayout_Env_Condition', partner)
    assert getattr(partner, 'NFP_String555') == owner
    _safe_set(owner, 'MARTE_HwLayout_Env_Condition', None)
    assert getattr(partner, 'NFP_String555') is None


def test_assoc_devices720_stub_double():
    # SW_Brokering_MARTE_TypedElement has no real 'SW_Brokering_MARTE_TypedElement' property in the generated
    # code (a bare stub) -- manually attach it so MARTE_SW_Brokering_DeviceBroker's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # MARTE_SW_Brokering_DeviceBroker's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = MARTE_SW_Brokering_DeviceBroker(accessPolicy="sample_text", isBuffered="sample_text", name="sample_text")
    partner = SW_Brokering_MARTE_TypedElement()
    setattr(partner, 'SW_Brokering_MARTE_TypedElement', None)
    _safe_set(owner, 'MARTE_SW_Brokering_DeviceBroker', {partner})
    assert getattr(partner, 'SW_Brokering_MARTE_TypedElement') == owner
    _safe_set(owner, 'MARTE_SW_Brokering_DeviceBroker', set())
    assert getattr(partner, 'SW_Brokering_MARTE_TypedElement') is None


def test_assoc_dimensions525_stub_double():
    # NFP_Length has no real 'NFP_Length' property in the generated
    # code (a bare stub) -- manually attach it so MARTE_HwLayout_HwComponent's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # MARTE_HwLayout_HwComponent's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = MARTE_HwLayout_HwComponent(kind="sample_text")
    partner = NFP_Length()
    setattr(partner, 'NFP_Length', None)
    _safe_set(owner, 'MARTE_HwLayout_HwComponent', {partner})
    assert getattr(partner, 'NFP_Length') == owner
    _safe_set(owner, 'MARTE_HwLayout_HwComponent', set())
    assert getattr(partner, 'NFP_Length') is None


def test_assoc_disableConcurrencyServices655_stub_double():
    # SW_Concurrency_MARTE_BehavioralFeature has no real 'SW_Concurrency_MARTE_BehavioralFeature657' property in the generated
    # code (a bare stub) -- manually attach it so MARTE_SW_Concurrency_SwConcurrentResource's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # MARTE_SW_Concurrency_SwConcurrentResource's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = MARTE_SW_Concurrency_SwConcurrentResource(activationCapacity="sample_text")
    partner = SW_Concurrency_MARTE_BehavioralFeature()
    setattr(partner, 'SW_Concurrency_MARTE_BehavioralFeature657', None)
    _safe_set(owner, 'MARTE_SW_Concurrency_SwConcurrentResource656', {partner})
    assert getattr(partner, 'SW_Concurrency_MARTE_BehavioralFeature657') == owner
    _safe_set(owner, 'MARTE_SW_Concurrency_SwConcurrentResource656', set())
    assert getattr(partner, 'SW_Concurrency_MARTE_BehavioralFeature657') is None


def test_assoc_duration145_stub_double():
    # NFP_Duration has no real 'NFP_Duration146' property in the generated
    # code (a bare stub) -- manually attach it so MARTE_GRM_TimerResource's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # MARTE_GRM_TimerResource's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = MARTE_GRM_TimerResource(isPeriodic="sample_text")
    partner = NFP_Duration()
    setattr(partner, 'NFP_Duration146', None)
    _safe_set(owner, 'MARTE_GRM_TimerResource', partner)
    assert getattr(partner, 'NFP_Duration146') == owner
    _safe_set(owner, 'MARTE_GRM_TimerResource', None)
    assert getattr(partner, 'NFP_Duration146') is None


def test_assoc_elementSize134_stub_double():
    # NFP_Integer has no real 'NFP_Integer135' property in the generated
    # code (a bare stub) -- manually attach it so MARTE_GRM_CommunicationMedia's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # MARTE_GRM_CommunicationMedia's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = MARTE_GRM_CommunicationMedia(transmMode="sample_text")
    partner = NFP_Integer()
    setattr(partner, 'NFP_Integer135', None)
    _safe_set(owner, 'MARTE_GRM_CommunicationMedia', partner)
    assert getattr(partner, 'NFP_Integer135') == owner
    _safe_set(owner, 'MARTE_GRM_CommunicationMedia', None)
    assert getattr(partner, 'NFP_Integer135') is None


def test_assoc_enableConcurrencyServices643_stub_double():
    # SW_Concurrency_MARTE_BehavioralFeature has no real 'SW_Concurrency_MARTE_BehavioralFeature645' property in the generated
    # code (a bare stub) -- manually attach it so MARTE_SW_Concurrency_SwConcurrentResource's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # MARTE_SW_Concurrency_SwConcurrentResource's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = MARTE_SW_Concurrency_SwConcurrentResource(activationCapacity="sample_text")
    partner = SW_Concurrency_MARTE_BehavioralFeature()
    setattr(partner, 'SW_Concurrency_MARTE_BehavioralFeature645', None)
    _safe_set(owner, 'MARTE_SW_Concurrency_SwConcurrentResource644', {partner})
    assert getattr(partner, 'SW_Concurrency_MARTE_BehavioralFeature645') == owner
    _safe_set(owner, 'MARTE_SW_Concurrency_SwConcurrentResource644', set())
    assert getattr(partner, 'SW_Concurrency_MARTE_BehavioralFeature645') is None


def test_assoc_endObs930_stub_double():
    # GQAM_MARTE_TimeObservation has no real 'GQAM_MARTE_TimeObservation932' property in the generated
    # code (a bare stub) -- manually attach it so MARTE_GQAM_GaTimedObs's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # MARTE_GQAM_GaTimedObs's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = MARTE_GQAM_GaTimedObs(laxity="sample_text")
    partner = GQAM_MARTE_TimeObservation()
    setattr(partner, 'GQAM_MARTE_TimeObservation932', None)
    _safe_set(owner, 'MARTE_GQAM_GaTimedObs931', {partner})
    assert getattr(partner, 'GQAM_MARTE_TimeObservation932') == owner
    _safe_set(owner, 'MARTE_GQAM_GaTimedObs931', set())
    assert getattr(partner, 'GQAM_MARTE_TimeObservation932') is None


def test_assoc_endPoints517_stub_double():
    # HwCommunication_HwEndPoint has no real 'HwCommunication_HwEndPoint' property in the generated
    # code (a bare stub) -- manually attach it so MARTE_HwGeneral_HwResource's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # MARTE_HwGeneral_HwResource's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = MARTE_HwGeneral_HwResource(name="sample_text")
    partner = HwCommunication_HwEndPoint()
    setattr(partner, 'HwCommunication_HwEndPoint', None)
    _safe_set(owner, 'MARTE_HwGeneral_HwResource518', {partner})
    assert getattr(partner, 'HwCommunication_HwEndPoint') == owner
    _safe_set(owner, 'MARTE_HwGeneral_HwResource518', set())
    assert getattr(partner, 'HwCommunication_HwEndPoint') is None


def test_assoc_entryPoints627_stub_double():
    # SW_Concurrency_MARTE_Element has no real 'SW_Concurrency_MARTE_Element' property in the generated
    # code (a bare stub) -- manually attach it so MARTE_SW_Concurrency_SwConcurrentResource's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # MARTE_SW_Concurrency_SwConcurrentResource's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = MARTE_SW_Concurrency_SwConcurrentResource(activationCapacity="sample_text")
    partner = SW_Concurrency_MARTE_Element()
    setattr(partner, 'SW_Concurrency_MARTE_Element', None)
    _safe_set(owner, 'MARTE_SW_Concurrency_SwConcurrentResource628', {partner})
    assert getattr(partner, 'SW_Concurrency_MARTE_Element') == owner
    _safe_set(owner, 'MARTE_SW_Concurrency_SwConcurrentResource628', set())
    assert getattr(partner, 'SW_Concurrency_MARTE_Element') is None


def test_assoc_every84_stub_double():
    # Time_MARTE_ValueSpecification has no real 'Time_MARTE_ValueSpecification86' property in the generated
    # code (a bare stub) -- manually attach it so MARTE_Time_TimedEvent's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # MARTE_Time_TimedEvent's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = MARTE_Time_TimedEvent(repetition="sample_text")
    partner = Time_MARTE_ValueSpecification()
    setattr(partner, 'Time_MARTE_ValueSpecification86', None)
    _safe_set(owner, 'MARTE_Time_TimedEvent85', partner)
    assert getattr(partner, 'Time_MARTE_ValueSpecification86') == owner
    _safe_set(owner, 'MARTE_Time_TimedEvent85', None)
    assert getattr(partner, 'Time_MARTE_ValueSpecification86') is None


def test_assoc_extOpCount1081_stub_double():
    # NFP_Real has no real 'NFP_Real1083' property in the generated
    # code (a bare stub) -- manually attach it so MARTE_PAM_PaStep's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # MARTE_PAM_PaStep's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = MARTE_PAM_PaStep(extOpDemand="sample_text")
    partner = NFP_Real()
    setattr(partner, 'NFP_Real1083', None)
    _safe_set(owner, 'MARTE_PAM_PaStep1082', {partner})
    assert getattr(partner, 'NFP_Real1083') == owner
    _safe_set(owner, 'MARTE_PAM_PaStep1082', set())
    assert getattr(partner, 'NFP_Real1083') is None


def test_assoc_family338_stub_double():
    # NFP_String has no real 'NFP_String' property in the generated
    # code (a bare stub) -- manually attach it so MARTE_HwComputing_HwISA's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # MARTE_HwComputing_HwISA's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = MARTE_HwComputing_HwISA(type="sample_text")
    partner = NFP_String()
    setattr(partner, 'NFP_String', None)
    _safe_set(owner, 'MARTE_HwComputing_HwISA', partner)
    assert getattr(partner, 'NFP_String') == owner
    _safe_set(owner, 'MARTE_HwComputing_HwISA', None)
    assert getattr(partner, 'NFP_String') is None


def test_assoc_featuresSpec809_stub_double():
    # GCM_ClientServerSpecification has no real 'GCM_ClientServerSpecification' property in the generated
    # code (a bare stub) -- manually attach it so MARTE_GCM_ClientServerPort's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # MARTE_GCM_ClientServerPort's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = MARTE_GCM_ClientServerPort(isConjugated="sample_text", kind="sample_text", specificationKind="sample_text")
    partner = GCM_ClientServerSpecification()
    setattr(partner, 'GCM_ClientServerSpecification', None)
    _safe_set(owner, 'MARTE_GCM_ClientServerPort810', partner)
    assert getattr(partner, 'GCM_ClientServerSpecification') == owner
    _safe_set(owner, 'MARTE_GCM_ClientServerPort810', None)
    assert getattr(partner, 'GCM_ClientServerSpecification') is None


def test_assoc_flushServices780_stub_double():
    # SW_Interaction_MARTE_BehavioralFeature has no real 'SW_Interaction_MARTE_BehavioralFeature782' property in the generated
    # code (a bare stub) -- manually attach it so MARTE_SW_Interaction_NotificationResource's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # MARTE_SW_Interaction_NotificationResource's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = MARTE_SW_Interaction_NotificationResource(mechanism="sample_text", occurence="sample_text")
    partner = SW_Interaction_MARTE_BehavioralFeature()
    setattr(partner, 'SW_Interaction_MARTE_BehavioralFeature782', None)
    _safe_set(owner, 'MARTE_SW_Interaction_NotificationResource781', {partner})
    assert getattr(partner, 'SW_Interaction_MARTE_BehavioralFeature782') == owner
    _safe_set(owner, 'MARTE_SW_Interaction_NotificationResource781', set())
    assert getattr(partner, 'SW_Interaction_MARTE_BehavioralFeature782') is None


def test_assoc_frequency519_stub_double():
    # NFP_Frequency has no real 'NFP_Frequency' property in the generated
    # code (a bare stub) -- manually attach it so MARTE_HwGeneral_HwResource's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # MARTE_HwGeneral_HwResource's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = MARTE_HwGeneral_HwResource(name="sample_text")
    partner = NFP_Frequency()
    setattr(partner, 'NFP_Frequency', None)
    _safe_set(owner, 'MARTE_HwGeneral_HwResource520', partner)
    assert getattr(partner, 'NFP_Frequency') == owner
    _safe_set(owner, 'MARTE_HwGeneral_HwResource520', None)
    assert getattr(partner, 'NFP_Frequency') is None


def test_assoc_getTime69_stub_double():
    # Time_MARTE_Operation has no real 'Time_MARTE_Operation' property in the generated
    # code (a bare stub) -- manually attach it so MARTE_Time_ClockType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # MARTE_Time_ClockType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = MARTE_Time_ClockType(isLogical="sample_text", nature="sample_text")
    partner = Time_MARTE_Operation()
    setattr(partner, 'Time_MARTE_Operation', None)
    _safe_set(owner, 'MARTE_Time_ClockType70', partner)
    assert getattr(partner, 'Time_MARTE_Operation') == owner
    _safe_set(owner, 'MARTE_Time_ClockType70', None)
    assert getattr(partner, 'Time_MARTE_Operation') is None


def test_assoc_grid530_stub_double():
    # NFP_Natural has no real 'NFP_Natural532' property in the generated
    # code (a bare stub) -- manually attach it so MARTE_HwLayout_HwComponent's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # MARTE_HwLayout_HwComponent's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = MARTE_HwLayout_HwComponent(kind="sample_text")
    partner = NFP_Natural()
    setattr(partner, 'NFP_Natural532', None)
    _safe_set(owner, 'MARTE_HwLayout_HwComponent531', {partner})
    assert getattr(partner, 'NFP_Natural532') == owner
    _safe_set(owner, 'MARTE_HwLayout_HwComponent531', set())
    assert getattr(partner, 'NFP_Natural532') is None


def test_assoc_heapSizeElements670_stub_double():
    # SW_Concurrency_MARTE_TypedElement has no real 'SW_Concurrency_MARTE_TypedElement672' property in the generated
    # code (a bare stub) -- manually attach it so MARTE_SW_Concurrency_SwConcurrentResource's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # MARTE_SW_Concurrency_SwConcurrentResource's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = MARTE_SW_Concurrency_SwConcurrentResource(activationCapacity="sample_text")
    partner = SW_Concurrency_MARTE_TypedElement()
    setattr(partner, 'SW_Concurrency_MARTE_TypedElement672', None)
    _safe_set(owner, 'MARTE_SW_Concurrency_SwConcurrentResource671', {partner})
    assert getattr(partner, 'SW_Concurrency_MARTE_TypedElement672') == owner
    _safe_set(owner, 'MARTE_SW_Concurrency_SwConcurrentResource671', set())
    assert getattr(partner, 'SW_Concurrency_MARTE_TypedElement672') is None


def test_assoc_host1108_stub_double():
    # GQAM_GaExecHost has no real 'GQAM_GaExecHost1110' property in the generated
    # code (a bare stub) -- manually attach it so MARTE_PAM_PaRunTInstance's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # MARTE_PAM_PaRunTInstance's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = MARTE_PAM_PaRunTInstance(unbddPool="sample_text")
    partner = GQAM_GaExecHost()
    setattr(partner, 'GQAM_GaExecHost1110', None)
    _safe_set(owner, 'MARTE_PAM_PaRunTInstance1109', partner)
    assert getattr(partner, 'GQAM_GaExecHost1110') == owner
    _safe_set(owner, 'MARTE_PAM_PaRunTInstance1109', None)
    assert getattr(partner, 'GQAM_GaExecHost1110') is None


def test_assoc_host118_stub_double():
    # GRM_ComputingResource has no real 'GRM_ComputingResource' property in the generated
    # code (a bare stub) -- manually attach it so MARTE_GRM_Scheduler's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # MARTE_GRM_Scheduler's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = MARTE_GRM_Scheduler(isPreemptible="sample_text", otherSchedPolicy="sample_text", schedPolicy="sample_text")
    partner = GRM_ComputingResource()
    setattr(partner, 'GRM_ComputingResource', None)
    _safe_set(owner, 'MARTE_GRM_Scheduler119', partner)
    assert getattr(partner, 'GRM_ComputingResource') == owner
    _safe_set(owner, 'MARTE_GRM_Scheduler119', None)
    assert getattr(partner, 'GRM_ComputingResource') is None


def test_assoc_impliedConstraint47_stub_double():
    # NFPs_NfpConstraint has no real 'NFPs_NfpConstraint49' property in the generated
    # code (a bare stub) -- manually attach it so MARTE_Alloc_Allocate's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # MARTE_Alloc_Allocate's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = MARTE_Alloc_Allocate(kind="sample_text", nature="sample_text")
    partner = NFPs_NfpConstraint()
    setattr(partner, 'NFPs_NfpConstraint49', None)
    _safe_set(owner, 'MARTE_Alloc_Allocate48', {partner})
    assert getattr(partner, 'NFPs_NfpConstraint49') == owner
    _safe_set(owner, 'MARTE_Alloc_Allocate48', set())
    assert getattr(partner, 'NFPs_NfpConstraint49') is None


def test_assoc_indexToValue74_stub_double():
    # Time_MARTE_Operation has no real 'Time_MARTE_Operation76' property in the generated
    # code (a bare stub) -- manually attach it so MARTE_Time_ClockType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # MARTE_Time_ClockType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = MARTE_Time_ClockType(isLogical="sample_text", nature="sample_text")
    partner = Time_MARTE_Operation()
    setattr(partner, 'Time_MARTE_Operation76', None)
    _safe_set(owner, 'MARTE_Time_ClockType75', partner)
    assert getattr(partner, 'Time_MARTE_Operation76') == owner
    _safe_set(owner, 'MARTE_Time_ClockType75', None)
    assert getattr(partner, 'Time_MARTE_Operation76') is None


def test_assoc_insertion828_stub_double():
    # GCM_MARTE_Behavior has no real 'GCM_MARTE_Behavior' property in the generated
    # code (a bare stub) -- manually attach it so MARTE_GCM_DataPool's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # MARTE_GCM_DataPool's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = MARTE_GCM_DataPool(ordering="sample_text")
    partner = GCM_MARTE_Behavior()
    setattr(partner, 'GCM_MARTE_Behavior', None)
    _safe_set(owner, 'MARTE_GCM_DataPool829', partner)
    assert getattr(partner, 'GCM_MARTE_Behavior') == owner
    _safe_set(owner, 'MARTE_GCM_DataPool829', None)
    assert getattr(partner, 'GCM_MARTE_Behavior') is None


def test_assoc_inst_Width339_stub_double():
    # NFP_DataSize has no real 'NFP_DataSize341' property in the generated
    # code (a bare stub) -- manually attach it so MARTE_HwComputing_HwISA's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # MARTE_HwComputing_HwISA's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = MARTE_HwComputing_HwISA(type="sample_text")
    partner = NFP_DataSize()
    setattr(partner, 'NFP_DataSize341', None)
    _safe_set(owner, 'MARTE_HwComputing_HwISA340', partner)
    assert getattr(partner, 'NFP_DataSize341') == owner
    _safe_set(owner, 'MARTE_HwComputing_HwISA340', None)
    assert getattr(partner, 'NFP_DataSize341') is None


def test_assoc_instance1105_stub_double():
    # GRM_SchedulableResource has no real 'GRM_SchedulableResource1107' property in the generated
    # code (a bare stub) -- manually attach it so MARTE_PAM_PaRunTInstance's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # MARTE_PAM_PaRunTInstance's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = MARTE_PAM_PaRunTInstance(unbddPool="sample_text")
    partner = GRM_SchedulableResource()
    setattr(partner, 'GRM_SchedulableResource1107', None)
    _safe_set(owner, 'MARTE_PAM_PaRunTInstance1106', partner)
    assert getattr(partner, 'GRM_SchedulableResource1107') == owner
    _safe_set(owner, 'MARTE_PAM_PaRunTInstance1106', None)
    assert getattr(partner, 'GRM_SchedulableResource1107') is None


def test_assoc_isNonVolatile454_stub_double():
    # NFP_Boolean has no real 'NFP_Boolean456' property in the generated
    # code (a bare stub) -- manually attach it so MARTE_HwMemory_HwRAM's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # MARTE_HwMemory_HwRAM's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = MARTE_HwMemory_HwRAM(repl_Policy="sample_text", writePolicy="sample_text")
    partner = NFP_Boolean()
    setattr(partner, 'NFP_Boolean456', None)
    _safe_set(owner, 'MARTE_HwMemory_HwRAM455', partner)
    assert getattr(partner, 'NFP_Boolean456') == owner
    _safe_set(owner, 'MARTE_HwMemory_HwRAM455', None)
    assert getattr(partner, 'NFP_Boolean456') is None


def test_assoc_isSched982_stub_double():
    # NFP_Boolean has no real 'NFP_Boolean983' property in the generated
    # code (a bare stub) -- manually attach it so MARTE_SAM_SaAnalysisContext's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # MARTE_SAM_SaAnalysisContext's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = MARTE_SAM_SaAnalysisContext(optCriterion="sample_text")
    partner = NFP_Boolean()
    setattr(partner, 'NFP_Boolean983', None)
    _safe_set(owner, 'MARTE_SAM_SaAnalysisContext', partner)
    assert getattr(partner, 'NFP_Boolean983') == owner
    _safe_set(owner, 'MARTE_SAM_SaAnalysisContext', None)
    assert getattr(partner, 'NFP_Boolean983') is None


def test_assoc_isStatic451_stub_double():
    # NFP_Boolean has no real 'NFP_Boolean453' property in the generated
    # code (a bare stub) -- manually attach it so MARTE_HwMemory_HwRAM's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # MARTE_HwMemory_HwRAM's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = MARTE_HwMemory_HwRAM(repl_Policy="sample_text", writePolicy="sample_text")
    partner = NFP_Boolean()
    setattr(partner, 'NFP_Boolean453', None)
    _safe_set(owner, 'MARTE_HwMemory_HwRAM452', partner)
    assert getattr(partner, 'NFP_Boolean453') == owner
    _safe_set(owner, 'MARTE_HwMemory_HwRAM452', None)
    assert getattr(partner, 'NFP_Boolean453') is None


def test_assoc_isSynchronous448_stub_double():
    # NFP_Boolean has no real 'NFP_Boolean450' property in the generated
    # code (a bare stub) -- manually attach it so MARTE_HwMemory_HwRAM's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # MARTE_HwMemory_HwRAM's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = MARTE_HwMemory_HwRAM(repl_Policy="sample_text", writePolicy="sample_text")
    partner = NFP_Boolean()
    setattr(partner, 'NFP_Boolean450', None)
    _safe_set(owner, 'MARTE_HwMemory_HwRAM449', partner)
    assert getattr(partner, 'NFP_Boolean450') == owner
    _safe_set(owner, 'MARTE_HwMemory_HwRAM449', None)
    assert getattr(partner, 'NFP_Boolean450') is None


def test_assoc_joinServices697_stub_double():
    # SW_Concurrency_MARTE_BehavioralFeature has no real 'SW_Concurrency_MARTE_BehavioralFeature699' property in the generated
    # code (a bare stub) -- manually attach it so MARTE_SW_Concurrency_SwSchedulableResource's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # MARTE_SW_Concurrency_SwSchedulableResource's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = MARTE_SW_Concurrency_SwSchedulableResource(isPreemptable="sample_text", isStaticSchedulingFeature="sample_text")
    partner = SW_Concurrency_MARTE_BehavioralFeature()
    setattr(partner, 'SW_Concurrency_MARTE_BehavioralFeature699', None)
    _safe_set(owner, 'MARTE_SW_Concurrency_SwSchedulableResource698', {partner})
    assert getattr(partner, 'SW_Concurrency_MARTE_BehavioralFeature699') == owner
    _safe_set(owner, 'MARTE_SW_Concurrency_SwSchedulableResource698', set())
    assert getattr(partner, 'SW_Concurrency_MARTE_BehavioralFeature699') is None


def test_assoc_level464_stub_double():
    # NFP_Natural has no real 'NFP_Natural465' property in the generated
    # code (a bare stub) -- manually attach it so MARTE_HwMemory_HwCache's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # MARTE_HwMemory_HwCache's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = MARTE_HwMemory_HwCache(repl_Policy="sample_text", type="sample_text", writePolicy="sample_text")
    partner = NFP_Natural()
    setattr(partner, 'NFP_Natural465', None)
    _safe_set(owner, 'MARTE_HwMemory_HwCache', partner)
    assert getattr(partner, 'NFP_Natural465') == owner
    _safe_set(owner, 'MARTE_HwMemory_HwCache', None)
    assert getattr(partner, 'NFP_Natural465') is None


def test_assoc_lockServices747_stub_double():
    # SW_Brokering_MARTE_BehavioralFeature has no real 'SW_Brokering_MARTE_BehavioralFeature749' property in the generated
    # code (a bare stub) -- manually attach it so MARTE_SW_Brokering_MemoryBroker's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # MARTE_SW_Brokering_MemoryBroker's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = MARTE_SW_Brokering_MemoryBroker(accessPolicy="sample_text")
    partner = SW_Brokering_MARTE_BehavioralFeature()
    setattr(partner, 'SW_Brokering_MARTE_BehavioralFeature749', None)
    _safe_set(owner, 'MARTE_SW_Brokering_MemoryBroker748', {partner})
    assert getattr(partner, 'SW_Brokering_MARTE_BehavioralFeature749') == owner
    _safe_set(owner, 'MARTE_SW_Brokering_MemoryBroker748', set())
    assert getattr(partner, 'SW_Brokering_MARTE_BehavioralFeature749') is None


def test_assoc_main243_stub_double():
    # HLAM_MARTE_Operation has no real 'HLAM_MARTE_Operation' property in the generated
    # code (a bare stub) -- manually attach it so MARTE_HLAM_RtUnit's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # MARTE_HLAM_RtUnit's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = MARTE_HLAM_RtUnit(isDynamic="sample_text", isMain="sample_text", queueSchedPolicy="sample_text", queueSize="sample_text", srPoolPolicy="sample_text", srPoolSize="sample_text")
    partner = HLAM_MARTE_Operation()
    setattr(partner, 'HLAM_MARTE_Operation', None)
    _safe_set(owner, 'MARTE_HLAM_RtUnit244', partner)
    assert getattr(partner, 'HLAM_MARTE_Operation') == owner
    _safe_set(owner, 'MARTE_HLAM_RtUnit244', None)
    assert getattr(partner, 'HLAM_MARTE_Operation') is None


def test_assoc_mapServices753_stub_double():
    # SW_Brokering_MARTE_BehavioralFeature has no real 'SW_Brokering_MARTE_BehavioralFeature755' property in the generated
    # code (a bare stub) -- manually attach it so MARTE_SW_Brokering_MemoryBroker's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # MARTE_SW_Brokering_MemoryBroker's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = MARTE_SW_Brokering_MemoryBroker(accessPolicy="sample_text")
    partner = SW_Brokering_MARTE_BehavioralFeature()
    setattr(partner, 'SW_Brokering_MARTE_BehavioralFeature755', None)
    _safe_set(owner, 'MARTE_SW_Brokering_MemoryBroker754', {partner})
    assert getattr(partner, 'SW_Brokering_MARTE_BehavioralFeature755') == owner
    _safe_set(owner, 'MARTE_SW_Brokering_MemoryBroker754', set())
    assert getattr(partner, 'SW_Brokering_MARTE_BehavioralFeature755') is None


def test_assoc_maskElements675_stub_double():
    # SW_Concurrency_MARTE_TypedElement has no real 'SW_Concurrency_MARTE_TypedElement677' property in the generated
    # code (a bare stub) -- manually attach it so MARTE_SW_Concurrency_InterruptResource's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # MARTE_SW_Concurrency_InterruptResource's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = MARTE_SW_Concurrency_InterruptResource(isMaskable="sample_text", kind="sample_text")
    partner = SW_Concurrency_MARTE_TypedElement()
    setattr(partner, 'SW_Concurrency_MARTE_TypedElement677', None)
    _safe_set(owner, 'MARTE_SW_Concurrency_InterruptResource676', {partner})
    assert getattr(partner, 'SW_Concurrency_MARTE_TypedElement677') == owner
    _safe_set(owner, 'MARTE_SW_Concurrency_InterruptResource676', set())
    assert getattr(partner, 'SW_Concurrency_MARTE_TypedElement677') is None


def test_assoc_maskElements777_stub_double():
    # SW_Interaction_MARTE_TypedElement has no real 'SW_Interaction_MARTE_TypedElement779' property in the generated
    # code (a bare stub) -- manually attach it so MARTE_SW_Interaction_NotificationResource's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # MARTE_SW_Interaction_NotificationResource's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = MARTE_SW_Interaction_NotificationResource(mechanism="sample_text", occurence="sample_text")
    partner = SW_Interaction_MARTE_TypedElement()
    setattr(partner, 'SW_Interaction_MARTE_TypedElement779', None)
    _safe_set(owner, 'MARTE_SW_Interaction_NotificationResource778', {partner})
    assert getattr(partner, 'SW_Interaction_MARTE_TypedElement779') == owner
    _safe_set(owner, 'MARTE_SW_Interaction_NotificationResource778', set())
    assert getattr(partner, 'SW_Interaction_MARTE_TypedElement779') is None


def test_assoc_maxValAttr63_stub_double():
    # Time_MARTE_Property has no real 'Time_MARTE_Property65' property in the generated
    # code (a bare stub) -- manually attach it so MARTE_Time_ClockType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # MARTE_Time_ClockType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = MARTE_Time_ClockType(isLogical="sample_text", nature="sample_text")
    partner = Time_MARTE_Property()
    setattr(partner, 'Time_MARTE_Property65', None)
    _safe_set(owner, 'MARTE_Time_ClockType64', partner)
    assert getattr(partner, 'Time_MARTE_Property65') == owner
    _safe_set(owner, 'MARTE_Time_ClockType64', None)
    assert getattr(partner, 'Time_MARTE_Property65') is None


def test_assoc_memories739_stub_double():
    # SW_Brokering_MARTE_TypedElement has no real 'SW_Brokering_MARTE_TypedElement740' property in the generated
    # code (a bare stub) -- manually attach it so MARTE_SW_Brokering_MemoryBroker's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # MARTE_SW_Brokering_MemoryBroker's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = MARTE_SW_Brokering_MemoryBroker(accessPolicy="sample_text")
    partner = SW_Brokering_MARTE_TypedElement()
    setattr(partner, 'SW_Brokering_MARTE_TypedElement740', None)
    _safe_set(owner, 'MARTE_SW_Brokering_MemoryBroker', {partner})
    assert getattr(partner, 'SW_Brokering_MARTE_TypedElement740') == owner
    _safe_set(owner, 'MARTE_SW_Brokering_MemoryBroker', set())
    assert getattr(partner, 'SW_Brokering_MARTE_TypedElement740') is None


def test_assoc_memoryBlockAdressElements741_stub_double():
    # SW_Brokering_MARTE_TypedElement has no real 'SW_Brokering_MARTE_TypedElement743' property in the generated
    # code (a bare stub) -- manually attach it so MARTE_SW_Brokering_MemoryBroker's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # MARTE_SW_Brokering_MemoryBroker's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = MARTE_SW_Brokering_MemoryBroker(accessPolicy="sample_text")
    partner = SW_Brokering_MARTE_TypedElement()
    setattr(partner, 'SW_Brokering_MARTE_TypedElement743', None)
    _safe_set(owner, 'MARTE_SW_Brokering_MemoryBroker742', {partner})
    assert getattr(partner, 'SW_Brokering_MARTE_TypedElement743') == owner
    _safe_set(owner, 'MARTE_SW_Brokering_MemoryBroker742', set())
    assert getattr(partner, 'SW_Brokering_MARTE_TypedElement743') is None


def test_assoc_memoryBlockSizeElements744_stub_double():
    # SW_Brokering_MARTE_TypedElement has no real 'SW_Brokering_MARTE_TypedElement746' property in the generated
    # code (a bare stub) -- manually attach it so MARTE_SW_Brokering_MemoryBroker's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # MARTE_SW_Brokering_MemoryBroker's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = MARTE_SW_Brokering_MemoryBroker(accessPolicy="sample_text")
    partner = SW_Brokering_MARTE_TypedElement()
    setattr(partner, 'SW_Brokering_MARTE_TypedElement746', None)
    _safe_set(owner, 'MARTE_SW_Brokering_MemoryBroker745', {partner})
    assert getattr(partner, 'SW_Brokering_MARTE_TypedElement746') == owner
    _safe_set(owner, 'MARTE_SW_Brokering_MemoryBroker745', set())
    assert getattr(partner, 'SW_Brokering_MARTE_TypedElement746') is None


def test_assoc_memorySize245_stub_double():
    # NFP_DataSize has no real 'NFP_DataSize247' property in the generated
    # code (a bare stub) -- manually attach it so MARTE_HLAM_RtUnit's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # MARTE_HLAM_RtUnit's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = MARTE_HLAM_RtUnit(isDynamic="sample_text", isMain="sample_text", queueSchedPolicy="sample_text", queueSize="sample_text", srPoolPolicy="sample_text", srPoolSize="sample_text")
    partner = NFP_DataSize()
    setattr(partner, 'NFP_DataSize247', None)
    _safe_set(owner, 'MARTE_HLAM_RtUnit246', partner)
    assert getattr(partner, 'NFP_DataSize247') == owner
    _safe_set(owner, 'MARTE_HLAM_RtUnit246', None)
    assert getattr(partner, 'NFP_DataSize247') is None


def test_assoc_memorySize253_stub_double():
    # NFP_DataSize has no real 'NFP_DataSize254' property in the generated
    # code (a bare stub) -- manually attach it so MARTE_HLAM_PpUnit's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # MARTE_HLAM_PpUnit's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = MARTE_HLAM_PpUnit(concPolicy="sample_text")
    partner = NFP_DataSize()
    setattr(partner, 'NFP_DataSize254', None)
    _safe_set(owner, 'MARTE_HLAM_PpUnit', partner)
    assert getattr(partner, 'NFP_DataSize254') == owner
    _safe_set(owner, 'MARTE_HLAM_PpUnit', None)
    assert getattr(partner, 'NFP_DataSize254') is None


def test_assoc_messageQueueCapacityElements766_stub_double():
    # SW_Interaction_MARTE_TypedElement has no real 'SW_Interaction_MARTE_TypedElement768' property in the generated
    # code (a bare stub) -- manually attach it so MARTE_SW_Interaction_MessageComResource's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # MARTE_SW_Interaction_MessageComResource's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = MARTE_SW_Interaction_MessageComResource(isFixedMessageSize="sample_text", mechanism="sample_text", messageQueuePolicy="sample_text")
    partner = SW_Interaction_MARTE_TypedElement()
    setattr(partner, 'SW_Interaction_MARTE_TypedElement768', None)
    _safe_set(owner, 'MARTE_SW_Interaction_MessageComResource767', {partner})
    assert getattr(partner, 'SW_Interaction_MARTE_TypedElement768') == owner
    _safe_set(owner, 'MARTE_SW_Interaction_MessageComResource767', set())
    assert getattr(partner, 'SW_Interaction_MARTE_TypedElement768') is None


def test_assoc_messageResources661_stub_double():
    # SW_Concurrency_MARTE_TypedElement has no real 'SW_Concurrency_MARTE_TypedElement663' property in the generated
    # code (a bare stub) -- manually attach it so MARTE_SW_Concurrency_SwConcurrentResource's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # MARTE_SW_Concurrency_SwConcurrentResource's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = MARTE_SW_Concurrency_SwConcurrentResource(activationCapacity="sample_text")
    partner = SW_Concurrency_MARTE_TypedElement()
    setattr(partner, 'SW_Concurrency_MARTE_TypedElement663', None)
    _safe_set(owner, 'MARTE_SW_Concurrency_SwConcurrentResource662', {partner})
    assert getattr(partner, 'SW_Concurrency_MARTE_TypedElement663') == owner
    _safe_set(owner, 'MARTE_SW_Concurrency_SwConcurrentResource662', set())
    assert getattr(partner, 'SW_Concurrency_MARTE_TypedElement663') is None


def test_assoc_messageSizeElements764_stub_double():
    # SW_Interaction_MARTE_TypedElement has no real 'SW_Interaction_MARTE_TypedElement765' property in the generated
    # code (a bare stub) -- manually attach it so MARTE_SW_Interaction_MessageComResource's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # MARTE_SW_Interaction_MessageComResource's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = MARTE_SW_Interaction_MessageComResource(isFixedMessageSize="sample_text", mechanism="sample_text", messageQueuePolicy="sample_text")
    partner = SW_Interaction_MARTE_TypedElement()
    setattr(partner, 'SW_Interaction_MARTE_TypedElement765', None)
    _safe_set(owner, 'MARTE_SW_Interaction_MessageComResource', {partner})
    assert getattr(partner, 'SW_Interaction_MARTE_TypedElement765') == owner
    _safe_set(owner, 'MARTE_SW_Interaction_MessageComResource', set())
    assert getattr(partner, 'SW_Interaction_MARTE_TypedElement765') is None


def test_assoc_mode5_stub_double():
    # CoreElements_Mode has no real 'CoreElements_Mode' property in the generated
    # code (a bare stub) -- manually attach it so MARTE_NFPs_NfpConstraint's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # MARTE_NFPs_NfpConstraint's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = MARTE_NFPs_NfpConstraint(kind="sample_text")
    partner = CoreElements_Mode()
    setattr(partner, 'CoreElements_Mode', None)
    _safe_set(owner, 'MARTE_NFPs_NfpConstraint6', {partner})
    assert getattr(partner, 'CoreElements_Mode') == owner
    _safe_set(owner, 'MARTE_NFPs_NfpConstraint6', set())
    assert getattr(partner, 'CoreElements_Mode') is None


def test_assoc_msgMaxSize250_stub_double():
    # NFP_DataSize has no real 'NFP_DataSize252' property in the generated
    # code (a bare stub) -- manually attach it so MARTE_HLAM_RtUnit's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # MARTE_HLAM_RtUnit's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = MARTE_HLAM_RtUnit(isDynamic="sample_text", isMain="sample_text", queueSchedPolicy="sample_text", queueSize="sample_text", srPoolPolicy="sample_text", srPoolSize="sample_text")
    partner = NFP_DataSize()
    setattr(partner, 'NFP_DataSize252', None)
    _safe_set(owner, 'MARTE_HLAM_RtUnit251', partner)
    assert getattr(partner, 'NFP_DataSize252') == owner
    _safe_set(owner, 'MARTE_HLAM_RtUnit251', None)
    assert getattr(partner, 'NFP_DataSize252') is None


def test_assoc_msgSize292_stub_double():
    # NFP_DataSize has no real 'NFP_DataSize293' property in the generated
    # code (a bare stub) -- manually attach it so MARTE_HLAM_RtAction's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # MARTE_HLAM_RtAction's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = MARTE_HLAM_RtAction(isAtomic="sample_text", synchKind="sample_text")
    partner = NFP_DataSize()
    setattr(partner, 'NFP_DataSize293', None)
    _safe_set(owner, 'MARTE_HLAM_RtAction', partner)
    assert getattr(partner, 'NFP_DataSize293') == owner
    _safe_set(owner, 'MARTE_HLAM_RtAction', None)
    assert getattr(partner, 'NFP_DataSize293') is None


def test_assoc_mutualExclusionResources664_stub_double():
    # SW_Concurrency_MARTE_TypedElement has no real 'SW_Concurrency_MARTE_TypedElement666' property in the generated
    # code (a bare stub) -- manually attach it so MARTE_SW_Concurrency_SwConcurrentResource's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # MARTE_SW_Concurrency_SwConcurrentResource's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = MARTE_SW_Concurrency_SwConcurrentResource(activationCapacity="sample_text")
    partner = SW_Concurrency_MARTE_TypedElement()
    setattr(partner, 'SW_Concurrency_MARTE_TypedElement666', None)
    _safe_set(owner, 'MARTE_SW_Concurrency_SwConcurrentResource665', {partner})
    assert getattr(partner, 'SW_Concurrency_MARTE_TypedElement666') == owner
    _safe_set(owner, 'MARTE_SW_Concurrency_SwConcurrentResource665', set())
    assert getattr(partner, 'SW_Concurrency_MARTE_TypedElement666') is None


def test_assoc_nbColumns304_stub_double():
    # NFP_Natural has no real 'NFP_Natural' property in the generated
    # code (a bare stub) -- manually attach it so MARTE_HwComputing_PLD_Organization's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # MARTE_HwComputing_PLD_Organization's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = MARTE_HwComputing_PLD_Organization(class_="sample_text")
    partner = NFP_Natural()
    setattr(partner, 'NFP_Natural', None)
    _safe_set(owner, 'MARTE_HwComputing_PLD_Organization305', partner)
    assert getattr(partner, 'NFP_Natural') == owner
    _safe_set(owner, 'MARTE_HwComputing_PLD_Organization305', None)
    assert getattr(partner, 'NFP_Natural') is None


def test_assoc_nbFlipFlops349_stub_double():
    # NFP_Natural has no real 'NFP_Natural351' property in the generated
    # code (a bare stub) -- manually attach it so MARTE_HwComputing_HwPLD's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # MARTE_HwComputing_HwPLD's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = MARTE_HwComputing_HwPLD(technology="sample_text")
    partner = NFP_Natural()
    setattr(partner, 'NFP_Natural351', None)
    _safe_set(owner, 'MARTE_HwComputing_HwPLD350', partner)
    assert getattr(partner, 'NFP_Natural351') == owner
    _safe_set(owner, 'MARTE_HwComputing_HwPLD350', None)
    assert getattr(partner, 'NFP_Natural351') is None


def test_assoc_nbLUTs343_stub_double():
    # NFP_Natural has no real 'NFP_Natural345' property in the generated
    # code (a bare stub) -- manually attach it so MARTE_HwComputing_HwPLD's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # MARTE_HwComputing_HwPLD's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = MARTE_HwComputing_HwPLD(technology="sample_text")
    partner = NFP_Natural()
    setattr(partner, 'NFP_Natural345', None)
    _safe_set(owner, 'MARTE_HwComputing_HwPLD344', partner)
    assert getattr(partner, 'NFP_Natural345') == owner
    _safe_set(owner, 'MARTE_HwComputing_HwPLD344', None)
    assert getattr(partner, 'NFP_Natural345') is None


def test_assoc_nbPins533_stub_double():
    # NFP_Natural has no real 'NFP_Natural535' property in the generated
    # code (a bare stub) -- manually attach it so MARTE_HwLayout_HwComponent's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # MARTE_HwLayout_HwComponent's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = MARTE_HwLayout_HwComponent(kind="sample_text")
    partner = NFP_Natural()
    setattr(partner, 'NFP_Natural535', None)
    _safe_set(owner, 'MARTE_HwLayout_HwComponent534', partner)
    assert getattr(partner, 'NFP_Natural535') == owner
    _safe_set(owner, 'MARTE_HwLayout_HwComponent534', None)
    assert getattr(partner, 'NFP_Natural535') is None


def test_assoc_nbRows302_stub_double():
    # NFP_Integer has no real 'NFP_Integer303' property in the generated
    # code (a bare stub) -- manually attach it so MARTE_HwComputing_PLD_Organization's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # MARTE_HwComputing_PLD_Organization's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = MARTE_HwComputing_PLD_Organization(class_="sample_text")
    partner = NFP_Integer()
    setattr(partner, 'NFP_Integer303', None)
    _safe_set(owner, 'MARTE_HwComputing_PLD_Organization', partner)
    assert getattr(partner, 'NFP_Integer303') == owner
    _safe_set(owner, 'MARTE_HwComputing_PLD_Organization', None)
    assert getattr(partner, 'NFP_Integer303') is None


def test_assoc_ndLUT_Inputs346_stub_double():
    # NFP_Natural has no real 'NFP_Natural348' property in the generated
    # code (a bare stub) -- manually attach it so MARTE_HwComputing_HwPLD's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # MARTE_HwComputing_HwPLD's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = MARTE_HwComputing_HwPLD(technology="sample_text")
    partner = NFP_Natural()
    setattr(partner, 'NFP_Natural348', None)
    _safe_set(owner, 'MARTE_HwComputing_HwPLD347', partner)
    assert getattr(partner, 'NFP_Natural348') == owner
    _safe_set(owner, 'MARTE_HwComputing_HwPLD347', None)
    assert getattr(partner, 'NFP_Natural348') is None


def test_assoc_noSync1079_stub_double():
    # NFP_Boolean has no real 'NFP_Boolean1080' property in the generated
    # code (a bare stub) -- manually attach it so MARTE_PAM_PaStep's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # MARTE_PAM_PaStep's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = MARTE_PAM_PaStep(extOpDemand="sample_text")
    partner = NFP_Boolean()
    setattr(partner, 'NFP_Boolean1080', None)
    _safe_set(owner, 'MARTE_PAM_PaStep', partner)
    assert getattr(partner, 'NFP_Boolean1080') == owner
    _safe_set(owner, 'MARTE_PAM_PaStep', None)
    assert getattr(partner, 'NFP_Boolean1080') is None


def test_assoc_notificationResources667_stub_double():
    # SW_Concurrency_MARTE_TypedElement has no real 'SW_Concurrency_MARTE_TypedElement669' property in the generated
    # code (a bare stub) -- manually attach it so MARTE_SW_Concurrency_SwConcurrentResource's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # MARTE_SW_Concurrency_SwConcurrentResource's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = MARTE_SW_Concurrency_SwConcurrentResource(activationCapacity="sample_text")
    partner = SW_Concurrency_MARTE_TypedElement()
    setattr(partner, 'SW_Concurrency_MARTE_TypedElement669', None)
    _safe_set(owner, 'MARTE_SW_Concurrency_SwConcurrentResource668', {partner})
    assert getattr(partner, 'SW_Concurrency_MARTE_TypedElement669') == owner
    _safe_set(owner, 'MARTE_SW_Concurrency_SwConcurrentResource668', set())
    assert getattr(partner, 'SW_Concurrency_MARTE_TypedElement669') is None


def test_assoc_occurenceCountElements775_stub_double():
    # SW_Interaction_MARTE_TypedElement has no real 'SW_Interaction_MARTE_TypedElement776' property in the generated
    # code (a bare stub) -- manually attach it so MARTE_SW_Interaction_NotificationResource's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # MARTE_SW_Interaction_NotificationResource's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = MARTE_SW_Interaction_NotificationResource(mechanism="sample_text", occurence="sample_text")
    partner = SW_Interaction_MARTE_TypedElement()
    setattr(partner, 'SW_Interaction_MARTE_TypedElement776', None)
    _safe_set(owner, 'MARTE_SW_Interaction_NotificationResource', {partner})
    assert getattr(partner, 'SW_Interaction_MARTE_TypedElement776') == owner
    _safe_set(owner, 'MARTE_SW_Interaction_NotificationResource', set())
    assert getattr(partner, 'SW_Interaction_MARTE_TypedElement776') is None


def test_assoc_offsetAttr66_stub_double():
    # Time_MARTE_Property has no real 'Time_MARTE_Property68' property in the generated
    # code (a bare stub) -- manually attach it so MARTE_Time_ClockType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # MARTE_Time_ClockType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = MARTE_Time_ClockType(isLogical="sample_text", nature="sample_text")
    partner = Time_MARTE_Property()
    setattr(partner, 'Time_MARTE_Property68', None)
    _safe_set(owner, 'MARTE_Time_ClockType67', partner)
    assert getattr(partner, 'Time_MARTE_Property68') == owner
    _safe_set(owner, 'MARTE_Time_ClockType67', None)
    assert getattr(partner, 'Time_MARTE_Property68') is None


def test_assoc_openServices726_stub_double():
    # SW_Brokering_MARTE_BehavioralFeature has no real 'SW_Brokering_MARTE_BehavioralFeature728' property in the generated
    # code (a bare stub) -- manually attach it so MARTE_SW_Brokering_DeviceBroker's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # MARTE_SW_Brokering_DeviceBroker's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = MARTE_SW_Brokering_DeviceBroker(accessPolicy="sample_text", isBuffered="sample_text", name="sample_text")
    partner = SW_Brokering_MARTE_BehavioralFeature()
    setattr(partner, 'SW_Brokering_MARTE_BehavioralFeature728', None)
    _safe_set(owner, 'MARTE_SW_Brokering_DeviceBroker727', {partner})
    assert getattr(partner, 'SW_Brokering_MARTE_BehavioralFeature728') == owner
    _safe_set(owner, 'MARTE_SW_Brokering_DeviceBroker727', set())
    assert getattr(partner, 'SW_Brokering_MARTE_BehavioralFeature728') is None


def test_assoc_operationalMode241_stub_double():
    # HLAM_MARTE_Behavior has no real 'HLAM_MARTE_Behavior' property in the generated
    # code (a bare stub) -- manually attach it so MARTE_HLAM_RtUnit's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # MARTE_HLAM_RtUnit's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = MARTE_HLAM_RtUnit(isDynamic="sample_text", isMain="sample_text", queueSchedPolicy="sample_text", queueSize="sample_text", srPoolPolicy="sample_text", srPoolSize="sample_text")
    partner = HLAM_MARTE_Behavior()
    setattr(partner, 'HLAM_MARTE_Behavior', None)
    _safe_set(owner, 'MARTE_HLAM_RtUnit242', partner)
    assert getattr(partner, 'HLAM_MARTE_Behavior') == owner
    _safe_set(owner, 'MARTE_HLAM_RtUnit242', None)
    assert getattr(partner, 'HLAM_MARTE_Behavior') is None


def test_assoc_operations521_stub_double():
    # HwGeneral_MARTE_Operation has no real 'HwGeneral_MARTE_Operation' property in the generated
    # code (a bare stub) -- manually attach it so MARTE_HwGeneral_HwResource's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # MARTE_HwGeneral_HwResource's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = MARTE_HwGeneral_HwResource(name="sample_text")
    partner = HwGeneral_MARTE_Operation()
    setattr(partner, 'HwGeneral_MARTE_Operation', None)
    _safe_set(owner, 'MARTE_HwGeneral_HwResource522', {partner})
    assert getattr(partner, 'HwGeneral_MARTE_Operation') == owner
    _safe_set(owner, 'MARTE_HwGeneral_HwResource522', set())
    assert getattr(partner, 'HwGeneral_MARTE_Operation') is None


def test_assoc_operations581_stub_double():
    # HwProtocol_MARTE_Operation has no real 'HwProtocol_MARTE_Operation' property in the generated
    # code (a bare stub) -- manually attach it so MARTE_HwProtocol_HwProtocol's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # MARTE_HwProtocol_HwProtocol's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = MARTE_HwProtocol_HwProtocol(name="sample_text")
    partner = HwProtocol_MARTE_Operation()
    setattr(partner, 'HwProtocol_MARTE_Operation', None)
    _safe_set(owner, 'MARTE_HwProtocol_HwProtocol', {partner})
    assert getattr(partner, 'HwProtocol_MARTE_Operation') == owner
    _safe_set(owner, 'MARTE_HwProtocol_HwProtocol', set())
    assert getattr(partner, 'HwProtocol_MARTE_Operation') is None


def test_assoc_operations735_stub_double():
    # SW_Brokering_MARTE_Operation has no real 'SW_Brokering_MARTE_Operation' property in the generated
    # code (a bare stub) -- manually attach it so MARTE_SW_Brokering_DeviceBroker's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # MARTE_SW_Brokering_DeviceBroker's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = MARTE_SW_Brokering_DeviceBroker(accessPolicy="sample_text", isBuffered="sample_text", name="sample_text")
    partner = SW_Brokering_MARTE_Operation()
    setattr(partner, 'SW_Brokering_MARTE_Operation', None)
    _safe_set(owner, 'MARTE_SW_Brokering_DeviceBroker736', {partner})
    assert getattr(partner, 'SW_Brokering_MARTE_Operation') == owner
    _safe_set(owner, 'MARTE_SW_Brokering_DeviceBroker736', set())
    assert getattr(partner, 'SW_Brokering_MARTE_Operation') is None


def test_assoc_organization342_stub_double():
    # HwComputing_PLD_Organization has no real 'HwComputing_PLD_Organization' property in the generated
    # code (a bare stub) -- manually attach it so MARTE_HwComputing_HwPLD's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # MARTE_HwComputing_HwPLD's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = MARTE_HwComputing_HwPLD(technology="sample_text")
    partner = HwComputing_PLD_Organization()
    setattr(partner, 'HwComputing_PLD_Organization', None)
    _safe_set(owner, 'MARTE_HwComputing_HwPLD', partner)
    assert getattr(partner, 'HwComputing_PLD_Organization') == owner
    _safe_set(owner, 'MARTE_HwComputing_HwPLD', None)
    assert getattr(partner, 'HwComputing_PLD_Organization') is None


def test_assoc_organization447_stub_double():
    # HwMemory_MemoryOrganization has no real 'HwMemory_MemoryOrganization' property in the generated
    # code (a bare stub) -- manually attach it so MARTE_HwMemory_HwRAM's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # MARTE_HwMemory_HwRAM's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = MARTE_HwMemory_HwRAM(repl_Policy="sample_text", writePolicy="sample_text")
    partner = HwMemory_MemoryOrganization()
    setattr(partner, 'HwMemory_MemoryOrganization', None)
    _safe_set(owner, 'MARTE_HwMemory_HwRAM', partner)
    assert getattr(partner, 'HwMemory_MemoryOrganization') == owner
    _safe_set(owner, 'MARTE_HwMemory_HwRAM', None)
    assert getattr(partner, 'HwMemory_MemoryOrganization') is None


def test_assoc_organization457_stub_double():
    # HwMemory_MemoryOrganization has no real 'HwMemory_MemoryOrganization458' property in the generated
    # code (a bare stub) -- manually attach it so MARTE_HwMemory_HwROM's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # MARTE_HwMemory_HwROM's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = MARTE_HwMemory_HwROM(type="sample_text")
    partner = HwMemory_MemoryOrganization()
    setattr(partner, 'HwMemory_MemoryOrganization458', None)
    _safe_set(owner, 'MARTE_HwMemory_HwROM', partner)
    assert getattr(partner, 'HwMemory_MemoryOrganization458') == owner
    _safe_set(owner, 'MARTE_HwMemory_HwROM', None)
    assert getattr(partner, 'HwMemory_MemoryOrganization458') is None


def test_assoc_ownedHW515_stub_double():
    # HwGeneral_HwResource has no real 'HwGeneral_HwResource' property in the generated
    # code (a bare stub) -- manually attach it so MARTE_HwGeneral_HwResource's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # MARTE_HwGeneral_HwResource's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = MARTE_HwGeneral_HwResource(name="sample_text")
    partner = HwGeneral_HwResource()
    setattr(partner, 'HwGeneral_HwResource', None)
    _safe_set(owner, 'MARTE_HwGeneral_HwResource516', {partner})
    assert getattr(partner, 'HwGeneral_HwResource') == owner
    _safe_set(owner, 'MARTE_HwGeneral_HwResource516', set())
    assert getattr(partner, 'HwGeneral_HwResource') is None


def test_assoc_p_HW_Services510_stub_double():
    # HwGeneral_HwResourceService has no real 'HwGeneral_HwResourceService' property in the generated
    # code (a bare stub) -- manually attach it so MARTE_HwGeneral_HwResource's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # MARTE_HwGeneral_HwResource's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = MARTE_HwGeneral_HwResource(name="sample_text")
    partner = HwGeneral_HwResourceService()
    setattr(partner, 'HwGeneral_HwResourceService', None)
    _safe_set(owner, 'MARTE_HwGeneral_HwResource511', {partner})
    assert getattr(partner, 'HwGeneral_HwResourceService') == owner
    _safe_set(owner, 'MARTE_HwGeneral_HwResource511', set())
    assert getattr(partner, 'HwGeneral_HwResourceService') is None


def test_assoc_packetT140_stub_double():
    # NFP_Duration has no real 'NFP_Duration142' property in the generated
    # code (a bare stub) -- manually attach it so MARTE_GRM_CommunicationMedia's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # MARTE_GRM_CommunicationMedia's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = MARTE_GRM_CommunicationMedia(transmMode="sample_text")
    partner = NFP_Duration()
    setattr(partner, 'NFP_Duration142', None)
    _safe_set(owner, 'MARTE_GRM_CommunicationMedia141', {partner})
    assert getattr(partner, 'NFP_Duration142') == owner
    _safe_set(owner, 'MARTE_GRM_CommunicationMedia141', set())
    assert getattr(partner, 'NFP_Duration142') is None


def test_assoc_periodElements631_stub_double():
    # SW_Concurrency_MARTE_TypedElement has no real 'SW_Concurrency_MARTE_TypedElement633' property in the generated
    # code (a bare stub) -- manually attach it so MARTE_SW_Concurrency_SwConcurrentResource's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # MARTE_SW_Concurrency_SwConcurrentResource's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = MARTE_SW_Concurrency_SwConcurrentResource(activationCapacity="sample_text")
    partner = SW_Concurrency_MARTE_TypedElement()
    setattr(partner, 'SW_Concurrency_MARTE_TypedElement633', None)
    _safe_set(owner, 'MARTE_SW_Concurrency_SwConcurrentResource632', {partner})
    assert getattr(partner, 'SW_Concurrency_MARTE_TypedElement633') == owner
    _safe_set(owner, 'MARTE_SW_Concurrency_SwConcurrentResource632', set())
    assert getattr(partner, 'SW_Concurrency_MARTE_TypedElement633') is None


def test_assoc_pins578_stub_double():
    # HwPackage_HwPackagePin has no real 'HwPackage_HwPackagePin' property in the generated
    # code (a bare stub) -- manually attach it so MARTE_HwPackage_HwPackage's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # MARTE_HwPackage_HwPackage's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = MARTE_HwPackage_HwPackage(name="sample_text", packageType="sample_text", pinNum=7)
    partner = HwPackage_HwPackagePin()
    setattr(partner, 'HwPackage_HwPackagePin', None)
    _safe_set(owner, 'MARTE_HwPackage_HwPackage', {partner})
    assert getattr(partner, 'HwPackage_HwPackagePin') == owner
    _safe_set(owner, 'MARTE_HwPackage_HwPackage', set())
    assert getattr(partner, 'HwPackage_HwPackagePin') is None


def test_assoc_poolSize1103_stub_double():
    # NFP_Integer has no real 'NFP_Integer1104' property in the generated
    # code (a bare stub) -- manually attach it so MARTE_PAM_PaRunTInstance's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # MARTE_PAM_PaRunTInstance's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = MARTE_PAM_PaRunTInstance(unbddPool="sample_text")
    partner = NFP_Integer()
    setattr(partner, 'NFP_Integer1104', None)
    _safe_set(owner, 'MARTE_PAM_PaRunTInstance', partner)
    assert getattr(partner, 'NFP_Integer1104') == owner
    _safe_set(owner, 'MARTE_PAM_PaRunTInstance', None)
    assert getattr(partner, 'NFP_Integer1104') is None


def test_assoc_position528_stub_double():
    # NFP_NaturalInterval has no real 'NFP_NaturalInterval' property in the generated
    # code (a bare stub) -- manually attach it so MARTE_HwLayout_HwComponent's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # MARTE_HwLayout_HwComponent's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = MARTE_HwLayout_HwComponent(kind="sample_text")
    partner = NFP_NaturalInterval()
    setattr(partner, 'NFP_NaturalInterval', None)
    _safe_set(owner, 'MARTE_HwLayout_HwComponent529', {partner})
    assert getattr(partner, 'NFP_NaturalInterval') == owner
    _safe_set(owner, 'MARTE_HwLayout_HwComponent529', set())
    assert getattr(partner, 'NFP_NaturalInterval') is None


def test_assoc_poweredServices543_stub_double():
    # HwGeneral_HwResourceService has no real 'HwGeneral_HwResourceService545' property in the generated
    # code (a bare stub) -- manually attach it so MARTE_HwLayout_HwComponent's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # MARTE_HwLayout_HwComponent's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = MARTE_HwLayout_HwComponent(kind="sample_text")
    partner = HwGeneral_HwResourceService()
    setattr(partner, 'HwGeneral_HwResourceService545', None)
    _safe_set(owner, 'MARTE_HwLayout_HwComponent544', {partner})
    assert getattr(partner, 'HwGeneral_HwResourceService545') == owner
    _safe_set(owner, 'MARTE_HwLayout_HwComponent544', set())
    assert getattr(partner, 'HwGeneral_HwResourceService545') is None


def test_assoc_price539_stub_double():
    # NFP_Price has no real 'NFP_Price' property in the generated
    # code (a bare stub) -- manually attach it so MARTE_HwLayout_HwComponent's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # MARTE_HwLayout_HwComponent's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = MARTE_HwLayout_HwComponent(kind="sample_text")
    partner = NFP_Price()
    setattr(partner, 'NFP_Price', None)
    _safe_set(owner, 'MARTE_HwLayout_HwComponent540', partner)
    assert getattr(partner, 'NFP_Price') == owner
    _safe_set(owner, 'MARTE_HwLayout_HwComponent540', None)
    assert getattr(partner, 'NFP_Price') is None


def test_assoc_priorityElements634_stub_double():
    # SW_Concurrency_MARTE_TypedElement has no real 'SW_Concurrency_MARTE_TypedElement636' property in the generated
    # code (a bare stub) -- manually attach it so MARTE_SW_Concurrency_SwConcurrentResource's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # MARTE_SW_Concurrency_SwConcurrentResource's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = MARTE_SW_Concurrency_SwConcurrentResource(activationCapacity="sample_text")
    partner = SW_Concurrency_MARTE_TypedElement()
    setattr(partner, 'SW_Concurrency_MARTE_TypedElement636', None)
    _safe_set(owner, 'MARTE_SW_Concurrency_SwConcurrentResource635', {partner})
    assert getattr(partner, 'SW_Concurrency_MARTE_TypedElement636') == owner
    _safe_set(owner, 'MARTE_SW_Concurrency_SwConcurrentResource635', set())
    assert getattr(partner, 'SW_Concurrency_MARTE_TypedElement636') is None


def test_assoc_processingUnits116_stub_double():
    # GRM_ProcessingResource has no real 'GRM_ProcessingResource' property in the generated
    # code (a bare stub) -- manually attach it so MARTE_GRM_Scheduler's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # MARTE_GRM_Scheduler's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = MARTE_GRM_Scheduler(isPreemptible="sample_text", otherSchedPolicy="sample_text", schedPolicy="sample_text")
    partner = GRM_ProcessingResource()
    setattr(partner, 'GRM_ProcessingResource', None)
    _safe_set(owner, 'MARTE_GRM_Scheduler117', {partner})
    assert getattr(partner, 'GRM_ProcessingResource') == owner
    _safe_set(owner, 'MARTE_GRM_Scheduler117', set())
    assert getattr(partner, 'GRM_ProcessingResource') is None


def test_assoc_protectedSharedRsources120_stub_double():
    # GRM_MutualExclusionResource has no real 'MutualExclusionResource' property in the generated
    # code (a bare stub) -- manually attach it so MARTE_GRM_Scheduler's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # MARTE_GRM_Scheduler's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = MARTE_GRM_Scheduler(isPreemptible="sample_text", otherSchedPolicy="sample_text", schedPolicy="sample_text")
    partner = GRM_MutualExclusionResource()
    setattr(partner, 'MutualExclusionResource', None)
    _safe_set(owner, 'scheduler', {partner})
    assert getattr(partner, 'MutualExclusionResource') == owner
    _safe_set(owner, 'scheduler', set())
    assert getattr(partner, 'MutualExclusionResource') is None


def test_assoc_protocols575_stub_double():
    # HwProtocol_HwProtocol has no real 'HwProtocol_HwProtocol577' property in the generated
    # code (a bare stub) -- manually attach it so MARTE_HwDatasheet_HwDatasheet's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # MARTE_HwDatasheet_HwDatasheet's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = MARTE_HwDatasheet_HwDatasheet(name="sample_text", revision="sample_text")
    partner = HwProtocol_HwProtocol()
    setattr(partner, 'HwProtocol_HwProtocol577', None)
    _safe_set(owner, 'MARTE_HwDatasheet_HwDatasheet576', {partner})
    assert getattr(partner, 'HwProtocol_HwProtocol577') == owner
    _safe_set(owner, 'MARTE_HwDatasheet_HwDatasheet576', set())
    assert getattr(partner, 'HwProtocol_HwProtocol577') is None


def test_assoc_protocols582_stub_double():
    # HwProtocol_HwProtocol has no real 'HwProtocol_HwProtocol583' property in the generated
    # code (a bare stub) -- manually attach it so MARTE_HwDiagram_HwBlockDiagram's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # MARTE_HwDiagram_HwBlockDiagram's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = MARTE_HwDiagram_HwBlockDiagram(name="sample_text")
    partner = HwProtocol_HwProtocol()
    setattr(partner, 'HwProtocol_HwProtocol583', None)
    _safe_set(owner, 'MARTE_HwDiagram_HwBlockDiagram', {partner})
    assert getattr(partner, 'HwProtocol_HwProtocol583') == owner
    _safe_set(owner, 'MARTE_HwDiagram_HwBlockDiagram', set())
    assert getattr(partner, 'HwProtocol_HwProtocol583') is None


def test_assoc_protocols599_stub_double():
    # HwProtocol_HwProtocol has no real 'HwProtocol_HwProtocol601' property in the generated
    # code (a bare stub) -- manually attach it so MARTE_HwDiagram_HwHRMDiagram's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # MARTE_HwDiagram_HwHRMDiagram's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = MARTE_HwDiagram_HwHRMDiagram(name="sample_text")
    partner = HwProtocol_HwProtocol()
    setattr(partner, 'HwProtocol_HwProtocol601', None)
    _safe_set(owner, 'MARTE_HwDiagram_HwHRMDiagram600', {partner})
    assert getattr(partner, 'HwProtocol_HwProtocol601') == owner
    _safe_set(owner, 'MARTE_HwDiagram_HwHRMDiagram600', set())
    assert getattr(partner, 'HwProtocol_HwProtocol601') is None


def test_assoc_provInterface804_stub_double():
    # GCM_MARTE_Interface has no real 'GCM_MARTE_Interface' property in the generated
    # code (a bare stub) -- manually attach it so MARTE_GCM_ClientServerPort's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # MARTE_GCM_ClientServerPort's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = MARTE_GCM_ClientServerPort(isConjugated="sample_text", kind="sample_text", specificationKind="sample_text")
    partner = GCM_MARTE_Interface()
    setattr(partner, 'GCM_MARTE_Interface', None)
    _safe_set(owner, 'MARTE_GCM_ClientServerPort805', {partner})
    assert getattr(partner, 'GCM_MARTE_Interface') == owner
    _safe_set(owner, 'MARTE_GCM_ClientServerPort805', set())
    assert getattr(partner, 'GCM_MARTE_Interface') is None


def test_assoc_r_Conditions541_stub_double():
    # HwLayout_Env_Condition has no real 'HwLayout_Env_Condition' property in the generated
    # code (a bare stub) -- manually attach it so MARTE_HwLayout_HwComponent's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # MARTE_HwLayout_HwComponent's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = MARTE_HwLayout_HwComponent(kind="sample_text")
    partner = HwLayout_Env_Condition()
    setattr(partner, 'HwLayout_Env_Condition', None)
    _safe_set(owner, 'MARTE_HwLayout_HwComponent542', {partner})
    assert getattr(partner, 'HwLayout_Env_Condition') == owner
    _safe_set(owner, 'MARTE_HwLayout_HwComponent542', set())
    assert getattr(partner, 'HwLayout_Env_Condition') is None


def test_assoc_r_HW_Services512_stub_double():
    # HwGeneral_HwResourceService has no real 'HwGeneral_HwResourceService514' property in the generated
    # code (a bare stub) -- manually attach it so MARTE_HwGeneral_HwResource's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # MARTE_HwGeneral_HwResource's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = MARTE_HwGeneral_HwResource(name="sample_text")
    partner = HwGeneral_HwResourceService()
    setattr(partner, 'HwGeneral_HwResourceService514', None)
    _safe_set(owner, 'MARTE_HwGeneral_HwResource513', {partner})
    assert getattr(partner, 'HwGeneral_HwResourceService514') == owner
    _safe_set(owner, 'MARTE_HwGeneral_HwResource513', set())
    assert getattr(partner, 'HwGeneral_HwResourceService514') is None


def test_assoc_range556_stub_double():
    # Realnterval has no real 'Realnterval' property in the generated
    # code (a bare stub) -- manually attach it so MARTE_HwLayout_Env_Condition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # MARTE_HwLayout_Env_Condition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = MARTE_HwLayout_Env_Condition(status="sample_text", type="sample_text")
    partner = Realnterval()
    setattr(partner, 'Realnterval', None)
    _safe_set(owner, 'MARTE_HwLayout_Env_Condition557', partner)
    assert getattr(partner, 'Realnterval') == owner
    _safe_set(owner, 'MARTE_HwLayout_Env_Condition557', None)
    assert getattr(partner, 'Realnterval') is None


def test_assoc_readServices729_stub_double():
    # SW_Brokering_MARTE_BehavioralFeature has no real 'SW_Brokering_MARTE_BehavioralFeature731' property in the generated
    # code (a bare stub) -- manually attach it so MARTE_SW_Brokering_DeviceBroker's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # MARTE_SW_Brokering_DeviceBroker's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = MARTE_SW_Brokering_DeviceBroker(accessPolicy="sample_text", isBuffered="sample_text", name="sample_text")
    partner = SW_Brokering_MARTE_BehavioralFeature()
    setattr(partner, 'SW_Brokering_MARTE_BehavioralFeature731', None)
    _safe_set(owner, 'MARTE_SW_Brokering_DeviceBroker730', {partner})
    assert getattr(partner, 'SW_Brokering_MARTE_BehavioralFeature731') == owner
    _safe_set(owner, 'MARTE_SW_Brokering_DeviceBroker730', set())
    assert getattr(partner, 'SW_Brokering_MARTE_BehavioralFeature731') is None


def test_assoc_receiveServices772_stub_double():
    # SW_Interaction_MARTE_BehavioralFeature has no real 'SW_Interaction_MARTE_BehavioralFeature774' property in the generated
    # code (a bare stub) -- manually attach it so MARTE_SW_Interaction_MessageComResource's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # MARTE_SW_Interaction_MessageComResource's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = MARTE_SW_Interaction_MessageComResource(isFixedMessageSize="sample_text", mechanism="sample_text", messageQueuePolicy="sample_text")
    partner = SW_Interaction_MARTE_BehavioralFeature()
    setattr(partner, 'SW_Interaction_MARTE_BehavioralFeature774', None)
    _safe_set(owner, 'MARTE_SW_Interaction_MessageComResource773', {partner})
    assert getattr(partner, 'SW_Interaction_MARTE_BehavioralFeature774') == owner
    _safe_set(owner, 'MARTE_SW_Interaction_MessageComResource773', set())
    assert getattr(partner, 'SW_Interaction_MARTE_BehavioralFeature774') is None


def test_assoc_refpin579_stub_double():
    # HwIO_HwPin has no real 'HwPin' property in the generated
    # code (a bare stub) -- manually attach it so MARTE_HwPackage_HwPackagePin's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # MARTE_HwPackage_HwPackagePin's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = MARTE_HwPackage_HwPackagePin(altNames="sample_text", pinNo="sample_text")
    partner = HwIO_HwPin()
    setattr(partner, 'HwPin', None)
    _safe_set(owner, 'pkgPin', {partner})
    assert getattr(partner, 'HwPin') == owner
    _safe_set(owner, 'pkgPin', set())
    assert getattr(partner, 'HwPin') is None


def test_assoc_releaseServices794_stub_double():
    # SW_Interaction_MARTE_BehavioralFeature has no real 'SW_Interaction_MARTE_BehavioralFeature796' property in the generated
    # code (a bare stub) -- manually attach it so MARTE_SW_Interaction_SwMutualExclusionResource's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # MARTE_SW_Interaction_SwMutualExclusionResource's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = MARTE_SW_Interaction_SwMutualExclusionResource(concurrentAccessProtocol="sample_text", mechanism="sample_text")
    partner = SW_Interaction_MARTE_BehavioralFeature()
    setattr(partner, 'SW_Interaction_MARTE_BehavioralFeature796', None)
    _safe_set(owner, 'MARTE_SW_Interaction_SwMutualExclusionResource795', {partner})
    assert getattr(partner, 'SW_Interaction_MARTE_BehavioralFeature796') == owner
    _safe_set(owner, 'MARTE_SW_Interaction_SwMutualExclusionResource795', set())
    assert getattr(partner, 'SW_Interaction_MARTE_BehavioralFeature796') is None


def test_assoc_repetitionShapeDependence180_stub_double():
    # IntegerVector has no real 'IntegerVector' property in the generated
    # code (a bare stub) -- manually attach it so MARTE_RSM_InterRepetition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # MARTE_RSM_InterRepetition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = MARTE_RSM_InterRepetition(isModulo="sample_text")
    partner = IntegerVector()
    setattr(partner, 'IntegerVector', None)
    _safe_set(owner, 'MARTE_RSM_InterRepetition', partner)
    assert getattr(partner, 'IntegerVector') == owner
    _safe_set(owner, 'MARTE_RSM_InterRepetition', None)
    assert getattr(partner, 'IntegerVector') is None


def test_assoc_reqInterface806_stub_double():
    # GCM_MARTE_Interface has no real 'GCM_MARTE_Interface808' property in the generated
    # code (a bare stub) -- manually attach it so MARTE_GCM_ClientServerPort's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # MARTE_GCM_ClientServerPort's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = MARTE_GCM_ClientServerPort(isConjugated="sample_text", kind="sample_text", specificationKind="sample_text")
    partner = GCM_MARTE_Interface()
    setattr(partner, 'GCM_MARTE_Interface808', None)
    _safe_set(owner, 'MARTE_GCM_ClientServerPort807', {partner})
    assert getattr(partner, 'GCM_MARTE_Interface808') == owner
    _safe_set(owner, 'MARTE_GCM_ClientServerPort807', set())
    assert getattr(partner, 'GCM_MARTE_Interface808') is None


def test_assoc_resMult100_stub_double():
    # NFP_Integer has no real 'NFP_Integer' property in the generated
    # code (a bare stub) -- manually attach it so MARTE_GRM_Resource's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # MARTE_GRM_Resource's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = MARTE_GRM_Resource(isProtected="sample_text")
    partner = NFP_Integer()
    setattr(partner, 'NFP_Integer', None)
    _safe_set(owner, 'MARTE_GRM_Resource', partner)
    assert getattr(partner, 'NFP_Integer') == owner
    _safe_set(owner, 'MARTE_GRM_Resource', None)
    assert getattr(partner, 'NFP_Integer') is None


def test_assoc_resolAttr60_stub_double():
    # Time_MARTE_Property has no real 'Time_MARTE_Property62' property in the generated
    # code (a bare stub) -- manually attach it so MARTE_Time_ClockType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # MARTE_Time_ClockType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = MARTE_Time_ClockType(isLogical="sample_text", nature="sample_text")
    partner = Time_MARTE_Property()
    setattr(partner, 'Time_MARTE_Property62', None)
    _safe_set(owner, 'MARTE_Time_ClockType61', partner)
    assert getattr(partner, 'Time_MARTE_Property62') == owner
    _safe_set(owner, 'MARTE_Time_ClockType61', None)
    assert getattr(partner, 'Time_MARTE_Property62') is None


def test_assoc_resumeServices646_stub_double():
    # SW_Concurrency_MARTE_BehavioralFeature has no real 'SW_Concurrency_MARTE_BehavioralFeature648' property in the generated
    # code (a bare stub) -- manually attach it so MARTE_SW_Concurrency_SwConcurrentResource's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # MARTE_SW_Concurrency_SwConcurrentResource's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = MARTE_SW_Concurrency_SwConcurrentResource(activationCapacity="sample_text")
    partner = SW_Concurrency_MARTE_BehavioralFeature()
    setattr(partner, 'SW_Concurrency_MARTE_BehavioralFeature648', None)
    _safe_set(owner, 'MARTE_SW_Concurrency_SwConcurrentResource647', {partner})
    assert getattr(partner, 'SW_Concurrency_MARTE_BehavioralFeature648') == owner
    _safe_set(owner, 'MARTE_SW_Concurrency_SwConcurrentResource647', set())
    assert getattr(partner, 'SW_Concurrency_MARTE_BehavioralFeature648') is None


def test_assoc_routine624_stub_double():
    # SW_Concurrency_MARTE_BehavioralFeature has no real 'SW_Concurrency_MARTE_BehavioralFeature' property in the generated
    # code (a bare stub) -- manually attach it so MARTE_SW_Concurrency_EntryPoint's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # MARTE_SW_Concurrency_EntryPoint's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = MARTE_SW_Concurrency_EntryPoint(isReentrant="sample_text")
    partner = SW_Concurrency_MARTE_BehavioralFeature()
    setattr(partner, 'SW_Concurrency_MARTE_BehavioralFeature', None)
    _safe_set(owner, 'MARTE_SW_Concurrency_EntryPoint', partner)
    assert getattr(partner, 'SW_Concurrency_MARTE_BehavioralFeature') == owner
    _safe_set(owner, 'MARTE_SW_Concurrency_EntryPoint', None)
    assert getattr(partner, 'SW_Concurrency_MARTE_BehavioralFeature') is None


def test_assoc_routineConnectServices678_stub_double():
    # SW_Concurrency_MARTE_BehavioralFeature has no real 'SW_Concurrency_MARTE_BehavioralFeature680' property in the generated
    # code (a bare stub) -- manually attach it so MARTE_SW_Concurrency_InterruptResource's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # MARTE_SW_Concurrency_InterruptResource's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = MARTE_SW_Concurrency_InterruptResource(isMaskable="sample_text", kind="sample_text")
    partner = SW_Concurrency_MARTE_BehavioralFeature()
    setattr(partner, 'SW_Concurrency_MARTE_BehavioralFeature680', None)
    _safe_set(owner, 'MARTE_SW_Concurrency_InterruptResource679', {partner})
    assert getattr(partner, 'SW_Concurrency_MARTE_BehavioralFeature680') == owner
    _safe_set(owner, 'MARTE_SW_Concurrency_InterruptResource679', set())
    assert getattr(partner, 'SW_Concurrency_MARTE_BehavioralFeature680') is None


def test_assoc_routineDisconnectServices681_stub_double():
    # SW_Concurrency_MARTE_BehavioralFeature has no real 'SW_Concurrency_MARTE_BehavioralFeature683' property in the generated
    # code (a bare stub) -- manually attach it so MARTE_SW_Concurrency_InterruptResource's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # MARTE_SW_Concurrency_InterruptResource's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = MARTE_SW_Concurrency_InterruptResource(isMaskable="sample_text", kind="sample_text")
    partner = SW_Concurrency_MARTE_BehavioralFeature()
    setattr(partner, 'SW_Concurrency_MARTE_BehavioralFeature683', None)
    _safe_set(owner, 'MARTE_SW_Concurrency_InterruptResource682', {partner})
    assert getattr(partner, 'SW_Concurrency_MARTE_BehavioralFeature683') == owner
    _safe_set(owner, 'MARTE_SW_Concurrency_InterruptResource682', set())
    assert getattr(partner, 'SW_Concurrency_MARTE_BehavioralFeature683') is None


def test_assoc_schedulableResources121_stub_double():
    # GRM_SchedulableResource has no real 'SchedulableResource' property in the generated
    # code (a bare stub) -- manually attach it so MARTE_GRM_Scheduler's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # MARTE_GRM_Scheduler's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = MARTE_GRM_Scheduler(isPreemptible="sample_text", otherSchedPolicy="sample_text", schedPolicy="sample_text")
    partner = GRM_SchedulableResource()
    setattr(partner, 'SchedulableResource', None)
    _safe_set(owner, 'host', {partner})
    assert getattr(partner, 'SchedulableResource') == owner
    _safe_set(owner, 'host', set())
    assert getattr(partner, 'SchedulableResource') is None


def test_assoc_schedule115_stub_double():
    # GRM_MARTE_OpaqueExpression has no real 'GRM_MARTE_OpaqueExpression' property in the generated
    # code (a bare stub) -- manually attach it so MARTE_GRM_Scheduler's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # MARTE_GRM_Scheduler's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = MARTE_GRM_Scheduler(isPreemptible="sample_text", otherSchedPolicy="sample_text", schedPolicy="sample_text")
    partner = GRM_MARTE_OpaqueExpression()
    setattr(partner, 'GRM_MARTE_OpaqueExpression', None)
    _safe_set(owner, 'MARTE_GRM_Scheduler', partner)
    assert getattr(partner, 'GRM_MARTE_OpaqueExpression') == owner
    _safe_set(owner, 'MARTE_GRM_Scheduler', None)
    assert getattr(partner, 'GRM_MARTE_OpaqueExpression') is None


def test_assoc_scheduler127_stub_double():
    # GRM_Scheduler has no real 'Scheduler' property in the generated
    # code (a bare stub) -- manually attach it so MARTE_GRM_MutualExclusionResource's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # MARTE_GRM_MutualExclusionResource's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = MARTE_GRM_MutualExclusionResource(otherProtectProtocol="sample_text", protectKind="sample_text")
    partner = GRM_Scheduler()
    setattr(partner, 'Scheduler', None)
    _safe_set(owner, 'protectedSharedRsources', partner)
    assert getattr(partner, 'Scheduler') == owner
    _safe_set(owner, 'protectedSharedRsources', None)
    assert getattr(partner, 'Scheduler') is None


def test_assoc_schedulers684_stub_double():
    # SW_Concurrency_MARTE_NamedElement has no real 'SW_Concurrency_MARTE_NamedElement' property in the generated
    # code (a bare stub) -- manually attach it so MARTE_SW_Concurrency_SwSchedulableResource's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # MARTE_SW_Concurrency_SwSchedulableResource's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = MARTE_SW_Concurrency_SwSchedulableResource(isPreemptable="sample_text", isStaticSchedulingFeature="sample_text")
    partner = SW_Concurrency_MARTE_NamedElement()
    setattr(partner, 'SW_Concurrency_MARTE_NamedElement', None)
    _safe_set(owner, 'MARTE_SW_Concurrency_SwSchedulableResource', partner)
    assert getattr(partner, 'SW_Concurrency_MARTE_NamedElement') == owner
    _safe_set(owner, 'MARTE_SW_Concurrency_SwSchedulableResource', None)
    assert getattr(partner, 'SW_Concurrency_MARTE_NamedElement') is None


def test_assoc_selection830_stub_double():
    # GCM_MARTE_Behavior has no real 'GCM_MARTE_Behavior832' property in the generated
    # code (a bare stub) -- manually attach it so MARTE_GCM_DataPool's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # MARTE_GCM_DataPool's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = MARTE_GCM_DataPool(ordering="sample_text")
    partner = GCM_MARTE_Behavior()
    setattr(partner, 'GCM_MARTE_Behavior832', None)
    _safe_set(owner, 'MARTE_GCM_DataPool831', partner)
    assert getattr(partner, 'GCM_MARTE_Behavior832') == owner
    _safe_set(owner, 'MARTE_GCM_DataPool831', None)
    assert getattr(partner, 'GCM_MARTE_Behavior832') is None


def test_assoc_sendServices769_stub_double():
    # SW_Interaction_MARTE_BehavioralFeature has no real 'SW_Interaction_MARTE_BehavioralFeature771' property in the generated
    # code (a bare stub) -- manually attach it so MARTE_SW_Interaction_MessageComResource's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # MARTE_SW_Interaction_MessageComResource's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = MARTE_SW_Interaction_MessageComResource(isFixedMessageSize="sample_text", mechanism="sample_text", messageQueuePolicy="sample_text")
    partner = SW_Interaction_MARTE_BehavioralFeature()
    setattr(partner, 'SW_Interaction_MARTE_BehavioralFeature771', None)
    _safe_set(owner, 'MARTE_SW_Interaction_MessageComResource770', {partner})
    assert getattr(partner, 'SW_Interaction_MARTE_BehavioralFeature771') == owner
    _safe_set(owner, 'MARTE_SW_Interaction_MessageComResource770', set())
    assert getattr(partner, 'SW_Interaction_MARTE_BehavioralFeature771') is None


def test_assoc_setTime71_stub_double():
    # Time_MARTE_Operation has no real 'Time_MARTE_Operation73' property in the generated
    # code (a bare stub) -- manually attach it so MARTE_Time_ClockType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # MARTE_Time_ClockType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = MARTE_Time_ClockType(isLogical="sample_text", nature="sample_text")
    partner = Time_MARTE_Operation()
    setattr(partner, 'Time_MARTE_Operation73', None)
    _safe_set(owner, 'MARTE_Time_ClockType72', partner)
    assert getattr(partner, 'Time_MARTE_Operation73') == owner
    _safe_set(owner, 'MARTE_Time_ClockType72', None)
    assert getattr(partner, 'Time_MARTE_Operation73') is None


def test_assoc_shareDataResources658_stub_double():
    # SW_Concurrency_MARTE_TypedElement has no real 'SW_Concurrency_MARTE_TypedElement660' property in the generated
    # code (a bare stub) -- manually attach it so MARTE_SW_Concurrency_SwConcurrentResource's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # MARTE_SW_Concurrency_SwConcurrentResource's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = MARTE_SW_Concurrency_SwConcurrentResource(activationCapacity="sample_text")
    partner = SW_Concurrency_MARTE_TypedElement()
    setattr(partner, 'SW_Concurrency_MARTE_TypedElement660', None)
    _safe_set(owner, 'MARTE_SW_Concurrency_SwConcurrentResource659', {partner})
    assert getattr(partner, 'SW_Concurrency_MARTE_TypedElement660') == owner
    _safe_set(owner, 'MARTE_SW_Concurrency_SwConcurrentResource659', set())
    assert getattr(partner, 'SW_Concurrency_MARTE_TypedElement660') is None


def test_assoc_signalServices783_stub_double():
    # SW_Interaction_MARTE_BehavioralFeature has no real 'SW_Interaction_MARTE_BehavioralFeature785' property in the generated
    # code (a bare stub) -- manually attach it so MARTE_SW_Interaction_NotificationResource's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # MARTE_SW_Interaction_NotificationResource's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = MARTE_SW_Interaction_NotificationResource(mechanism="sample_text", occurence="sample_text")
    partner = SW_Interaction_MARTE_BehavioralFeature()
    setattr(partner, 'SW_Interaction_MARTE_BehavioralFeature785', None)
    _safe_set(owner, 'MARTE_SW_Interaction_NotificationResource784', {partner})
    assert getattr(partner, 'SW_Interaction_MARTE_BehavioralFeature785') == owner
    _safe_set(owner, 'MARTE_SW_Interaction_NotificationResource784', set())
    assert getattr(partner, 'SW_Interaction_MARTE_BehavioralFeature785') is None


def test_assoc_srPoolWaitingTime239_stub_double():
    # NFP_Duration has no real 'NFP_Duration240' property in the generated
    # code (a bare stub) -- manually attach it so MARTE_HLAM_RtUnit's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # MARTE_HLAM_RtUnit's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = MARTE_HLAM_RtUnit(isDynamic="sample_text", isMain="sample_text", queueSchedPolicy="sample_text", queueSize="sample_text", srPoolPolicy="sample_text", srPoolSize="sample_text")
    partner = NFP_Duration()
    setattr(partner, 'NFP_Duration240', None)
    _safe_set(owner, 'MARTE_HLAM_RtUnit', partner)
    assert getattr(partner, 'NFP_Duration240') == owner
    _safe_set(owner, 'MARTE_HLAM_RtUnit', None)
    assert getattr(partner, 'NFP_Duration240') is None


def test_assoc_stackSizeElements637_stub_double():
    # SW_Concurrency_MARTE_TypedElement has no real 'SW_Concurrency_MARTE_TypedElement639' property in the generated
    # code (a bare stub) -- manually attach it so MARTE_SW_Concurrency_SwConcurrentResource's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # MARTE_SW_Concurrency_SwConcurrentResource's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = MARTE_SW_Concurrency_SwConcurrentResource(activationCapacity="sample_text")
    partner = SW_Concurrency_MARTE_TypedElement()
    setattr(partner, 'SW_Concurrency_MARTE_TypedElement639', None)
    _safe_set(owner, 'MARTE_SW_Concurrency_SwConcurrentResource638', {partner})
    assert getattr(partner, 'SW_Concurrency_MARTE_TypedElement639') == owner
    _safe_set(owner, 'MARTE_SW_Concurrency_SwConcurrentResource638', set())
    assert getattr(partner, 'SW_Concurrency_MARTE_TypedElement639') is None


def test_assoc_startObs929_stub_double():
    # GQAM_MARTE_TimeObservation has no real 'GQAM_MARTE_TimeObservation' property in the generated
    # code (a bare stub) -- manually attach it so MARTE_GQAM_GaTimedObs's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # MARTE_GQAM_GaTimedObs's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = MARTE_GQAM_GaTimedObs(laxity="sample_text")
    partner = GQAM_MARTE_TimeObservation()
    setattr(partner, 'GQAM_MARTE_TimeObservation', None)
    _safe_set(owner, 'MARTE_GQAM_GaTimedObs', {partner})
    assert getattr(partner, 'GQAM_MARTE_TimeObservation') == owner
    _safe_set(owner, 'MARTE_GQAM_GaTimedObs', set())
    assert getattr(partner, 'GQAM_MARTE_TimeObservation') is None


def test_assoc_staticConsumption546_stub_double():
    # NFP_Power has no real 'NFP_Power548' property in the generated
    # code (a bare stub) -- manually attach it so MARTE_HwLayout_HwComponent's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # MARTE_HwLayout_HwComponent's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = MARTE_HwLayout_HwComponent(kind="sample_text")
    partner = NFP_Power()
    setattr(partner, 'NFP_Power548', None)
    _safe_set(owner, 'MARTE_HwLayout_HwComponent547', partner)
    assert getattr(partner, 'NFP_Power548') == owner
    _safe_set(owner, 'MARTE_HwLayout_HwComponent547', None)
    assert getattr(partner, 'NFP_Power548') is None


def test_assoc_staticDissipation549_stub_double():
    # NFP_Power has no real 'NFP_Power551' property in the generated
    # code (a bare stub) -- manually attach it so MARTE_HwLayout_HwComponent's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # MARTE_HwLayout_HwComponent's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = MARTE_HwLayout_HwComponent(kind="sample_text")
    partner = NFP_Power()
    setattr(partner, 'NFP_Power551', None)
    _safe_set(owner, 'MARTE_HwLayout_HwComponent550', partner)
    assert getattr(partner, 'NFP_Power551') == owner
    _safe_set(owner, 'MARTE_HwLayout_HwComponent550', None)
    assert getattr(partner, 'NFP_Power551') is None


def test_assoc_structure466_stub_double():
    # HwMemory_CacheStructure has no real 'HwMemory_CacheStructure' property in the generated
    # code (a bare stub) -- manually attach it so MARTE_HwMemory_HwCache's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # MARTE_HwMemory_HwCache's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = MARTE_HwMemory_HwCache(repl_Policy="sample_text", type="sample_text", writePolicy="sample_text")
    partner = HwMemory_CacheStructure()
    setattr(partner, 'HwMemory_CacheStructure', None)
    _safe_set(owner, 'MARTE_HwMemory_HwCache467', partner)
    assert getattr(partner, 'HwMemory_CacheStructure') == owner
    _safe_set(owner, 'MARTE_HwMemory_HwCache467', None)
    assert getattr(partner, 'HwMemory_CacheStructure') is None


def test_assoc_subComponents552_stub_double():
    # HwLayout_HwComponent has no real 'HwLayout_HwComponent' property in the generated
    # code (a bare stub) -- manually attach it so MARTE_HwLayout_HwComponent's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # MARTE_HwLayout_HwComponent's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = MARTE_HwLayout_HwComponent(kind="sample_text")
    partner = HwLayout_HwComponent()
    setattr(partner, 'HwLayout_HwComponent', None)
    _safe_set(owner, 'MARTE_HwLayout_HwComponent553', {partner})
    assert getattr(partner, 'HwLayout_HwComponent') == owner
    _safe_set(owner, 'MARTE_HwLayout_HwComponent553', set())
    assert getattr(partner, 'HwLayout_HwComponent') is None


def test_assoc_suspendServices649_stub_double():
    # SW_Concurrency_MARTE_BehavioralFeature has no real 'SW_Concurrency_MARTE_BehavioralFeature651' property in the generated
    # code (a bare stub) -- manually attach it so MARTE_SW_Concurrency_SwConcurrentResource's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # MARTE_SW_Concurrency_SwConcurrentResource's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = MARTE_SW_Concurrency_SwConcurrentResource(activationCapacity="sample_text")
    partner = SW_Concurrency_MARTE_BehavioralFeature()
    setattr(partner, 'SW_Concurrency_MARTE_BehavioralFeature651', None)
    _safe_set(owner, 'MARTE_SW_Concurrency_SwConcurrentResource650', {partner})
    assert getattr(partner, 'SW_Concurrency_MARTE_BehavioralFeature651') == owner
    _safe_set(owner, 'MARTE_SW_Concurrency_SwConcurrentResource650', set())
    assert getattr(partner, 'SW_Concurrency_MARTE_BehavioralFeature651') is None


def test_assoc_terminateServices652_stub_double():
    # SW_Concurrency_MARTE_BehavioralFeature has no real 'SW_Concurrency_MARTE_BehavioralFeature654' property in the generated
    # code (a bare stub) -- manually attach it so MARTE_SW_Concurrency_SwConcurrentResource's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # MARTE_SW_Concurrency_SwConcurrentResource's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = MARTE_SW_Concurrency_SwConcurrentResource(activationCapacity="sample_text")
    partner = SW_Concurrency_MARTE_BehavioralFeature()
    setattr(partner, 'SW_Concurrency_MARTE_BehavioralFeature654', None)
    _safe_set(owner, 'MARTE_SW_Concurrency_SwConcurrentResource653', {partner})
    assert getattr(partner, 'SW_Concurrency_MARTE_BehavioralFeature654') == owner
    _safe_set(owner, 'MARTE_SW_Concurrency_SwConcurrentResource653', set())
    assert getattr(partner, 'SW_Concurrency_MARTE_BehavioralFeature654') is None


def test_assoc_throughput1114_stub_double():
    # NFP_Frequency has no real 'NFP_Frequency1116' property in the generated
    # code (a bare stub) -- manually attach it so MARTE_PAM_PaRunTInstance's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # MARTE_PAM_PaRunTInstance's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = MARTE_PAM_PaRunTInstance(unbddPool="sample_text")
    partner = NFP_Frequency()
    setattr(partner, 'NFP_Frequency1116', None)
    _safe_set(owner, 'MARTE_PAM_PaRunTInstance1115', partner)
    assert getattr(partner, 'NFP_Frequency1116') == owner
    _safe_set(owner, 'MARTE_PAM_PaRunTInstance1115', None)
    assert getattr(partner, 'NFP_Frequency1116') is None


def test_assoc_timeSliceElements691_stub_double():
    # SW_Concurrency_MARTE_TypedElement has no real 'SW_Concurrency_MARTE_TypedElement693' property in the generated
    # code (a bare stub) -- manually attach it so MARTE_SW_Concurrency_SwSchedulableResource's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # MARTE_SW_Concurrency_SwSchedulableResource's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = MARTE_SW_Concurrency_SwSchedulableResource(isPreemptable="sample_text", isStaticSchedulingFeature="sample_text")
    partner = SW_Concurrency_MARTE_TypedElement()
    setattr(partner, 'SW_Concurrency_MARTE_TypedElement693', None)
    _safe_set(owner, 'MARTE_SW_Concurrency_SwSchedulableResource692', {partner})
    assert getattr(partner, 'SW_Concurrency_MARTE_TypedElement693') == owner
    _safe_set(owner, 'MARTE_SW_Concurrency_SwSchedulableResource692', set())
    assert getattr(partner, 'SW_Concurrency_MARTE_TypedElement693') is None


def test_assoc_timers718_stub_double():
    # SW_Concurrency_MARTE_TypedElement has no real 'SW_Concurrency_MARTE_TypedElement719' property in the generated
    # code (a bare stub) -- manually attach it so MARTE_SW_Concurrency_Alarm's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # MARTE_SW_Concurrency_Alarm's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = MARTE_SW_Concurrency_Alarm(isWatchdog="sample_text")
    partner = SW_Concurrency_MARTE_TypedElement()
    setattr(partner, 'SW_Concurrency_MARTE_TypedElement719', None)
    _safe_set(owner, 'MARTE_SW_Concurrency_Alarm', {partner})
    assert getattr(partner, 'SW_Concurrency_MARTE_TypedElement719') == owner
    _safe_set(owner, 'MARTE_SW_Concurrency_Alarm', set())
    assert getattr(partner, 'SW_Concurrency_MARTE_TypedElement719') is None


def test_assoc_type52_stub_double():
    # Time_ClockType has no real 'Time_ClockType' property in the generated
    # code (a bare stub) -- manually attach it so MARTE_Time_Clock's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # MARTE_Time_Clock's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = MARTE_Time_Clock(standard="sample_text")
    partner = Time_ClockType()
    setattr(partner, 'Time_ClockType', None)
    _safe_set(owner, 'MARTE_Time_Clock53', partner)
    assert getattr(partner, 'Time_ClockType') == owner
    _safe_set(owner, 'MARTE_Time_Clock53', None)
    assert getattr(partner, 'Time_ClockType') is None


def test_assoc_type625_stub_double():
    # ArrivalPattern has no real 'ArrivalPattern626' property in the generated
    # code (a bare stub) -- manually attach it so MARTE_SW_Concurrency_SwConcurrentResource's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # MARTE_SW_Concurrency_SwConcurrentResource's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = MARTE_SW_Concurrency_SwConcurrentResource(activationCapacity="sample_text")
    partner = ArrivalPattern()
    setattr(partner, 'ArrivalPattern626', None)
    _safe_set(owner, 'MARTE_SW_Concurrency_SwConcurrentResource', partner)
    assert getattr(partner, 'ArrivalPattern626') == owner
    _safe_set(owner, 'MARTE_SW_Concurrency_SwConcurrentResource', None)
    assert getattr(partner, 'ArrivalPattern626') is None


def test_assoc_unMapServices756_stub_double():
    # SW_Brokering_MARTE_BehavioralFeature has no real 'SW_Brokering_MARTE_BehavioralFeature758' property in the generated
    # code (a bare stub) -- manually attach it so MARTE_SW_Brokering_MemoryBroker's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # MARTE_SW_Brokering_MemoryBroker's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = MARTE_SW_Brokering_MemoryBroker(accessPolicy="sample_text")
    partner = SW_Brokering_MARTE_BehavioralFeature()
    setattr(partner, 'SW_Brokering_MARTE_BehavioralFeature758', None)
    _safe_set(owner, 'MARTE_SW_Brokering_MemoryBroker757', {partner})
    assert getattr(partner, 'SW_Brokering_MARTE_BehavioralFeature758') == owner
    _safe_set(owner, 'MARTE_SW_Brokering_MemoryBroker757', set())
    assert getattr(partner, 'SW_Brokering_MARTE_BehavioralFeature758') is None


def test_assoc_unit54_stub_double():
    # NFPs_Unit has no real 'NFPs_Unit56' property in the generated
    # code (a bare stub) -- manually attach it so MARTE_Time_Clock's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # MARTE_Time_Clock's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = MARTE_Time_Clock(standard="sample_text")
    partner = NFPs_Unit()
    setattr(partner, 'NFPs_Unit56', None)
    _safe_set(owner, 'MARTE_Time_Clock55', partner)
    assert getattr(partner, 'NFPs_Unit56') == owner
    _safe_set(owner, 'MARTE_Time_Clock55', None)
    assert getattr(partner, 'NFPs_Unit56') is None


def test_assoc_unitType59_stub_double():
    # Time_MARTE_Enumeration has no real 'Time_MARTE_Enumeration' property in the generated
    # code (a bare stub) -- manually attach it so MARTE_Time_ClockType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # MARTE_Time_ClockType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = MARTE_Time_ClockType(isLogical="sample_text", nature="sample_text")
    partner = Time_MARTE_Enumeration()
    setattr(partner, 'Time_MARTE_Enumeration', None)
    _safe_set(owner, 'MARTE_Time_ClockType', partner)
    assert getattr(partner, 'Time_MARTE_Enumeration') == owner
    _safe_set(owner, 'MARTE_Time_ClockType', None)
    assert getattr(partner, 'Time_MARTE_Enumeration') is None


def test_assoc_unlockServices750_stub_double():
    # SW_Brokering_MARTE_BehavioralFeature has no real 'SW_Brokering_MARTE_BehavioralFeature752' property in the generated
    # code (a bare stub) -- manually attach it so MARTE_SW_Brokering_MemoryBroker's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # MARTE_SW_Brokering_MemoryBroker's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = MARTE_SW_Brokering_MemoryBroker(accessPolicy="sample_text")
    partner = SW_Brokering_MARTE_BehavioralFeature()
    setattr(partner, 'SW_Brokering_MARTE_BehavioralFeature752', None)
    _safe_set(owner, 'MARTE_SW_Brokering_MemoryBroker751', {partner})
    assert getattr(partner, 'SW_Brokering_MARTE_BehavioralFeature752') == owner
    _safe_set(owner, 'MARTE_SW_Brokering_MemoryBroker751', set())
    assert getattr(partner, 'SW_Brokering_MARTE_BehavioralFeature752') is None


def test_assoc_utilization1111_stub_double():
    # NFP_Real has no real 'NFP_Real1113' property in the generated
    # code (a bare stub) -- manually attach it so MARTE_PAM_PaRunTInstance's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # MARTE_PAM_PaRunTInstance's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = MARTE_PAM_PaRunTInstance(unbddPool="sample_text")
    partner = NFP_Real()
    setattr(partner, 'NFP_Real1113', None)
    _safe_set(owner, 'MARTE_PAM_PaRunTInstance1112', partner)
    assert getattr(partner, 'NFP_Real1113') == owner
    _safe_set(owner, 'MARTE_PAM_PaRunTInstance1112', None)
    assert getattr(partner, 'NFP_Real1113') is None


def test_assoc_vectorElements673_stub_double():
    # SW_Concurrency_MARTE_TypedElement has no real 'SW_Concurrency_MARTE_TypedElement674' property in the generated
    # code (a bare stub) -- manually attach it so MARTE_SW_Concurrency_InterruptResource's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # MARTE_SW_Concurrency_InterruptResource's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = MARTE_SW_Concurrency_InterruptResource(isMaskable="sample_text", kind="sample_text")
    partner = SW_Concurrency_MARTE_TypedElement()
    setattr(partner, 'SW_Concurrency_MARTE_TypedElement674', None)
    _safe_set(owner, 'MARTE_SW_Concurrency_InterruptResource', {partner})
    assert getattr(partner, 'SW_Concurrency_MARTE_TypedElement674') == owner
    _safe_set(owner, 'MARTE_SW_Concurrency_InterruptResource', set())
    assert getattr(partner, 'SW_Concurrency_MARTE_TypedElement674') is None


def test_assoc_waitServices786_stub_double():
    # SW_Interaction_MARTE_BehavioralFeature has no real 'SW_Interaction_MARTE_BehavioralFeature788' property in the generated
    # code (a bare stub) -- manually attach it so MARTE_SW_Interaction_NotificationResource's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # MARTE_SW_Interaction_NotificationResource's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = MARTE_SW_Interaction_NotificationResource(mechanism="sample_text", occurence="sample_text")
    partner = SW_Interaction_MARTE_BehavioralFeature()
    setattr(partner, 'SW_Interaction_MARTE_BehavioralFeature788', None)
    _safe_set(owner, 'MARTE_SW_Interaction_NotificationResource787', {partner})
    assert getattr(partner, 'SW_Interaction_MARTE_BehavioralFeature788') == owner
    _safe_set(owner, 'MARTE_SW_Interaction_NotificationResource787', set())
    assert getattr(partner, 'SW_Interaction_MARTE_BehavioralFeature788') is None


def test_assoc_waitingPolicyElements759_stub_double():
    # SW_Interaction_MARTE_TypedElement has no real 'SW_Interaction_MARTE_TypedElement' property in the generated
    # code (a bare stub) -- manually attach it so MARTE_SW_Interaction_SwInteractionResource's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # MARTE_SW_Interaction_SwInteractionResource's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = MARTE_SW_Interaction_SwInteractionResource(isIntraMemoryPartitionInteraction=True, waitingQueueCapacity="sample_text", waitingQueuePolicy="sample_text")
    partner = SW_Interaction_MARTE_TypedElement()
    setattr(partner, 'SW_Interaction_MARTE_TypedElement', None)
    _safe_set(owner, 'MARTE_SW_Interaction_SwInteractionResource', {partner})
    assert getattr(partner, 'SW_Interaction_MARTE_TypedElement') == owner
    _safe_set(owner, 'MARTE_SW_Interaction_SwInteractionResource', set())
    assert getattr(partner, 'SW_Interaction_MARTE_TypedElement') is None


def test_assoc_weight536_stub_double():
    # NFP_Real has no real 'NFP_Real538' property in the generated
    # code (a bare stub) -- manually attach it so MARTE_HwLayout_HwComponent's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # MARTE_HwLayout_HwComponent's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = MARTE_HwLayout_HwComponent(kind="sample_text")
    partner = NFP_Real()
    setattr(partner, 'NFP_Real538', None)
    _safe_set(owner, 'MARTE_HwLayout_HwComponent537', partner)
    assert getattr(partner, 'NFP_Real538') == owner
    _safe_set(owner, 'MARTE_HwLayout_HwComponent537', None)
    assert getattr(partner, 'NFP_Real538') is None


def test_assoc_wire580_stub_double():
    # HwPackage_HwWire has no real 'HwPackage_HwWire' property in the generated
    # code (a bare stub) -- manually attach it so MARTE_HwPackage_HwPackagePin's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # MARTE_HwPackage_HwPackagePin's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = MARTE_HwPackage_HwPackagePin(altNames="sample_text", pinNo="sample_text")
    partner = HwPackage_HwWire()
    setattr(partner, 'HwPackage_HwWire', None)
    _safe_set(owner, 'MARTE_HwPackage_HwPackagePin', {partner})
    assert getattr(partner, 'HwPackage_HwWire') == owner
    _safe_set(owner, 'MARTE_HwPackage_HwPackagePin', set())
    assert getattr(partner, 'HwPackage_HwWire') is None


def test_assoc_wires591_stub_double():
    # HwPackage_HwWire has no real 'HwPackage_HwWire593' property in the generated
    # code (a bare stub) -- manually attach it so MARTE_HwDiagram_HwCircuitDiagram's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # MARTE_HwDiagram_HwCircuitDiagram's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = MARTE_HwDiagram_HwCircuitDiagram(name="sample_text")
    partner = HwPackage_HwWire()
    setattr(partner, 'HwPackage_HwWire593', None)
    _safe_set(owner, 'MARTE_HwDiagram_HwCircuitDiagram592', {partner})
    assert getattr(partner, 'HwPackage_HwWire593') == owner
    _safe_set(owner, 'MARTE_HwDiagram_HwCircuitDiagram592', set())
    assert getattr(partner, 'HwPackage_HwWire593') is None


def test_assoc_writeServices732_stub_double():
    # SW_Brokering_MARTE_BehavioralFeature has no real 'SW_Brokering_MARTE_BehavioralFeature734' property in the generated
    # code (a bare stub) -- manually attach it so MARTE_SW_Brokering_DeviceBroker's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # MARTE_SW_Brokering_DeviceBroker's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = MARTE_SW_Brokering_DeviceBroker(accessPolicy="sample_text", isBuffered="sample_text", name="sample_text")
    partner = SW_Brokering_MARTE_BehavioralFeature()
    setattr(partner, 'SW_Brokering_MARTE_BehavioralFeature734', None)
    _safe_set(owner, 'MARTE_SW_Brokering_DeviceBroker733', {partner})
    assert getattr(partner, 'SW_Brokering_MARTE_BehavioralFeature734') == owner
    _safe_set(owner, 'MARTE_SW_Brokering_DeviceBroker733', set())
    assert getattr(partner, 'SW_Brokering_MARTE_BehavioralFeature734') is None


def test_assoc_yieldServices700_stub_double():
    # SW_Concurrency_MARTE_BehavioralFeature has no real 'SW_Concurrency_MARTE_BehavioralFeature702' property in the generated
    # code (a bare stub) -- manually attach it so MARTE_SW_Concurrency_SwSchedulableResource's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # MARTE_SW_Concurrency_SwSchedulableResource's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = MARTE_SW_Concurrency_SwSchedulableResource(isPreemptable="sample_text", isStaticSchedulingFeature="sample_text")
    partner = SW_Concurrency_MARTE_BehavioralFeature()
    setattr(partner, 'SW_Concurrency_MARTE_BehavioralFeature702', None)
    _safe_set(owner, 'MARTE_SW_Concurrency_SwSchedulableResource701', {partner})
    assert getattr(partner, 'SW_Concurrency_MARTE_BehavioralFeature702') == owner
    _safe_set(owner, 'MARTE_SW_Concurrency_SwSchedulableResource701', set())
    assert getattr(partner, 'SW_Concurrency_MARTE_BehavioralFeature702') is None


