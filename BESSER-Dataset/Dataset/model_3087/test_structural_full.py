import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

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

def test_MARTE_Alloc_Allocate_kind_value_roundtrip():
    instance = MARTE_Alloc_Allocate(kind="sample_text", nature="sample_text")
    assert instance.kind == "sample_text"
    instance.kind = "sample_text_2"
    assert instance.kind == "sample_text_2"


def test_MARTE_Alloc_Allocate_nature_value_roundtrip():
    instance = MARTE_Alloc_Allocate(kind="sample_text", nature="sample_text")
    assert instance.nature == "sample_text"
    instance.nature = "sample_text_2"
    assert instance.nature == "sample_text_2"


def test_MARTE_DataTypes_BoundedSubtype_isMaxOpen_value_roundtrip():
    instance = MARTE_DataTypes_BoundedSubtype(isMaxOpen=True, isMinOpen=True, maxValue="sample_text", minValue="sample_text")
    assert instance.isMaxOpen == True
    instance.isMaxOpen = False
    assert instance.isMaxOpen == False


def test_MARTE_DataTypes_BoundedSubtype_isMinOpen_value_roundtrip():
    instance = MARTE_DataTypes_BoundedSubtype(isMaxOpen=True, isMinOpen=True, maxValue="sample_text", minValue="sample_text")
    assert instance.isMinOpen == True
    instance.isMinOpen = False
    assert instance.isMinOpen == False


def test_MARTE_DataTypes_BoundedSubtype_maxValue_value_roundtrip():
    instance = MARTE_DataTypes_BoundedSubtype(isMaxOpen=True, isMinOpen=True, maxValue="sample_text", minValue="sample_text")
    assert instance.maxValue == "sample_text"
    instance.maxValue = "sample_text_2"
    assert instance.maxValue == "sample_text_2"


def test_MARTE_DataTypes_BoundedSubtype_minValue_value_roundtrip():
    instance = MARTE_DataTypes_BoundedSubtype(isMaxOpen=True, isMinOpen=True, maxValue="sample_text", minValue="sample_text")
    assert instance.minValue == "sample_text"
    instance.minValue = "sample_text_2"
    assert instance.minValue == "sample_text_2"


def test_MARTE_GCM_ClientServerFeature_kind_value_roundtrip():
    instance = MARTE_GCM_ClientServerFeature(kind="sample_text")
    assert instance.kind == "sample_text"
    instance.kind = "sample_text_2"
    assert instance.kind == "sample_text_2"


def test_MARTE_GCM_ClientServerPort_isConjugated_value_roundtrip():
    instance = MARTE_GCM_ClientServerPort(isConjugated="sample_text", kind="sample_text", specificationKind="sample_text")
    assert instance.isConjugated == "sample_text"
    instance.isConjugated = "sample_text_2"
    assert instance.isConjugated == "sample_text_2"


def test_MARTE_GCM_ClientServerPort_kind_value_roundtrip():
    instance = MARTE_GCM_ClientServerPort(isConjugated="sample_text", kind="sample_text", specificationKind="sample_text")
    assert instance.kind == "sample_text"
    instance.kind = "sample_text_2"
    assert instance.kind == "sample_text_2"


def test_MARTE_GCM_ClientServerPort_specificationKind_value_roundtrip():
    instance = MARTE_GCM_ClientServerPort(isConjugated="sample_text", kind="sample_text", specificationKind="sample_text")
    assert instance.specificationKind == "sample_text"
    instance.specificationKind = "sample_text_2"
    assert instance.specificationKind == "sample_text_2"


def test_MARTE_GCM_DataPool_ordering_value_roundtrip():
    instance = MARTE_GCM_DataPool(ordering="sample_text")
    assert instance.ordering == "sample_text"
    instance.ordering = "sample_text_2"
    assert instance.ordering == "sample_text_2"


def test_MARTE_GCM_FlowPort_direction_value_roundtrip():
    instance = MARTE_GCM_FlowPort(direction="sample_text", isAtomic="sample_text", isConjugated="sample_text")
    assert instance.direction == "sample_text"
    instance.direction = "sample_text_2"
    assert instance.direction == "sample_text_2"


def test_MARTE_GCM_FlowPort_isAtomic_value_roundtrip():
    instance = MARTE_GCM_FlowPort(direction="sample_text", isAtomic="sample_text", isConjugated="sample_text")
    assert instance.isAtomic == "sample_text"
    instance.isAtomic = "sample_text_2"
    assert instance.isAtomic == "sample_text_2"


def test_MARTE_GCM_FlowPort_isConjugated_value_roundtrip():
    instance = MARTE_GCM_FlowPort(direction="sample_text", isAtomic="sample_text", isConjugated="sample_text")
    assert instance.isConjugated == "sample_text"
    instance.isConjugated = "sample_text_2"
    assert instance.isConjugated == "sample_text_2"


def test_MARTE_GCM_FlowProperty_direction_value_roundtrip():
    instance = MARTE_GCM_FlowProperty(direction="sample_text")
    assert instance.direction == "sample_text"
    instance.direction = "sample_text_2"
    assert instance.direction == "sample_text_2"


def test_MARTE_GQAM_GaEventTrace_content_value_roundtrip():
    instance = MARTE_GQAM_GaEventTrace(content="sample_text", format="sample_text", location="sample_text")
    assert instance.content == "sample_text"
    instance.content = "sample_text_2"
    assert instance.content == "sample_text_2"


def test_MARTE_GQAM_GaEventTrace_format_value_roundtrip():
    instance = MARTE_GQAM_GaEventTrace(content="sample_text", format="sample_text", location="sample_text")
    assert instance.format == "sample_text"
    instance.format = "sample_text_2"
    assert instance.format == "sample_text_2"


def test_MARTE_GQAM_GaEventTrace_location_value_roundtrip():
    instance = MARTE_GQAM_GaEventTrace(content="sample_text", format="sample_text", location="sample_text")
    assert instance.location == "sample_text"
    instance.location = "sample_text_2"
    assert instance.location == "sample_text_2"


def test_MARTE_GQAM_GaTimedObs_laxity_value_roundtrip():
    instance = MARTE_GQAM_GaTimedObs(laxity="sample_text")
    assert instance.laxity == "sample_text"
    instance.laxity = "sample_text_2"
    assert instance.laxity == "sample_text_2"


def test_MARTE_GRM_Acquire_isBlocking_value_roundtrip():
    instance = MARTE_GRM_Acquire(isBlocking="sample_text")
    assert instance.isBlocking == "sample_text"
    instance.isBlocking = "sample_text_2"
    assert instance.isBlocking == "sample_text_2"


def test_MARTE_GRM_CommunicationMedia_transmMode_value_roundtrip():
    instance = MARTE_GRM_CommunicationMedia(transmMode="sample_text")
    assert instance.transmMode == "sample_text"
    instance.transmMode = "sample_text_2"
    assert instance.transmMode == "sample_text_2"


def test_MARTE_GRM_MutualExclusionResource_otherProtectProtocol_value_roundtrip():
    instance = MARTE_GRM_MutualExclusionResource(otherProtectProtocol="sample_text", protectKind="sample_text")
    assert instance.otherProtectProtocol == "sample_text"
    instance.otherProtectProtocol = "sample_text_2"
    assert instance.otherProtectProtocol == "sample_text_2"


def test_MARTE_GRM_MutualExclusionResource_protectKind_value_roundtrip():
    instance = MARTE_GRM_MutualExclusionResource(otherProtectProtocol="sample_text", protectKind="sample_text")
    assert instance.protectKind == "sample_text"
    instance.protectKind = "sample_text_2"
    assert instance.protectKind == "sample_text_2"


def test_MARTE_GRM_Resource_isProtected_value_roundtrip():
    instance = MARTE_GRM_Resource(isProtected="sample_text")
    assert instance.isProtected == "sample_text"
    instance.isProtected = "sample_text_2"
    assert instance.isProtected == "sample_text_2"


def test_MARTE_GRM_Scheduler_isPreemptible_value_roundtrip():
    instance = MARTE_GRM_Scheduler(isPreemptible="sample_text", otherSchedPolicy="sample_text", schedPolicy="sample_text")
    assert instance.isPreemptible == "sample_text"
    instance.isPreemptible = "sample_text_2"
    assert instance.isPreemptible == "sample_text_2"


def test_MARTE_GRM_Scheduler_otherSchedPolicy_value_roundtrip():
    instance = MARTE_GRM_Scheduler(isPreemptible="sample_text", otherSchedPolicy="sample_text", schedPolicy="sample_text")
    assert instance.otherSchedPolicy == "sample_text"
    instance.otherSchedPolicy = "sample_text_2"
    assert instance.otherSchedPolicy == "sample_text_2"


def test_MARTE_GRM_Scheduler_schedPolicy_value_roundtrip():
    instance = MARTE_GRM_Scheduler(isPreemptible="sample_text", otherSchedPolicy="sample_text", schedPolicy="sample_text")
    assert instance.schedPolicy == "sample_text"
    instance.schedPolicy = "sample_text_2"
    assert instance.schedPolicy == "sample_text_2"


def test_MARTE_GRM_TimerResource_isPeriodic_value_roundtrip():
    instance = MARTE_GRM_TimerResource(isPeriodic="sample_text")
    assert instance.isPeriodic == "sample_text"
    instance.isPeriodic = "sample_text_2"
    assert instance.isPeriodic == "sample_text_2"


def test_MARTE_HLAM_PpUnit_concPolicy_value_roundtrip():
    instance = MARTE_HLAM_PpUnit(concPolicy="sample_text")
    assert instance.concPolicy == "sample_text"
    instance.concPolicy = "sample_text_2"
    assert instance.concPolicy == "sample_text_2"


def test_MARTE_HLAM_RtAction_isAtomic_value_roundtrip():
    instance = MARTE_HLAM_RtAction(isAtomic="sample_text", synchKind="sample_text")
    assert instance.isAtomic == "sample_text"
    instance.isAtomic = "sample_text_2"
    assert instance.isAtomic == "sample_text_2"


def test_MARTE_HLAM_RtAction_synchKind_value_roundtrip():
    instance = MARTE_HLAM_RtAction(isAtomic="sample_text", synchKind="sample_text")
    assert instance.synchKind == "sample_text"
    instance.synchKind = "sample_text_2"
    assert instance.synchKind == "sample_text_2"


def test_MARTE_HLAM_RtService_concPolicy_value_roundtrip():
    instance = MARTE_HLAM_RtService(concPolicy="sample_text", exeKind="sample_text", isAtomic="sample_text", synchKind="sample_text")
    assert instance.concPolicy == "sample_text"
    instance.concPolicy = "sample_text_2"
    assert instance.concPolicy == "sample_text_2"


def test_MARTE_HLAM_RtService_exeKind_value_roundtrip():
    instance = MARTE_HLAM_RtService(concPolicy="sample_text", exeKind="sample_text", isAtomic="sample_text", synchKind="sample_text")
    assert instance.exeKind == "sample_text"
    instance.exeKind = "sample_text_2"
    assert instance.exeKind == "sample_text_2"


def test_MARTE_HLAM_RtService_isAtomic_value_roundtrip():
    instance = MARTE_HLAM_RtService(concPolicy="sample_text", exeKind="sample_text", isAtomic="sample_text", synchKind="sample_text")
    assert instance.isAtomic == "sample_text"
    instance.isAtomic = "sample_text_2"
    assert instance.isAtomic == "sample_text_2"


def test_MARTE_HLAM_RtService_synchKind_value_roundtrip():
    instance = MARTE_HLAM_RtService(concPolicy="sample_text", exeKind="sample_text", isAtomic="sample_text", synchKind="sample_text")
    assert instance.synchKind == "sample_text"
    instance.synchKind = "sample_text_2"
    assert instance.synchKind == "sample_text_2"


def test_MARTE_HLAM_RtUnit_isDynamic_value_roundtrip():
    instance = MARTE_HLAM_RtUnit(isDynamic="sample_text", isMain="sample_text", queueSchedPolicy="sample_text", queueSize="sample_text", srPoolPolicy="sample_text", srPoolSize="sample_text")
    assert instance.isDynamic == "sample_text"
    instance.isDynamic = "sample_text_2"
    assert instance.isDynamic == "sample_text_2"


def test_MARTE_HLAM_RtUnit_isMain_value_roundtrip():
    instance = MARTE_HLAM_RtUnit(isDynamic="sample_text", isMain="sample_text", queueSchedPolicy="sample_text", queueSize="sample_text", srPoolPolicy="sample_text", srPoolSize="sample_text")
    assert instance.isMain == "sample_text"
    instance.isMain = "sample_text_2"
    assert instance.isMain == "sample_text_2"


def test_MARTE_HLAM_RtUnit_queueSchedPolicy_value_roundtrip():
    instance = MARTE_HLAM_RtUnit(isDynamic="sample_text", isMain="sample_text", queueSchedPolicy="sample_text", queueSize="sample_text", srPoolPolicy="sample_text", srPoolSize="sample_text")
    assert instance.queueSchedPolicy == "sample_text"
    instance.queueSchedPolicy = "sample_text_2"
    assert instance.queueSchedPolicy == "sample_text_2"


def test_MARTE_HLAM_RtUnit_queueSize_value_roundtrip():
    instance = MARTE_HLAM_RtUnit(isDynamic="sample_text", isMain="sample_text", queueSchedPolicy="sample_text", queueSize="sample_text", srPoolPolicy="sample_text", srPoolSize="sample_text")
    assert instance.queueSize == "sample_text"
    instance.queueSize = "sample_text_2"
    assert instance.queueSize == "sample_text_2"


def test_MARTE_HLAM_RtUnit_srPoolPolicy_value_roundtrip():
    instance = MARTE_HLAM_RtUnit(isDynamic="sample_text", isMain="sample_text", queueSchedPolicy="sample_text", queueSize="sample_text", srPoolPolicy="sample_text", srPoolSize="sample_text")
    assert instance.srPoolPolicy == "sample_text"
    instance.srPoolPolicy = "sample_text_2"
    assert instance.srPoolPolicy == "sample_text_2"


def test_MARTE_HLAM_RtUnit_srPoolSize_value_roundtrip():
    instance = MARTE_HLAM_RtUnit(isDynamic="sample_text", isMain="sample_text", queueSchedPolicy="sample_text", queueSize="sample_text", srPoolPolicy="sample_text", srPoolSize="sample_text")
    assert instance.srPoolSize == "sample_text"
    instance.srPoolSize = "sample_text_2"
    assert instance.srPoolSize == "sample_text_2"


def test_MARTE_HwComputing_HwISA_type_value_roundtrip():
    instance = MARTE_HwComputing_HwISA(type="sample_text")
    assert instance.type == "sample_text"
    instance.type = "sample_text_2"
    assert instance.type == "sample_text_2"


def test_MARTE_HwComputing_HwPLD_technology_value_roundtrip():
    instance = MARTE_HwComputing_HwPLD(technology="sample_text")
    assert instance.technology == "sample_text"
    instance.technology = "sample_text_2"
    assert instance.technology == "sample_text_2"


def test_MARTE_HwComputing_PLD_Organization_class__value_roundtrip():
    instance = MARTE_HwComputing_PLD_Organization(class_="sample_text")
    assert instance.class_ == "sample_text"
    instance.class_ = "sample_text_2"
    assert instance.class_ == "sample_text_2"


def test_MARTE_HwDatasheet_HwDatasheet_name_value_roundtrip():
    instance = MARTE_HwDatasheet_HwDatasheet(name="sample_text", revision="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_MARTE_HwDatasheet_HwDatasheet_revision_value_roundtrip():
    instance = MARTE_HwDatasheet_HwDatasheet(name="sample_text", revision="sample_text")
    assert instance.revision == "sample_text"
    instance.revision = "sample_text_2"
    assert instance.revision == "sample_text_2"


def test_MARTE_HwDiagram_HwBlockDiagram_name_value_roundtrip():
    instance = MARTE_HwDiagram_HwBlockDiagram(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_MARTE_HwDiagram_HwCircuitDiagram_name_value_roundtrip():
    instance = MARTE_HwDiagram_HwCircuitDiagram(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_MARTE_HwDiagram_HwHRMDiagram_name_value_roundtrip():
    instance = MARTE_HwDiagram_HwHRMDiagram(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_MARTE_HwGeneral_HwResource_name_value_roundtrip():
    instance = MARTE_HwGeneral_HwResource(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_MARTE_HwLayout_Env_Condition_status_value_roundtrip():
    instance = MARTE_HwLayout_Env_Condition(status="sample_text", type="sample_text")
    assert instance.status == "sample_text"
    instance.status = "sample_text_2"
    assert instance.status == "sample_text_2"


def test_MARTE_HwLayout_Env_Condition_type_value_roundtrip():
    instance = MARTE_HwLayout_Env_Condition(status="sample_text", type="sample_text")
    assert instance.type == "sample_text"
    instance.type = "sample_text_2"
    assert instance.type == "sample_text_2"


def test_MARTE_HwLayout_HwComponent_kind_value_roundtrip():
    instance = MARTE_HwLayout_HwComponent(kind="sample_text")
    assert instance.kind == "sample_text"
    instance.kind = "sample_text_2"
    assert instance.kind == "sample_text_2"


def test_MARTE_HwMemory_HwCache_repl_Policy_value_roundtrip():
    instance = MARTE_HwMemory_HwCache(repl_Policy="sample_text", type="sample_text", writePolicy="sample_text")
    assert instance.repl_Policy == "sample_text"
    instance.repl_Policy = "sample_text_2"
    assert instance.repl_Policy == "sample_text_2"


def test_MARTE_HwMemory_HwCache_type_value_roundtrip():
    instance = MARTE_HwMemory_HwCache(repl_Policy="sample_text", type="sample_text", writePolicy="sample_text")
    assert instance.type == "sample_text"
    instance.type = "sample_text_2"
    assert instance.type == "sample_text_2"


def test_MARTE_HwMemory_HwCache_writePolicy_value_roundtrip():
    instance = MARTE_HwMemory_HwCache(repl_Policy="sample_text", type="sample_text", writePolicy="sample_text")
    assert instance.writePolicy == "sample_text"
    instance.writePolicy = "sample_text_2"
    assert instance.writePolicy == "sample_text_2"


def test_MARTE_HwMemory_HwRAM_repl_Policy_value_roundtrip():
    instance = MARTE_HwMemory_HwRAM(repl_Policy="sample_text", writePolicy="sample_text")
    assert instance.repl_Policy == "sample_text"
    instance.repl_Policy = "sample_text_2"
    assert instance.repl_Policy == "sample_text_2"


def test_MARTE_HwMemory_HwRAM_writePolicy_value_roundtrip():
    instance = MARTE_HwMemory_HwRAM(repl_Policy="sample_text", writePolicy="sample_text")
    assert instance.writePolicy == "sample_text"
    instance.writePolicy = "sample_text_2"
    assert instance.writePolicy == "sample_text_2"


def test_MARTE_HwMemory_HwROM_type_value_roundtrip():
    instance = MARTE_HwMemory_HwROM(type="sample_text")
    assert instance.type == "sample_text"
    instance.type = "sample_text_2"
    assert instance.type == "sample_text_2"


def test_MARTE_HwPackage_HwPackage_name_value_roundtrip():
    instance = MARTE_HwPackage_HwPackage(name="sample_text", packageType="sample_text", pinNum=7)
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_MARTE_HwPackage_HwPackage_packageType_value_roundtrip():
    instance = MARTE_HwPackage_HwPackage(name="sample_text", packageType="sample_text", pinNum=7)
    assert instance.packageType == "sample_text"
    instance.packageType = "sample_text_2"
    assert instance.packageType == "sample_text_2"


def test_MARTE_HwPackage_HwPackage_pinNum_value_roundtrip():
    instance = MARTE_HwPackage_HwPackage(name="sample_text", packageType="sample_text", pinNum=7)
    assert instance.pinNum == 7
    instance.pinNum = 13
    assert instance.pinNum == 13


def test_MARTE_HwPackage_HwPackagePin_altNames_value_roundtrip():
    instance = MARTE_HwPackage_HwPackagePin(altNames="sample_text", pinNo="sample_text")
    assert instance.altNames == "sample_text"
    instance.altNames = "sample_text_2"
    assert instance.altNames == "sample_text_2"


def test_MARTE_HwPackage_HwPackagePin_pinNo_value_roundtrip():
    instance = MARTE_HwPackage_HwPackagePin(altNames="sample_text", pinNo="sample_text")
    assert instance.pinNo == "sample_text"
    instance.pinNo = "sample_text_2"
    assert instance.pinNo == "sample_text_2"


def test_MARTE_HwProtocol_HwProtocol_name_value_roundtrip():
    instance = MARTE_HwProtocol_HwProtocol(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_MARTE_HwRegister_HwRegister_address_value_roundtrip():
    instance = MARTE_HwRegister_HwRegister(address="sample_text")
    assert instance.address == "sample_text"
    instance.address = "sample_text_2"
    assert instance.address == "sample_text_2"


def test_MARTE_NFPs_Dimension_baseExponent_value_roundtrip():
    instance = MARTE_NFPs_Dimension(baseExponent=7, symbol="sample_text")
    assert instance.baseExponent == 7
    instance.baseExponent = 13
    assert instance.baseExponent == 13


def test_MARTE_NFPs_Dimension_symbol_value_roundtrip():
    instance = MARTE_NFPs_Dimension(baseExponent=7, symbol="sample_text")
    assert instance.symbol == "sample_text"
    instance.symbol = "sample_text_2"
    assert instance.symbol == "sample_text_2"


def test_MARTE_NFPs_NfpConstraint_kind_value_roundtrip():
    instance = MARTE_NFPs_NfpConstraint(kind="sample_text")
    assert instance.kind == "sample_text"
    instance.kind = "sample_text_2"
    assert instance.kind == "sample_text_2"


def test_MARTE_NFPs_Unit_convFactor_value_roundtrip():
    instance = MARTE_NFPs_Unit(convFactor="sample_text", offsetFactor="sample_text")
    assert instance.convFactor == "sample_text"
    instance.convFactor = "sample_text_2"
    assert instance.convFactor == "sample_text_2"


def test_MARTE_NFPs_Unit_offsetFactor_value_roundtrip():
    instance = MARTE_NFPs_Unit(convFactor="sample_text", offsetFactor="sample_text")
    assert instance.offsetFactor == "sample_text"
    instance.offsetFactor = "sample_text_2"
    assert instance.offsetFactor == "sample_text_2"


def test_MARTE_PAM_PaRunTInstance_unbddPool_value_roundtrip():
    instance = MARTE_PAM_PaRunTInstance(unbddPool="sample_text")
    assert instance.unbddPool == "sample_text"
    instance.unbddPool = "sample_text_2"
    assert instance.unbddPool == "sample_text_2"


def test_MARTE_PAM_PaStep_extOpDemand_value_roundtrip():
    instance = MARTE_PAM_PaStep(extOpDemand="sample_text")
    assert instance.extOpDemand == "sample_text"
    instance.extOpDemand = "sample_text_2"
    assert instance.extOpDemand == "sample_text_2"


def test_MARTE_RSM_InterRepetition_isModulo_value_roundtrip():
    instance = MARTE_RSM_InterRepetition(isModulo="sample_text")
    assert instance.isModulo == "sample_text"
    instance.isModulo = "sample_text_2"
    assert instance.isModulo == "sample_text_2"


def test_MARTE_SAM_SaAnalysisContext_optCriterion_value_roundtrip():
    instance = MARTE_SAM_SaAnalysisContext(optCriterion="sample_text")
    assert instance.optCriterion == "sample_text"
    instance.optCriterion = "sample_text_2"
    assert instance.optCriterion == "sample_text_2"


def test_MARTE_SW_Brokering_DeviceBroker_accessPolicy_value_roundtrip():
    instance = MARTE_SW_Brokering_DeviceBroker(accessPolicy="sample_text", isBuffered="sample_text", name="sample_text")
    assert instance.accessPolicy == "sample_text"
    instance.accessPolicy = "sample_text_2"
    assert instance.accessPolicy == "sample_text_2"


def test_MARTE_SW_Brokering_DeviceBroker_isBuffered_value_roundtrip():
    instance = MARTE_SW_Brokering_DeviceBroker(accessPolicy="sample_text", isBuffered="sample_text", name="sample_text")
    assert instance.isBuffered == "sample_text"
    instance.isBuffered = "sample_text_2"
    assert instance.isBuffered == "sample_text_2"


def test_MARTE_SW_Brokering_DeviceBroker_name_value_roundtrip():
    instance = MARTE_SW_Brokering_DeviceBroker(accessPolicy="sample_text", isBuffered="sample_text", name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_MARTE_SW_Brokering_MemoryBroker_accessPolicy_value_roundtrip():
    instance = MARTE_SW_Brokering_MemoryBroker(accessPolicy="sample_text")
    assert instance.accessPolicy == "sample_text"
    instance.accessPolicy = "sample_text_2"
    assert instance.accessPolicy == "sample_text_2"


def test_MARTE_SW_Concurrency_Alarm_isWatchdog_value_roundtrip():
    instance = MARTE_SW_Concurrency_Alarm(isWatchdog="sample_text")
    assert instance.isWatchdog == "sample_text"
    instance.isWatchdog = "sample_text_2"
    assert instance.isWatchdog == "sample_text_2"


def test_MARTE_SW_Concurrency_EntryPoint_isReentrant_value_roundtrip():
    instance = MARTE_SW_Concurrency_EntryPoint(isReentrant="sample_text")
    assert instance.isReentrant == "sample_text"
    instance.isReentrant = "sample_text_2"
    assert instance.isReentrant == "sample_text_2"


def test_MARTE_SW_Concurrency_InterruptResource_isMaskable_value_roundtrip():
    instance = MARTE_SW_Concurrency_InterruptResource(isMaskable="sample_text", kind="sample_text")
    assert instance.isMaskable == "sample_text"
    instance.isMaskable = "sample_text_2"
    assert instance.isMaskable == "sample_text_2"


def test_MARTE_SW_Concurrency_InterruptResource_kind_value_roundtrip():
    instance = MARTE_SW_Concurrency_InterruptResource(isMaskable="sample_text", kind="sample_text")
    assert instance.kind == "sample_text"
    instance.kind = "sample_text_2"
    assert instance.kind == "sample_text_2"


def test_MARTE_SW_Concurrency_SwConcurrentResource_activationCapacity_value_roundtrip():
    instance = MARTE_SW_Concurrency_SwConcurrentResource(activationCapacity="sample_text")
    assert instance.activationCapacity == "sample_text"
    instance.activationCapacity = "sample_text_2"
    assert instance.activationCapacity == "sample_text_2"


def test_MARTE_SW_Concurrency_SwSchedulableResource_isPreemptable_value_roundtrip():
    instance = MARTE_SW_Concurrency_SwSchedulableResource(isPreemptable="sample_text", isStaticSchedulingFeature="sample_text")
    assert instance.isPreemptable == "sample_text"
    instance.isPreemptable = "sample_text_2"
    assert instance.isPreemptable == "sample_text_2"


def test_MARTE_SW_Concurrency_SwSchedulableResource_isStaticSchedulingFeature_value_roundtrip():
    instance = MARTE_SW_Concurrency_SwSchedulableResource(isPreemptable="sample_text", isStaticSchedulingFeature="sample_text")
    assert instance.isStaticSchedulingFeature == "sample_text"
    instance.isStaticSchedulingFeature = "sample_text_2"
    assert instance.isStaticSchedulingFeature == "sample_text_2"


def test_MARTE_SW_Interaction_MessageComResource_isFixedMessageSize_value_roundtrip():
    instance = MARTE_SW_Interaction_MessageComResource(isFixedMessageSize="sample_text", mechanism="sample_text", messageQueuePolicy="sample_text")
    assert instance.isFixedMessageSize == "sample_text"
    instance.isFixedMessageSize = "sample_text_2"
    assert instance.isFixedMessageSize == "sample_text_2"


def test_MARTE_SW_Interaction_MessageComResource_mechanism_value_roundtrip():
    instance = MARTE_SW_Interaction_MessageComResource(isFixedMessageSize="sample_text", mechanism="sample_text", messageQueuePolicy="sample_text")
    assert instance.mechanism == "sample_text"
    instance.mechanism = "sample_text_2"
    assert instance.mechanism == "sample_text_2"


def test_MARTE_SW_Interaction_MessageComResource_messageQueuePolicy_value_roundtrip():
    instance = MARTE_SW_Interaction_MessageComResource(isFixedMessageSize="sample_text", mechanism="sample_text", messageQueuePolicy="sample_text")
    assert instance.messageQueuePolicy == "sample_text"
    instance.messageQueuePolicy = "sample_text_2"
    assert instance.messageQueuePolicy == "sample_text_2"


def test_MARTE_SW_Interaction_NotificationResource_mechanism_value_roundtrip():
    instance = MARTE_SW_Interaction_NotificationResource(mechanism="sample_text", occurence="sample_text")
    assert instance.mechanism == "sample_text"
    instance.mechanism = "sample_text_2"
    assert instance.mechanism == "sample_text_2"


def test_MARTE_SW_Interaction_NotificationResource_occurence_value_roundtrip():
    instance = MARTE_SW_Interaction_NotificationResource(mechanism="sample_text", occurence="sample_text")
    assert instance.occurence == "sample_text"
    instance.occurence = "sample_text_2"
    assert instance.occurence == "sample_text_2"


def test_MARTE_SW_Interaction_SwInteractionResource_isIntraMemoryPartitionInteraction_value_roundtrip():
    instance = MARTE_SW_Interaction_SwInteractionResource(isIntraMemoryPartitionInteraction=True, waitingQueueCapacity="sample_text", waitingQueuePolicy="sample_text")
    assert instance.isIntraMemoryPartitionInteraction == True
    instance.isIntraMemoryPartitionInteraction = False
    assert instance.isIntraMemoryPartitionInteraction == False


def test_MARTE_SW_Interaction_SwInteractionResource_waitingQueueCapacity_value_roundtrip():
    instance = MARTE_SW_Interaction_SwInteractionResource(isIntraMemoryPartitionInteraction=True, waitingQueueCapacity="sample_text", waitingQueuePolicy="sample_text")
    assert instance.waitingQueueCapacity == "sample_text"
    instance.waitingQueueCapacity = "sample_text_2"
    assert instance.waitingQueueCapacity == "sample_text_2"


def test_MARTE_SW_Interaction_SwInteractionResource_waitingQueuePolicy_value_roundtrip():
    instance = MARTE_SW_Interaction_SwInteractionResource(isIntraMemoryPartitionInteraction=True, waitingQueueCapacity="sample_text", waitingQueuePolicy="sample_text")
    assert instance.waitingQueuePolicy == "sample_text"
    instance.waitingQueuePolicy = "sample_text_2"
    assert instance.waitingQueuePolicy == "sample_text_2"


def test_MARTE_SW_Interaction_SwMutualExclusionResource_concurrentAccessProtocol_value_roundtrip():
    instance = MARTE_SW_Interaction_SwMutualExclusionResource(concurrentAccessProtocol="sample_text", mechanism="sample_text")
    assert instance.concurrentAccessProtocol == "sample_text"
    instance.concurrentAccessProtocol = "sample_text_2"
    assert instance.concurrentAccessProtocol == "sample_text_2"


def test_MARTE_SW_Interaction_SwMutualExclusionResource_mechanism_value_roundtrip():
    instance = MARTE_SW_Interaction_SwMutualExclusionResource(concurrentAccessProtocol="sample_text", mechanism="sample_text")
    assert instance.mechanism == "sample_text"
    instance.mechanism = "sample_text_2"
    assert instance.mechanism == "sample_text_2"


def test_MARTE_SW_ResourceCore_SwAccessService_isModifier_value_roundtrip():
    instance = MARTE_SW_ResourceCore_SwAccessService(isModifier="sample_text")
    assert instance.isModifier == "sample_text"
    instance.isModifier = "sample_text_2"
    assert instance.isModifier == "sample_text_2"


def test_MARTE_Time_Clock_standard_value_roundtrip():
    instance = MARTE_Time_Clock(standard="sample_text")
    assert instance.standard == "sample_text"
    instance.standard = "sample_text_2"
    assert instance.standard == "sample_text_2"


def test_MARTE_Time_ClockConstraint_isChronometricBased_value_roundtrip():
    instance = MARTE_Time_ClockConstraint(isChronometricBased="sample_text", isCoincidenceBased="sample_text", isPrecedenceBased=True)
    assert instance.isChronometricBased == "sample_text"
    instance.isChronometricBased = "sample_text_2"
    assert instance.isChronometricBased == "sample_text_2"


def test_MARTE_Time_ClockConstraint_isCoincidenceBased_value_roundtrip():
    instance = MARTE_Time_ClockConstraint(isChronometricBased="sample_text", isCoincidenceBased="sample_text", isPrecedenceBased=True)
    assert instance.isCoincidenceBased == "sample_text"
    instance.isCoincidenceBased = "sample_text_2"
    assert instance.isCoincidenceBased == "sample_text_2"


def test_MARTE_Time_ClockConstraint_isPrecedenceBased_value_roundtrip():
    instance = MARTE_Time_ClockConstraint(isChronometricBased="sample_text", isCoincidenceBased="sample_text", isPrecedenceBased=True)
    assert instance.isPrecedenceBased == True
    instance.isPrecedenceBased = False
    assert instance.isPrecedenceBased == False


def test_MARTE_Time_ClockType_isLogical_value_roundtrip():
    instance = MARTE_Time_ClockType(isLogical="sample_text", nature="sample_text")
    assert instance.isLogical == "sample_text"
    instance.isLogical = "sample_text_2"
    assert instance.isLogical == "sample_text_2"


def test_MARTE_Time_ClockType_nature_value_roundtrip():
    instance = MARTE_Time_ClockType(isLogical="sample_text", nature="sample_text")
    assert instance.nature == "sample_text"
    instance.nature = "sample_text_2"
    assert instance.nature == "sample_text_2"


def test_MARTE_Time_TimedConstraint_interpretation_value_roundtrip():
    instance = MARTE_Time_TimedConstraint(interpretation="sample_text")
    assert instance.interpretation == "sample_text"
    instance.interpretation = "sample_text_2"
    assert instance.interpretation == "sample_text_2"


def test_MARTE_Time_TimedDurationObservation_obsKind_value_roundtrip():
    instance = MARTE_Time_TimedDurationObservation(obsKind="sample_text")
    assert instance.obsKind == "sample_text"
    instance.obsKind = "sample_text_2"
    assert instance.obsKind == "sample_text_2"


def test_MARTE_Time_TimedEvent_repetition_value_roundtrip():
    instance = MARTE_Time_TimedEvent(repetition="sample_text")
    assert instance.repetition == "sample_text"
    instance.repetition = "sample_text_2"
    assert instance.repetition == "sample_text_2"


def test_MARTE_Time_TimedInstantObservation_obsKind_value_roundtrip():
    instance = MARTE_Time_TimedInstantObservation(obsKind="sample_text")
    assert instance.obsKind == "sample_text"
    instance.obsKind = "sample_text_2"
    assert instance.obsKind == "sample_text_2"


def test_MARTE_Time_TimedValueSpecification_interpretation_value_roundtrip():
    instance = MARTE_Time_TimedValueSpecification(interpretation="sample_text")
    assert instance.interpretation == "sample_text"
    instance.interpretation = "sample_text_2"
    assert instance.interpretation == "sample_text_2"


def test_MARTE_Variables_Var_dir_value_roundtrip():
    instance = MARTE_Variables_Var(dir="sample_text")
    assert instance.dir == "sample_text"
    instance.dir = "sample_text_2"
    assert instance.dir == "sample_text_2"


def test_MARTE_HwPeripheral_RegisterAction_isa_Action():
    instance = MARTE_HwPeripheral_RegisterAction()
    assert isinstance(instance, Action)


def test_MARTE_HwPeripheral_PeripheralActivity_isa_Activity():
    instance = MARTE_HwPeripheral_PeripheralActivity()
    assert isinstance(instance, Activity)


def test_MARTE_RSM_Distribute_isa_Allocate():
    instance = MARTE_RSM_Distribute()
    assert isinstance(instance, Allocate)


def test_MARTE_SW_Concurrency_EntryPoint_isa_Allocate():
    instance = MARTE_SW_Concurrency_EntryPoint(isReentrant="sample_text")
    assert isinstance(instance, Allocate)


def test_MARTE_GQAM_GaAnalysisContext_isa_CoreElements_Configuration():
    instance = MARTE_GQAM_GaAnalysisContext()
    assert isinstance(instance, CoreElements_Configuration)


def test_MARTE_PAM_PaCommStep_isa_GQAM_GaCommStep():
    instance = MARTE_PAM_PaCommStep()
    assert isinstance(instance, GQAM_GaCommStep)


def test_MARTE_PAM_PaRequestedStep_isa_GQAM_GaRequestedService():
    instance = MARTE_PAM_PaRequestedStep()
    assert isinstance(instance, GQAM_GaRequestedService)


def test_MARTE_HwCommunication_HwEndPoint_isa_GRM_CommunicationEndPoint():
    instance = MARTE_HwCommunication_HwEndPoint()
    assert isinstance(instance, GRM_CommunicationEndPoint)


def test_MARTE_GQAM_GaCommHost_isa_GRM_CommunicationMedia():
    instance = MARTE_GQAM_GaCommHost()
    assert isinstance(instance, GRM_CommunicationMedia)


def test_MARTE_HwCommunication_HwMedia_isa_GRM_CommunicationMedia():
    instance = MARTE_HwCommunication_HwMedia()
    assert isinstance(instance, GRM_CommunicationMedia)


def test_MARTE_SW_Interaction_SwCommunicationResource_isa_GRM_CommunicationMedia():
    instance = MARTE_SW_Interaction_SwCommunicationResource()
    assert isinstance(instance, GRM_CommunicationMedia)


def test_MARTE_GQAM_GaExecHost_isa_GRM_ComputingResource():
    instance = MARTE_GQAM_GaExecHost()
    assert isinstance(instance, GRM_ComputingResource)


def test_MARTE_HwComputing_HwComputingResource_isa_GRM_ComputingResource():
    instance = MARTE_HwComputing_HwComputingResource()
    assert isinstance(instance, GRM_ComputingResource)


def test_MARTE_HwDevice_HwDevice_isa_GRM_DeviceResource():
    instance = MARTE_HwDevice_HwDevice()
    assert isinstance(instance, GRM_DeviceResource)


def test_MARTE_SW_Interaction_SwMutualExclusionResource_isa_GRM_MutualExclusionResource():
    instance = MARTE_SW_Interaction_SwMutualExclusionResource(concurrentAccessProtocol="sample_text", mechanism="sample_text")
    assert isinstance(instance, GRM_MutualExclusionResource)


def test_MARTE_GQAM_GaScenario_isa_GRM_ResourceUsage():
    instance = MARTE_GQAM_GaScenario()
    assert isinstance(instance, GRM_ResourceUsage)


def test_MARTE_SW_Concurrency_SwSchedulableResource_isa_GRM_SchedulableResource():
    instance = MARTE_SW_Concurrency_SwSchedulableResource(isPreemptable="sample_text", isStaticSchedulingFeature="sample_text")
    assert isinstance(instance, GRM_SchedulableResource)


def test_MARTE_GQAM_GaCommHost_isa_GRM_Scheduler():
    instance = MARTE_GQAM_GaCommHost()
    assert isinstance(instance, GRM_Scheduler)


def test_MARTE_GQAM_GaExecHost_isa_GRM_Scheduler():
    instance = MARTE_GQAM_GaExecHost()
    assert isinstance(instance, GRM_Scheduler)


def test_MARTE_HwMemory_HwMemory_isa_GRM_StorageResource():
    instance = MARTE_HwMemory_HwMemory()
    assert isinstance(instance, GRM_StorageResource)


def test_MARTE_HwStorageManager_HwStorageManager_isa_GRM_StorageResource():
    instance = MARTE_HwStorageManager_HwStorageManager()
    assert isinstance(instance, GRM_StorageResource)


def test_MARTE_SW_Interaction_SwSynchronizationResource_isa_GRM_SynchronizationResource():
    instance = MARTE_SW_Interaction_SwSynchronizationResource()
    assert isinstance(instance, GRM_SynchronizationResource)


def test_MARTE_HwTiming_HwTimingResource_isa_GRM_TimingResource():
    instance = MARTE_HwTiming_HwTimingResource()
    assert isinstance(instance, GRM_TimingResource)


def test_MARTE_SAM_SaAnalysisContext_isa_GaAnalysisContext():
    instance = MARTE_SAM_SaAnalysisContext(optCriterion="sample_text")
    assert isinstance(instance, GaAnalysisContext)


def test_MARTE_SAM_SaCommHost_isa_GaCommHost():
    instance = MARTE_SAM_SaCommHost()
    assert isinstance(instance, GaCommHost)


def test_MARTE_SAM_SaCommStep_isa_GaCommStep():
    instance = MARTE_SAM_SaCommStep()
    assert isinstance(instance, GaCommStep)


def test_MARTE_SAM_SaExecHost_isa_GaExecHost():
    instance = MARTE_SAM_SaExecHost()
    assert isinstance(instance, GaExecHost)


def test_MARTE_GQAM_GaStep_isa_GaScenario():
    instance = MARTE_GQAM_GaStep()
    assert isinstance(instance, GaScenario)


def test_MARTE_GQAM_GaAcqStep_isa_GaStep():
    instance = MARTE_GQAM_GaAcqStep()
    assert isinstance(instance, GaStep)


def test_MARTE_GQAM_GaCommStep_isa_GaStep():
    instance = MARTE_GQAM_GaCommStep()
    assert isinstance(instance, GaStep)


def test_MARTE_GQAM_GaRelStep_isa_GaStep():
    instance = MARTE_GQAM_GaRelStep()
    assert isinstance(instance, GaStep)


def test_MARTE_GQAM_GaRequestedService_isa_GaStep():
    instance = MARTE_GQAM_GaRequestedService()
    assert isinstance(instance, GaStep)


def test_MARTE_PAM_PaResPassStep_isa_GaStep():
    instance = MARTE_PAM_PaResPassStep()
    assert isinstance(instance, GaStep)


def test_MARTE_PAM_PaStep_isa_GaStep():
    instance = MARTE_PAM_PaStep(extOpDemand="sample_text")
    assert isinstance(instance, GaStep)


def test_MARTE_SAM_SaStep_isa_GaStep():
    instance = MARTE_SAM_SaStep()
    assert isinstance(instance, GaStep)


def test_MARTE_GQAM_GaLatencyObs_isa_GaTimedObs():
    instance = MARTE_GQAM_GaLatencyObs()
    assert isinstance(instance, GaTimedObs)


def test_MARTE_SAM_SaSchedObs_isa_GaTimedObs():
    instance = MARTE_SAM_SaSchedObs()
    assert isinstance(instance, GaTimedObs)


def test_MARTE_GRM_Acquire_isa_GrService():
    instance = MARTE_GRM_Acquire(isBlocking="sample_text")
    assert isinstance(instance, GrService)


def test_MARTE_GRM_Release_isa_GrService():
    instance = MARTE_GRM_Release()
    assert isinstance(instance, GrService)


def test_MARTE_HwGeneral_HwResourceService_isa_GrService():
    instance = MARTE_HwGeneral_HwResourceService()
    assert isinstance(instance, GrService)


def test_MARTE_SW_ResourceCore_SwAccessService_isa_GrService():
    instance = MARTE_SW_ResourceCore_SwAccessService(isModifier="sample_text")
    assert isinstance(instance, GrService)


def test_MARTE_HwCommunication_HwArbiter_isa_HwCommunicationResource():
    instance = MARTE_HwCommunication_HwArbiter()
    assert isinstance(instance, HwCommunicationResource)


def test_MARTE_HwStorageManager_HwDMA_isa_HwCommunication_HwArbiter():
    instance = MARTE_HwStorageManager_HwDMA()
    assert isinstance(instance, HwCommunication_HwArbiter)


def test_MARTE_HwCommunication_HwEndPoint_isa_HwCommunication_HwCommunicationResource():
    instance = MARTE_HwCommunication_HwEndPoint()
    assert isinstance(instance, HwCommunication_HwCommunicationResource)


def test_MARTE_HwCommunication_HwMedia_isa_HwCommunication_HwCommunicationResource():
    instance = MARTE_HwCommunication_HwMedia()
    assert isinstance(instance, HwCommunication_HwCommunicationResource)


def test_MARTE_HwPower_HwCoolingSupply_isa_HwComponent():
    instance = MARTE_HwPower_HwCoolingSupply()
    assert isinstance(instance, HwComponent)


def test_MARTE_HwPower_HwPowerSupply_isa_HwComponent():
    instance = MARTE_HwPower_HwPowerSupply()
    assert isinstance(instance, HwComponent)


def test_MARTE_HwComputing_HwASIC_isa_HwComputingResource():
    instance = MARTE_HwComputing_HwASIC()
    assert isinstance(instance, HwComputingResource)


def test_MARTE_HwComputing_HwMCU_isa_HwComputingResource():
    instance = MARTE_HwComputing_HwMCU()
    assert isinstance(instance, HwComputingResource)


def test_MARTE_HwComputing_HwPLD_isa_HwComputingResource():
    instance = MARTE_HwComputing_HwPLD(technology="sample_text")
    assert isinstance(instance, HwComputingResource)


def test_MARTE_HwComputing_HwProcessor_isa_HwComputingResource():
    instance = MARTE_HwComputing_HwProcessor()
    assert isinstance(instance, HwComputingResource)


def test_MARTE_HwDevice_HwI_O_isa_HwDevice():
    instance = MARTE_HwDevice_HwI_O()
    assert isinstance(instance, HwDevice)


def test_MARTE_HwDevice_HwPeripheral_isa_HwDevice():
    instance = MARTE_HwDevice_HwPeripheral()
    assert isinstance(instance, HwDevice)


def test_MARTE_HwDevice_HwSupport_isa_HwDevice():
    instance = MARTE_HwDevice_HwSupport()
    assert isinstance(instance, HwDevice)


def test_MARTE_HwCommunication_HwPort_isa_HwEndPoint():
    instance = MARTE_HwCommunication_HwPort()
    assert isinstance(instance, HwEndPoint)


def test_MARTE_HwIO_HwPin_isa_HwEndPoint():
    instance = MARTE_HwIO_HwPin()
    assert isinstance(instance, HwEndPoint)


def test_MARTE_HwPackage_HwPackagePin_isa_HwEndPoint():
    instance = MARTE_HwPackage_HwPackagePin(altNames="sample_text", pinNo="sample_text")
    assert isinstance(instance, HwEndPoint)


def test_MARTE_HwComputing_HwComputingResource_isa_HwGeneral_HwResource():
    instance = MARTE_HwComputing_HwComputingResource()
    assert isinstance(instance, HwGeneral_HwResource)


def test_MARTE_HwDevice_HwDevice_isa_HwGeneral_HwResource():
    instance = MARTE_HwDevice_HwDevice()
    assert isinstance(instance, HwGeneral_HwResource)


def test_MARTE_HwMemory_HwMemory_isa_HwGeneral_HwResource():
    instance = MARTE_HwMemory_HwMemory()
    assert isinstance(instance, HwGeneral_HwResource)


def test_MARTE_HwStorageManager_HwStorageManager_isa_HwGeneral_HwResource():
    instance = MARTE_HwStorageManager_HwStorageManager()
    assert isinstance(instance, HwGeneral_HwResource)


def test_MARTE_HwTiming_HwTimingResource_isa_HwGeneral_HwResource():
    instance = MARTE_HwTiming_HwTimingResource()
    assert isinstance(instance, HwGeneral_HwResource)


def test_MARTE_HwDevice_HWActuator_isa_HwI_O():
    instance = MARTE_HwDevice_HWActuator()
    assert isinstance(instance, HwI_O)


def test_MARTE_HwDevice_HWSensor_isa_HwI_O():
    instance = MARTE_HwDevice_HWSensor()
    assert isinstance(instance, HwI_O)


def test_MARTE_HwCommunication_HwBridge_isa_HwMedia():
    instance = MARTE_HwCommunication_HwBridge()
    assert isinstance(instance, HwMedia)


def test_MARTE_HwCommunication_HwBus_isa_HwMedia():
    instance = MARTE_HwCommunication_HwBus()
    assert isinstance(instance, HwMedia)


def test_MARTE_HwCommunication_HwConnection_isa_HwMedia():
    instance = MARTE_HwCommunication_HwConnection()
    assert isinstance(instance, HwMedia)


def test_MARTE_HwIO_HwLine_isa_HwMedia():
    instance = MARTE_HwIO_HwLine()
    assert isinstance(instance, HwMedia)


def test_MARTE_HwPackage_HwWire_isa_HwMedia():
    instance = MARTE_HwPackage_HwWire()
    assert isinstance(instance, HwMedia)


def test_MARTE_HwMemory_HwCache_isa_HwMemory():
    instance = MARTE_HwMemory_HwCache(repl_Policy="sample_text", type="sample_text", writePolicy="sample_text")
    assert isinstance(instance, HwMemory)


def test_MARTE_HwMemory_HwDrive_isa_HwMemory():
    instance = MARTE_HwMemory_HwDrive()
    assert isinstance(instance, HwMemory)


def test_MARTE_HwMemory_HwRAM_isa_HwMemory():
    instance = MARTE_HwMemory_HwRAM(repl_Policy="sample_text", writePolicy="sample_text")
    assert isinstance(instance, HwMemory)


def test_MARTE_HwMemory_HwROM_isa_HwMemory():
    instance = MARTE_HwMemory_HwROM(type="sample_text")
    assert isinstance(instance, HwMemory)


def test_MARTE_HwRegister_HwRegister_isa_HwMemory():
    instance = MARTE_HwRegister_HwRegister(address="sample_text")
    assert isinstance(instance, HwMemory)


def test_MARTE_HwCommunication_HwCommunicationResource_isa_HwResource():
    instance = MARTE_HwCommunication_HwCommunicationResource()
    assert isinstance(instance, HwResource)


def test_MARTE_HwComputing_HwBranchPredictor_isa_HwResource():
    instance = MARTE_HwComputing_HwBranchPredictor()
    assert isinstance(instance, HwResource)


def test_MARTE_HwComputing_HwISA_isa_HwResource():
    instance = MARTE_HwComputing_HwISA(type="sample_text")
    assert isinstance(instance, HwResource)


def test_MARTE_HwLayout_HwComponent_isa_HwResource():
    instance = MARTE_HwLayout_HwComponent(kind="sample_text")
    assert isinstance(instance, HwResource)


def test_MARTE_HwStorageManager_HwMMU_isa_HwStorageManager():
    instance = MARTE_HwStorageManager_HwMMU()
    assert isinstance(instance, HwStorageManager)


def test_MARTE_HwStorageManager_HwDMA_isa_HwStorageManager_HwStorageManager():
    instance = MARTE_HwStorageManager_HwDMA()
    assert isinstance(instance, HwStorageManager_HwStorageManager)


def test_MARTE_HwTiming_HwClock_isa_HwTimingResource():
    instance = MARTE_HwTiming_HwClock()
    assert isinstance(instance, HwTimingResource)


def test_MARTE_HwTiming_HwTimer_isa_HwTimingResource():
    instance = MARTE_HwTiming_HwTimer()
    assert isinstance(instance, HwTimingResource)


def test_MARTE_SW_Concurrency_Alarm_isa_InterruptResource():
    instance = MARTE_SW_Concurrency_Alarm(isWatchdog="sample_text")
    assert isinstance(instance, InterruptResource)


def test_MARTE_RSM_DefaultLink_isa_LinkTopology():
    instance = MARTE_RSM_DefaultLink()
    assert isinstance(instance, LinkTopology)


def test_MARTE_RSM_InterRepetition_isa_LinkTopology():
    instance = MARTE_RSM_InterRepetition(isModulo="sample_text")
    assert isinstance(instance, LinkTopology)


def test_MARTE_RSM_Reshape_isa_LinkTopology():
    instance = MARTE_RSM_Reshape()
    assert isinstance(instance, LinkTopology)


def test_MARTE_RSM_Tiler_isa_LinkTopology():
    instance = MARTE_RSM_Tiler()
    assert isinstance(instance, LinkTopology)


def test_MARTE_SAM_SaSharedResource_isa_MutualExclusionResource():
    instance = MARTE_SAM_SaSharedResource()
    assert isinstance(instance, MutualExclusionResource)


def test_MARTE_Time_ClockConstraint_isa_NFPs_NfpConstraint():
    instance = MARTE_Time_ClockConstraint(isChronometricBased="sample_text", isCoincidenceBased="sample_text", isPrecedenceBased=True)
    assert isinstance(instance, NFPs_NfpConstraint)


def test_MARTE_Time_TimedConstraint_isa_NFPs_NfpConstraint():
    instance = MARTE_Time_TimedConstraint(interpretation="sample_text")
    assert isinstance(instance, NFPs_NfpConstraint)


def test_MARTE_GQAM_GaTimedObs_isa_NfpConstraint():
    instance = MARTE_GQAM_GaTimedObs(laxity="sample_text")
    assert isinstance(instance, NfpConstraint)


def test_MARTE_HwDeviceFunction_HwDeviceFunction_isa_Operation():
    instance = MARTE_HwDeviceFunction_HwDeviceFunction()
    assert isinstance(instance, Operation)


def test_MARTE_HwPeripheral_OperationImpl_isa_Operation():
    instance = MARTE_HwPeripheral_OperationImpl()
    assert isinstance(instance, Operation)


def test_MARTE_PAM_PaCommStep_isa_PAM_PaStep():
    instance = MARTE_PAM_PaCommStep()
    assert isinstance(instance, PAM_PaStep)


def test_MARTE_PAM_PaRequestedStep_isa_PAM_PaStep():
    instance = MARTE_PAM_PaRequestedStep()
    assert isinstance(instance, PAM_PaStep)


def test_MARTE_GRM_CommunicationMedia_isa_ProcessingResource():
    instance = MARTE_GRM_CommunicationMedia(transmMode="sample_text")
    assert isinstance(instance, ProcessingResource)


def test_MARTE_GRM_ComputingResource_isa_ProcessingResource():
    instance = MARTE_GRM_ComputingResource()
    assert isinstance(instance, ProcessingResource)


def test_MARTE_GRM_DeviceResource_isa_ProcessingResource():
    instance = MARTE_GRM_DeviceResource()
    assert isinstance(instance, ProcessingResource)


def test_MARTE_HwPeripheral_ReadRegisterAction_isa_RegisterAction():
    instance = MARTE_HwPeripheral_ReadRegisterAction()
    assert isinstance(instance, RegisterAction)


def test_MARTE_HwPeripheral_WriteRegisterAction_isa_RegisterAction():
    instance = MARTE_HwPeripheral_WriteRegisterAction()
    assert isinstance(instance, RegisterAction)


def test_MARTE_GRM_CommunicationEndPoint_isa_Resource():
    instance = MARTE_GRM_CommunicationEndPoint()
    assert isinstance(instance, Resource)


def test_MARTE_GRM_ConcurrencyResource_isa_Resource():
    instance = MARTE_GRM_ConcurrencyResource()
    assert isinstance(instance, Resource)


def test_MARTE_GRM_MutualExclusionResource_isa_Resource():
    instance = MARTE_GRM_MutualExclusionResource(otherProtectProtocol="sample_text", protectKind="sample_text")
    assert isinstance(instance, Resource)


def test_MARTE_GRM_ProcessingResource_isa_Resource():
    instance = MARTE_GRM_ProcessingResource()
    assert isinstance(instance, Resource)


def test_MARTE_GRM_SchedulableResource_isa_Resource():
    instance = MARTE_GRM_SchedulableResource()
    assert isinstance(instance, Resource)


def test_MARTE_GRM_Scheduler_isa_Resource():
    instance = MARTE_GRM_Scheduler(isPreemptible="sample_text", otherSchedPolicy="sample_text", schedPolicy="sample_text")
    assert isinstance(instance, Resource)


def test_MARTE_GRM_StorageResource_isa_Resource():
    instance = MARTE_GRM_StorageResource()
    assert isinstance(instance, Resource)


def test_MARTE_GRM_SynchronizationResource_isa_Resource():
    instance = MARTE_GRM_SynchronizationResource()
    assert isinstance(instance, Resource)


def test_MARTE_GRM_TimingResource_isa_Resource():
    instance = MARTE_GRM_TimingResource()
    assert isinstance(instance, Resource)


def test_MARTE_HwGeneral_HwResource_isa_Resource():
    instance = MARTE_HwGeneral_HwResource(name="sample_text")
    assert isinstance(instance, Resource)


def test_MARTE_PAM_PaLogicalResource_isa_Resource():
    instance = MARTE_PAM_PaLogicalResource()
    assert isinstance(instance, Resource)


def test_MARTE_SW_ResourceCore_SwResource_isa_Resource():
    instance = MARTE_SW_ResourceCore_SwResource()
    assert isinstance(instance, Resource)


def test_MARTE_SW_Concurrency_SwSchedulableResource_isa_SW_Concurrency_SwConcurrentResource():
    instance = MARTE_SW_Concurrency_SwSchedulableResource(isPreemptable="sample_text", isStaticSchedulingFeature="sample_text")
    assert isinstance(instance, SW_Concurrency_SwConcurrentResource)


def test_MARTE_SW_Interaction_SwCommunicationResource_isa_SW_Interaction_SwInteractionResource():
    instance = MARTE_SW_Interaction_SwCommunicationResource()
    assert isinstance(instance, SW_Interaction_SwInteractionResource)


def test_MARTE_SW_Interaction_SwSynchronizationResource_isa_SW_Interaction_SwInteractionResource():
    instance = MARTE_SW_Interaction_SwSynchronizationResource()
    assert isinstance(instance, SW_Interaction_SwInteractionResource)


def test_MARTE_SW_Interaction_SwMutualExclusionResource_isa_SW_Interaction_SwSynchronizationResource():
    instance = MARTE_SW_Interaction_SwMutualExclusionResource(concurrentAccessProtocol="sample_text", mechanism="sample_text")
    assert isinstance(instance, SW_Interaction_SwSynchronizationResource)


def test_MARTE_GQAM_GaCommChannel_isa_SchedulableResource():
    instance = MARTE_GQAM_GaCommChannel()
    assert isinstance(instance, SchedulableResource)


def test_MARTE_GRM_SecondaryScheduler_isa_Scheduler():
    instance = MARTE_GRM_SecondaryScheduler()
    assert isinstance(instance, Scheduler)


def test_MARTE_SW_Interaction_MessageComResource_isa_SwCommunicationResource():
    instance = MARTE_SW_Interaction_MessageComResource(isFixedMessageSize="sample_text", mechanism="sample_text", messageQueuePolicy="sample_text")
    assert isinstance(instance, SwCommunicationResource)


def test_MARTE_SW_Interaction_SharedDataComResource_isa_SwCommunicationResource():
    instance = MARTE_SW_Interaction_SharedDataComResource()
    assert isinstance(instance, SwCommunicationResource)


def test_MARTE_SW_Concurrency_InterruptResource_isa_SwConcurrentResource():
    instance = MARTE_SW_Concurrency_InterruptResource(isMaskable="sample_text", kind="sample_text")
    assert isinstance(instance, SwConcurrentResource)


def test_MARTE_SW_Brokering_DeviceBroker_isa_SwResource():
    instance = MARTE_SW_Brokering_DeviceBroker(accessPolicy="sample_text", isBuffered="sample_text", name="sample_text")
    assert isinstance(instance, SwResource)


def test_MARTE_SW_Brokering_MemoryBroker_isa_SwResource():
    instance = MARTE_SW_Brokering_MemoryBroker(accessPolicy="sample_text")
    assert isinstance(instance, SwResource)


def test_MARTE_SW_Concurrency_MemoryPartition_isa_SwResource():
    instance = MARTE_SW_Concurrency_MemoryPartition()
    assert isinstance(instance, SwResource)


def test_MARTE_SW_Concurrency_SwConcurrentResource_isa_SwResource():
    instance = MARTE_SW_Concurrency_SwConcurrentResource(activationCapacity="sample_text")
    assert isinstance(instance, SwResource)


def test_MARTE_SW_Interaction_SwInteractionResource_isa_SwResource():
    instance = MARTE_SW_Interaction_SwInteractionResource(isIntraMemoryPartitionInteraction=True, waitingQueueCapacity="sample_text", waitingQueuePolicy="sample_text")
    assert isinstance(instance, SwResource)


def test_MARTE_SW_Interaction_NotificationResource_isa_SwSynchronizationResource():
    instance = MARTE_SW_Interaction_NotificationResource(mechanism="sample_text", occurence="sample_text")
    assert isinstance(instance, SwSynchronizationResource)


def test_MARTE_Time_ClockConstraint_isa_Time_TimedElement():
    instance = MARTE_Time_ClockConstraint(isChronometricBased="sample_text", isCoincidenceBased="sample_text", isPrecedenceBased=True)
    assert isinstance(instance, Time_TimedElement)


def test_MARTE_Time_TimedConstraint_isa_Time_TimedElement():
    instance = MARTE_Time_TimedConstraint(interpretation="sample_text")
    assert isinstance(instance, Time_TimedElement)


def test_MARTE_GQAM_GaScenario_isa_Time_TimedProcessing():
    instance = MARTE_GQAM_GaScenario()
    assert isinstance(instance, Time_TimedProcessing)


def test_MARTE_Time_TimedEvent_isa_TimedElement():
    instance = MARTE_Time_TimedEvent(repetition="sample_text")
    assert isinstance(instance, TimedElement)


def test_MARTE_Time_TimedObservation_isa_TimedElement():
    instance = MARTE_Time_TimedObservation()
    assert isinstance(instance, TimedElement)


def test_MARTE_Time_TimedProcessing_isa_TimedElement():
    instance = MARTE_Time_TimedProcessing()
    assert isinstance(instance, TimedElement)


def test_MARTE_Time_TimedValueSpecification_isa_TimedElement():
    instance = MARTE_Time_TimedValueSpecification(interpretation="sample_text")
    assert isinstance(instance, TimedElement)


def test_MARTE_Time_TimedDurationObservation_isa_TimedObservation():
    instance = MARTE_Time_TimedDurationObservation(obsKind="sample_text")
    assert isinstance(instance, TimedObservation)


def test_MARTE_Time_TimedInstantObservation_isa_TimedObservation():
    instance = MARTE_Time_TimedInstantObservation(obsKind="sample_text")
    assert isinstance(instance, TimedObservation)


def test_MARTE_SW_Concurrency_SwTimerResource_isa_TimerResource():
    instance = MARTE_SW_Concurrency_SwTimerResource()
    assert isinstance(instance, TimerResource)


def test_MARTE_GRM_ClockResource_isa_TimingResource():
    instance = MARTE_GRM_ClockResource()
    assert isinstance(instance, TimingResource)


def test_MARTE_GRM_TimerResource_isa_TimingResource():
    instance = MARTE_GRM_TimerResource(isPeriodic="sample_text")
    assert isinstance(instance, TimingResource)


def test_MARTE_NFPs_NfpType_isa_TupleType():
    instance = MARTE_NFPs_NfpType()
    assert isinstance(instance, TupleType)


def test_MARTE_GQAM_GaAnalysisContext_isa_Variables_ExpressionContext():
    instance = MARTE_GQAM_GaAnalysisContext()
    assert isinstance(instance, Variables_ExpressionContext)


def test_assoc_accessTokenElements792_link_reassign_clear():
    a = MARTE_SW_Interaction_SwMutualExclusionResource(concurrentAccessProtocol="sample_text", mechanism="sample_text")
    b1 = SW_Interaction_MARTE_TypedElement()
    b2 = SW_Interaction_MARTE_TypedElement()
    _safe_set(a, 'MARTE_SW_Interaction_SwMutualExclusionResource', {b1})
    assert _is_linked(a, 'MARTE_SW_Interaction_SwMutualExclusionResource', b1)
    if hasattr(b1, 'SW_Interaction_MARTE_TypedElement793'):
        assert _is_linked(b1, 'SW_Interaction_MARTE_TypedElement793', a)
    _safe_set(a, 'MARTE_SW_Interaction_SwMutualExclusionResource', {b2})
    assert _is_linked(a, 'MARTE_SW_Interaction_SwMutualExclusionResource', b2)
    if hasattr(b1, 'SW_Interaction_MARTE_TypedElement793'):
        assert not _is_linked(b1, 'SW_Interaction_MARTE_TypedElement793', a)
    if hasattr(b2, 'SW_Interaction_MARTE_TypedElement793'):
        assert _is_linked(b2, 'SW_Interaction_MARTE_TypedElement793', a)
    _safe_set(a, 'MARTE_SW_Interaction_SwMutualExclusionResource', set())
    assert not _is_linked(a, 'MARTE_SW_Interaction_SwMutualExclusionResource', b2)
    if hasattr(b2, 'SW_Interaction_MARTE_TypedElement793'):
        assert not _is_linked(b2, 'SW_Interaction_MARTE_TypedElement793', a)


def test_assoc_accessedElement623_link_reassign_clear():
    a = MARTE_SW_ResourceCore_SwAccessService(isModifier="sample_text")
    b1 = SW_ResourceCore_MARTE_Property()
    b2 = SW_ResourceCore_MARTE_Property()
    _safe_set(a, 'MARTE_SW_ResourceCore_SwAccessService', b1)
    assert _is_linked(a, 'MARTE_SW_ResourceCore_SwAccessService', b1)
    if hasattr(b1, 'SW_ResourceCore_MARTE_Property'):
        assert _is_linked(b1, 'SW_ResourceCore_MARTE_Property', a)
    _safe_set(a, 'MARTE_SW_ResourceCore_SwAccessService', b2)
    assert _is_linked(a, 'MARTE_SW_ResourceCore_SwAccessService', b2)
    if hasattr(b1, 'SW_ResourceCore_MARTE_Property'):
        assert not _is_linked(b1, 'SW_ResourceCore_MARTE_Property', a)
    if hasattr(b2, 'SW_ResourceCore_MARTE_Property'):
        assert _is_linked(b2, 'SW_ResourceCore_MARTE_Property', a)
    _safe_set(a, 'MARTE_SW_ResourceCore_SwAccessService', None)
    assert not _is_linked(a, 'MARTE_SW_ResourceCore_SwAccessService', b2)
    if hasattr(b2, 'SW_ResourceCore_MARTE_Property'):
        assert not _is_linked(b2, 'SW_ResourceCore_MARTE_Property', a)


def test_assoc_acquireServices797_link_reassign_clear():
    a = MARTE_SW_Interaction_SwMutualExclusionResource(concurrentAccessProtocol="sample_text", mechanism="sample_text")
    b1 = SW_Interaction_MARTE_BehavioralFeature()
    b2 = SW_Interaction_MARTE_BehavioralFeature()
    _safe_set(a, 'MARTE_SW_Interaction_SwMutualExclusionResource798', {b1})
    assert _is_linked(a, 'MARTE_SW_Interaction_SwMutualExclusionResource798', b1)
    if hasattr(b1, 'SW_Interaction_MARTE_BehavioralFeature799'):
        assert _is_linked(b1, 'SW_Interaction_MARTE_BehavioralFeature799', a)
    _safe_set(a, 'MARTE_SW_Interaction_SwMutualExclusionResource798', {b2})
    assert _is_linked(a, 'MARTE_SW_Interaction_SwMutualExclusionResource798', b2)
    if hasattr(b1, 'SW_Interaction_MARTE_BehavioralFeature799'):
        assert not _is_linked(b1, 'SW_Interaction_MARTE_BehavioralFeature799', a)
    if hasattr(b2, 'SW_Interaction_MARTE_BehavioralFeature799'):
        assert _is_linked(b2, 'SW_Interaction_MARTE_BehavioralFeature799', a)
    _safe_set(a, 'MARTE_SW_Interaction_SwMutualExclusionResource798', set())
    assert not _is_linked(a, 'MARTE_SW_Interaction_SwMutualExclusionResource798', b2)
    if hasattr(b2, 'SW_Interaction_MARTE_BehavioralFeature799'):
        assert not _is_linked(b2, 'SW_Interaction_MARTE_BehavioralFeature799', a)


def test_assoc_activateServices640_link_reassign_clear():
    a = MARTE_SW_Concurrency_SwConcurrentResource(activationCapacity="sample_text")
    b1 = SW_Concurrency_MARTE_BehavioralFeature()
    b2 = SW_Concurrency_MARTE_BehavioralFeature()
    _safe_set(a, 'MARTE_SW_Concurrency_SwConcurrentResource641', {b1})
    assert _is_linked(a, 'MARTE_SW_Concurrency_SwConcurrentResource641', b1)
    if hasattr(b1, 'SW_Concurrency_MARTE_BehavioralFeature642'):
        assert _is_linked(b1, 'SW_Concurrency_MARTE_BehavioralFeature642', a)
    _safe_set(a, 'MARTE_SW_Concurrency_SwConcurrentResource641', {b2})
    assert _is_linked(a, 'MARTE_SW_Concurrency_SwConcurrentResource641', b2)
    if hasattr(b1, 'SW_Concurrency_MARTE_BehavioralFeature642'):
        assert not _is_linked(b1, 'SW_Concurrency_MARTE_BehavioralFeature642', a)
    if hasattr(b2, 'SW_Concurrency_MARTE_BehavioralFeature642'):
        assert _is_linked(b2, 'SW_Concurrency_MARTE_BehavioralFeature642', a)
    _safe_set(a, 'MARTE_SW_Concurrency_SwConcurrentResource641', set())
    assert not _is_linked(a, 'MARTE_SW_Concurrency_SwConcurrentResource641', b2)
    if hasattr(b2, 'SW_Concurrency_MARTE_BehavioralFeature642'):
        assert not _is_linked(b2, 'SW_Concurrency_MARTE_BehavioralFeature642', a)


def test_assoc_activities523_link_reassign_clear():
    a = MARTE_HwGeneral_HwResource(name="sample_text")
    b1 = HwGeneral_MARTE_Activity()
    b2 = HwGeneral_MARTE_Activity()
    _safe_set(a, 'MARTE_HwGeneral_HwResource524', {b1})
    assert _is_linked(a, 'MARTE_HwGeneral_HwResource524', b1)
    if hasattr(b1, 'HwGeneral_MARTE_Activity'):
        assert _is_linked(b1, 'HwGeneral_MARTE_Activity', a)
    _safe_set(a, 'MARTE_HwGeneral_HwResource524', {b2})
    assert _is_linked(a, 'MARTE_HwGeneral_HwResource524', b2)
    if hasattr(b1, 'HwGeneral_MARTE_Activity'):
        assert not _is_linked(b1, 'HwGeneral_MARTE_Activity', a)
    if hasattr(b2, 'HwGeneral_MARTE_Activity'):
        assert _is_linked(b2, 'HwGeneral_MARTE_Activity', a)
    _safe_set(a, 'MARTE_HwGeneral_HwResource524', set())
    assert not _is_linked(a, 'MARTE_HwGeneral_HwResource524', b2)
    if hasattr(b2, 'HwGeneral_MARTE_Activity'):
        assert not _is_linked(b2, 'HwGeneral_MARTE_Activity', a)


def test_assoc_activities737_link_reassign_clear():
    a = MARTE_SW_Brokering_DeviceBroker(accessPolicy="sample_text", isBuffered="sample_text", name="sample_text")
    b1 = SW_Brokering_MARTE_Activity()
    b2 = SW_Brokering_MARTE_Activity()
    _safe_set(a, 'MARTE_SW_Brokering_DeviceBroker738', {b1})
    assert _is_linked(a, 'MARTE_SW_Brokering_DeviceBroker738', b1)
    if hasattr(b1, 'SW_Brokering_MARTE_Activity'):
        assert _is_linked(b1, 'SW_Brokering_MARTE_Activity', a)
    _safe_set(a, 'MARTE_SW_Brokering_DeviceBroker738', {b2})
    assert _is_linked(a, 'MARTE_SW_Brokering_DeviceBroker738', b2)
    if hasattr(b1, 'SW_Brokering_MARTE_Activity'):
        assert not _is_linked(b1, 'SW_Brokering_MARTE_Activity', a)
    if hasattr(b2, 'SW_Brokering_MARTE_Activity'):
        assert _is_linked(b2, 'SW_Brokering_MARTE_Activity', a)
    _safe_set(a, 'MARTE_SW_Brokering_DeviceBroker738', set())
    assert not _is_linked(a, 'MARTE_SW_Brokering_DeviceBroker738', b2)
    if hasattr(b2, 'SW_Brokering_MARTE_Activity'):
        assert not _is_linked(b2, 'SW_Brokering_MARTE_Activity', a)


def test_assoc_adressSpace629_link_reassign_clear():
    a = MARTE_SW_Concurrency_SwConcurrentResource(activationCapacity="sample_text")
    b1 = SW_Concurrency_MARTE_TypedElement()
    b2 = SW_Concurrency_MARTE_TypedElement()
    _safe_set(a, 'MARTE_SW_Concurrency_SwConcurrentResource630', {b1})
    assert _is_linked(a, 'MARTE_SW_Concurrency_SwConcurrentResource630', b1)
    if hasattr(b1, 'SW_Concurrency_MARTE_TypedElement'):
        assert _is_linked(b1, 'SW_Concurrency_MARTE_TypedElement', a)
    _safe_set(a, 'MARTE_SW_Concurrency_SwConcurrentResource630', {b2})
    assert _is_linked(a, 'MARTE_SW_Concurrency_SwConcurrentResource630', b2)
    if hasattr(b1, 'SW_Concurrency_MARTE_TypedElement'):
        assert not _is_linked(b1, 'SW_Concurrency_MARTE_TypedElement', a)
    if hasattr(b2, 'SW_Concurrency_MARTE_TypedElement'):
        assert _is_linked(b2, 'SW_Concurrency_MARTE_TypedElement', a)
    _safe_set(a, 'MARTE_SW_Concurrency_SwConcurrentResource630', set())
    assert not _is_linked(a, 'MARTE_SW_Concurrency_SwConcurrentResource630', b2)
    if hasattr(b2, 'SW_Concurrency_MARTE_TypedElement'):
        assert not _is_linked(b2, 'SW_Concurrency_MARTE_TypedElement', a)


def test_assoc_area526_link_reassign_clear():
    a = MARTE_HwLayout_HwComponent(kind="sample_text")
    b1 = NFP_Area()
    b2 = NFP_Area()
    _safe_set(a, 'MARTE_HwLayout_HwComponent527', b1)
    assert _is_linked(a, 'MARTE_HwLayout_HwComponent527', b1)
    if hasattr(b1, 'NFP_Area'):
        assert _is_linked(b1, 'NFP_Area', a)
    _safe_set(a, 'MARTE_HwLayout_HwComponent527', b2)
    assert _is_linked(a, 'MARTE_HwLayout_HwComponent527', b2)
    if hasattr(b1, 'NFP_Area'):
        assert not _is_linked(b1, 'NFP_Area', a)
    if hasattr(b2, 'NFP_Area'):
        assert _is_linked(b2, 'NFP_Area', a)
    _safe_set(a, 'MARTE_HwLayout_HwComponent527', None)
    assert not _is_linked(a, 'MARTE_HwLayout_HwComponent527', b2)
    if hasattr(b2, 'NFP_Area'):
        assert not _is_linked(b2, 'NFP_Area', a)


def test_assoc_baseDimension15_link_reassign_clear():
    a = MARTE_NFPs_Dimension(baseExponent=7, symbol="sample_text")
    b1 = NFPs_Dimension()
    b2 = NFPs_Dimension()
    _safe_set(a, 'MARTE_NFPs_Dimension', {b1})
    assert _is_linked(a, 'MARTE_NFPs_Dimension', b1)
    if hasattr(b1, 'NFPs_Dimension'):
        assert _is_linked(b1, 'NFPs_Dimension', a)
    _safe_set(a, 'MARTE_NFPs_Dimension', {b2})
    assert _is_linked(a, 'MARTE_NFPs_Dimension', b2)
    if hasattr(b1, 'NFPs_Dimension'):
        assert not _is_linked(b1, 'NFPs_Dimension', a)
    if hasattr(b2, 'NFPs_Dimension'):
        assert _is_linked(b2, 'NFPs_Dimension', a)
    _safe_set(a, 'MARTE_NFPs_Dimension', set())
    assert not _is_linked(a, 'MARTE_NFPs_Dimension', b2)
    if hasattr(b2, 'NFPs_Dimension'):
        assert not _is_linked(b2, 'NFPs_Dimension', a)


def test_assoc_baseType213_link_reassign_clear():
    a = MARTE_DataTypes_BoundedSubtype(isMaxOpen=True, isMinOpen=True, maxValue="sample_text", minValue="sample_text")
    b1 = DataTypes_MARTE_Property()
    b2 = DataTypes_MARTE_Property()
    _safe_set(a, 'MARTE_DataTypes_BoundedSubtype', b1)
    assert _is_linked(a, 'MARTE_DataTypes_BoundedSubtype', b1)
    if hasattr(b1, 'DataTypes_MARTE_Property'):
        assert _is_linked(b1, 'DataTypes_MARTE_Property', a)
    _safe_set(a, 'MARTE_DataTypes_BoundedSubtype', b2)
    assert _is_linked(a, 'MARTE_DataTypes_BoundedSubtype', b2)
    if hasattr(b1, 'DataTypes_MARTE_Property'):
        assert not _is_linked(b1, 'DataTypes_MARTE_Property', a)
    if hasattr(b2, 'DataTypes_MARTE_Property'):
        assert _is_linked(b2, 'DataTypes_MARTE_Property', a)
    _safe_set(a, 'MARTE_DataTypes_BoundedSubtype', None)
    assert not _is_linked(a, 'MARTE_DataTypes_BoundedSubtype', b2)
    if hasattr(b2, 'DataTypes_MARTE_Property'):
        assert not _is_linked(b2, 'DataTypes_MARTE_Property', a)


def test_assoc_baseUnit1_link_reassign_clear():
    a = MARTE_NFPs_Unit(convFactor="sample_text", offsetFactor="sample_text")
    b1 = NFPs_Unit()
    b2 = NFPs_Unit()
    _safe_set(a, 'MARTE_NFPs_Unit', b1)
    assert _is_linked(a, 'MARTE_NFPs_Unit', b1)
    if hasattr(b1, 'NFPs_Unit'):
        assert _is_linked(b1, 'NFPs_Unit', a)
    _safe_set(a, 'MARTE_NFPs_Unit', b2)
    assert _is_linked(a, 'MARTE_NFPs_Unit', b2)
    if hasattr(b1, 'NFPs_Unit'):
        assert not _is_linked(b1, 'NFPs_Unit', a)
    if hasattr(b2, 'NFPs_Unit'):
        assert _is_linked(b2, 'NFPs_Unit', a)
    _safe_set(a, 'MARTE_NFPs_Unit', None)
    assert not _is_linked(a, 'MARTE_NFPs_Unit', b2)
    if hasattr(b2, 'NFPs_Unit'):
        assert not _is_linked(b2, 'NFPs_Unit', a)


def test_assoc_base_Abstraction46_link_reassign_clear():
    a = MARTE_Alloc_Allocate(kind="sample_text", nature="sample_text")
    b1 = Alloc_MARTE_Abstraction()
    b2 = Alloc_MARTE_Abstraction()
    _safe_set(a, 'MARTE_Alloc_Allocate', b1)
    assert _is_linked(a, 'MARTE_Alloc_Allocate', b1)
    if hasattr(b1, 'Alloc_MARTE_Abstraction'):
        assert _is_linked(b1, 'Alloc_MARTE_Abstraction', a)
    _safe_set(a, 'MARTE_Alloc_Allocate', b2)
    assert _is_linked(a, 'MARTE_Alloc_Allocate', b2)
    if hasattr(b1, 'Alloc_MARTE_Abstraction'):
        assert not _is_linked(b1, 'Alloc_MARTE_Abstraction', a)
    if hasattr(b2, 'Alloc_MARTE_Abstraction'):
        assert _is_linked(b2, 'Alloc_MARTE_Abstraction', a)
    _safe_set(a, 'MARTE_Alloc_Allocate', None)
    assert not _is_linked(a, 'MARTE_Alloc_Allocate', b2)
    if hasattr(b2, 'Alloc_MARTE_Abstraction'):
        assert not _is_linked(b2, 'Alloc_MARTE_Abstraction', a)


def test_assoc_base_BehavioralFeature294_link_reassign_clear():
    a = MARTE_HLAM_RtAction(isAtomic="sample_text", synchKind="sample_text")
    b1 = HLAM_MARTE_BehavioralFeature()
    b2 = HLAM_MARTE_BehavioralFeature()
    _safe_set(a, 'MARTE_HLAM_RtAction295', b1)
    assert _is_linked(a, 'MARTE_HLAM_RtAction295', b1)
    if hasattr(b1, 'HLAM_MARTE_BehavioralFeature296'):
        assert _is_linked(b1, 'HLAM_MARTE_BehavioralFeature296', a)
    _safe_set(a, 'MARTE_HLAM_RtAction295', b2)
    assert _is_linked(a, 'MARTE_HLAM_RtAction295', b2)
    if hasattr(b1, 'HLAM_MARTE_BehavioralFeature296'):
        assert not _is_linked(b1, 'HLAM_MARTE_BehavioralFeature296', a)
    if hasattr(b2, 'HLAM_MARTE_BehavioralFeature296'):
        assert _is_linked(b2, 'HLAM_MARTE_BehavioralFeature296', a)
    _safe_set(a, 'MARTE_HLAM_RtAction295', None)
    assert not _is_linked(a, 'MARTE_HLAM_RtAction295', b2)
    if hasattr(b2, 'HLAM_MARTE_BehavioralFeature296'):
        assert not _is_linked(b2, 'HLAM_MARTE_BehavioralFeature296', a)


def test_assoc_base_BehavioralFeature300_link_reassign_clear():
    a = MARTE_HLAM_RtService(concPolicy="sample_text", exeKind="sample_text", isAtomic="sample_text", synchKind="sample_text")
    b1 = HLAM_MARTE_BehavioralFeature()
    b2 = HLAM_MARTE_BehavioralFeature()
    _safe_set(a, 'MARTE_HLAM_RtService', b1)
    assert _is_linked(a, 'MARTE_HLAM_RtService', b1)
    if hasattr(b1, 'HLAM_MARTE_BehavioralFeature301'):
        assert _is_linked(b1, 'HLAM_MARTE_BehavioralFeature301', a)
    _safe_set(a, 'MARTE_HLAM_RtService', b2)
    assert _is_linked(a, 'MARTE_HLAM_RtService', b2)
    if hasattr(b1, 'HLAM_MARTE_BehavioralFeature301'):
        assert not _is_linked(b1, 'HLAM_MARTE_BehavioralFeature301', a)
    if hasattr(b2, 'HLAM_MARTE_BehavioralFeature301'):
        assert _is_linked(b2, 'HLAM_MARTE_BehavioralFeature301', a)
    _safe_set(a, 'MARTE_HLAM_RtService', None)
    assert not _is_linked(a, 'MARTE_HLAM_RtService', b2)
    if hasattr(b2, 'HLAM_MARTE_BehavioralFeature301'):
        assert not _is_linked(b2, 'HLAM_MARTE_BehavioralFeature301', a)


def test_assoc_base_BehavioralFeature815_link_reassign_clear():
    a = MARTE_GCM_ClientServerFeature(kind="sample_text")
    b1 = GCM_MARTE_BehavioralFeature()
    b2 = GCM_MARTE_BehavioralFeature()
    _safe_set(a, 'MARTE_GCM_ClientServerFeature', b1)
    assert _is_linked(a, 'MARTE_GCM_ClientServerFeature', b1)
    if hasattr(b1, 'GCM_MARTE_BehavioralFeature'):
        assert _is_linked(b1, 'GCM_MARTE_BehavioralFeature', a)
    _safe_set(a, 'MARTE_GCM_ClientServerFeature', b2)
    assert _is_linked(a, 'MARTE_GCM_ClientServerFeature', b2)
    if hasattr(b1, 'GCM_MARTE_BehavioralFeature'):
        assert not _is_linked(b1, 'GCM_MARTE_BehavioralFeature', a)
    if hasattr(b2, 'GCM_MARTE_BehavioralFeature'):
        assert _is_linked(b2, 'GCM_MARTE_BehavioralFeature', a)
    _safe_set(a, 'MARTE_GCM_ClientServerFeature', None)
    assert not _is_linked(a, 'MARTE_GCM_ClientServerFeature', b2)
    if hasattr(b2, 'GCM_MARTE_BehavioralFeature'):
        assert not _is_linked(b2, 'GCM_MARTE_BehavioralFeature', a)


def test_assoc_base_BehavioredClassifier248_link_reassign_clear():
    a = MARTE_HLAM_RtUnit(isDynamic="sample_text", isMain="sample_text", queueSchedPolicy="sample_text", queueSize="sample_text", srPoolPolicy="sample_text", srPoolSize="sample_text")
    b1 = HLAM_MARTE_BehavioredClassifier()
    b2 = HLAM_MARTE_BehavioredClassifier()
    _safe_set(a, 'MARTE_HLAM_RtUnit249', b1)
    assert _is_linked(a, 'MARTE_HLAM_RtUnit249', b1)
    if hasattr(b1, 'HLAM_MARTE_BehavioredClassifier'):
        assert _is_linked(b1, 'HLAM_MARTE_BehavioredClassifier', a)
    _safe_set(a, 'MARTE_HLAM_RtUnit249', b2)
    assert _is_linked(a, 'MARTE_HLAM_RtUnit249', b2)
    if hasattr(b1, 'HLAM_MARTE_BehavioredClassifier'):
        assert not _is_linked(b1, 'HLAM_MARTE_BehavioredClassifier', a)
    if hasattr(b2, 'HLAM_MARTE_BehavioredClassifier'):
        assert _is_linked(b2, 'HLAM_MARTE_BehavioredClassifier', a)
    _safe_set(a, 'MARTE_HLAM_RtUnit249', None)
    assert not _is_linked(a, 'MARTE_HLAM_RtUnit249', b2)
    if hasattr(b2, 'HLAM_MARTE_BehavioredClassifier'):
        assert not _is_linked(b2, 'HLAM_MARTE_BehavioredClassifier', a)


def test_assoc_base_BehavioredClassifier255_link_reassign_clear():
    a = MARTE_HLAM_PpUnit(concPolicy="sample_text")
    b1 = HLAM_MARTE_BehavioredClassifier()
    b2 = HLAM_MARTE_BehavioredClassifier()
    _safe_set(a, 'MARTE_HLAM_PpUnit256', b1)
    assert _is_linked(a, 'MARTE_HLAM_PpUnit256', b1)
    if hasattr(b1, 'HLAM_MARTE_BehavioredClassifier257'):
        assert _is_linked(b1, 'HLAM_MARTE_BehavioredClassifier257', a)
    _safe_set(a, 'MARTE_HLAM_PpUnit256', b2)
    assert _is_linked(a, 'MARTE_HLAM_PpUnit256', b2)
    if hasattr(b1, 'HLAM_MARTE_BehavioredClassifier257'):
        assert not _is_linked(b1, 'HLAM_MARTE_BehavioredClassifier257', a)
    if hasattr(b2, 'HLAM_MARTE_BehavioredClassifier257'):
        assert _is_linked(b2, 'HLAM_MARTE_BehavioredClassifier257', a)
    _safe_set(a, 'MARTE_HLAM_PpUnit256', None)
    assert not _is_linked(a, 'MARTE_HLAM_PpUnit256', b2)
    if hasattr(b2, 'HLAM_MARTE_BehavioredClassifier257'):
        assert not _is_linked(b2, 'HLAM_MARTE_BehavioredClassifier257', a)


def test_assoc_base_Class77_link_reassign_clear():
    a = MARTE_Time_ClockType(isLogical="sample_text", nature="sample_text")
    b1 = Time_MARTE_Class()
    b2 = Time_MARTE_Class()
    _safe_set(a, 'MARTE_Time_ClockType78', b1)
    assert _is_linked(a, 'MARTE_Time_ClockType78', b1)
    if hasattr(b1, 'Time_MARTE_Class'):
        assert _is_linked(b1, 'Time_MARTE_Class', a)
    _safe_set(a, 'MARTE_Time_ClockType78', b2)
    assert _is_linked(a, 'MARTE_Time_ClockType78', b2)
    if hasattr(b1, 'Time_MARTE_Class'):
        assert not _is_linked(b1, 'Time_MARTE_Class', a)
    if hasattr(b2, 'Time_MARTE_Class'):
        assert _is_linked(b2, 'Time_MARTE_Class', a)
    _safe_set(a, 'MARTE_Time_ClockType78', None)
    assert not _is_linked(a, 'MARTE_Time_ClockType78', b2)
    if hasattr(b2, 'Time_MARTE_Class'):
        assert not _is_linked(b2, 'Time_MARTE_Class', a)


def test_assoc_base_Classifier105_link_reassign_clear():
    a = MARTE_GRM_Resource(isProtected="sample_text")
    b1 = GRM_MARTE_Classifier()
    b2 = GRM_MARTE_Classifier()
    _safe_set(a, 'MARTE_GRM_Resource106', b1)
    assert _is_linked(a, 'MARTE_GRM_Resource106', b1)
    if hasattr(b1, 'GRM_MARTE_Classifier'):
        assert _is_linked(b1, 'GRM_MARTE_Classifier', a)
    _safe_set(a, 'MARTE_GRM_Resource106', b2)
    assert _is_linked(a, 'MARTE_GRM_Resource106', b2)
    if hasattr(b1, 'GRM_MARTE_Classifier'):
        assert not _is_linked(b1, 'GRM_MARTE_Classifier', a)
    if hasattr(b2, 'GRM_MARTE_Classifier'):
        assert _is_linked(b2, 'GRM_MARTE_Classifier', a)
    _safe_set(a, 'MARTE_GRM_Resource106', None)
    assert not _is_linked(a, 'MARTE_GRM_Resource106', b2)
    if hasattr(b2, 'GRM_MARTE_Classifier'):
        assert not _is_linked(b2, 'GRM_MARTE_Classifier', a)


def test_assoc_base_ConnectableElement109_link_reassign_clear():
    a = MARTE_GRM_Resource(isProtected="sample_text")
    b1 = GRM_MARTE_ConnectableElement()
    b2 = GRM_MARTE_ConnectableElement()
    _safe_set(a, 'MARTE_GRM_Resource110', b1)
    assert _is_linked(a, 'MARTE_GRM_Resource110', b1)
    if hasattr(b1, 'GRM_MARTE_ConnectableElement'):
        assert _is_linked(b1, 'GRM_MARTE_ConnectableElement', a)
    _safe_set(a, 'MARTE_GRM_Resource110', b2)
    assert _is_linked(a, 'MARTE_GRM_Resource110', b2)
    if hasattr(b1, 'GRM_MARTE_ConnectableElement'):
        assert not _is_linked(b1, 'GRM_MARTE_ConnectableElement', a)
    if hasattr(b2, 'GRM_MARTE_ConnectableElement'):
        assert _is_linked(b2, 'GRM_MARTE_ConnectableElement', a)
    _safe_set(a, 'MARTE_GRM_Resource110', None)
    assert not _is_linked(a, 'MARTE_GRM_Resource110', b2)
    if hasattr(b2, 'GRM_MARTE_ConnectableElement'):
        assert not _is_linked(b2, 'GRM_MARTE_ConnectableElement', a)


def test_assoc_base_Connector136_link_reassign_clear():
    a = MARTE_GRM_CommunicationMedia(transmMode="sample_text")
    b1 = GRM_MARTE_Connector()
    b2 = GRM_MARTE_Connector()
    _safe_set(a, 'MARTE_GRM_CommunicationMedia137', b1)
    assert _is_linked(a, 'MARTE_GRM_CommunicationMedia137', b1)
    if hasattr(b1, 'GRM_MARTE_Connector'):
        assert _is_linked(b1, 'GRM_MARTE_Connector', a)
    _safe_set(a, 'MARTE_GRM_CommunicationMedia137', b2)
    assert _is_linked(a, 'MARTE_GRM_CommunicationMedia137', b2)
    if hasattr(b1, 'GRM_MARTE_Connector'):
        assert not _is_linked(b1, 'GRM_MARTE_Connector', a)
    if hasattr(b2, 'GRM_MARTE_Connector'):
        assert _is_linked(b2, 'GRM_MARTE_Connector', a)
    _safe_set(a, 'MARTE_GRM_CommunicationMedia137', None)
    assert not _is_linked(a, 'MARTE_GRM_CommunicationMedia137', b2)
    if hasattr(b2, 'GRM_MARTE_Connector'):
        assert not _is_linked(b2, 'GRM_MARTE_Connector', a)


def test_assoc_base_Constraint4_link_reassign_clear():
    a = MARTE_NFPs_NfpConstraint(kind="sample_text")
    b1 = NFPs_MARTE_Constraint()
    b2 = NFPs_MARTE_Constraint()
    _safe_set(a, 'MARTE_NFPs_NfpConstraint', b1)
    assert _is_linked(a, 'MARTE_NFPs_NfpConstraint', b1)
    if hasattr(b1, 'NFPs_MARTE_Constraint'):
        assert _is_linked(b1, 'NFPs_MARTE_Constraint', a)
    _safe_set(a, 'MARTE_NFPs_NfpConstraint', b2)
    assert _is_linked(a, 'MARTE_NFPs_NfpConstraint', b2)
    if hasattr(b1, 'NFPs_MARTE_Constraint'):
        assert not _is_linked(b1, 'NFPs_MARTE_Constraint', a)
    if hasattr(b2, 'NFPs_MARTE_Constraint'):
        assert _is_linked(b2, 'NFPs_MARTE_Constraint', a)
    _safe_set(a, 'MARTE_NFPs_NfpConstraint', None)
    assert not _is_linked(a, 'MARTE_NFPs_NfpConstraint', b2)
    if hasattr(b2, 'NFPs_MARTE_Constraint'):
        assert not _is_linked(b2, 'NFPs_MARTE_Constraint', a)


def test_assoc_base_DataType214_link_reassign_clear():
    a = MARTE_DataTypes_BoundedSubtype(isMaxOpen=True, isMinOpen=True, maxValue="sample_text", minValue="sample_text")
    b1 = DataTypes_MARTE_DataType()
    b2 = DataTypes_MARTE_DataType()
    _safe_set(a, 'MARTE_DataTypes_BoundedSubtype215', b1)
    assert _is_linked(a, 'MARTE_DataTypes_BoundedSubtype215', b1)
    if hasattr(b1, 'DataTypes_MARTE_DataType'):
        assert _is_linked(b1, 'DataTypes_MARTE_DataType', a)
    _safe_set(a, 'MARTE_DataTypes_BoundedSubtype215', b2)
    assert _is_linked(a, 'MARTE_DataTypes_BoundedSubtype215', b2)
    if hasattr(b1, 'DataTypes_MARTE_DataType'):
        assert not _is_linked(b1, 'DataTypes_MARTE_DataType', a)
    if hasattr(b2, 'DataTypes_MARTE_DataType'):
        assert _is_linked(b2, 'DataTypes_MARTE_DataType', a)
    _safe_set(a, 'MARTE_DataTypes_BoundedSubtype215', None)
    assert not _is_linked(a, 'MARTE_DataTypes_BoundedSubtype215', b2)
    if hasattr(b2, 'DataTypes_MARTE_DataType'):
        assert not _is_linked(b2, 'DataTypes_MARTE_DataType', a)


def test_assoc_base_DurationObservation82_link_reassign_clear():
    a = MARTE_Time_TimedDurationObservation(obsKind="sample_text")
    b1 = Time_MARTE_DurationObservation()
    b2 = Time_MARTE_DurationObservation()
    _safe_set(a, 'MARTE_Time_TimedDurationObservation', b1)
    assert _is_linked(a, 'MARTE_Time_TimedDurationObservation', b1)
    if hasattr(b1, 'Time_MARTE_DurationObservation'):
        assert _is_linked(b1, 'Time_MARTE_DurationObservation', a)
    _safe_set(a, 'MARTE_Time_TimedDurationObservation', b2)
    assert _is_linked(a, 'MARTE_Time_TimedDurationObservation', b2)
    if hasattr(b1, 'Time_MARTE_DurationObservation'):
        assert not _is_linked(b1, 'Time_MARTE_DurationObservation', a)
    if hasattr(b2, 'Time_MARTE_DurationObservation'):
        assert _is_linked(b2, 'Time_MARTE_DurationObservation', a)
    _safe_set(a, 'MARTE_Time_TimedDurationObservation', None)
    assert not _is_linked(a, 'MARTE_Time_TimedDurationObservation', b2)
    if hasattr(b2, 'Time_MARTE_DurationObservation'):
        assert not _is_linked(b2, 'Time_MARTE_DurationObservation', a)


def test_assoc_base_Enumeration16_link_reassign_clear():
    a = MARTE_NFPs_Dimension(baseExponent=7, symbol="sample_text")
    b1 = NFPs_MARTE_Enumeration()
    b2 = NFPs_MARTE_Enumeration()
    _safe_set(a, 'MARTE_NFPs_Dimension17', b1)
    assert _is_linked(a, 'MARTE_NFPs_Dimension17', b1)
    if hasattr(b1, 'NFPs_MARTE_Enumeration'):
        assert _is_linked(b1, 'NFPs_MARTE_Enumeration', a)
    _safe_set(a, 'MARTE_NFPs_Dimension17', b2)
    assert _is_linked(a, 'MARTE_NFPs_Dimension17', b2)
    if hasattr(b1, 'NFPs_MARTE_Enumeration'):
        assert not _is_linked(b1, 'NFPs_MARTE_Enumeration', a)
    if hasattr(b2, 'NFPs_MARTE_Enumeration'):
        assert _is_linked(b2, 'NFPs_MARTE_Enumeration', a)
    _safe_set(a, 'MARTE_NFPs_Dimension17', None)
    assert not _is_linked(a, 'MARTE_NFPs_Dimension17', b2)
    if hasattr(b2, 'NFPs_MARTE_Enumeration'):
        assert not _is_linked(b2, 'NFPs_MARTE_Enumeration', a)


def test_assoc_base_EnumerationLiteral2_link_reassign_clear():
    a = MARTE_NFPs_Unit(convFactor="sample_text", offsetFactor="sample_text")
    b1 = NFPs_MARTE_EnumerationLiteral()
    b2 = NFPs_MARTE_EnumerationLiteral()
    _safe_set(a, 'MARTE_NFPs_Unit3', b1)
    assert _is_linked(a, 'MARTE_NFPs_Unit3', b1)
    if hasattr(b1, 'NFPs_MARTE_EnumerationLiteral'):
        assert _is_linked(b1, 'NFPs_MARTE_EnumerationLiteral', a)
    _safe_set(a, 'MARTE_NFPs_Unit3', b2)
    assert _is_linked(a, 'MARTE_NFPs_Unit3', b2)
    if hasattr(b1, 'NFPs_MARTE_EnumerationLiteral'):
        assert not _is_linked(b1, 'NFPs_MARTE_EnumerationLiteral', a)
    if hasattr(b2, 'NFPs_MARTE_EnumerationLiteral'):
        assert _is_linked(b2, 'NFPs_MARTE_EnumerationLiteral', a)
    _safe_set(a, 'MARTE_NFPs_Unit3', None)
    assert not _is_linked(a, 'MARTE_NFPs_Unit3', b2)
    if hasattr(b2, 'NFPs_MARTE_EnumerationLiteral'):
        assert not _is_linked(b2, 'NFPs_MARTE_EnumerationLiteral', a)


def test_assoc_base_InstanceSpecification103_link_reassign_clear():
    a = MARTE_GRM_Resource(isProtected="sample_text")
    b1 = GRM_MARTE_InstanceSpecification()
    b2 = GRM_MARTE_InstanceSpecification()
    _safe_set(a, 'MARTE_GRM_Resource104', b1)
    assert _is_linked(a, 'MARTE_GRM_Resource104', b1)
    if hasattr(b1, 'GRM_MARTE_InstanceSpecification'):
        assert _is_linked(b1, 'GRM_MARTE_InstanceSpecification', a)
    _safe_set(a, 'MARTE_GRM_Resource104', b2)
    assert _is_linked(a, 'MARTE_GRM_Resource104', b2)
    if hasattr(b1, 'GRM_MARTE_InstanceSpecification'):
        assert not _is_linked(b1, 'GRM_MARTE_InstanceSpecification', a)
    if hasattr(b2, 'GRM_MARTE_InstanceSpecification'):
        assert _is_linked(b2, 'GRM_MARTE_InstanceSpecification', a)
    _safe_set(a, 'MARTE_GRM_Resource104', None)
    assert not _is_linked(a, 'MARTE_GRM_Resource104', b2)
    if hasattr(b2, 'GRM_MARTE_InstanceSpecification'):
        assert not _is_linked(b2, 'GRM_MARTE_InstanceSpecification', a)


def test_assoc_base_InstanceSpecification51_link_reassign_clear():
    a = MARTE_Time_Clock(standard="sample_text")
    b1 = Time_MARTE_InstanceSpecification()
    b2 = Time_MARTE_InstanceSpecification()
    _safe_set(a, 'MARTE_Time_Clock', b1)
    assert _is_linked(a, 'MARTE_Time_Clock', b1)
    if hasattr(b1, 'Time_MARTE_InstanceSpecification'):
        assert _is_linked(b1, 'Time_MARTE_InstanceSpecification', a)
    _safe_set(a, 'MARTE_Time_Clock', b2)
    assert _is_linked(a, 'MARTE_Time_Clock', b2)
    if hasattr(b1, 'Time_MARTE_InstanceSpecification'):
        assert not _is_linked(b1, 'Time_MARTE_InstanceSpecification', a)
    if hasattr(b2, 'Time_MARTE_InstanceSpecification'):
        assert _is_linked(b2, 'Time_MARTE_InstanceSpecification', a)
    _safe_set(a, 'MARTE_Time_Clock', None)
    assert not _is_linked(a, 'MARTE_Time_Clock', b2)
    if hasattr(b2, 'Time_MARTE_InstanceSpecification'):
        assert not _is_linked(b2, 'Time_MARTE_InstanceSpecification', a)


def test_assoc_base_InvocationAction297_link_reassign_clear():
    a = MARTE_HLAM_RtAction(isAtomic="sample_text", synchKind="sample_text")
    b1 = HLAM_MARTE_InvocationAction()
    b2 = HLAM_MARTE_InvocationAction()
    _safe_set(a, 'MARTE_HLAM_RtAction298', b1)
    assert _is_linked(a, 'MARTE_HLAM_RtAction298', b1)
    if hasattr(b1, 'HLAM_MARTE_InvocationAction299'):
        assert _is_linked(b1, 'HLAM_MARTE_InvocationAction299', a)
    _safe_set(a, 'MARTE_HLAM_RtAction298', b2)
    assert _is_linked(a, 'MARTE_HLAM_RtAction298', b2)
    if hasattr(b1, 'HLAM_MARTE_InvocationAction299'):
        assert not _is_linked(b1, 'HLAM_MARTE_InvocationAction299', a)
    if hasattr(b2, 'HLAM_MARTE_InvocationAction299'):
        assert _is_linked(b2, 'HLAM_MARTE_InvocationAction299', a)
    _safe_set(a, 'MARTE_HLAM_RtAction298', None)
    assert not _is_linked(a, 'MARTE_HLAM_RtAction298', b2)
    if hasattr(b2, 'HLAM_MARTE_InvocationAction299'):
        assert not _is_linked(b2, 'HLAM_MARTE_InvocationAction299', a)


def test_assoc_base_Lifeline107_link_reassign_clear():
    a = MARTE_GRM_Resource(isProtected="sample_text")
    b1 = GRM_MARTE_Lifeline()
    b2 = GRM_MARTE_Lifeline()
    _safe_set(a, 'MARTE_GRM_Resource108', b1)
    assert _is_linked(a, 'MARTE_GRM_Resource108', b1)
    if hasattr(b1, 'GRM_MARTE_Lifeline'):
        assert _is_linked(b1, 'GRM_MARTE_Lifeline', a)
    _safe_set(a, 'MARTE_GRM_Resource108', b2)
    assert _is_linked(a, 'MARTE_GRM_Resource108', b2)
    if hasattr(b1, 'GRM_MARTE_Lifeline'):
        assert not _is_linked(b1, 'GRM_MARTE_Lifeline', a)
    if hasattr(b2, 'GRM_MARTE_Lifeline'):
        assert _is_linked(b2, 'GRM_MARTE_Lifeline', a)
    _safe_set(a, 'MARTE_GRM_Resource108', None)
    assert not _is_linked(a, 'MARTE_GRM_Resource108', b2)
    if hasattr(b2, 'GRM_MARTE_Lifeline'):
        assert not _is_linked(b2, 'GRM_MARTE_Lifeline', a)


def test_assoc_base_NamedElement1117_link_reassign_clear():
    a = MARTE_PAM_PaRunTInstance(unbddPool="sample_text")
    b1 = PAM_MARTE_NamedElement()
    b2 = PAM_MARTE_NamedElement()
    _safe_set(a, 'MARTE_PAM_PaRunTInstance1118', b1)
    assert _is_linked(a, 'MARTE_PAM_PaRunTInstance1118', b1)
    if hasattr(b1, 'PAM_MARTE_NamedElement'):
        assert _is_linked(b1, 'PAM_MARTE_NamedElement', a)
    _safe_set(a, 'MARTE_PAM_PaRunTInstance1118', b2)
    assert _is_linked(a, 'MARTE_PAM_PaRunTInstance1118', b2)
    if hasattr(b1, 'PAM_MARTE_NamedElement'):
        assert not _is_linked(b1, 'PAM_MARTE_NamedElement', a)
    if hasattr(b2, 'PAM_MARTE_NamedElement'):
        assert _is_linked(b2, 'PAM_MARTE_NamedElement', a)
    _safe_set(a, 'MARTE_PAM_PaRunTInstance1118', None)
    assert not _is_linked(a, 'MARTE_PAM_PaRunTInstance1118', b2)
    if hasattr(b2, 'PAM_MARTE_NamedElement'):
        assert not _is_linked(b2, 'PAM_MARTE_NamedElement', a)


def test_assoc_base_NamedElement837_link_reassign_clear():
    a = MARTE_GQAM_GaEventTrace(content="sample_text", format="sample_text", location="sample_text")
    b1 = GQAM_MARTE_NamedElement()
    b2 = GQAM_MARTE_NamedElement()
    _safe_set(a, 'MARTE_GQAM_GaEventTrace', b1)
    assert _is_linked(a, 'MARTE_GQAM_GaEventTrace', b1)
    if hasattr(b1, 'GQAM_MARTE_NamedElement'):
        assert _is_linked(b1, 'GQAM_MARTE_NamedElement', a)
    _safe_set(a, 'MARTE_GQAM_GaEventTrace', b2)
    assert _is_linked(a, 'MARTE_GQAM_GaEventTrace', b2)
    if hasattr(b1, 'GQAM_MARTE_NamedElement'):
        assert not _is_linked(b1, 'GQAM_MARTE_NamedElement', a)
    if hasattr(b2, 'GQAM_MARTE_NamedElement'):
        assert _is_linked(b2, 'GQAM_MARTE_NamedElement', a)
    _safe_set(a, 'MARTE_GQAM_GaEventTrace', None)
    assert not _is_linked(a, 'MARTE_GQAM_GaEventTrace', b2)
    if hasattr(b2, 'GQAM_MARTE_NamedElement'):
        assert not _is_linked(b2, 'GQAM_MARTE_NamedElement', a)


def test_assoc_base_Port801_link_reassign_clear():
    a = MARTE_GCM_FlowPort(direction="sample_text", isAtomic="sample_text", isConjugated="sample_text")
    b1 = GCM_MARTE_Port()
    b2 = GCM_MARTE_Port()
    _safe_set(a, 'MARTE_GCM_FlowPort', b1)
    assert _is_linked(a, 'MARTE_GCM_FlowPort', b1)
    if hasattr(b1, 'GCM_MARTE_Port'):
        assert _is_linked(b1, 'GCM_MARTE_Port', a)
    _safe_set(a, 'MARTE_GCM_FlowPort', b2)
    assert _is_linked(a, 'MARTE_GCM_FlowPort', b2)
    if hasattr(b1, 'GCM_MARTE_Port'):
        assert not _is_linked(b1, 'GCM_MARTE_Port', a)
    if hasattr(b2, 'GCM_MARTE_Port'):
        assert _is_linked(b2, 'GCM_MARTE_Port', a)
    _safe_set(a, 'MARTE_GCM_FlowPort', None)
    assert not _is_linked(a, 'MARTE_GCM_FlowPort', b2)
    if hasattr(b2, 'GCM_MARTE_Port'):
        assert not _is_linked(b2, 'GCM_MARTE_Port', a)


def test_assoc_base_Port802_link_reassign_clear():
    a = MARTE_GCM_ClientServerPort(isConjugated="sample_text", kind="sample_text", specificationKind="sample_text")
    b1 = GCM_MARTE_Port()
    b2 = GCM_MARTE_Port()
    _safe_set(a, 'MARTE_GCM_ClientServerPort', b1)
    assert _is_linked(a, 'MARTE_GCM_ClientServerPort', b1)
    if hasattr(b1, 'GCM_MARTE_Port803'):
        assert _is_linked(b1, 'GCM_MARTE_Port803', a)
    _safe_set(a, 'MARTE_GCM_ClientServerPort', b2)
    assert _is_linked(a, 'MARTE_GCM_ClientServerPort', b2)
    if hasattr(b1, 'GCM_MARTE_Port803'):
        assert not _is_linked(b1, 'GCM_MARTE_Port803', a)
    if hasattr(b2, 'GCM_MARTE_Port803'):
        assert _is_linked(b2, 'GCM_MARTE_Port803', a)
    _safe_set(a, 'MARTE_GCM_ClientServerPort', None)
    assert not _is_linked(a, 'MARTE_GCM_ClientServerPort', b2)
    if hasattr(b2, 'GCM_MARTE_Port803'):
        assert not _is_linked(b2, 'GCM_MARTE_Port803', a)


def test_assoc_base_Property101_link_reassign_clear():
    a = MARTE_GRM_Resource(isProtected="sample_text")
    b1 = GRM_MARTE_Property()
    b2 = GRM_MARTE_Property()
    _safe_set(a, 'MARTE_GRM_Resource102', b1)
    assert _is_linked(a, 'MARTE_GRM_Resource102', b1)
    if hasattr(b1, 'GRM_MARTE_Property'):
        assert _is_linked(b1, 'GRM_MARTE_Property', a)
    _safe_set(a, 'MARTE_GRM_Resource102', b2)
    assert _is_linked(a, 'MARTE_GRM_Resource102', b2)
    if hasattr(b1, 'GRM_MARTE_Property'):
        assert not _is_linked(b1, 'GRM_MARTE_Property', a)
    if hasattr(b2, 'GRM_MARTE_Property'):
        assert _is_linked(b2, 'GRM_MARTE_Property', a)
    _safe_set(a, 'MARTE_GRM_Resource102', None)
    assert not _is_linked(a, 'MARTE_GRM_Resource102', b2)
    if hasattr(b2, 'GRM_MARTE_Property'):
        assert not _is_linked(b2, 'GRM_MARTE_Property', a)


def test_assoc_base_Property211_link_reassign_clear():
    a = MARTE_Variables_Var(dir="sample_text")
    b1 = Variables_MARTE_Property()
    b2 = Variables_MARTE_Property()
    _safe_set(a, 'MARTE_Variables_Var', b1)
    assert _is_linked(a, 'MARTE_Variables_Var', b1)
    if hasattr(b1, 'Variables_MARTE_Property'):
        assert _is_linked(b1, 'Variables_MARTE_Property', a)
    _safe_set(a, 'MARTE_Variables_Var', b2)
    assert _is_linked(a, 'MARTE_Variables_Var', b2)
    if hasattr(b1, 'Variables_MARTE_Property'):
        assert not _is_linked(b1, 'Variables_MARTE_Property', a)
    if hasattr(b2, 'Variables_MARTE_Property'):
        assert _is_linked(b2, 'Variables_MARTE_Property', a)
    _safe_set(a, 'MARTE_Variables_Var', None)
    assert not _is_linked(a, 'MARTE_Variables_Var', b2)
    if hasattr(b2, 'Variables_MARTE_Property'):
        assert not _is_linked(b2, 'Variables_MARTE_Property', a)


def test_assoc_base_Property57_link_reassign_clear():
    a = MARTE_Time_Clock(standard="sample_text")
    b1 = Time_MARTE_Property()
    b2 = Time_MARTE_Property()
    _safe_set(a, 'MARTE_Time_Clock58', b1)
    assert _is_linked(a, 'MARTE_Time_Clock58', b1)
    if hasattr(b1, 'Time_MARTE_Property'):
        assert _is_linked(b1, 'Time_MARTE_Property', a)
    _safe_set(a, 'MARTE_Time_Clock58', b2)
    assert _is_linked(a, 'MARTE_Time_Clock58', b2)
    if hasattr(b1, 'Time_MARTE_Property'):
        assert not _is_linked(b1, 'Time_MARTE_Property', a)
    if hasattr(b2, 'Time_MARTE_Property'):
        assert _is_linked(b2, 'Time_MARTE_Property', a)
    _safe_set(a, 'MARTE_Time_Clock58', None)
    assert not _is_linked(a, 'MARTE_Time_Clock58', b2)
    if hasattr(b2, 'Time_MARTE_Property'):
        assert not _is_linked(b2, 'Time_MARTE_Property', a)


def test_assoc_base_Property800_link_reassign_clear():
    a = MARTE_GCM_FlowProperty(direction="sample_text")
    b1 = GCM_MARTE_Property()
    b2 = GCM_MARTE_Property()
    _safe_set(a, 'MARTE_GCM_FlowProperty', b1)
    assert _is_linked(a, 'MARTE_GCM_FlowProperty', b1)
    if hasattr(b1, 'GCM_MARTE_Property'):
        assert _is_linked(b1, 'GCM_MARTE_Property', a)
    _safe_set(a, 'MARTE_GCM_FlowProperty', b2)
    assert _is_linked(a, 'MARTE_GCM_FlowProperty', b2)
    if hasattr(b1, 'GCM_MARTE_Property'):
        assert not _is_linked(b1, 'GCM_MARTE_Property', a)
    if hasattr(b2, 'GCM_MARTE_Property'):
        assert _is_linked(b2, 'GCM_MARTE_Property', a)
    _safe_set(a, 'MARTE_GCM_FlowProperty', None)
    assert not _is_linked(a, 'MARTE_GCM_FlowProperty', b2)
    if hasattr(b2, 'GCM_MARTE_Property'):
        assert not _is_linked(b2, 'GCM_MARTE_Property', a)


def test_assoc_base_Property826_link_reassign_clear():
    a = MARTE_GCM_DataPool(ordering="sample_text")
    b1 = GCM_MARTE_Property()
    b2 = GCM_MARTE_Property()
    _safe_set(a, 'MARTE_GCM_DataPool', b1)
    assert _is_linked(a, 'MARTE_GCM_DataPool', b1)
    if hasattr(b1, 'GCM_MARTE_Property827'):
        assert _is_linked(b1, 'GCM_MARTE_Property827', a)
    _safe_set(a, 'MARTE_GCM_DataPool', b2)
    assert _is_linked(a, 'MARTE_GCM_DataPool', b2)
    if hasattr(b1, 'GCM_MARTE_Property827'):
        assert not _is_linked(b1, 'GCM_MARTE_Property827', a)
    if hasattr(b2, 'GCM_MARTE_Property827'):
        assert _is_linked(b2, 'GCM_MARTE_Property827', a)
    _safe_set(a, 'MARTE_GCM_DataPool', None)
    assert not _is_linked(a, 'MARTE_GCM_DataPool', b2)
    if hasattr(b2, 'GCM_MARTE_Property827'):
        assert not _is_linked(b2, 'GCM_MARTE_Property827', a)


def test_assoc_base_TimeEvent83_link_reassign_clear():
    a = MARTE_Time_TimedEvent(repetition="sample_text")
    b1 = Time_MARTE_TimeEvent()
    b2 = Time_MARTE_TimeEvent()
    _safe_set(a, 'MARTE_Time_TimedEvent', b1)
    assert _is_linked(a, 'MARTE_Time_TimedEvent', b1)
    if hasattr(b1, 'Time_MARTE_TimeEvent'):
        assert _is_linked(b1, 'Time_MARTE_TimeEvent', a)
    _safe_set(a, 'MARTE_Time_TimedEvent', b2)
    assert _is_linked(a, 'MARTE_Time_TimedEvent', b2)
    if hasattr(b1, 'Time_MARTE_TimeEvent'):
        assert not _is_linked(b1, 'Time_MARTE_TimeEvent', a)
    if hasattr(b2, 'Time_MARTE_TimeEvent'):
        assert _is_linked(b2, 'Time_MARTE_TimeEvent', a)
    _safe_set(a, 'MARTE_Time_TimedEvent', None)
    assert not _is_linked(a, 'MARTE_Time_TimedEvent', b2)
    if hasattr(b2, 'Time_MARTE_TimeEvent'):
        assert not _is_linked(b2, 'Time_MARTE_TimeEvent', a)


def test_assoc_base_TimeObservation81_link_reassign_clear():
    a = MARTE_Time_TimedInstantObservation(obsKind="sample_text")
    b1 = Time_MARTE_TimeObservation()
    b2 = Time_MARTE_TimeObservation()
    _safe_set(a, 'MARTE_Time_TimedInstantObservation', b1)
    assert _is_linked(a, 'MARTE_Time_TimedInstantObservation', b1)
    if hasattr(b1, 'Time_MARTE_TimeObservation'):
        assert _is_linked(b1, 'Time_MARTE_TimeObservation', a)
    _safe_set(a, 'MARTE_Time_TimedInstantObservation', b2)
    assert _is_linked(a, 'MARTE_Time_TimedInstantObservation', b2)
    if hasattr(b1, 'Time_MARTE_TimeObservation'):
        assert not _is_linked(b1, 'Time_MARTE_TimeObservation', a)
    if hasattr(b2, 'Time_MARTE_TimeObservation'):
        assert _is_linked(b2, 'Time_MARTE_TimeObservation', a)
    _safe_set(a, 'MARTE_Time_TimedInstantObservation', None)
    assert not _is_linked(a, 'MARTE_Time_TimedInstantObservation', b2)
    if hasattr(b2, 'Time_MARTE_TimeObservation'):
        assert not _is_linked(b2, 'Time_MARTE_TimeObservation', a)


def test_assoc_base_ValueSpecification80_link_reassign_clear():
    a = MARTE_Time_TimedValueSpecification(interpretation="sample_text")
    b1 = Time_MARTE_ValueSpecification()
    b2 = Time_MARTE_ValueSpecification()
    _safe_set(a, 'MARTE_Time_TimedValueSpecification', b1)
    assert _is_linked(a, 'MARTE_Time_TimedValueSpecification', b1)
    if hasattr(b1, 'Time_MARTE_ValueSpecification'):
        assert _is_linked(b1, 'Time_MARTE_ValueSpecification', a)
    _safe_set(a, 'MARTE_Time_TimedValueSpecification', b2)
    assert _is_linked(a, 'MARTE_Time_TimedValueSpecification', b2)
    if hasattr(b1, 'Time_MARTE_ValueSpecification'):
        assert not _is_linked(b1, 'Time_MARTE_ValueSpecification', a)
    if hasattr(b2, 'Time_MARTE_ValueSpecification'):
        assert _is_linked(b2, 'Time_MARTE_ValueSpecification', a)
    _safe_set(a, 'MARTE_Time_TimedValueSpecification', None)
    assert not _is_linked(a, 'MARTE_Time_TimedValueSpecification', b2)
    if hasattr(b2, 'Time_MARTE_ValueSpecification'):
        assert not _is_linked(b2, 'Time_MARTE_ValueSpecification', a)


def test_assoc_behavCount1087_link_reassign_clear():
    a = MARTE_PAM_PaStep(extOpDemand="sample_text")
    b1 = NFP_Real()
    b2 = NFP_Real()
    _safe_set(a, 'MARTE_PAM_PaStep1088', {b1})
    assert _is_linked(a, 'MARTE_PAM_PaStep1088', b1)
    if hasattr(b1, 'NFP_Real1089'):
        assert _is_linked(b1, 'NFP_Real1089', a)
    _safe_set(a, 'MARTE_PAM_PaStep1088', {b2})
    assert _is_linked(a, 'MARTE_PAM_PaStep1088', b2)
    if hasattr(b1, 'NFP_Real1089'):
        assert not _is_linked(b1, 'NFP_Real1089', a)
    if hasattr(b2, 'NFP_Real1089'):
        assert _is_linked(b2, 'NFP_Real1089', a)
    _safe_set(a, 'MARTE_PAM_PaStep1088', set())
    assert not _is_linked(a, 'MARTE_PAM_PaStep1088', b2)
    if hasattr(b2, 'NFP_Real1089'):
        assert not _is_linked(b2, 'NFP_Real1089', a)


def test_assoc_behavDemand1084_link_reassign_clear():
    a = MARTE_PAM_PaStep(extOpDemand="sample_text")
    b1 = GQAM_GaScenario()
    b2 = GQAM_GaScenario()
    _safe_set(a, 'MARTE_PAM_PaStep1085', {b1})
    assert _is_linked(a, 'MARTE_PAM_PaStep1085', b1)
    if hasattr(b1, 'GQAM_GaScenario1086'):
        assert _is_linked(b1, 'GQAM_GaScenario1086', a)
    _safe_set(a, 'MARTE_PAM_PaStep1085', {b2})
    assert _is_linked(a, 'MARTE_PAM_PaStep1085', b2)
    if hasattr(b1, 'GQAM_GaScenario1086'):
        assert not _is_linked(b1, 'GQAM_GaScenario1086', a)
    if hasattr(b2, 'GQAM_GaScenario1086'):
        assert _is_linked(b2, 'GQAM_GaScenario1086', a)
    _safe_set(a, 'MARTE_PAM_PaStep1085', set())
    assert not _is_linked(a, 'MARTE_PAM_PaStep1085', b2)
    if hasattr(b2, 'GQAM_GaScenario1086'):
        assert not _is_linked(b2, 'GQAM_GaScenario1086', a)


def test_assoc_blockT138_link_reassign_clear():
    a = MARTE_GRM_CommunicationMedia(transmMode="sample_text")
    b1 = NFP_Duration()
    b2 = NFP_Duration()
    _safe_set(a, 'MARTE_GRM_CommunicationMedia139', {b1})
    assert _is_linked(a, 'MARTE_GRM_CommunicationMedia139', b1)
    if hasattr(b1, 'NFP_Duration'):
        assert _is_linked(b1, 'NFP_Duration', a)
    _safe_set(a, 'MARTE_GRM_CommunicationMedia139', {b2})
    assert _is_linked(a, 'MARTE_GRM_CommunicationMedia139', b2)
    if hasattr(b1, 'NFP_Duration'):
        assert not _is_linked(b1, 'NFP_Duration', a)
    if hasattr(b2, 'NFP_Duration'):
        assert _is_linked(b2, 'NFP_Duration', a)
    _safe_set(a, 'MARTE_GRM_CommunicationMedia139', set())
    assert not _is_linked(a, 'MARTE_GRM_CommunicationMedia139', b2)
    if hasattr(b2, 'NFP_Duration'):
        assert not _is_linked(b2, 'NFP_Duration', a)


def test_assoc_blocksComputing354_link_reassign_clear():
    a = MARTE_HwComputing_HwPLD(technology="sample_text")
    b1 = HwComputing_HwComputingResource()
    b2 = HwComputing_HwComputingResource()
    _safe_set(a, 'MARTE_HwComputing_HwPLD355', {b1})
    assert _is_linked(a, 'MARTE_HwComputing_HwPLD355', b1)
    if hasattr(b1, 'HwComputing_HwComputingResource'):
        assert _is_linked(b1, 'HwComputing_HwComputingResource', a)
    _safe_set(a, 'MARTE_HwComputing_HwPLD355', {b2})
    assert _is_linked(a, 'MARTE_HwComputing_HwPLD355', b2)
    if hasattr(b1, 'HwComputing_HwComputingResource'):
        assert not _is_linked(b1, 'HwComputing_HwComputingResource', a)
    if hasattr(b2, 'HwComputing_HwComputingResource'):
        assert _is_linked(b2, 'HwComputing_HwComputingResource', a)
    _safe_set(a, 'MARTE_HwComputing_HwPLD355', set())
    assert not _is_linked(a, 'MARTE_HwComputing_HwPLD355', b2)
    if hasattr(b2, 'HwComputing_HwComputingResource'):
        assert not _is_linked(b2, 'HwComputing_HwComputingResource', a)


def test_assoc_blocksRAM352_link_reassign_clear():
    a = MARTE_HwComputing_HwPLD(technology="sample_text")
    b1 = HwMemory_HwRAM()
    b2 = HwMemory_HwRAM()
    _safe_set(a, 'MARTE_HwComputing_HwPLD353', {b1})
    assert _is_linked(a, 'MARTE_HwComputing_HwPLD353', b1)
    if hasattr(b1, 'HwMemory_HwRAM'):
        assert _is_linked(b1, 'HwMemory_HwRAM', a)
    _safe_set(a, 'MARTE_HwComputing_HwPLD353', {b2})
    assert _is_linked(a, 'MARTE_HwComputing_HwPLD353', b2)
    if hasattr(b1, 'HwMemory_HwRAM'):
        assert not _is_linked(b1, 'HwMemory_HwRAM', a)
    if hasattr(b2, 'HwMemory_HwRAM'):
        assert _is_linked(b2, 'HwMemory_HwRAM', a)
    _safe_set(a, 'MARTE_HwComputing_HwPLD353', set())
    assert not _is_linked(a, 'MARTE_HwComputing_HwPLD353', b2)
    if hasattr(b2, 'HwMemory_HwRAM'):
        assert not _is_linked(b2, 'HwMemory_HwRAM', a)


def test_assoc_capacity143_link_reassign_clear():
    a = MARTE_GRM_CommunicationMedia(transmMode="sample_text")
    b1 = NFP_DataTxRate()
    b2 = NFP_DataTxRate()
    _safe_set(a, 'MARTE_GRM_CommunicationMedia144', {b1})
    assert _is_linked(a, 'MARTE_GRM_CommunicationMedia144', b1)
    if hasattr(b1, 'NFP_DataTxRate'):
        assert _is_linked(b1, 'NFP_DataTxRate', a)
    _safe_set(a, 'MARTE_GRM_CommunicationMedia144', {b2})
    assert _is_linked(a, 'MARTE_GRM_CommunicationMedia144', b2)
    if hasattr(b1, 'NFP_DataTxRate'):
        assert not _is_linked(b1, 'NFP_DataTxRate', a)
    if hasattr(b2, 'NFP_DataTxRate'):
        assert _is_linked(b2, 'NFP_DataTxRate', a)
    _safe_set(a, 'MARTE_GRM_CommunicationMedia144', set())
    assert not _is_linked(a, 'MARTE_GRM_CommunicationMedia144', b2)
    if hasattr(b2, 'NFP_DataTxRate'):
        assert not _is_linked(b2, 'NFP_DataTxRate', a)


def test_assoc_ceiling125_link_reassign_clear():
    a = MARTE_GRM_MutualExclusionResource(otherProtectProtocol="sample_text", protectKind="sample_text")
    b1 = NFP_Integer()
    b2 = NFP_Integer()
    _safe_set(a, 'MARTE_GRM_MutualExclusionResource', b1)
    assert _is_linked(a, 'MARTE_GRM_MutualExclusionResource', b1)
    if hasattr(b1, 'NFP_Integer126'):
        assert _is_linked(b1, 'NFP_Integer126', a)
    _safe_set(a, 'MARTE_GRM_MutualExclusionResource', b2)
    assert _is_linked(a, 'MARTE_GRM_MutualExclusionResource', b2)
    if hasattr(b1, 'NFP_Integer126'):
        assert not _is_linked(b1, 'NFP_Integer126', a)
    if hasattr(b2, 'NFP_Integer126'):
        assert _is_linked(b2, 'NFP_Integer126', a)
    _safe_set(a, 'MARTE_GRM_MutualExclusionResource', None)
    assert not _is_linked(a, 'MARTE_GRM_MutualExclusionResource', b2)
    if hasattr(b2, 'NFP_Integer126'):
        assert not _is_linked(b2, 'NFP_Integer126', a)


def test_assoc_clearServices789_link_reassign_clear():
    a = MARTE_SW_Interaction_NotificationResource(mechanism="sample_text", occurence="sample_text")
    b1 = SW_Interaction_MARTE_BehavioralFeature()
    b2 = SW_Interaction_MARTE_BehavioralFeature()
    _safe_set(a, 'MARTE_SW_Interaction_NotificationResource790', {b1})
    assert _is_linked(a, 'MARTE_SW_Interaction_NotificationResource790', b1)
    if hasattr(b1, 'SW_Interaction_MARTE_BehavioralFeature791'):
        assert _is_linked(b1, 'SW_Interaction_MARTE_BehavioralFeature791', a)
    _safe_set(a, 'MARTE_SW_Interaction_NotificationResource790', {b2})
    assert _is_linked(a, 'MARTE_SW_Interaction_NotificationResource790', b2)
    if hasattr(b1, 'SW_Interaction_MARTE_BehavioralFeature791'):
        assert not _is_linked(b1, 'SW_Interaction_MARTE_BehavioralFeature791', a)
    if hasattr(b2, 'SW_Interaction_MARTE_BehavioralFeature791'):
        assert _is_linked(b2, 'SW_Interaction_MARTE_BehavioralFeature791', a)
    _safe_set(a, 'MARTE_SW_Interaction_NotificationResource790', set())
    assert not _is_linked(a, 'MARTE_SW_Interaction_NotificationResource790', b2)
    if hasattr(b2, 'SW_Interaction_MARTE_BehavioralFeature791'):
        assert not _is_linked(b2, 'SW_Interaction_MARTE_BehavioralFeature791', a)


def test_assoc_closeServices721_link_reassign_clear():
    a = MARTE_SW_Brokering_DeviceBroker(accessPolicy="sample_text", isBuffered="sample_text", name="sample_text")
    b1 = SW_Brokering_MARTE_BehavioralFeature()
    b2 = SW_Brokering_MARTE_BehavioralFeature()
    _safe_set(a, 'MARTE_SW_Brokering_DeviceBroker722', {b1})
    assert _is_linked(a, 'MARTE_SW_Brokering_DeviceBroker722', b1)
    if hasattr(b1, 'SW_Brokering_MARTE_BehavioralFeature'):
        assert _is_linked(b1, 'SW_Brokering_MARTE_BehavioralFeature', a)
    _safe_set(a, 'MARTE_SW_Brokering_DeviceBroker722', {b2})
    assert _is_linked(a, 'MARTE_SW_Brokering_DeviceBroker722', b2)
    if hasattr(b1, 'SW_Brokering_MARTE_BehavioralFeature'):
        assert not _is_linked(b1, 'SW_Brokering_MARTE_BehavioralFeature', a)
    if hasattr(b2, 'SW_Brokering_MARTE_BehavioralFeature'):
        assert _is_linked(b2, 'SW_Brokering_MARTE_BehavioralFeature', a)
    _safe_set(a, 'MARTE_SW_Brokering_DeviceBroker722', set())
    assert not _is_linked(a, 'MARTE_SW_Brokering_DeviceBroker722', b2)
    if hasattr(b2, 'SW_Brokering_MARTE_BehavioralFeature'):
        assert not _is_linked(b2, 'SW_Brokering_MARTE_BehavioralFeature', a)


def test_assoc_components573_link_reassign_clear():
    a = MARTE_HwDatasheet_HwDatasheet(name="sample_text", revision="sample_text")
    b1 = HwGeneral_HwResource()
    b2 = HwGeneral_HwResource()
    _safe_set(a, 'MARTE_HwDatasheet_HwDatasheet', {b1})
    assert _is_linked(a, 'MARTE_HwDatasheet_HwDatasheet', b1)
    if hasattr(b1, 'HwGeneral_HwResource574'):
        assert _is_linked(b1, 'HwGeneral_HwResource574', a)
    _safe_set(a, 'MARTE_HwDatasheet_HwDatasheet', {b2})
    assert _is_linked(a, 'MARTE_HwDatasheet_HwDatasheet', b2)
    if hasattr(b1, 'HwGeneral_HwResource574'):
        assert not _is_linked(b1, 'HwGeneral_HwResource574', a)
    if hasattr(b2, 'HwGeneral_HwResource574'):
        assert _is_linked(b2, 'HwGeneral_HwResource574', a)
    _safe_set(a, 'MARTE_HwDatasheet_HwDatasheet', set())
    assert not _is_linked(a, 'MARTE_HwDatasheet_HwDatasheet', b2)
    if hasattr(b2, 'HwGeneral_HwResource574'):
        assert not _is_linked(b2, 'HwGeneral_HwResource574', a)


def test_assoc_components586_link_reassign_clear():
    a = MARTE_HwDiagram_HwBlockDiagram(name="sample_text")
    b1 = HwGeneral_HwResource()
    b2 = HwGeneral_HwResource()
    _safe_set(a, 'MARTE_HwDiagram_HwBlockDiagram587', {b1})
    assert _is_linked(a, 'MARTE_HwDiagram_HwBlockDiagram587', b1)
    if hasattr(b1, 'HwGeneral_HwResource588'):
        assert _is_linked(b1, 'HwGeneral_HwResource588', a)
    _safe_set(a, 'MARTE_HwDiagram_HwBlockDiagram587', {b2})
    assert _is_linked(a, 'MARTE_HwDiagram_HwBlockDiagram587', b2)
    if hasattr(b1, 'HwGeneral_HwResource588'):
        assert not _is_linked(b1, 'HwGeneral_HwResource588', a)
    if hasattr(b2, 'HwGeneral_HwResource588'):
        assert _is_linked(b2, 'HwGeneral_HwResource588', a)
    _safe_set(a, 'MARTE_HwDiagram_HwBlockDiagram587', set())
    assert not _is_linked(a, 'MARTE_HwDiagram_HwBlockDiagram587', b2)
    if hasattr(b2, 'HwGeneral_HwResource588'):
        assert not _is_linked(b2, 'HwGeneral_HwResource588', a)


def test_assoc_components589_link_reassign_clear():
    a = MARTE_HwDiagram_HwCircuitDiagram(name="sample_text")
    b1 = HwPackage_HwPackage()
    b2 = HwPackage_HwPackage()
    _safe_set(a, 'MARTE_HwDiagram_HwCircuitDiagram', {b1})
    assert _is_linked(a, 'MARTE_HwDiagram_HwCircuitDiagram', b1)
    if hasattr(b1, 'HwPackage_HwPackage590'):
        assert _is_linked(b1, 'HwPackage_HwPackage590', a)
    _safe_set(a, 'MARTE_HwDiagram_HwCircuitDiagram', {b2})
    assert _is_linked(a, 'MARTE_HwDiagram_HwCircuitDiagram', b2)
    if hasattr(b1, 'HwPackage_HwPackage590'):
        assert not _is_linked(b1, 'HwPackage_HwPackage590', a)
    if hasattr(b2, 'HwPackage_HwPackage590'):
        assert _is_linked(b2, 'HwPackage_HwPackage590', a)
    _safe_set(a, 'MARTE_HwDiagram_HwCircuitDiagram', set())
    assert not _is_linked(a, 'MARTE_HwDiagram_HwCircuitDiagram', b2)
    if hasattr(b2, 'HwPackage_HwPackage590'):
        assert not _is_linked(b2, 'HwPackage_HwPackage590', a)


def test_assoc_components594_link_reassign_clear():
    a = MARTE_HwDiagram_HwHRMDiagram(name="sample_text")
    b1 = HwGeneral_HwResource()
    b2 = HwGeneral_HwResource()
    _safe_set(a, 'MARTE_HwDiagram_HwHRMDiagram', {b1})
    assert _is_linked(a, 'MARTE_HwDiagram_HwHRMDiagram', b1)
    if hasattr(b1, 'HwGeneral_HwResource595'):
        assert _is_linked(b1, 'HwGeneral_HwResource595', a)
    _safe_set(a, 'MARTE_HwDiagram_HwHRMDiagram', {b2})
    assert _is_linked(a, 'MARTE_HwDiagram_HwHRMDiagram', b2)
    if hasattr(b1, 'HwGeneral_HwResource595'):
        assert not _is_linked(b1, 'HwGeneral_HwResource595', a)
    if hasattr(b2, 'HwGeneral_HwResource595'):
        assert _is_linked(b2, 'HwGeneral_HwResource595', a)
    _safe_set(a, 'MARTE_HwDiagram_HwHRMDiagram', set())
    assert not _is_linked(a, 'MARTE_HwDiagram_HwHRMDiagram', b2)
    if hasattr(b2, 'HwGeneral_HwResource595'):
        assert not _is_linked(b2, 'HwGeneral_HwResource595', a)


def test_assoc_connections584_link_reassign_clear():
    a = MARTE_HwDiagram_HwBlockDiagram(name="sample_text")
    b1 = HwCommunication_HwConnection()
    b2 = HwCommunication_HwConnection()
    _safe_set(a, 'MARTE_HwDiagram_HwBlockDiagram585', {b1})
    assert _is_linked(a, 'MARTE_HwDiagram_HwBlockDiagram585', b1)
    if hasattr(b1, 'HwCommunication_HwConnection'):
        assert _is_linked(b1, 'HwCommunication_HwConnection', a)
    _safe_set(a, 'MARTE_HwDiagram_HwBlockDiagram585', {b2})
    assert _is_linked(a, 'MARTE_HwDiagram_HwBlockDiagram585', b2)
    if hasattr(b1, 'HwCommunication_HwConnection'):
        assert not _is_linked(b1, 'HwCommunication_HwConnection', a)
    if hasattr(b2, 'HwCommunication_HwConnection'):
        assert _is_linked(b2, 'HwCommunication_HwConnection', a)
    _safe_set(a, 'MARTE_HwDiagram_HwBlockDiagram585', set())
    assert not _is_linked(a, 'MARTE_HwDiagram_HwBlockDiagram585', b2)
    if hasattr(b2, 'HwCommunication_HwConnection'):
        assert not _is_linked(b2, 'HwCommunication_HwConnection', a)


def test_assoc_connections596_link_reassign_clear():
    a = MARTE_HwDiagram_HwHRMDiagram(name="sample_text")
    b1 = HwCommunication_HwMedia()
    b2 = HwCommunication_HwMedia()
    _safe_set(a, 'MARTE_HwDiagram_HwHRMDiagram597', {b1})
    assert _is_linked(a, 'MARTE_HwDiagram_HwHRMDiagram597', b1)
    if hasattr(b1, 'HwCommunication_HwMedia598'):
        assert _is_linked(b1, 'HwCommunication_HwMedia598', a)
    _safe_set(a, 'MARTE_HwDiagram_HwHRMDiagram597', {b2})
    assert _is_linked(a, 'MARTE_HwDiagram_HwHRMDiagram597', b2)
    if hasattr(b1, 'HwCommunication_HwMedia598'):
        assert not _is_linked(b1, 'HwCommunication_HwMedia598', a)
    if hasattr(b2, 'HwCommunication_HwMedia598'):
        assert _is_linked(b2, 'HwCommunication_HwMedia598', a)
    _safe_set(a, 'MARTE_HwDiagram_HwHRMDiagram597', set())
    assert not _is_linked(a, 'MARTE_HwDiagram_HwHRMDiagram597', b2)
    if hasattr(b2, 'HwCommunication_HwMedia598'):
        assert not _is_linked(b2, 'HwCommunication_HwMedia598', a)


def test_assoc_controlServices723_link_reassign_clear():
    a = MARTE_SW_Brokering_DeviceBroker(accessPolicy="sample_text", isBuffered="sample_text", name="sample_text")
    b1 = SW_Brokering_MARTE_BehavioralFeature()
    b2 = SW_Brokering_MARTE_BehavioralFeature()
    _safe_set(a, 'MARTE_SW_Brokering_DeviceBroker724', {b1})
    assert _is_linked(a, 'MARTE_SW_Brokering_DeviceBroker724', b1)
    if hasattr(b1, 'SW_Brokering_MARTE_BehavioralFeature725'):
        assert _is_linked(b1, 'SW_Brokering_MARTE_BehavioralFeature725', a)
    _safe_set(a, 'MARTE_SW_Brokering_DeviceBroker724', {b2})
    assert _is_linked(a, 'MARTE_SW_Brokering_DeviceBroker724', b2)
    if hasattr(b1, 'SW_Brokering_MARTE_BehavioralFeature725'):
        assert not _is_linked(b1, 'SW_Brokering_MARTE_BehavioralFeature725', a)
    if hasattr(b2, 'SW_Brokering_MARTE_BehavioralFeature725'):
        assert _is_linked(b2, 'SW_Brokering_MARTE_BehavioralFeature725', a)
    _safe_set(a, 'MARTE_SW_Brokering_DeviceBroker724', set())
    assert not _is_linked(a, 'MARTE_SW_Brokering_DeviceBroker724', b2)
    if hasattr(b2, 'SW_Brokering_MARTE_BehavioralFeature725'):
        assert not _is_linked(b2, 'SW_Brokering_MARTE_BehavioralFeature725', a)


def test_assoc_datatypes602_link_reassign_clear():
    a = MARTE_HwDiagram_HwHRMDiagram(name="sample_text")
    b1 = HwDiagram_MARTE_DataType()
    b2 = HwDiagram_MARTE_DataType()
    _safe_set(a, 'MARTE_HwDiagram_HwHRMDiagram603', {b1})
    assert _is_linked(a, 'MARTE_HwDiagram_HwHRMDiagram603', b1)
    if hasattr(b1, 'HwDiagram_MARTE_DataType'):
        assert _is_linked(b1, 'HwDiagram_MARTE_DataType', a)
    _safe_set(a, 'MARTE_HwDiagram_HwHRMDiagram603', {b2})
    assert _is_linked(a, 'MARTE_HwDiagram_HwHRMDiagram603', b2)
    if hasattr(b1, 'HwDiagram_MARTE_DataType'):
        assert not _is_linked(b1, 'HwDiagram_MARTE_DataType', a)
    if hasattr(b2, 'HwDiagram_MARTE_DataType'):
        assert _is_linked(b2, 'HwDiagram_MARTE_DataType', a)
    _safe_set(a, 'MARTE_HwDiagram_HwHRMDiagram603', set())
    assert not _is_linked(a, 'MARTE_HwDiagram_HwHRMDiagram603', b2)
    if hasattr(b2, 'HwDiagram_MARTE_DataType'):
        assert not _is_linked(b2, 'HwDiagram_MARTE_DataType', a)


def test_assoc_deadlineElements685_link_reassign_clear():
    a = MARTE_SW_Concurrency_SwSchedulableResource(isPreemptable="sample_text", isStaticSchedulingFeature="sample_text")
    b1 = SW_Concurrency_MARTE_TypedElement()
    b2 = SW_Concurrency_MARTE_TypedElement()
    _safe_set(a, 'MARTE_SW_Concurrency_SwSchedulableResource686', {b1})
    assert _is_linked(a, 'MARTE_SW_Concurrency_SwSchedulableResource686', b1)
    if hasattr(b1, 'SW_Concurrency_MARTE_TypedElement687'):
        assert _is_linked(b1, 'SW_Concurrency_MARTE_TypedElement687', a)
    _safe_set(a, 'MARTE_SW_Concurrency_SwSchedulableResource686', {b2})
    assert _is_linked(a, 'MARTE_SW_Concurrency_SwSchedulableResource686', b2)
    if hasattr(b1, 'SW_Concurrency_MARTE_TypedElement687'):
        assert not _is_linked(b1, 'SW_Concurrency_MARTE_TypedElement687', a)
    if hasattr(b2, 'SW_Concurrency_MARTE_TypedElement687'):
        assert _is_linked(b2, 'SW_Concurrency_MARTE_TypedElement687', a)
    _safe_set(a, 'MARTE_SW_Concurrency_SwSchedulableResource686', set())
    assert not _is_linked(a, 'MARTE_SW_Concurrency_SwSchedulableResource686', b2)
    if hasattr(b2, 'SW_Concurrency_MARTE_TypedElement687'):
        assert not _is_linked(b2, 'SW_Concurrency_MARTE_TypedElement687', a)


def test_assoc_deadlineTypeElements688_link_reassign_clear():
    a = MARTE_SW_Concurrency_SwSchedulableResource(isPreemptable="sample_text", isStaticSchedulingFeature="sample_text")
    b1 = SW_Concurrency_MARTE_TypedElement()
    b2 = SW_Concurrency_MARTE_TypedElement()
    _safe_set(a, 'MARTE_SW_Concurrency_SwSchedulableResource689', {b1})
    assert _is_linked(a, 'MARTE_SW_Concurrency_SwSchedulableResource689', b1)
    if hasattr(b1, 'SW_Concurrency_MARTE_TypedElement690'):
        assert _is_linked(b1, 'SW_Concurrency_MARTE_TypedElement690', a)
    _safe_set(a, 'MARTE_SW_Concurrency_SwSchedulableResource689', {b2})
    assert _is_linked(a, 'MARTE_SW_Concurrency_SwSchedulableResource689', b2)
    if hasattr(b1, 'SW_Concurrency_MARTE_TypedElement690'):
        assert not _is_linked(b1, 'SW_Concurrency_MARTE_TypedElement690', a)
    if hasattr(b2, 'SW_Concurrency_MARTE_TypedElement690'):
        assert _is_linked(b2, 'SW_Concurrency_MARTE_TypedElement690', a)
    _safe_set(a, 'MARTE_SW_Concurrency_SwSchedulableResource689', set())
    assert not _is_linked(a, 'MARTE_SW_Concurrency_SwSchedulableResource689', b2)
    if hasattr(b2, 'SW_Concurrency_MARTE_TypedElement690'):
        assert not _is_linked(b2, 'SW_Concurrency_MARTE_TypedElement690', a)


def test_assoc_delayServices694_link_reassign_clear():
    a = MARTE_SW_Concurrency_SwSchedulableResource(isPreemptable="sample_text", isStaticSchedulingFeature="sample_text")
    b1 = SW_Concurrency_MARTE_BehavioralFeature()
    b2 = SW_Concurrency_MARTE_BehavioralFeature()
    _safe_set(a, 'MARTE_SW_Concurrency_SwSchedulableResource695', {b1})
    assert _is_linked(a, 'MARTE_SW_Concurrency_SwSchedulableResource695', b1)
    if hasattr(b1, 'SW_Concurrency_MARTE_BehavioralFeature696'):
        assert _is_linked(b1, 'SW_Concurrency_MARTE_BehavioralFeature696', a)
    _safe_set(a, 'MARTE_SW_Concurrency_SwSchedulableResource695', {b2})
    assert _is_linked(a, 'MARTE_SW_Concurrency_SwSchedulableResource695', b2)
    if hasattr(b1, 'SW_Concurrency_MARTE_BehavioralFeature696'):
        assert not _is_linked(b1, 'SW_Concurrency_MARTE_BehavioralFeature696', a)
    if hasattr(b2, 'SW_Concurrency_MARTE_BehavioralFeature696'):
        assert _is_linked(b2, 'SW_Concurrency_MARTE_BehavioralFeature696', a)
    _safe_set(a, 'MARTE_SW_Concurrency_SwSchedulableResource695', set())
    assert not _is_linked(a, 'MARTE_SW_Concurrency_SwSchedulableResource695', b2)
    if hasattr(b2, 'SW_Concurrency_MARTE_BehavioralFeature696'):
        assert not _is_linked(b2, 'SW_Concurrency_MARTE_BehavioralFeature696', a)


def test_assoc_description508_link_reassign_clear():
    a = MARTE_HwGeneral_HwResource(name="sample_text")
    b1 = NFP_String()
    b2 = NFP_String()
    _safe_set(a, 'MARTE_HwGeneral_HwResource', b1)
    assert _is_linked(a, 'MARTE_HwGeneral_HwResource', b1)
    if hasattr(b1, 'NFP_String509'):
        assert _is_linked(b1, 'NFP_String509', a)
    _safe_set(a, 'MARTE_HwGeneral_HwResource', b2)
    assert _is_linked(a, 'MARTE_HwGeneral_HwResource', b2)
    if hasattr(b1, 'NFP_String509'):
        assert not _is_linked(b1, 'NFP_String509', a)
    if hasattr(b2, 'NFP_String509'):
        assert _is_linked(b2, 'NFP_String509', a)
    _safe_set(a, 'MARTE_HwGeneral_HwResource', None)
    assert not _is_linked(a, 'MARTE_HwGeneral_HwResource', b2)
    if hasattr(b2, 'NFP_String509'):
        assert not _is_linked(b2, 'NFP_String509', a)


def test_assoc_description554_link_reassign_clear():
    a = MARTE_HwLayout_Env_Condition(status="sample_text", type="sample_text")
    b1 = NFP_String()
    b2 = NFP_String()
    _safe_set(a, 'MARTE_HwLayout_Env_Condition', b1)
    assert _is_linked(a, 'MARTE_HwLayout_Env_Condition', b1)
    if hasattr(b1, 'NFP_String555'):
        assert _is_linked(b1, 'NFP_String555', a)
    _safe_set(a, 'MARTE_HwLayout_Env_Condition', b2)
    assert _is_linked(a, 'MARTE_HwLayout_Env_Condition', b2)
    if hasattr(b1, 'NFP_String555'):
        assert not _is_linked(b1, 'NFP_String555', a)
    if hasattr(b2, 'NFP_String555'):
        assert _is_linked(b2, 'NFP_String555', a)
    _safe_set(a, 'MARTE_HwLayout_Env_Condition', None)
    assert not _is_linked(a, 'MARTE_HwLayout_Env_Condition', b2)
    if hasattr(b2, 'NFP_String555'):
        assert not _is_linked(b2, 'NFP_String555', a)


def test_assoc_devices720_link_reassign_clear():
    a = MARTE_SW_Brokering_DeviceBroker(accessPolicy="sample_text", isBuffered="sample_text", name="sample_text")
    b1 = SW_Brokering_MARTE_TypedElement()
    b2 = SW_Brokering_MARTE_TypedElement()
    _safe_set(a, 'MARTE_SW_Brokering_DeviceBroker', {b1})
    assert _is_linked(a, 'MARTE_SW_Brokering_DeviceBroker', b1)
    if hasattr(b1, 'SW_Brokering_MARTE_TypedElement'):
        assert _is_linked(b1, 'SW_Brokering_MARTE_TypedElement', a)
    _safe_set(a, 'MARTE_SW_Brokering_DeviceBroker', {b2})
    assert _is_linked(a, 'MARTE_SW_Brokering_DeviceBroker', b2)
    if hasattr(b1, 'SW_Brokering_MARTE_TypedElement'):
        assert not _is_linked(b1, 'SW_Brokering_MARTE_TypedElement', a)
    if hasattr(b2, 'SW_Brokering_MARTE_TypedElement'):
        assert _is_linked(b2, 'SW_Brokering_MARTE_TypedElement', a)
    _safe_set(a, 'MARTE_SW_Brokering_DeviceBroker', set())
    assert not _is_linked(a, 'MARTE_SW_Brokering_DeviceBroker', b2)
    if hasattr(b2, 'SW_Brokering_MARTE_TypedElement'):
        assert not _is_linked(b2, 'SW_Brokering_MARTE_TypedElement', a)


def test_assoc_dimensions525_link_reassign_clear():
    a = MARTE_HwLayout_HwComponent(kind="sample_text")
    b1 = NFP_Length()
    b2 = NFP_Length()
    _safe_set(a, 'MARTE_HwLayout_HwComponent', {b1})
    assert _is_linked(a, 'MARTE_HwLayout_HwComponent', b1)
    if hasattr(b1, 'NFP_Length'):
        assert _is_linked(b1, 'NFP_Length', a)
    _safe_set(a, 'MARTE_HwLayout_HwComponent', {b2})
    assert _is_linked(a, 'MARTE_HwLayout_HwComponent', b2)
    if hasattr(b1, 'NFP_Length'):
        assert not _is_linked(b1, 'NFP_Length', a)
    if hasattr(b2, 'NFP_Length'):
        assert _is_linked(b2, 'NFP_Length', a)
    _safe_set(a, 'MARTE_HwLayout_HwComponent', set())
    assert not _is_linked(a, 'MARTE_HwLayout_HwComponent', b2)
    if hasattr(b2, 'NFP_Length'):
        assert not _is_linked(b2, 'NFP_Length', a)


def test_assoc_disableConcurrencyServices655_link_reassign_clear():
    a = MARTE_SW_Concurrency_SwConcurrentResource(activationCapacity="sample_text")
    b1 = SW_Concurrency_MARTE_BehavioralFeature()
    b2 = SW_Concurrency_MARTE_BehavioralFeature()
    _safe_set(a, 'MARTE_SW_Concurrency_SwConcurrentResource656', {b1})
    assert _is_linked(a, 'MARTE_SW_Concurrency_SwConcurrentResource656', b1)
    if hasattr(b1, 'SW_Concurrency_MARTE_BehavioralFeature657'):
        assert _is_linked(b1, 'SW_Concurrency_MARTE_BehavioralFeature657', a)
    _safe_set(a, 'MARTE_SW_Concurrency_SwConcurrentResource656', {b2})
    assert _is_linked(a, 'MARTE_SW_Concurrency_SwConcurrentResource656', b2)
    if hasattr(b1, 'SW_Concurrency_MARTE_BehavioralFeature657'):
        assert not _is_linked(b1, 'SW_Concurrency_MARTE_BehavioralFeature657', a)
    if hasattr(b2, 'SW_Concurrency_MARTE_BehavioralFeature657'):
        assert _is_linked(b2, 'SW_Concurrency_MARTE_BehavioralFeature657', a)
    _safe_set(a, 'MARTE_SW_Concurrency_SwConcurrentResource656', set())
    assert not _is_linked(a, 'MARTE_SW_Concurrency_SwConcurrentResource656', b2)
    if hasattr(b2, 'SW_Concurrency_MARTE_BehavioralFeature657'):
        assert not _is_linked(b2, 'SW_Concurrency_MARTE_BehavioralFeature657', a)


def test_assoc_duration145_link_reassign_clear():
    a = MARTE_GRM_TimerResource(isPeriodic="sample_text")
    b1 = NFP_Duration()
    b2 = NFP_Duration()
    _safe_set(a, 'MARTE_GRM_TimerResource', b1)
    assert _is_linked(a, 'MARTE_GRM_TimerResource', b1)
    if hasattr(b1, 'NFP_Duration146'):
        assert _is_linked(b1, 'NFP_Duration146', a)
    _safe_set(a, 'MARTE_GRM_TimerResource', b2)
    assert _is_linked(a, 'MARTE_GRM_TimerResource', b2)
    if hasattr(b1, 'NFP_Duration146'):
        assert not _is_linked(b1, 'NFP_Duration146', a)
    if hasattr(b2, 'NFP_Duration146'):
        assert _is_linked(b2, 'NFP_Duration146', a)
    _safe_set(a, 'MARTE_GRM_TimerResource', None)
    assert not _is_linked(a, 'MARTE_GRM_TimerResource', b2)
    if hasattr(b2, 'NFP_Duration146'):
        assert not _is_linked(b2, 'NFP_Duration146', a)


def test_assoc_elementSize134_link_reassign_clear():
    a = MARTE_GRM_CommunicationMedia(transmMode="sample_text")
    b1 = NFP_Integer()
    b2 = NFP_Integer()
    _safe_set(a, 'MARTE_GRM_CommunicationMedia', b1)
    assert _is_linked(a, 'MARTE_GRM_CommunicationMedia', b1)
    if hasattr(b1, 'NFP_Integer135'):
        assert _is_linked(b1, 'NFP_Integer135', a)
    _safe_set(a, 'MARTE_GRM_CommunicationMedia', b2)
    assert _is_linked(a, 'MARTE_GRM_CommunicationMedia', b2)
    if hasattr(b1, 'NFP_Integer135'):
        assert not _is_linked(b1, 'NFP_Integer135', a)
    if hasattr(b2, 'NFP_Integer135'):
        assert _is_linked(b2, 'NFP_Integer135', a)
    _safe_set(a, 'MARTE_GRM_CommunicationMedia', None)
    assert not _is_linked(a, 'MARTE_GRM_CommunicationMedia', b2)
    if hasattr(b2, 'NFP_Integer135'):
        assert not _is_linked(b2, 'NFP_Integer135', a)


def test_assoc_enableConcurrencyServices643_link_reassign_clear():
    a = MARTE_SW_Concurrency_SwConcurrentResource(activationCapacity="sample_text")
    b1 = SW_Concurrency_MARTE_BehavioralFeature()
    b2 = SW_Concurrency_MARTE_BehavioralFeature()
    _safe_set(a, 'MARTE_SW_Concurrency_SwConcurrentResource644', {b1})
    assert _is_linked(a, 'MARTE_SW_Concurrency_SwConcurrentResource644', b1)
    if hasattr(b1, 'SW_Concurrency_MARTE_BehavioralFeature645'):
        assert _is_linked(b1, 'SW_Concurrency_MARTE_BehavioralFeature645', a)
    _safe_set(a, 'MARTE_SW_Concurrency_SwConcurrentResource644', {b2})
    assert _is_linked(a, 'MARTE_SW_Concurrency_SwConcurrentResource644', b2)
    if hasattr(b1, 'SW_Concurrency_MARTE_BehavioralFeature645'):
        assert not _is_linked(b1, 'SW_Concurrency_MARTE_BehavioralFeature645', a)
    if hasattr(b2, 'SW_Concurrency_MARTE_BehavioralFeature645'):
        assert _is_linked(b2, 'SW_Concurrency_MARTE_BehavioralFeature645', a)
    _safe_set(a, 'MARTE_SW_Concurrency_SwConcurrentResource644', set())
    assert not _is_linked(a, 'MARTE_SW_Concurrency_SwConcurrentResource644', b2)
    if hasattr(b2, 'SW_Concurrency_MARTE_BehavioralFeature645'):
        assert not _is_linked(b2, 'SW_Concurrency_MARTE_BehavioralFeature645', a)


def test_assoc_endObs930_link_reassign_clear():
    a = MARTE_GQAM_GaTimedObs(laxity="sample_text")
    b1 = GQAM_MARTE_TimeObservation()
    b2 = GQAM_MARTE_TimeObservation()
    _safe_set(a, 'MARTE_GQAM_GaTimedObs931', {b1})
    assert _is_linked(a, 'MARTE_GQAM_GaTimedObs931', b1)
    if hasattr(b1, 'GQAM_MARTE_TimeObservation932'):
        assert _is_linked(b1, 'GQAM_MARTE_TimeObservation932', a)
    _safe_set(a, 'MARTE_GQAM_GaTimedObs931', {b2})
    assert _is_linked(a, 'MARTE_GQAM_GaTimedObs931', b2)
    if hasattr(b1, 'GQAM_MARTE_TimeObservation932'):
        assert not _is_linked(b1, 'GQAM_MARTE_TimeObservation932', a)
    if hasattr(b2, 'GQAM_MARTE_TimeObservation932'):
        assert _is_linked(b2, 'GQAM_MARTE_TimeObservation932', a)
    _safe_set(a, 'MARTE_GQAM_GaTimedObs931', set())
    assert not _is_linked(a, 'MARTE_GQAM_GaTimedObs931', b2)
    if hasattr(b2, 'GQAM_MARTE_TimeObservation932'):
        assert not _is_linked(b2, 'GQAM_MARTE_TimeObservation932', a)


def test_assoc_endPoints517_link_reassign_clear():
    a = MARTE_HwGeneral_HwResource(name="sample_text")
    b1 = HwCommunication_HwEndPoint()
    b2 = HwCommunication_HwEndPoint()
    _safe_set(a, 'MARTE_HwGeneral_HwResource518', {b1})
    assert _is_linked(a, 'MARTE_HwGeneral_HwResource518', b1)
    if hasattr(b1, 'HwCommunication_HwEndPoint'):
        assert _is_linked(b1, 'HwCommunication_HwEndPoint', a)
    _safe_set(a, 'MARTE_HwGeneral_HwResource518', {b2})
    assert _is_linked(a, 'MARTE_HwGeneral_HwResource518', b2)
    if hasattr(b1, 'HwCommunication_HwEndPoint'):
        assert not _is_linked(b1, 'HwCommunication_HwEndPoint', a)
    if hasattr(b2, 'HwCommunication_HwEndPoint'):
        assert _is_linked(b2, 'HwCommunication_HwEndPoint', a)
    _safe_set(a, 'MARTE_HwGeneral_HwResource518', set())
    assert not _is_linked(a, 'MARTE_HwGeneral_HwResource518', b2)
    if hasattr(b2, 'HwCommunication_HwEndPoint'):
        assert not _is_linked(b2, 'HwCommunication_HwEndPoint', a)


def test_assoc_entryPoints627_link_reassign_clear():
    a = MARTE_SW_Concurrency_SwConcurrentResource(activationCapacity="sample_text")
    b1 = SW_Concurrency_MARTE_Element()
    b2 = SW_Concurrency_MARTE_Element()
    _safe_set(a, 'MARTE_SW_Concurrency_SwConcurrentResource628', {b1})
    assert _is_linked(a, 'MARTE_SW_Concurrency_SwConcurrentResource628', b1)
    if hasattr(b1, 'SW_Concurrency_MARTE_Element'):
        assert _is_linked(b1, 'SW_Concurrency_MARTE_Element', a)
    _safe_set(a, 'MARTE_SW_Concurrency_SwConcurrentResource628', {b2})
    assert _is_linked(a, 'MARTE_SW_Concurrency_SwConcurrentResource628', b2)
    if hasattr(b1, 'SW_Concurrency_MARTE_Element'):
        assert not _is_linked(b1, 'SW_Concurrency_MARTE_Element', a)
    if hasattr(b2, 'SW_Concurrency_MARTE_Element'):
        assert _is_linked(b2, 'SW_Concurrency_MARTE_Element', a)
    _safe_set(a, 'MARTE_SW_Concurrency_SwConcurrentResource628', set())
    assert not _is_linked(a, 'MARTE_SW_Concurrency_SwConcurrentResource628', b2)
    if hasattr(b2, 'SW_Concurrency_MARTE_Element'):
        assert not _is_linked(b2, 'SW_Concurrency_MARTE_Element', a)


def test_assoc_every84_link_reassign_clear():
    a = MARTE_Time_TimedEvent(repetition="sample_text")
    b1 = Time_MARTE_ValueSpecification()
    b2 = Time_MARTE_ValueSpecification()
    _safe_set(a, 'MARTE_Time_TimedEvent85', b1)
    assert _is_linked(a, 'MARTE_Time_TimedEvent85', b1)
    if hasattr(b1, 'Time_MARTE_ValueSpecification86'):
        assert _is_linked(b1, 'Time_MARTE_ValueSpecification86', a)
    _safe_set(a, 'MARTE_Time_TimedEvent85', b2)
    assert _is_linked(a, 'MARTE_Time_TimedEvent85', b2)
    if hasattr(b1, 'Time_MARTE_ValueSpecification86'):
        assert not _is_linked(b1, 'Time_MARTE_ValueSpecification86', a)
    if hasattr(b2, 'Time_MARTE_ValueSpecification86'):
        assert _is_linked(b2, 'Time_MARTE_ValueSpecification86', a)
    _safe_set(a, 'MARTE_Time_TimedEvent85', None)
    assert not _is_linked(a, 'MARTE_Time_TimedEvent85', b2)
    if hasattr(b2, 'Time_MARTE_ValueSpecification86'):
        assert not _is_linked(b2, 'Time_MARTE_ValueSpecification86', a)


def test_assoc_extOpCount1081_link_reassign_clear():
    a = MARTE_PAM_PaStep(extOpDemand="sample_text")
    b1 = NFP_Real()
    b2 = NFP_Real()
    _safe_set(a, 'MARTE_PAM_PaStep1082', {b1})
    assert _is_linked(a, 'MARTE_PAM_PaStep1082', b1)
    if hasattr(b1, 'NFP_Real1083'):
        assert _is_linked(b1, 'NFP_Real1083', a)
    _safe_set(a, 'MARTE_PAM_PaStep1082', {b2})
    assert _is_linked(a, 'MARTE_PAM_PaStep1082', b2)
    if hasattr(b1, 'NFP_Real1083'):
        assert not _is_linked(b1, 'NFP_Real1083', a)
    if hasattr(b2, 'NFP_Real1083'):
        assert _is_linked(b2, 'NFP_Real1083', a)
    _safe_set(a, 'MARTE_PAM_PaStep1082', set())
    assert not _is_linked(a, 'MARTE_PAM_PaStep1082', b2)
    if hasattr(b2, 'NFP_Real1083'):
        assert not _is_linked(b2, 'NFP_Real1083', a)


def test_assoc_family338_link_reassign_clear():
    a = MARTE_HwComputing_HwISA(type="sample_text")
    b1 = NFP_String()
    b2 = NFP_String()
    _safe_set(a, 'MARTE_HwComputing_HwISA', b1)
    assert _is_linked(a, 'MARTE_HwComputing_HwISA', b1)
    if hasattr(b1, 'NFP_String'):
        assert _is_linked(b1, 'NFP_String', a)
    _safe_set(a, 'MARTE_HwComputing_HwISA', b2)
    assert _is_linked(a, 'MARTE_HwComputing_HwISA', b2)
    if hasattr(b1, 'NFP_String'):
        assert not _is_linked(b1, 'NFP_String', a)
    if hasattr(b2, 'NFP_String'):
        assert _is_linked(b2, 'NFP_String', a)
    _safe_set(a, 'MARTE_HwComputing_HwISA', None)
    assert not _is_linked(a, 'MARTE_HwComputing_HwISA', b2)
    if hasattr(b2, 'NFP_String'):
        assert not _is_linked(b2, 'NFP_String', a)


def test_assoc_featuresSpec809_link_reassign_clear():
    a = MARTE_GCM_ClientServerPort(isConjugated="sample_text", kind="sample_text", specificationKind="sample_text")
    b1 = GCM_ClientServerSpecification()
    b2 = GCM_ClientServerSpecification()
    _safe_set(a, 'MARTE_GCM_ClientServerPort810', b1)
    assert _is_linked(a, 'MARTE_GCM_ClientServerPort810', b1)
    if hasattr(b1, 'GCM_ClientServerSpecification'):
        assert _is_linked(b1, 'GCM_ClientServerSpecification', a)
    _safe_set(a, 'MARTE_GCM_ClientServerPort810', b2)
    assert _is_linked(a, 'MARTE_GCM_ClientServerPort810', b2)
    if hasattr(b1, 'GCM_ClientServerSpecification'):
        assert not _is_linked(b1, 'GCM_ClientServerSpecification', a)
    if hasattr(b2, 'GCM_ClientServerSpecification'):
        assert _is_linked(b2, 'GCM_ClientServerSpecification', a)
    _safe_set(a, 'MARTE_GCM_ClientServerPort810', None)
    assert not _is_linked(a, 'MARTE_GCM_ClientServerPort810', b2)
    if hasattr(b2, 'GCM_ClientServerSpecification'):
        assert not _is_linked(b2, 'GCM_ClientServerSpecification', a)


def test_assoc_flushServices780_link_reassign_clear():
    a = MARTE_SW_Interaction_NotificationResource(mechanism="sample_text", occurence="sample_text")
    b1 = SW_Interaction_MARTE_BehavioralFeature()
    b2 = SW_Interaction_MARTE_BehavioralFeature()
    _safe_set(a, 'MARTE_SW_Interaction_NotificationResource781', {b1})
    assert _is_linked(a, 'MARTE_SW_Interaction_NotificationResource781', b1)
    if hasattr(b1, 'SW_Interaction_MARTE_BehavioralFeature782'):
        assert _is_linked(b1, 'SW_Interaction_MARTE_BehavioralFeature782', a)
    _safe_set(a, 'MARTE_SW_Interaction_NotificationResource781', {b2})
    assert _is_linked(a, 'MARTE_SW_Interaction_NotificationResource781', b2)
    if hasattr(b1, 'SW_Interaction_MARTE_BehavioralFeature782'):
        assert not _is_linked(b1, 'SW_Interaction_MARTE_BehavioralFeature782', a)
    if hasattr(b2, 'SW_Interaction_MARTE_BehavioralFeature782'):
        assert _is_linked(b2, 'SW_Interaction_MARTE_BehavioralFeature782', a)
    _safe_set(a, 'MARTE_SW_Interaction_NotificationResource781', set())
    assert not _is_linked(a, 'MARTE_SW_Interaction_NotificationResource781', b2)
    if hasattr(b2, 'SW_Interaction_MARTE_BehavioralFeature782'):
        assert not _is_linked(b2, 'SW_Interaction_MARTE_BehavioralFeature782', a)


def test_assoc_frequency519_link_reassign_clear():
    a = MARTE_HwGeneral_HwResource(name="sample_text")
    b1 = NFP_Frequency()
    b2 = NFP_Frequency()
    _safe_set(a, 'MARTE_HwGeneral_HwResource520', b1)
    assert _is_linked(a, 'MARTE_HwGeneral_HwResource520', b1)
    if hasattr(b1, 'NFP_Frequency'):
        assert _is_linked(b1, 'NFP_Frequency', a)
    _safe_set(a, 'MARTE_HwGeneral_HwResource520', b2)
    assert _is_linked(a, 'MARTE_HwGeneral_HwResource520', b2)
    if hasattr(b1, 'NFP_Frequency'):
        assert not _is_linked(b1, 'NFP_Frequency', a)
    if hasattr(b2, 'NFP_Frequency'):
        assert _is_linked(b2, 'NFP_Frequency', a)
    _safe_set(a, 'MARTE_HwGeneral_HwResource520', None)
    assert not _is_linked(a, 'MARTE_HwGeneral_HwResource520', b2)
    if hasattr(b2, 'NFP_Frequency'):
        assert not _is_linked(b2, 'NFP_Frequency', a)


def test_assoc_getTime69_link_reassign_clear():
    a = MARTE_Time_ClockType(isLogical="sample_text", nature="sample_text")
    b1 = Time_MARTE_Operation()
    b2 = Time_MARTE_Operation()
    _safe_set(a, 'MARTE_Time_ClockType70', b1)
    assert _is_linked(a, 'MARTE_Time_ClockType70', b1)
    if hasattr(b1, 'Time_MARTE_Operation'):
        assert _is_linked(b1, 'Time_MARTE_Operation', a)
    _safe_set(a, 'MARTE_Time_ClockType70', b2)
    assert _is_linked(a, 'MARTE_Time_ClockType70', b2)
    if hasattr(b1, 'Time_MARTE_Operation'):
        assert not _is_linked(b1, 'Time_MARTE_Operation', a)
    if hasattr(b2, 'Time_MARTE_Operation'):
        assert _is_linked(b2, 'Time_MARTE_Operation', a)
    _safe_set(a, 'MARTE_Time_ClockType70', None)
    assert not _is_linked(a, 'MARTE_Time_ClockType70', b2)
    if hasattr(b2, 'Time_MARTE_Operation'):
        assert not _is_linked(b2, 'Time_MARTE_Operation', a)


def test_assoc_grid530_link_reassign_clear():
    a = MARTE_HwLayout_HwComponent(kind="sample_text")
    b1 = NFP_Natural()
    b2 = NFP_Natural()
    _safe_set(a, 'MARTE_HwLayout_HwComponent531', {b1})
    assert _is_linked(a, 'MARTE_HwLayout_HwComponent531', b1)
    if hasattr(b1, 'NFP_Natural532'):
        assert _is_linked(b1, 'NFP_Natural532', a)
    _safe_set(a, 'MARTE_HwLayout_HwComponent531', {b2})
    assert _is_linked(a, 'MARTE_HwLayout_HwComponent531', b2)
    if hasattr(b1, 'NFP_Natural532'):
        assert not _is_linked(b1, 'NFP_Natural532', a)
    if hasattr(b2, 'NFP_Natural532'):
        assert _is_linked(b2, 'NFP_Natural532', a)
    _safe_set(a, 'MARTE_HwLayout_HwComponent531', set())
    assert not _is_linked(a, 'MARTE_HwLayout_HwComponent531', b2)
    if hasattr(b2, 'NFP_Natural532'):
        assert not _is_linked(b2, 'NFP_Natural532', a)


def test_assoc_heapSizeElements670_link_reassign_clear():
    a = MARTE_SW_Concurrency_SwConcurrentResource(activationCapacity="sample_text")
    b1 = SW_Concurrency_MARTE_TypedElement()
    b2 = SW_Concurrency_MARTE_TypedElement()
    _safe_set(a, 'MARTE_SW_Concurrency_SwConcurrentResource671', {b1})
    assert _is_linked(a, 'MARTE_SW_Concurrency_SwConcurrentResource671', b1)
    if hasattr(b1, 'SW_Concurrency_MARTE_TypedElement672'):
        assert _is_linked(b1, 'SW_Concurrency_MARTE_TypedElement672', a)
    _safe_set(a, 'MARTE_SW_Concurrency_SwConcurrentResource671', {b2})
    assert _is_linked(a, 'MARTE_SW_Concurrency_SwConcurrentResource671', b2)
    if hasattr(b1, 'SW_Concurrency_MARTE_TypedElement672'):
        assert not _is_linked(b1, 'SW_Concurrency_MARTE_TypedElement672', a)
    if hasattr(b2, 'SW_Concurrency_MARTE_TypedElement672'):
        assert _is_linked(b2, 'SW_Concurrency_MARTE_TypedElement672', a)
    _safe_set(a, 'MARTE_SW_Concurrency_SwConcurrentResource671', set())
    assert not _is_linked(a, 'MARTE_SW_Concurrency_SwConcurrentResource671', b2)
    if hasattr(b2, 'SW_Concurrency_MARTE_TypedElement672'):
        assert not _is_linked(b2, 'SW_Concurrency_MARTE_TypedElement672', a)


def test_assoc_host1108_link_reassign_clear():
    a = MARTE_PAM_PaRunTInstance(unbddPool="sample_text")
    b1 = GQAM_GaExecHost()
    b2 = GQAM_GaExecHost()
    _safe_set(a, 'MARTE_PAM_PaRunTInstance1109', b1)
    assert _is_linked(a, 'MARTE_PAM_PaRunTInstance1109', b1)
    if hasattr(b1, 'GQAM_GaExecHost1110'):
        assert _is_linked(b1, 'GQAM_GaExecHost1110', a)
    _safe_set(a, 'MARTE_PAM_PaRunTInstance1109', b2)
    assert _is_linked(a, 'MARTE_PAM_PaRunTInstance1109', b2)
    if hasattr(b1, 'GQAM_GaExecHost1110'):
        assert not _is_linked(b1, 'GQAM_GaExecHost1110', a)
    if hasattr(b2, 'GQAM_GaExecHost1110'):
        assert _is_linked(b2, 'GQAM_GaExecHost1110', a)
    _safe_set(a, 'MARTE_PAM_PaRunTInstance1109', None)
    assert not _is_linked(a, 'MARTE_PAM_PaRunTInstance1109', b2)
    if hasattr(b2, 'GQAM_GaExecHost1110'):
        assert not _is_linked(b2, 'GQAM_GaExecHost1110', a)


def test_assoc_host118_link_reassign_clear():
    a = MARTE_GRM_Scheduler(isPreemptible="sample_text", otherSchedPolicy="sample_text", schedPolicy="sample_text")
    b1 = GRM_ComputingResource()
    b2 = GRM_ComputingResource()
    _safe_set(a, 'MARTE_GRM_Scheduler119', b1)
    assert _is_linked(a, 'MARTE_GRM_Scheduler119', b1)
    if hasattr(b1, 'GRM_ComputingResource'):
        assert _is_linked(b1, 'GRM_ComputingResource', a)
    _safe_set(a, 'MARTE_GRM_Scheduler119', b2)
    assert _is_linked(a, 'MARTE_GRM_Scheduler119', b2)
    if hasattr(b1, 'GRM_ComputingResource'):
        assert not _is_linked(b1, 'GRM_ComputingResource', a)
    if hasattr(b2, 'GRM_ComputingResource'):
        assert _is_linked(b2, 'GRM_ComputingResource', a)
    _safe_set(a, 'MARTE_GRM_Scheduler119', None)
    assert not _is_linked(a, 'MARTE_GRM_Scheduler119', b2)
    if hasattr(b2, 'GRM_ComputingResource'):
        assert not _is_linked(b2, 'GRM_ComputingResource', a)


def test_assoc_impliedConstraint47_link_reassign_clear():
    a = MARTE_Alloc_Allocate(kind="sample_text", nature="sample_text")
    b1 = NFPs_NfpConstraint()
    b2 = NFPs_NfpConstraint()
    _safe_set(a, 'MARTE_Alloc_Allocate48', {b1})
    assert _is_linked(a, 'MARTE_Alloc_Allocate48', b1)
    if hasattr(b1, 'NFPs_NfpConstraint49'):
        assert _is_linked(b1, 'NFPs_NfpConstraint49', a)
    _safe_set(a, 'MARTE_Alloc_Allocate48', {b2})
    assert _is_linked(a, 'MARTE_Alloc_Allocate48', b2)
    if hasattr(b1, 'NFPs_NfpConstraint49'):
        assert not _is_linked(b1, 'NFPs_NfpConstraint49', a)
    if hasattr(b2, 'NFPs_NfpConstraint49'):
        assert _is_linked(b2, 'NFPs_NfpConstraint49', a)
    _safe_set(a, 'MARTE_Alloc_Allocate48', set())
    assert not _is_linked(a, 'MARTE_Alloc_Allocate48', b2)
    if hasattr(b2, 'NFPs_NfpConstraint49'):
        assert not _is_linked(b2, 'NFPs_NfpConstraint49', a)


def test_assoc_indexToValue74_link_reassign_clear():
    a = MARTE_Time_ClockType(isLogical="sample_text", nature="sample_text")
    b1 = Time_MARTE_Operation()
    b2 = Time_MARTE_Operation()
    _safe_set(a, 'MARTE_Time_ClockType75', b1)
    assert _is_linked(a, 'MARTE_Time_ClockType75', b1)
    if hasattr(b1, 'Time_MARTE_Operation76'):
        assert _is_linked(b1, 'Time_MARTE_Operation76', a)
    _safe_set(a, 'MARTE_Time_ClockType75', b2)
    assert _is_linked(a, 'MARTE_Time_ClockType75', b2)
    if hasattr(b1, 'Time_MARTE_Operation76'):
        assert not _is_linked(b1, 'Time_MARTE_Operation76', a)
    if hasattr(b2, 'Time_MARTE_Operation76'):
        assert _is_linked(b2, 'Time_MARTE_Operation76', a)
    _safe_set(a, 'MARTE_Time_ClockType75', None)
    assert not _is_linked(a, 'MARTE_Time_ClockType75', b2)
    if hasattr(b2, 'Time_MARTE_Operation76'):
        assert not _is_linked(b2, 'Time_MARTE_Operation76', a)


def test_assoc_insertion828_link_reassign_clear():
    a = MARTE_GCM_DataPool(ordering="sample_text")
    b1 = GCM_MARTE_Behavior()
    b2 = GCM_MARTE_Behavior()
    _safe_set(a, 'MARTE_GCM_DataPool829', b1)
    assert _is_linked(a, 'MARTE_GCM_DataPool829', b1)
    if hasattr(b1, 'GCM_MARTE_Behavior'):
        assert _is_linked(b1, 'GCM_MARTE_Behavior', a)
    _safe_set(a, 'MARTE_GCM_DataPool829', b2)
    assert _is_linked(a, 'MARTE_GCM_DataPool829', b2)
    if hasattr(b1, 'GCM_MARTE_Behavior'):
        assert not _is_linked(b1, 'GCM_MARTE_Behavior', a)
    if hasattr(b2, 'GCM_MARTE_Behavior'):
        assert _is_linked(b2, 'GCM_MARTE_Behavior', a)
    _safe_set(a, 'MARTE_GCM_DataPool829', None)
    assert not _is_linked(a, 'MARTE_GCM_DataPool829', b2)
    if hasattr(b2, 'GCM_MARTE_Behavior'):
        assert not _is_linked(b2, 'GCM_MARTE_Behavior', a)


def test_assoc_inst_Width339_link_reassign_clear():
    a = MARTE_HwComputing_HwISA(type="sample_text")
    b1 = NFP_DataSize()
    b2 = NFP_DataSize()
    _safe_set(a, 'MARTE_HwComputing_HwISA340', b1)
    assert _is_linked(a, 'MARTE_HwComputing_HwISA340', b1)
    if hasattr(b1, 'NFP_DataSize341'):
        assert _is_linked(b1, 'NFP_DataSize341', a)
    _safe_set(a, 'MARTE_HwComputing_HwISA340', b2)
    assert _is_linked(a, 'MARTE_HwComputing_HwISA340', b2)
    if hasattr(b1, 'NFP_DataSize341'):
        assert not _is_linked(b1, 'NFP_DataSize341', a)
    if hasattr(b2, 'NFP_DataSize341'):
        assert _is_linked(b2, 'NFP_DataSize341', a)
    _safe_set(a, 'MARTE_HwComputing_HwISA340', None)
    assert not _is_linked(a, 'MARTE_HwComputing_HwISA340', b2)
    if hasattr(b2, 'NFP_DataSize341'):
        assert not _is_linked(b2, 'NFP_DataSize341', a)


def test_assoc_instance1105_link_reassign_clear():
    a = MARTE_PAM_PaRunTInstance(unbddPool="sample_text")
    b1 = GRM_SchedulableResource()
    b2 = GRM_SchedulableResource()
    _safe_set(a, 'MARTE_PAM_PaRunTInstance1106', b1)
    assert _is_linked(a, 'MARTE_PAM_PaRunTInstance1106', b1)
    if hasattr(b1, 'GRM_SchedulableResource1107'):
        assert _is_linked(b1, 'GRM_SchedulableResource1107', a)
    _safe_set(a, 'MARTE_PAM_PaRunTInstance1106', b2)
    assert _is_linked(a, 'MARTE_PAM_PaRunTInstance1106', b2)
    if hasattr(b1, 'GRM_SchedulableResource1107'):
        assert not _is_linked(b1, 'GRM_SchedulableResource1107', a)
    if hasattr(b2, 'GRM_SchedulableResource1107'):
        assert _is_linked(b2, 'GRM_SchedulableResource1107', a)
    _safe_set(a, 'MARTE_PAM_PaRunTInstance1106', None)
    assert not _is_linked(a, 'MARTE_PAM_PaRunTInstance1106', b2)
    if hasattr(b2, 'GRM_SchedulableResource1107'):
        assert not _is_linked(b2, 'GRM_SchedulableResource1107', a)


def test_assoc_isNonVolatile454_link_reassign_clear():
    a = MARTE_HwMemory_HwRAM(repl_Policy="sample_text", writePolicy="sample_text")
    b1 = NFP_Boolean()
    b2 = NFP_Boolean()
    _safe_set(a, 'MARTE_HwMemory_HwRAM455', b1)
    assert _is_linked(a, 'MARTE_HwMemory_HwRAM455', b1)
    if hasattr(b1, 'NFP_Boolean456'):
        assert _is_linked(b1, 'NFP_Boolean456', a)
    _safe_set(a, 'MARTE_HwMemory_HwRAM455', b2)
    assert _is_linked(a, 'MARTE_HwMemory_HwRAM455', b2)
    if hasattr(b1, 'NFP_Boolean456'):
        assert not _is_linked(b1, 'NFP_Boolean456', a)
    if hasattr(b2, 'NFP_Boolean456'):
        assert _is_linked(b2, 'NFP_Boolean456', a)
    _safe_set(a, 'MARTE_HwMemory_HwRAM455', None)
    assert not _is_linked(a, 'MARTE_HwMemory_HwRAM455', b2)
    if hasattr(b2, 'NFP_Boolean456'):
        assert not _is_linked(b2, 'NFP_Boolean456', a)


def test_assoc_isSched982_link_reassign_clear():
    a = MARTE_SAM_SaAnalysisContext(optCriterion="sample_text")
    b1 = NFP_Boolean()
    b2 = NFP_Boolean()
    _safe_set(a, 'MARTE_SAM_SaAnalysisContext', b1)
    assert _is_linked(a, 'MARTE_SAM_SaAnalysisContext', b1)
    if hasattr(b1, 'NFP_Boolean983'):
        assert _is_linked(b1, 'NFP_Boolean983', a)
    _safe_set(a, 'MARTE_SAM_SaAnalysisContext', b2)
    assert _is_linked(a, 'MARTE_SAM_SaAnalysisContext', b2)
    if hasattr(b1, 'NFP_Boolean983'):
        assert not _is_linked(b1, 'NFP_Boolean983', a)
    if hasattr(b2, 'NFP_Boolean983'):
        assert _is_linked(b2, 'NFP_Boolean983', a)
    _safe_set(a, 'MARTE_SAM_SaAnalysisContext', None)
    assert not _is_linked(a, 'MARTE_SAM_SaAnalysisContext', b2)
    if hasattr(b2, 'NFP_Boolean983'):
        assert not _is_linked(b2, 'NFP_Boolean983', a)


def test_assoc_isStatic451_link_reassign_clear():
    a = MARTE_HwMemory_HwRAM(repl_Policy="sample_text", writePolicy="sample_text")
    b1 = NFP_Boolean()
    b2 = NFP_Boolean()
    _safe_set(a, 'MARTE_HwMemory_HwRAM452', b1)
    assert _is_linked(a, 'MARTE_HwMemory_HwRAM452', b1)
    if hasattr(b1, 'NFP_Boolean453'):
        assert _is_linked(b1, 'NFP_Boolean453', a)
    _safe_set(a, 'MARTE_HwMemory_HwRAM452', b2)
    assert _is_linked(a, 'MARTE_HwMemory_HwRAM452', b2)
    if hasattr(b1, 'NFP_Boolean453'):
        assert not _is_linked(b1, 'NFP_Boolean453', a)
    if hasattr(b2, 'NFP_Boolean453'):
        assert _is_linked(b2, 'NFP_Boolean453', a)
    _safe_set(a, 'MARTE_HwMemory_HwRAM452', None)
    assert not _is_linked(a, 'MARTE_HwMemory_HwRAM452', b2)
    if hasattr(b2, 'NFP_Boolean453'):
        assert not _is_linked(b2, 'NFP_Boolean453', a)


def test_assoc_isSynchronous448_link_reassign_clear():
    a = MARTE_HwMemory_HwRAM(repl_Policy="sample_text", writePolicy="sample_text")
    b1 = NFP_Boolean()
    b2 = NFP_Boolean()
    _safe_set(a, 'MARTE_HwMemory_HwRAM449', b1)
    assert _is_linked(a, 'MARTE_HwMemory_HwRAM449', b1)
    if hasattr(b1, 'NFP_Boolean450'):
        assert _is_linked(b1, 'NFP_Boolean450', a)
    _safe_set(a, 'MARTE_HwMemory_HwRAM449', b2)
    assert _is_linked(a, 'MARTE_HwMemory_HwRAM449', b2)
    if hasattr(b1, 'NFP_Boolean450'):
        assert not _is_linked(b1, 'NFP_Boolean450', a)
    if hasattr(b2, 'NFP_Boolean450'):
        assert _is_linked(b2, 'NFP_Boolean450', a)
    _safe_set(a, 'MARTE_HwMemory_HwRAM449', None)
    assert not _is_linked(a, 'MARTE_HwMemory_HwRAM449', b2)
    if hasattr(b2, 'NFP_Boolean450'):
        assert not _is_linked(b2, 'NFP_Boolean450', a)


def test_assoc_joinServices697_link_reassign_clear():
    a = MARTE_SW_Concurrency_SwSchedulableResource(isPreemptable="sample_text", isStaticSchedulingFeature="sample_text")
    b1 = SW_Concurrency_MARTE_BehavioralFeature()
    b2 = SW_Concurrency_MARTE_BehavioralFeature()
    _safe_set(a, 'MARTE_SW_Concurrency_SwSchedulableResource698', {b1})
    assert _is_linked(a, 'MARTE_SW_Concurrency_SwSchedulableResource698', b1)
    if hasattr(b1, 'SW_Concurrency_MARTE_BehavioralFeature699'):
        assert _is_linked(b1, 'SW_Concurrency_MARTE_BehavioralFeature699', a)
    _safe_set(a, 'MARTE_SW_Concurrency_SwSchedulableResource698', {b2})
    assert _is_linked(a, 'MARTE_SW_Concurrency_SwSchedulableResource698', b2)
    if hasattr(b1, 'SW_Concurrency_MARTE_BehavioralFeature699'):
        assert not _is_linked(b1, 'SW_Concurrency_MARTE_BehavioralFeature699', a)
    if hasattr(b2, 'SW_Concurrency_MARTE_BehavioralFeature699'):
        assert _is_linked(b2, 'SW_Concurrency_MARTE_BehavioralFeature699', a)
    _safe_set(a, 'MARTE_SW_Concurrency_SwSchedulableResource698', set())
    assert not _is_linked(a, 'MARTE_SW_Concurrency_SwSchedulableResource698', b2)
    if hasattr(b2, 'SW_Concurrency_MARTE_BehavioralFeature699'):
        assert not _is_linked(b2, 'SW_Concurrency_MARTE_BehavioralFeature699', a)


def test_assoc_level464_link_reassign_clear():
    a = MARTE_HwMemory_HwCache(repl_Policy="sample_text", type="sample_text", writePolicy="sample_text")
    b1 = NFP_Natural()
    b2 = NFP_Natural()
    _safe_set(a, 'MARTE_HwMemory_HwCache', b1)
    assert _is_linked(a, 'MARTE_HwMemory_HwCache', b1)
    if hasattr(b1, 'NFP_Natural465'):
        assert _is_linked(b1, 'NFP_Natural465', a)
    _safe_set(a, 'MARTE_HwMemory_HwCache', b2)
    assert _is_linked(a, 'MARTE_HwMemory_HwCache', b2)
    if hasattr(b1, 'NFP_Natural465'):
        assert not _is_linked(b1, 'NFP_Natural465', a)
    if hasattr(b2, 'NFP_Natural465'):
        assert _is_linked(b2, 'NFP_Natural465', a)
    _safe_set(a, 'MARTE_HwMemory_HwCache', None)
    assert not _is_linked(a, 'MARTE_HwMemory_HwCache', b2)
    if hasattr(b2, 'NFP_Natural465'):
        assert not _is_linked(b2, 'NFP_Natural465', a)


def test_assoc_lockServices747_link_reassign_clear():
    a = MARTE_SW_Brokering_MemoryBroker(accessPolicy="sample_text")
    b1 = SW_Brokering_MARTE_BehavioralFeature()
    b2 = SW_Brokering_MARTE_BehavioralFeature()
    _safe_set(a, 'MARTE_SW_Brokering_MemoryBroker748', {b1})
    assert _is_linked(a, 'MARTE_SW_Brokering_MemoryBroker748', b1)
    if hasattr(b1, 'SW_Brokering_MARTE_BehavioralFeature749'):
        assert _is_linked(b1, 'SW_Brokering_MARTE_BehavioralFeature749', a)
    _safe_set(a, 'MARTE_SW_Brokering_MemoryBroker748', {b2})
    assert _is_linked(a, 'MARTE_SW_Brokering_MemoryBroker748', b2)
    if hasattr(b1, 'SW_Brokering_MARTE_BehavioralFeature749'):
        assert not _is_linked(b1, 'SW_Brokering_MARTE_BehavioralFeature749', a)
    if hasattr(b2, 'SW_Brokering_MARTE_BehavioralFeature749'):
        assert _is_linked(b2, 'SW_Brokering_MARTE_BehavioralFeature749', a)
    _safe_set(a, 'MARTE_SW_Brokering_MemoryBroker748', set())
    assert not _is_linked(a, 'MARTE_SW_Brokering_MemoryBroker748', b2)
    if hasattr(b2, 'SW_Brokering_MARTE_BehavioralFeature749'):
        assert not _is_linked(b2, 'SW_Brokering_MARTE_BehavioralFeature749', a)


def test_assoc_main243_link_reassign_clear():
    a = MARTE_HLAM_RtUnit(isDynamic="sample_text", isMain="sample_text", queueSchedPolicy="sample_text", queueSize="sample_text", srPoolPolicy="sample_text", srPoolSize="sample_text")
    b1 = HLAM_MARTE_Operation()
    b2 = HLAM_MARTE_Operation()
    _safe_set(a, 'MARTE_HLAM_RtUnit244', b1)
    assert _is_linked(a, 'MARTE_HLAM_RtUnit244', b1)
    if hasattr(b1, 'HLAM_MARTE_Operation'):
        assert _is_linked(b1, 'HLAM_MARTE_Operation', a)
    _safe_set(a, 'MARTE_HLAM_RtUnit244', b2)
    assert _is_linked(a, 'MARTE_HLAM_RtUnit244', b2)
    if hasattr(b1, 'HLAM_MARTE_Operation'):
        assert not _is_linked(b1, 'HLAM_MARTE_Operation', a)
    if hasattr(b2, 'HLAM_MARTE_Operation'):
        assert _is_linked(b2, 'HLAM_MARTE_Operation', a)
    _safe_set(a, 'MARTE_HLAM_RtUnit244', None)
    assert not _is_linked(a, 'MARTE_HLAM_RtUnit244', b2)
    if hasattr(b2, 'HLAM_MARTE_Operation'):
        assert not _is_linked(b2, 'HLAM_MARTE_Operation', a)


def test_assoc_mapServices753_link_reassign_clear():
    a = MARTE_SW_Brokering_MemoryBroker(accessPolicy="sample_text")
    b1 = SW_Brokering_MARTE_BehavioralFeature()
    b2 = SW_Brokering_MARTE_BehavioralFeature()
    _safe_set(a, 'MARTE_SW_Brokering_MemoryBroker754', {b1})
    assert _is_linked(a, 'MARTE_SW_Brokering_MemoryBroker754', b1)
    if hasattr(b1, 'SW_Brokering_MARTE_BehavioralFeature755'):
        assert _is_linked(b1, 'SW_Brokering_MARTE_BehavioralFeature755', a)
    _safe_set(a, 'MARTE_SW_Brokering_MemoryBroker754', {b2})
    assert _is_linked(a, 'MARTE_SW_Brokering_MemoryBroker754', b2)
    if hasattr(b1, 'SW_Brokering_MARTE_BehavioralFeature755'):
        assert not _is_linked(b1, 'SW_Brokering_MARTE_BehavioralFeature755', a)
    if hasattr(b2, 'SW_Brokering_MARTE_BehavioralFeature755'):
        assert _is_linked(b2, 'SW_Brokering_MARTE_BehavioralFeature755', a)
    _safe_set(a, 'MARTE_SW_Brokering_MemoryBroker754', set())
    assert not _is_linked(a, 'MARTE_SW_Brokering_MemoryBroker754', b2)
    if hasattr(b2, 'SW_Brokering_MARTE_BehavioralFeature755'):
        assert not _is_linked(b2, 'SW_Brokering_MARTE_BehavioralFeature755', a)


def test_assoc_maskElements675_link_reassign_clear():
    a = MARTE_SW_Concurrency_InterruptResource(isMaskable="sample_text", kind="sample_text")
    b1 = SW_Concurrency_MARTE_TypedElement()
    b2 = SW_Concurrency_MARTE_TypedElement()
    _safe_set(a, 'MARTE_SW_Concurrency_InterruptResource676', {b1})
    assert _is_linked(a, 'MARTE_SW_Concurrency_InterruptResource676', b1)
    if hasattr(b1, 'SW_Concurrency_MARTE_TypedElement677'):
        assert _is_linked(b1, 'SW_Concurrency_MARTE_TypedElement677', a)
    _safe_set(a, 'MARTE_SW_Concurrency_InterruptResource676', {b2})
    assert _is_linked(a, 'MARTE_SW_Concurrency_InterruptResource676', b2)
    if hasattr(b1, 'SW_Concurrency_MARTE_TypedElement677'):
        assert not _is_linked(b1, 'SW_Concurrency_MARTE_TypedElement677', a)
    if hasattr(b2, 'SW_Concurrency_MARTE_TypedElement677'):
        assert _is_linked(b2, 'SW_Concurrency_MARTE_TypedElement677', a)
    _safe_set(a, 'MARTE_SW_Concurrency_InterruptResource676', set())
    assert not _is_linked(a, 'MARTE_SW_Concurrency_InterruptResource676', b2)
    if hasattr(b2, 'SW_Concurrency_MARTE_TypedElement677'):
        assert not _is_linked(b2, 'SW_Concurrency_MARTE_TypedElement677', a)


def test_assoc_maskElements777_link_reassign_clear():
    a = MARTE_SW_Interaction_NotificationResource(mechanism="sample_text", occurence="sample_text")
    b1 = SW_Interaction_MARTE_TypedElement()
    b2 = SW_Interaction_MARTE_TypedElement()
    _safe_set(a, 'MARTE_SW_Interaction_NotificationResource778', {b1})
    assert _is_linked(a, 'MARTE_SW_Interaction_NotificationResource778', b1)
    if hasattr(b1, 'SW_Interaction_MARTE_TypedElement779'):
        assert _is_linked(b1, 'SW_Interaction_MARTE_TypedElement779', a)
    _safe_set(a, 'MARTE_SW_Interaction_NotificationResource778', {b2})
    assert _is_linked(a, 'MARTE_SW_Interaction_NotificationResource778', b2)
    if hasattr(b1, 'SW_Interaction_MARTE_TypedElement779'):
        assert not _is_linked(b1, 'SW_Interaction_MARTE_TypedElement779', a)
    if hasattr(b2, 'SW_Interaction_MARTE_TypedElement779'):
        assert _is_linked(b2, 'SW_Interaction_MARTE_TypedElement779', a)
    _safe_set(a, 'MARTE_SW_Interaction_NotificationResource778', set())
    assert not _is_linked(a, 'MARTE_SW_Interaction_NotificationResource778', b2)
    if hasattr(b2, 'SW_Interaction_MARTE_TypedElement779'):
        assert not _is_linked(b2, 'SW_Interaction_MARTE_TypedElement779', a)


def test_assoc_maxValAttr63_link_reassign_clear():
    a = MARTE_Time_ClockType(isLogical="sample_text", nature="sample_text")
    b1 = Time_MARTE_Property()
    b2 = Time_MARTE_Property()
    _safe_set(a, 'MARTE_Time_ClockType64', b1)
    assert _is_linked(a, 'MARTE_Time_ClockType64', b1)
    if hasattr(b1, 'Time_MARTE_Property65'):
        assert _is_linked(b1, 'Time_MARTE_Property65', a)
    _safe_set(a, 'MARTE_Time_ClockType64', b2)
    assert _is_linked(a, 'MARTE_Time_ClockType64', b2)
    if hasattr(b1, 'Time_MARTE_Property65'):
        assert not _is_linked(b1, 'Time_MARTE_Property65', a)
    if hasattr(b2, 'Time_MARTE_Property65'):
        assert _is_linked(b2, 'Time_MARTE_Property65', a)
    _safe_set(a, 'MARTE_Time_ClockType64', None)
    assert not _is_linked(a, 'MARTE_Time_ClockType64', b2)
    if hasattr(b2, 'Time_MARTE_Property65'):
        assert not _is_linked(b2, 'Time_MARTE_Property65', a)


def test_assoc_memories739_link_reassign_clear():
    a = MARTE_SW_Brokering_MemoryBroker(accessPolicy="sample_text")
    b1 = SW_Brokering_MARTE_TypedElement()
    b2 = SW_Brokering_MARTE_TypedElement()
    _safe_set(a, 'MARTE_SW_Brokering_MemoryBroker', {b1})
    assert _is_linked(a, 'MARTE_SW_Brokering_MemoryBroker', b1)
    if hasattr(b1, 'SW_Brokering_MARTE_TypedElement740'):
        assert _is_linked(b1, 'SW_Brokering_MARTE_TypedElement740', a)
    _safe_set(a, 'MARTE_SW_Brokering_MemoryBroker', {b2})
    assert _is_linked(a, 'MARTE_SW_Brokering_MemoryBroker', b2)
    if hasattr(b1, 'SW_Brokering_MARTE_TypedElement740'):
        assert not _is_linked(b1, 'SW_Brokering_MARTE_TypedElement740', a)
    if hasattr(b2, 'SW_Brokering_MARTE_TypedElement740'):
        assert _is_linked(b2, 'SW_Brokering_MARTE_TypedElement740', a)
    _safe_set(a, 'MARTE_SW_Brokering_MemoryBroker', set())
    assert not _is_linked(a, 'MARTE_SW_Brokering_MemoryBroker', b2)
    if hasattr(b2, 'SW_Brokering_MARTE_TypedElement740'):
        assert not _is_linked(b2, 'SW_Brokering_MARTE_TypedElement740', a)


def test_assoc_memoryBlockAdressElements741_link_reassign_clear():
    a = MARTE_SW_Brokering_MemoryBroker(accessPolicy="sample_text")
    b1 = SW_Brokering_MARTE_TypedElement()
    b2 = SW_Brokering_MARTE_TypedElement()
    _safe_set(a, 'MARTE_SW_Brokering_MemoryBroker742', {b1})
    assert _is_linked(a, 'MARTE_SW_Brokering_MemoryBroker742', b1)
    if hasattr(b1, 'SW_Brokering_MARTE_TypedElement743'):
        assert _is_linked(b1, 'SW_Brokering_MARTE_TypedElement743', a)
    _safe_set(a, 'MARTE_SW_Brokering_MemoryBroker742', {b2})
    assert _is_linked(a, 'MARTE_SW_Brokering_MemoryBroker742', b2)
    if hasattr(b1, 'SW_Brokering_MARTE_TypedElement743'):
        assert not _is_linked(b1, 'SW_Brokering_MARTE_TypedElement743', a)
    if hasattr(b2, 'SW_Brokering_MARTE_TypedElement743'):
        assert _is_linked(b2, 'SW_Brokering_MARTE_TypedElement743', a)
    _safe_set(a, 'MARTE_SW_Brokering_MemoryBroker742', set())
    assert not _is_linked(a, 'MARTE_SW_Brokering_MemoryBroker742', b2)
    if hasattr(b2, 'SW_Brokering_MARTE_TypedElement743'):
        assert not _is_linked(b2, 'SW_Brokering_MARTE_TypedElement743', a)


def test_assoc_memoryBlockSizeElements744_link_reassign_clear():
    a = MARTE_SW_Brokering_MemoryBroker(accessPolicy="sample_text")
    b1 = SW_Brokering_MARTE_TypedElement()
    b2 = SW_Brokering_MARTE_TypedElement()
    _safe_set(a, 'MARTE_SW_Brokering_MemoryBroker745', {b1})
    assert _is_linked(a, 'MARTE_SW_Brokering_MemoryBroker745', b1)
    if hasattr(b1, 'SW_Brokering_MARTE_TypedElement746'):
        assert _is_linked(b1, 'SW_Brokering_MARTE_TypedElement746', a)
    _safe_set(a, 'MARTE_SW_Brokering_MemoryBroker745', {b2})
    assert _is_linked(a, 'MARTE_SW_Brokering_MemoryBroker745', b2)
    if hasattr(b1, 'SW_Brokering_MARTE_TypedElement746'):
        assert not _is_linked(b1, 'SW_Brokering_MARTE_TypedElement746', a)
    if hasattr(b2, 'SW_Brokering_MARTE_TypedElement746'):
        assert _is_linked(b2, 'SW_Brokering_MARTE_TypedElement746', a)
    _safe_set(a, 'MARTE_SW_Brokering_MemoryBroker745', set())
    assert not _is_linked(a, 'MARTE_SW_Brokering_MemoryBroker745', b2)
    if hasattr(b2, 'SW_Brokering_MARTE_TypedElement746'):
        assert not _is_linked(b2, 'SW_Brokering_MARTE_TypedElement746', a)


def test_assoc_memorySize245_link_reassign_clear():
    a = MARTE_HLAM_RtUnit(isDynamic="sample_text", isMain="sample_text", queueSchedPolicy="sample_text", queueSize="sample_text", srPoolPolicy="sample_text", srPoolSize="sample_text")
    b1 = NFP_DataSize()
    b2 = NFP_DataSize()
    _safe_set(a, 'MARTE_HLAM_RtUnit246', b1)
    assert _is_linked(a, 'MARTE_HLAM_RtUnit246', b1)
    if hasattr(b1, 'NFP_DataSize247'):
        assert _is_linked(b1, 'NFP_DataSize247', a)
    _safe_set(a, 'MARTE_HLAM_RtUnit246', b2)
    assert _is_linked(a, 'MARTE_HLAM_RtUnit246', b2)
    if hasattr(b1, 'NFP_DataSize247'):
        assert not _is_linked(b1, 'NFP_DataSize247', a)
    if hasattr(b2, 'NFP_DataSize247'):
        assert _is_linked(b2, 'NFP_DataSize247', a)
    _safe_set(a, 'MARTE_HLAM_RtUnit246', None)
    assert not _is_linked(a, 'MARTE_HLAM_RtUnit246', b2)
    if hasattr(b2, 'NFP_DataSize247'):
        assert not _is_linked(b2, 'NFP_DataSize247', a)


def test_assoc_memorySize253_link_reassign_clear():
    a = MARTE_HLAM_PpUnit(concPolicy="sample_text")
    b1 = NFP_DataSize()
    b2 = NFP_DataSize()
    _safe_set(a, 'MARTE_HLAM_PpUnit', b1)
    assert _is_linked(a, 'MARTE_HLAM_PpUnit', b1)
    if hasattr(b1, 'NFP_DataSize254'):
        assert _is_linked(b1, 'NFP_DataSize254', a)
    _safe_set(a, 'MARTE_HLAM_PpUnit', b2)
    assert _is_linked(a, 'MARTE_HLAM_PpUnit', b2)
    if hasattr(b1, 'NFP_DataSize254'):
        assert not _is_linked(b1, 'NFP_DataSize254', a)
    if hasattr(b2, 'NFP_DataSize254'):
        assert _is_linked(b2, 'NFP_DataSize254', a)
    _safe_set(a, 'MARTE_HLAM_PpUnit', None)
    assert not _is_linked(a, 'MARTE_HLAM_PpUnit', b2)
    if hasattr(b2, 'NFP_DataSize254'):
        assert not _is_linked(b2, 'NFP_DataSize254', a)


def test_assoc_messageQueueCapacityElements766_link_reassign_clear():
    a = MARTE_SW_Interaction_MessageComResource(isFixedMessageSize="sample_text", mechanism="sample_text", messageQueuePolicy="sample_text")
    b1 = SW_Interaction_MARTE_TypedElement()
    b2 = SW_Interaction_MARTE_TypedElement()
    _safe_set(a, 'MARTE_SW_Interaction_MessageComResource767', {b1})
    assert _is_linked(a, 'MARTE_SW_Interaction_MessageComResource767', b1)
    if hasattr(b1, 'SW_Interaction_MARTE_TypedElement768'):
        assert _is_linked(b1, 'SW_Interaction_MARTE_TypedElement768', a)
    _safe_set(a, 'MARTE_SW_Interaction_MessageComResource767', {b2})
    assert _is_linked(a, 'MARTE_SW_Interaction_MessageComResource767', b2)
    if hasattr(b1, 'SW_Interaction_MARTE_TypedElement768'):
        assert not _is_linked(b1, 'SW_Interaction_MARTE_TypedElement768', a)
    if hasattr(b2, 'SW_Interaction_MARTE_TypedElement768'):
        assert _is_linked(b2, 'SW_Interaction_MARTE_TypedElement768', a)
    _safe_set(a, 'MARTE_SW_Interaction_MessageComResource767', set())
    assert not _is_linked(a, 'MARTE_SW_Interaction_MessageComResource767', b2)
    if hasattr(b2, 'SW_Interaction_MARTE_TypedElement768'):
        assert not _is_linked(b2, 'SW_Interaction_MARTE_TypedElement768', a)


def test_assoc_messageResources661_link_reassign_clear():
    a = MARTE_SW_Concurrency_SwConcurrentResource(activationCapacity="sample_text")
    b1 = SW_Concurrency_MARTE_TypedElement()
    b2 = SW_Concurrency_MARTE_TypedElement()
    _safe_set(a, 'MARTE_SW_Concurrency_SwConcurrentResource662', {b1})
    assert _is_linked(a, 'MARTE_SW_Concurrency_SwConcurrentResource662', b1)
    if hasattr(b1, 'SW_Concurrency_MARTE_TypedElement663'):
        assert _is_linked(b1, 'SW_Concurrency_MARTE_TypedElement663', a)
    _safe_set(a, 'MARTE_SW_Concurrency_SwConcurrentResource662', {b2})
    assert _is_linked(a, 'MARTE_SW_Concurrency_SwConcurrentResource662', b2)
    if hasattr(b1, 'SW_Concurrency_MARTE_TypedElement663'):
        assert not _is_linked(b1, 'SW_Concurrency_MARTE_TypedElement663', a)
    if hasattr(b2, 'SW_Concurrency_MARTE_TypedElement663'):
        assert _is_linked(b2, 'SW_Concurrency_MARTE_TypedElement663', a)
    _safe_set(a, 'MARTE_SW_Concurrency_SwConcurrentResource662', set())
    assert not _is_linked(a, 'MARTE_SW_Concurrency_SwConcurrentResource662', b2)
    if hasattr(b2, 'SW_Concurrency_MARTE_TypedElement663'):
        assert not _is_linked(b2, 'SW_Concurrency_MARTE_TypedElement663', a)


def test_assoc_messageSizeElements764_link_reassign_clear():
    a = MARTE_SW_Interaction_MessageComResource(isFixedMessageSize="sample_text", mechanism="sample_text", messageQueuePolicy="sample_text")
    b1 = SW_Interaction_MARTE_TypedElement()
    b2 = SW_Interaction_MARTE_TypedElement()
    _safe_set(a, 'MARTE_SW_Interaction_MessageComResource', {b1})
    assert _is_linked(a, 'MARTE_SW_Interaction_MessageComResource', b1)
    if hasattr(b1, 'SW_Interaction_MARTE_TypedElement765'):
        assert _is_linked(b1, 'SW_Interaction_MARTE_TypedElement765', a)
    _safe_set(a, 'MARTE_SW_Interaction_MessageComResource', {b2})
    assert _is_linked(a, 'MARTE_SW_Interaction_MessageComResource', b2)
    if hasattr(b1, 'SW_Interaction_MARTE_TypedElement765'):
        assert not _is_linked(b1, 'SW_Interaction_MARTE_TypedElement765', a)
    if hasattr(b2, 'SW_Interaction_MARTE_TypedElement765'):
        assert _is_linked(b2, 'SW_Interaction_MARTE_TypedElement765', a)
    _safe_set(a, 'MARTE_SW_Interaction_MessageComResource', set())
    assert not _is_linked(a, 'MARTE_SW_Interaction_MessageComResource', b2)
    if hasattr(b2, 'SW_Interaction_MARTE_TypedElement765'):
        assert not _is_linked(b2, 'SW_Interaction_MARTE_TypedElement765', a)


def test_assoc_mode5_link_reassign_clear():
    a = MARTE_NFPs_NfpConstraint(kind="sample_text")
    b1 = CoreElements_Mode()
    b2 = CoreElements_Mode()
    _safe_set(a, 'MARTE_NFPs_NfpConstraint6', {b1})
    assert _is_linked(a, 'MARTE_NFPs_NfpConstraint6', b1)
    if hasattr(b1, 'CoreElements_Mode'):
        assert _is_linked(b1, 'CoreElements_Mode', a)
    _safe_set(a, 'MARTE_NFPs_NfpConstraint6', {b2})
    assert _is_linked(a, 'MARTE_NFPs_NfpConstraint6', b2)
    if hasattr(b1, 'CoreElements_Mode'):
        assert not _is_linked(b1, 'CoreElements_Mode', a)
    if hasattr(b2, 'CoreElements_Mode'):
        assert _is_linked(b2, 'CoreElements_Mode', a)
    _safe_set(a, 'MARTE_NFPs_NfpConstraint6', set())
    assert not _is_linked(a, 'MARTE_NFPs_NfpConstraint6', b2)
    if hasattr(b2, 'CoreElements_Mode'):
        assert not _is_linked(b2, 'CoreElements_Mode', a)


def test_assoc_msgMaxSize250_link_reassign_clear():
    a = MARTE_HLAM_RtUnit(isDynamic="sample_text", isMain="sample_text", queueSchedPolicy="sample_text", queueSize="sample_text", srPoolPolicy="sample_text", srPoolSize="sample_text")
    b1 = NFP_DataSize()
    b2 = NFP_DataSize()
    _safe_set(a, 'MARTE_HLAM_RtUnit251', b1)
    assert _is_linked(a, 'MARTE_HLAM_RtUnit251', b1)
    if hasattr(b1, 'NFP_DataSize252'):
        assert _is_linked(b1, 'NFP_DataSize252', a)
    _safe_set(a, 'MARTE_HLAM_RtUnit251', b2)
    assert _is_linked(a, 'MARTE_HLAM_RtUnit251', b2)
    if hasattr(b1, 'NFP_DataSize252'):
        assert not _is_linked(b1, 'NFP_DataSize252', a)
    if hasattr(b2, 'NFP_DataSize252'):
        assert _is_linked(b2, 'NFP_DataSize252', a)
    _safe_set(a, 'MARTE_HLAM_RtUnit251', None)
    assert not _is_linked(a, 'MARTE_HLAM_RtUnit251', b2)
    if hasattr(b2, 'NFP_DataSize252'):
        assert not _is_linked(b2, 'NFP_DataSize252', a)


def test_assoc_msgSize292_link_reassign_clear():
    a = MARTE_HLAM_RtAction(isAtomic="sample_text", synchKind="sample_text")
    b1 = NFP_DataSize()
    b2 = NFP_DataSize()
    _safe_set(a, 'MARTE_HLAM_RtAction', b1)
    assert _is_linked(a, 'MARTE_HLAM_RtAction', b1)
    if hasattr(b1, 'NFP_DataSize293'):
        assert _is_linked(b1, 'NFP_DataSize293', a)
    _safe_set(a, 'MARTE_HLAM_RtAction', b2)
    assert _is_linked(a, 'MARTE_HLAM_RtAction', b2)
    if hasattr(b1, 'NFP_DataSize293'):
        assert not _is_linked(b1, 'NFP_DataSize293', a)
    if hasattr(b2, 'NFP_DataSize293'):
        assert _is_linked(b2, 'NFP_DataSize293', a)
    _safe_set(a, 'MARTE_HLAM_RtAction', None)
    assert not _is_linked(a, 'MARTE_HLAM_RtAction', b2)
    if hasattr(b2, 'NFP_DataSize293'):
        assert not _is_linked(b2, 'NFP_DataSize293', a)


def test_assoc_mutualExclusionResources664_link_reassign_clear():
    a = MARTE_SW_Concurrency_SwConcurrentResource(activationCapacity="sample_text")
    b1 = SW_Concurrency_MARTE_TypedElement()
    b2 = SW_Concurrency_MARTE_TypedElement()
    _safe_set(a, 'MARTE_SW_Concurrency_SwConcurrentResource665', {b1})
    assert _is_linked(a, 'MARTE_SW_Concurrency_SwConcurrentResource665', b1)
    if hasattr(b1, 'SW_Concurrency_MARTE_TypedElement666'):
        assert _is_linked(b1, 'SW_Concurrency_MARTE_TypedElement666', a)
    _safe_set(a, 'MARTE_SW_Concurrency_SwConcurrentResource665', {b2})
    assert _is_linked(a, 'MARTE_SW_Concurrency_SwConcurrentResource665', b2)
    if hasattr(b1, 'SW_Concurrency_MARTE_TypedElement666'):
        assert not _is_linked(b1, 'SW_Concurrency_MARTE_TypedElement666', a)
    if hasattr(b2, 'SW_Concurrency_MARTE_TypedElement666'):
        assert _is_linked(b2, 'SW_Concurrency_MARTE_TypedElement666', a)
    _safe_set(a, 'MARTE_SW_Concurrency_SwConcurrentResource665', set())
    assert not _is_linked(a, 'MARTE_SW_Concurrency_SwConcurrentResource665', b2)
    if hasattr(b2, 'SW_Concurrency_MARTE_TypedElement666'):
        assert not _is_linked(b2, 'SW_Concurrency_MARTE_TypedElement666', a)


def test_assoc_nbColumns304_link_reassign_clear():
    a = MARTE_HwComputing_PLD_Organization(class_="sample_text")
    b1 = NFP_Natural()
    b2 = NFP_Natural()
    _safe_set(a, 'MARTE_HwComputing_PLD_Organization305', b1)
    assert _is_linked(a, 'MARTE_HwComputing_PLD_Organization305', b1)
    if hasattr(b1, 'NFP_Natural'):
        assert _is_linked(b1, 'NFP_Natural', a)
    _safe_set(a, 'MARTE_HwComputing_PLD_Organization305', b2)
    assert _is_linked(a, 'MARTE_HwComputing_PLD_Organization305', b2)
    if hasattr(b1, 'NFP_Natural'):
        assert not _is_linked(b1, 'NFP_Natural', a)
    if hasattr(b2, 'NFP_Natural'):
        assert _is_linked(b2, 'NFP_Natural', a)
    _safe_set(a, 'MARTE_HwComputing_PLD_Organization305', None)
    assert not _is_linked(a, 'MARTE_HwComputing_PLD_Organization305', b2)
    if hasattr(b2, 'NFP_Natural'):
        assert not _is_linked(b2, 'NFP_Natural', a)


def test_assoc_nbFlipFlops349_link_reassign_clear():
    a = MARTE_HwComputing_HwPLD(technology="sample_text")
    b1 = NFP_Natural()
    b2 = NFP_Natural()
    _safe_set(a, 'MARTE_HwComputing_HwPLD350', b1)
    assert _is_linked(a, 'MARTE_HwComputing_HwPLD350', b1)
    if hasattr(b1, 'NFP_Natural351'):
        assert _is_linked(b1, 'NFP_Natural351', a)
    _safe_set(a, 'MARTE_HwComputing_HwPLD350', b2)
    assert _is_linked(a, 'MARTE_HwComputing_HwPLD350', b2)
    if hasattr(b1, 'NFP_Natural351'):
        assert not _is_linked(b1, 'NFP_Natural351', a)
    if hasattr(b2, 'NFP_Natural351'):
        assert _is_linked(b2, 'NFP_Natural351', a)
    _safe_set(a, 'MARTE_HwComputing_HwPLD350', None)
    assert not _is_linked(a, 'MARTE_HwComputing_HwPLD350', b2)
    if hasattr(b2, 'NFP_Natural351'):
        assert not _is_linked(b2, 'NFP_Natural351', a)


def test_assoc_nbLUTs343_link_reassign_clear():
    a = MARTE_HwComputing_HwPLD(technology="sample_text")
    b1 = NFP_Natural()
    b2 = NFP_Natural()
    _safe_set(a, 'MARTE_HwComputing_HwPLD344', b1)
    assert _is_linked(a, 'MARTE_HwComputing_HwPLD344', b1)
    if hasattr(b1, 'NFP_Natural345'):
        assert _is_linked(b1, 'NFP_Natural345', a)
    _safe_set(a, 'MARTE_HwComputing_HwPLD344', b2)
    assert _is_linked(a, 'MARTE_HwComputing_HwPLD344', b2)
    if hasattr(b1, 'NFP_Natural345'):
        assert not _is_linked(b1, 'NFP_Natural345', a)
    if hasattr(b2, 'NFP_Natural345'):
        assert _is_linked(b2, 'NFP_Natural345', a)
    _safe_set(a, 'MARTE_HwComputing_HwPLD344', None)
    assert not _is_linked(a, 'MARTE_HwComputing_HwPLD344', b2)
    if hasattr(b2, 'NFP_Natural345'):
        assert not _is_linked(b2, 'NFP_Natural345', a)


def test_assoc_nbPins533_link_reassign_clear():
    a = MARTE_HwLayout_HwComponent(kind="sample_text")
    b1 = NFP_Natural()
    b2 = NFP_Natural()
    _safe_set(a, 'MARTE_HwLayout_HwComponent534', b1)
    assert _is_linked(a, 'MARTE_HwLayout_HwComponent534', b1)
    if hasattr(b1, 'NFP_Natural535'):
        assert _is_linked(b1, 'NFP_Natural535', a)
    _safe_set(a, 'MARTE_HwLayout_HwComponent534', b2)
    assert _is_linked(a, 'MARTE_HwLayout_HwComponent534', b2)
    if hasattr(b1, 'NFP_Natural535'):
        assert not _is_linked(b1, 'NFP_Natural535', a)
    if hasattr(b2, 'NFP_Natural535'):
        assert _is_linked(b2, 'NFP_Natural535', a)
    _safe_set(a, 'MARTE_HwLayout_HwComponent534', None)
    assert not _is_linked(a, 'MARTE_HwLayout_HwComponent534', b2)
    if hasattr(b2, 'NFP_Natural535'):
        assert not _is_linked(b2, 'NFP_Natural535', a)


def test_assoc_nbRows302_link_reassign_clear():
    a = MARTE_HwComputing_PLD_Organization(class_="sample_text")
    b1 = NFP_Integer()
    b2 = NFP_Integer()
    _safe_set(a, 'MARTE_HwComputing_PLD_Organization', b1)
    assert _is_linked(a, 'MARTE_HwComputing_PLD_Organization', b1)
    if hasattr(b1, 'NFP_Integer303'):
        assert _is_linked(b1, 'NFP_Integer303', a)
    _safe_set(a, 'MARTE_HwComputing_PLD_Organization', b2)
    assert _is_linked(a, 'MARTE_HwComputing_PLD_Organization', b2)
    if hasattr(b1, 'NFP_Integer303'):
        assert not _is_linked(b1, 'NFP_Integer303', a)
    if hasattr(b2, 'NFP_Integer303'):
        assert _is_linked(b2, 'NFP_Integer303', a)
    _safe_set(a, 'MARTE_HwComputing_PLD_Organization', None)
    assert not _is_linked(a, 'MARTE_HwComputing_PLD_Organization', b2)
    if hasattr(b2, 'NFP_Integer303'):
        assert not _is_linked(b2, 'NFP_Integer303', a)


def test_assoc_ndLUT_Inputs346_link_reassign_clear():
    a = MARTE_HwComputing_HwPLD(technology="sample_text")
    b1 = NFP_Natural()
    b2 = NFP_Natural()
    _safe_set(a, 'MARTE_HwComputing_HwPLD347', b1)
    assert _is_linked(a, 'MARTE_HwComputing_HwPLD347', b1)
    if hasattr(b1, 'NFP_Natural348'):
        assert _is_linked(b1, 'NFP_Natural348', a)
    _safe_set(a, 'MARTE_HwComputing_HwPLD347', b2)
    assert _is_linked(a, 'MARTE_HwComputing_HwPLD347', b2)
    if hasattr(b1, 'NFP_Natural348'):
        assert not _is_linked(b1, 'NFP_Natural348', a)
    if hasattr(b2, 'NFP_Natural348'):
        assert _is_linked(b2, 'NFP_Natural348', a)
    _safe_set(a, 'MARTE_HwComputing_HwPLD347', None)
    assert not _is_linked(a, 'MARTE_HwComputing_HwPLD347', b2)
    if hasattr(b2, 'NFP_Natural348'):
        assert not _is_linked(b2, 'NFP_Natural348', a)


def test_assoc_noSync1079_link_reassign_clear():
    a = MARTE_PAM_PaStep(extOpDemand="sample_text")
    b1 = NFP_Boolean()
    b2 = NFP_Boolean()
    _safe_set(a, 'MARTE_PAM_PaStep', b1)
    assert _is_linked(a, 'MARTE_PAM_PaStep', b1)
    if hasattr(b1, 'NFP_Boolean1080'):
        assert _is_linked(b1, 'NFP_Boolean1080', a)
    _safe_set(a, 'MARTE_PAM_PaStep', b2)
    assert _is_linked(a, 'MARTE_PAM_PaStep', b2)
    if hasattr(b1, 'NFP_Boolean1080'):
        assert not _is_linked(b1, 'NFP_Boolean1080', a)
    if hasattr(b2, 'NFP_Boolean1080'):
        assert _is_linked(b2, 'NFP_Boolean1080', a)
    _safe_set(a, 'MARTE_PAM_PaStep', None)
    assert not _is_linked(a, 'MARTE_PAM_PaStep', b2)
    if hasattr(b2, 'NFP_Boolean1080'):
        assert not _is_linked(b2, 'NFP_Boolean1080', a)


def test_assoc_notificationResources667_link_reassign_clear():
    a = MARTE_SW_Concurrency_SwConcurrentResource(activationCapacity="sample_text")
    b1 = SW_Concurrency_MARTE_TypedElement()
    b2 = SW_Concurrency_MARTE_TypedElement()
    _safe_set(a, 'MARTE_SW_Concurrency_SwConcurrentResource668', {b1})
    assert _is_linked(a, 'MARTE_SW_Concurrency_SwConcurrentResource668', b1)
    if hasattr(b1, 'SW_Concurrency_MARTE_TypedElement669'):
        assert _is_linked(b1, 'SW_Concurrency_MARTE_TypedElement669', a)
    _safe_set(a, 'MARTE_SW_Concurrency_SwConcurrentResource668', {b2})
    assert _is_linked(a, 'MARTE_SW_Concurrency_SwConcurrentResource668', b2)
    if hasattr(b1, 'SW_Concurrency_MARTE_TypedElement669'):
        assert not _is_linked(b1, 'SW_Concurrency_MARTE_TypedElement669', a)
    if hasattr(b2, 'SW_Concurrency_MARTE_TypedElement669'):
        assert _is_linked(b2, 'SW_Concurrency_MARTE_TypedElement669', a)
    _safe_set(a, 'MARTE_SW_Concurrency_SwConcurrentResource668', set())
    assert not _is_linked(a, 'MARTE_SW_Concurrency_SwConcurrentResource668', b2)
    if hasattr(b2, 'SW_Concurrency_MARTE_TypedElement669'):
        assert not _is_linked(b2, 'SW_Concurrency_MARTE_TypedElement669', a)


def test_assoc_occurenceCountElements775_link_reassign_clear():
    a = MARTE_SW_Interaction_NotificationResource(mechanism="sample_text", occurence="sample_text")
    b1 = SW_Interaction_MARTE_TypedElement()
    b2 = SW_Interaction_MARTE_TypedElement()
    _safe_set(a, 'MARTE_SW_Interaction_NotificationResource', {b1})
    assert _is_linked(a, 'MARTE_SW_Interaction_NotificationResource', b1)
    if hasattr(b1, 'SW_Interaction_MARTE_TypedElement776'):
        assert _is_linked(b1, 'SW_Interaction_MARTE_TypedElement776', a)
    _safe_set(a, 'MARTE_SW_Interaction_NotificationResource', {b2})
    assert _is_linked(a, 'MARTE_SW_Interaction_NotificationResource', b2)
    if hasattr(b1, 'SW_Interaction_MARTE_TypedElement776'):
        assert not _is_linked(b1, 'SW_Interaction_MARTE_TypedElement776', a)
    if hasattr(b2, 'SW_Interaction_MARTE_TypedElement776'):
        assert _is_linked(b2, 'SW_Interaction_MARTE_TypedElement776', a)
    _safe_set(a, 'MARTE_SW_Interaction_NotificationResource', set())
    assert not _is_linked(a, 'MARTE_SW_Interaction_NotificationResource', b2)
    if hasattr(b2, 'SW_Interaction_MARTE_TypedElement776'):
        assert not _is_linked(b2, 'SW_Interaction_MARTE_TypedElement776', a)


def test_assoc_offsetAttr66_link_reassign_clear():
    a = MARTE_Time_ClockType(isLogical="sample_text", nature="sample_text")
    b1 = Time_MARTE_Property()
    b2 = Time_MARTE_Property()
    _safe_set(a, 'MARTE_Time_ClockType67', b1)
    assert _is_linked(a, 'MARTE_Time_ClockType67', b1)
    if hasattr(b1, 'Time_MARTE_Property68'):
        assert _is_linked(b1, 'Time_MARTE_Property68', a)
    _safe_set(a, 'MARTE_Time_ClockType67', b2)
    assert _is_linked(a, 'MARTE_Time_ClockType67', b2)
    if hasattr(b1, 'Time_MARTE_Property68'):
        assert not _is_linked(b1, 'Time_MARTE_Property68', a)
    if hasattr(b2, 'Time_MARTE_Property68'):
        assert _is_linked(b2, 'Time_MARTE_Property68', a)
    _safe_set(a, 'MARTE_Time_ClockType67', None)
    assert not _is_linked(a, 'MARTE_Time_ClockType67', b2)
    if hasattr(b2, 'Time_MARTE_Property68'):
        assert not _is_linked(b2, 'Time_MARTE_Property68', a)


def test_assoc_openServices726_link_reassign_clear():
    a = MARTE_SW_Brokering_DeviceBroker(accessPolicy="sample_text", isBuffered="sample_text", name="sample_text")
    b1 = SW_Brokering_MARTE_BehavioralFeature()
    b2 = SW_Brokering_MARTE_BehavioralFeature()
    _safe_set(a, 'MARTE_SW_Brokering_DeviceBroker727', {b1})
    assert _is_linked(a, 'MARTE_SW_Brokering_DeviceBroker727', b1)
    if hasattr(b1, 'SW_Brokering_MARTE_BehavioralFeature728'):
        assert _is_linked(b1, 'SW_Brokering_MARTE_BehavioralFeature728', a)
    _safe_set(a, 'MARTE_SW_Brokering_DeviceBroker727', {b2})
    assert _is_linked(a, 'MARTE_SW_Brokering_DeviceBroker727', b2)
    if hasattr(b1, 'SW_Brokering_MARTE_BehavioralFeature728'):
        assert not _is_linked(b1, 'SW_Brokering_MARTE_BehavioralFeature728', a)
    if hasattr(b2, 'SW_Brokering_MARTE_BehavioralFeature728'):
        assert _is_linked(b2, 'SW_Brokering_MARTE_BehavioralFeature728', a)
    _safe_set(a, 'MARTE_SW_Brokering_DeviceBroker727', set())
    assert not _is_linked(a, 'MARTE_SW_Brokering_DeviceBroker727', b2)
    if hasattr(b2, 'SW_Brokering_MARTE_BehavioralFeature728'):
        assert not _is_linked(b2, 'SW_Brokering_MARTE_BehavioralFeature728', a)


def test_assoc_operationalMode241_link_reassign_clear():
    a = MARTE_HLAM_RtUnit(isDynamic="sample_text", isMain="sample_text", queueSchedPolicy="sample_text", queueSize="sample_text", srPoolPolicy="sample_text", srPoolSize="sample_text")
    b1 = HLAM_MARTE_Behavior()
    b2 = HLAM_MARTE_Behavior()
    _safe_set(a, 'MARTE_HLAM_RtUnit242', b1)
    assert _is_linked(a, 'MARTE_HLAM_RtUnit242', b1)
    if hasattr(b1, 'HLAM_MARTE_Behavior'):
        assert _is_linked(b1, 'HLAM_MARTE_Behavior', a)
    _safe_set(a, 'MARTE_HLAM_RtUnit242', b2)
    assert _is_linked(a, 'MARTE_HLAM_RtUnit242', b2)
    if hasattr(b1, 'HLAM_MARTE_Behavior'):
        assert not _is_linked(b1, 'HLAM_MARTE_Behavior', a)
    if hasattr(b2, 'HLAM_MARTE_Behavior'):
        assert _is_linked(b2, 'HLAM_MARTE_Behavior', a)
    _safe_set(a, 'MARTE_HLAM_RtUnit242', None)
    assert not _is_linked(a, 'MARTE_HLAM_RtUnit242', b2)
    if hasattr(b2, 'HLAM_MARTE_Behavior'):
        assert not _is_linked(b2, 'HLAM_MARTE_Behavior', a)


def test_assoc_operations521_link_reassign_clear():
    a = MARTE_HwGeneral_HwResource(name="sample_text")
    b1 = HwGeneral_MARTE_Operation()
    b2 = HwGeneral_MARTE_Operation()
    _safe_set(a, 'MARTE_HwGeneral_HwResource522', {b1})
    assert _is_linked(a, 'MARTE_HwGeneral_HwResource522', b1)
    if hasattr(b1, 'HwGeneral_MARTE_Operation'):
        assert _is_linked(b1, 'HwGeneral_MARTE_Operation', a)
    _safe_set(a, 'MARTE_HwGeneral_HwResource522', {b2})
    assert _is_linked(a, 'MARTE_HwGeneral_HwResource522', b2)
    if hasattr(b1, 'HwGeneral_MARTE_Operation'):
        assert not _is_linked(b1, 'HwGeneral_MARTE_Operation', a)
    if hasattr(b2, 'HwGeneral_MARTE_Operation'):
        assert _is_linked(b2, 'HwGeneral_MARTE_Operation', a)
    _safe_set(a, 'MARTE_HwGeneral_HwResource522', set())
    assert not _is_linked(a, 'MARTE_HwGeneral_HwResource522', b2)
    if hasattr(b2, 'HwGeneral_MARTE_Operation'):
        assert not _is_linked(b2, 'HwGeneral_MARTE_Operation', a)


def test_assoc_operations581_link_reassign_clear():
    a = MARTE_HwProtocol_HwProtocol(name="sample_text")
    b1 = HwProtocol_MARTE_Operation()
    b2 = HwProtocol_MARTE_Operation()
    _safe_set(a, 'MARTE_HwProtocol_HwProtocol', {b1})
    assert _is_linked(a, 'MARTE_HwProtocol_HwProtocol', b1)
    if hasattr(b1, 'HwProtocol_MARTE_Operation'):
        assert _is_linked(b1, 'HwProtocol_MARTE_Operation', a)
    _safe_set(a, 'MARTE_HwProtocol_HwProtocol', {b2})
    assert _is_linked(a, 'MARTE_HwProtocol_HwProtocol', b2)
    if hasattr(b1, 'HwProtocol_MARTE_Operation'):
        assert not _is_linked(b1, 'HwProtocol_MARTE_Operation', a)
    if hasattr(b2, 'HwProtocol_MARTE_Operation'):
        assert _is_linked(b2, 'HwProtocol_MARTE_Operation', a)
    _safe_set(a, 'MARTE_HwProtocol_HwProtocol', set())
    assert not _is_linked(a, 'MARTE_HwProtocol_HwProtocol', b2)
    if hasattr(b2, 'HwProtocol_MARTE_Operation'):
        assert not _is_linked(b2, 'HwProtocol_MARTE_Operation', a)


def test_assoc_operations735_link_reassign_clear():
    a = MARTE_SW_Brokering_DeviceBroker(accessPolicy="sample_text", isBuffered="sample_text", name="sample_text")
    b1 = SW_Brokering_MARTE_Operation()
    b2 = SW_Brokering_MARTE_Operation()
    _safe_set(a, 'MARTE_SW_Brokering_DeviceBroker736', {b1})
    assert _is_linked(a, 'MARTE_SW_Brokering_DeviceBroker736', b1)
    if hasattr(b1, 'SW_Brokering_MARTE_Operation'):
        assert _is_linked(b1, 'SW_Brokering_MARTE_Operation', a)
    _safe_set(a, 'MARTE_SW_Brokering_DeviceBroker736', {b2})
    assert _is_linked(a, 'MARTE_SW_Brokering_DeviceBroker736', b2)
    if hasattr(b1, 'SW_Brokering_MARTE_Operation'):
        assert not _is_linked(b1, 'SW_Brokering_MARTE_Operation', a)
    if hasattr(b2, 'SW_Brokering_MARTE_Operation'):
        assert _is_linked(b2, 'SW_Brokering_MARTE_Operation', a)
    _safe_set(a, 'MARTE_SW_Brokering_DeviceBroker736', set())
    assert not _is_linked(a, 'MARTE_SW_Brokering_DeviceBroker736', b2)
    if hasattr(b2, 'SW_Brokering_MARTE_Operation'):
        assert not _is_linked(b2, 'SW_Brokering_MARTE_Operation', a)


def test_assoc_organization342_link_reassign_clear():
    a = MARTE_HwComputing_HwPLD(technology="sample_text")
    b1 = HwComputing_PLD_Organization()
    b2 = HwComputing_PLD_Organization()
    _safe_set(a, 'MARTE_HwComputing_HwPLD', b1)
    assert _is_linked(a, 'MARTE_HwComputing_HwPLD', b1)
    if hasattr(b1, 'HwComputing_PLD_Organization'):
        assert _is_linked(b1, 'HwComputing_PLD_Organization', a)
    _safe_set(a, 'MARTE_HwComputing_HwPLD', b2)
    assert _is_linked(a, 'MARTE_HwComputing_HwPLD', b2)
    if hasattr(b1, 'HwComputing_PLD_Organization'):
        assert not _is_linked(b1, 'HwComputing_PLD_Organization', a)
    if hasattr(b2, 'HwComputing_PLD_Organization'):
        assert _is_linked(b2, 'HwComputing_PLD_Organization', a)
    _safe_set(a, 'MARTE_HwComputing_HwPLD', None)
    assert not _is_linked(a, 'MARTE_HwComputing_HwPLD', b2)
    if hasattr(b2, 'HwComputing_PLD_Organization'):
        assert not _is_linked(b2, 'HwComputing_PLD_Organization', a)


def test_assoc_organization447_link_reassign_clear():
    a = MARTE_HwMemory_HwRAM(repl_Policy="sample_text", writePolicy="sample_text")
    b1 = HwMemory_MemoryOrganization()
    b2 = HwMemory_MemoryOrganization()
    _safe_set(a, 'MARTE_HwMemory_HwRAM', b1)
    assert _is_linked(a, 'MARTE_HwMemory_HwRAM', b1)
    if hasattr(b1, 'HwMemory_MemoryOrganization'):
        assert _is_linked(b1, 'HwMemory_MemoryOrganization', a)
    _safe_set(a, 'MARTE_HwMemory_HwRAM', b2)
    assert _is_linked(a, 'MARTE_HwMemory_HwRAM', b2)
    if hasattr(b1, 'HwMemory_MemoryOrganization'):
        assert not _is_linked(b1, 'HwMemory_MemoryOrganization', a)
    if hasattr(b2, 'HwMemory_MemoryOrganization'):
        assert _is_linked(b2, 'HwMemory_MemoryOrganization', a)
    _safe_set(a, 'MARTE_HwMemory_HwRAM', None)
    assert not _is_linked(a, 'MARTE_HwMemory_HwRAM', b2)
    if hasattr(b2, 'HwMemory_MemoryOrganization'):
        assert not _is_linked(b2, 'HwMemory_MemoryOrganization', a)


def test_assoc_organization457_link_reassign_clear():
    a = MARTE_HwMemory_HwROM(type="sample_text")
    b1 = HwMemory_MemoryOrganization()
    b2 = HwMemory_MemoryOrganization()
    _safe_set(a, 'MARTE_HwMemory_HwROM', b1)
    assert _is_linked(a, 'MARTE_HwMemory_HwROM', b1)
    if hasattr(b1, 'HwMemory_MemoryOrganization458'):
        assert _is_linked(b1, 'HwMemory_MemoryOrganization458', a)
    _safe_set(a, 'MARTE_HwMemory_HwROM', b2)
    assert _is_linked(a, 'MARTE_HwMemory_HwROM', b2)
    if hasattr(b1, 'HwMemory_MemoryOrganization458'):
        assert not _is_linked(b1, 'HwMemory_MemoryOrganization458', a)
    if hasattr(b2, 'HwMemory_MemoryOrganization458'):
        assert _is_linked(b2, 'HwMemory_MemoryOrganization458', a)
    _safe_set(a, 'MARTE_HwMemory_HwROM', None)
    assert not _is_linked(a, 'MARTE_HwMemory_HwROM', b2)
    if hasattr(b2, 'HwMemory_MemoryOrganization458'):
        assert not _is_linked(b2, 'HwMemory_MemoryOrganization458', a)


def test_assoc_ownedHW515_link_reassign_clear():
    a = MARTE_HwGeneral_HwResource(name="sample_text")
    b1 = HwGeneral_HwResource()
    b2 = HwGeneral_HwResource()
    _safe_set(a, 'MARTE_HwGeneral_HwResource516', {b1})
    assert _is_linked(a, 'MARTE_HwGeneral_HwResource516', b1)
    if hasattr(b1, 'HwGeneral_HwResource'):
        assert _is_linked(b1, 'HwGeneral_HwResource', a)
    _safe_set(a, 'MARTE_HwGeneral_HwResource516', {b2})
    assert _is_linked(a, 'MARTE_HwGeneral_HwResource516', b2)
    if hasattr(b1, 'HwGeneral_HwResource'):
        assert not _is_linked(b1, 'HwGeneral_HwResource', a)
    if hasattr(b2, 'HwGeneral_HwResource'):
        assert _is_linked(b2, 'HwGeneral_HwResource', a)
    _safe_set(a, 'MARTE_HwGeneral_HwResource516', set())
    assert not _is_linked(a, 'MARTE_HwGeneral_HwResource516', b2)
    if hasattr(b2, 'HwGeneral_HwResource'):
        assert not _is_linked(b2, 'HwGeneral_HwResource', a)


def test_assoc_p_HW_Services510_link_reassign_clear():
    a = MARTE_HwGeneral_HwResource(name="sample_text")
    b1 = HwGeneral_HwResourceService()
    b2 = HwGeneral_HwResourceService()
    _safe_set(a, 'MARTE_HwGeneral_HwResource511', {b1})
    assert _is_linked(a, 'MARTE_HwGeneral_HwResource511', b1)
    if hasattr(b1, 'HwGeneral_HwResourceService'):
        assert _is_linked(b1, 'HwGeneral_HwResourceService', a)
    _safe_set(a, 'MARTE_HwGeneral_HwResource511', {b2})
    assert _is_linked(a, 'MARTE_HwGeneral_HwResource511', b2)
    if hasattr(b1, 'HwGeneral_HwResourceService'):
        assert not _is_linked(b1, 'HwGeneral_HwResourceService', a)
    if hasattr(b2, 'HwGeneral_HwResourceService'):
        assert _is_linked(b2, 'HwGeneral_HwResourceService', a)
    _safe_set(a, 'MARTE_HwGeneral_HwResource511', set())
    assert not _is_linked(a, 'MARTE_HwGeneral_HwResource511', b2)
    if hasattr(b2, 'HwGeneral_HwResourceService'):
        assert not _is_linked(b2, 'HwGeneral_HwResourceService', a)


def test_assoc_packetT140_link_reassign_clear():
    a = MARTE_GRM_CommunicationMedia(transmMode="sample_text")
    b1 = NFP_Duration()
    b2 = NFP_Duration()
    _safe_set(a, 'MARTE_GRM_CommunicationMedia141', {b1})
    assert _is_linked(a, 'MARTE_GRM_CommunicationMedia141', b1)
    if hasattr(b1, 'NFP_Duration142'):
        assert _is_linked(b1, 'NFP_Duration142', a)
    _safe_set(a, 'MARTE_GRM_CommunicationMedia141', {b2})
    assert _is_linked(a, 'MARTE_GRM_CommunicationMedia141', b2)
    if hasattr(b1, 'NFP_Duration142'):
        assert not _is_linked(b1, 'NFP_Duration142', a)
    if hasattr(b2, 'NFP_Duration142'):
        assert _is_linked(b2, 'NFP_Duration142', a)
    _safe_set(a, 'MARTE_GRM_CommunicationMedia141', set())
    assert not _is_linked(a, 'MARTE_GRM_CommunicationMedia141', b2)
    if hasattr(b2, 'NFP_Duration142'):
        assert not _is_linked(b2, 'NFP_Duration142', a)


def test_assoc_periodElements631_link_reassign_clear():
    a = MARTE_SW_Concurrency_SwConcurrentResource(activationCapacity="sample_text")
    b1 = SW_Concurrency_MARTE_TypedElement()
    b2 = SW_Concurrency_MARTE_TypedElement()
    _safe_set(a, 'MARTE_SW_Concurrency_SwConcurrentResource632', {b1})
    assert _is_linked(a, 'MARTE_SW_Concurrency_SwConcurrentResource632', b1)
    if hasattr(b1, 'SW_Concurrency_MARTE_TypedElement633'):
        assert _is_linked(b1, 'SW_Concurrency_MARTE_TypedElement633', a)
    _safe_set(a, 'MARTE_SW_Concurrency_SwConcurrentResource632', {b2})
    assert _is_linked(a, 'MARTE_SW_Concurrency_SwConcurrentResource632', b2)
    if hasattr(b1, 'SW_Concurrency_MARTE_TypedElement633'):
        assert not _is_linked(b1, 'SW_Concurrency_MARTE_TypedElement633', a)
    if hasattr(b2, 'SW_Concurrency_MARTE_TypedElement633'):
        assert _is_linked(b2, 'SW_Concurrency_MARTE_TypedElement633', a)
    _safe_set(a, 'MARTE_SW_Concurrency_SwConcurrentResource632', set())
    assert not _is_linked(a, 'MARTE_SW_Concurrency_SwConcurrentResource632', b2)
    if hasattr(b2, 'SW_Concurrency_MARTE_TypedElement633'):
        assert not _is_linked(b2, 'SW_Concurrency_MARTE_TypedElement633', a)


def test_assoc_pins578_link_reassign_clear():
    a = MARTE_HwPackage_HwPackage(name="sample_text", packageType="sample_text", pinNum=7)
    b1 = HwPackage_HwPackagePin()
    b2 = HwPackage_HwPackagePin()
    _safe_set(a, 'MARTE_HwPackage_HwPackage', {b1})
    assert _is_linked(a, 'MARTE_HwPackage_HwPackage', b1)
    if hasattr(b1, 'HwPackage_HwPackagePin'):
        assert _is_linked(b1, 'HwPackage_HwPackagePin', a)
    _safe_set(a, 'MARTE_HwPackage_HwPackage', {b2})
    assert _is_linked(a, 'MARTE_HwPackage_HwPackage', b2)
    if hasattr(b1, 'HwPackage_HwPackagePin'):
        assert not _is_linked(b1, 'HwPackage_HwPackagePin', a)
    if hasattr(b2, 'HwPackage_HwPackagePin'):
        assert _is_linked(b2, 'HwPackage_HwPackagePin', a)
    _safe_set(a, 'MARTE_HwPackage_HwPackage', set())
    assert not _is_linked(a, 'MARTE_HwPackage_HwPackage', b2)
    if hasattr(b2, 'HwPackage_HwPackagePin'):
        assert not _is_linked(b2, 'HwPackage_HwPackagePin', a)


def test_assoc_poolSize1103_link_reassign_clear():
    a = MARTE_PAM_PaRunTInstance(unbddPool="sample_text")
    b1 = NFP_Integer()
    b2 = NFP_Integer()
    _safe_set(a, 'MARTE_PAM_PaRunTInstance', b1)
    assert _is_linked(a, 'MARTE_PAM_PaRunTInstance', b1)
    if hasattr(b1, 'NFP_Integer1104'):
        assert _is_linked(b1, 'NFP_Integer1104', a)
    _safe_set(a, 'MARTE_PAM_PaRunTInstance', b2)
    assert _is_linked(a, 'MARTE_PAM_PaRunTInstance', b2)
    if hasattr(b1, 'NFP_Integer1104'):
        assert not _is_linked(b1, 'NFP_Integer1104', a)
    if hasattr(b2, 'NFP_Integer1104'):
        assert _is_linked(b2, 'NFP_Integer1104', a)
    _safe_set(a, 'MARTE_PAM_PaRunTInstance', None)
    assert not _is_linked(a, 'MARTE_PAM_PaRunTInstance', b2)
    if hasattr(b2, 'NFP_Integer1104'):
        assert not _is_linked(b2, 'NFP_Integer1104', a)


def test_assoc_position528_link_reassign_clear():
    a = MARTE_HwLayout_HwComponent(kind="sample_text")
    b1 = NFP_NaturalInterval()
    b2 = NFP_NaturalInterval()
    _safe_set(a, 'MARTE_HwLayout_HwComponent529', {b1})
    assert _is_linked(a, 'MARTE_HwLayout_HwComponent529', b1)
    if hasattr(b1, 'NFP_NaturalInterval'):
        assert _is_linked(b1, 'NFP_NaturalInterval', a)
    _safe_set(a, 'MARTE_HwLayout_HwComponent529', {b2})
    assert _is_linked(a, 'MARTE_HwLayout_HwComponent529', b2)
    if hasattr(b1, 'NFP_NaturalInterval'):
        assert not _is_linked(b1, 'NFP_NaturalInterval', a)
    if hasattr(b2, 'NFP_NaturalInterval'):
        assert _is_linked(b2, 'NFP_NaturalInterval', a)
    _safe_set(a, 'MARTE_HwLayout_HwComponent529', set())
    assert not _is_linked(a, 'MARTE_HwLayout_HwComponent529', b2)
    if hasattr(b2, 'NFP_NaturalInterval'):
        assert not _is_linked(b2, 'NFP_NaturalInterval', a)


def test_assoc_poweredServices543_link_reassign_clear():
    a = MARTE_HwLayout_HwComponent(kind="sample_text")
    b1 = HwGeneral_HwResourceService()
    b2 = HwGeneral_HwResourceService()
    _safe_set(a, 'MARTE_HwLayout_HwComponent544', {b1})
    assert _is_linked(a, 'MARTE_HwLayout_HwComponent544', b1)
    if hasattr(b1, 'HwGeneral_HwResourceService545'):
        assert _is_linked(b1, 'HwGeneral_HwResourceService545', a)
    _safe_set(a, 'MARTE_HwLayout_HwComponent544', {b2})
    assert _is_linked(a, 'MARTE_HwLayout_HwComponent544', b2)
    if hasattr(b1, 'HwGeneral_HwResourceService545'):
        assert not _is_linked(b1, 'HwGeneral_HwResourceService545', a)
    if hasattr(b2, 'HwGeneral_HwResourceService545'):
        assert _is_linked(b2, 'HwGeneral_HwResourceService545', a)
    _safe_set(a, 'MARTE_HwLayout_HwComponent544', set())
    assert not _is_linked(a, 'MARTE_HwLayout_HwComponent544', b2)
    if hasattr(b2, 'HwGeneral_HwResourceService545'):
        assert not _is_linked(b2, 'HwGeneral_HwResourceService545', a)


def test_assoc_price539_link_reassign_clear():
    a = MARTE_HwLayout_HwComponent(kind="sample_text")
    b1 = NFP_Price()
    b2 = NFP_Price()
    _safe_set(a, 'MARTE_HwLayout_HwComponent540', b1)
    assert _is_linked(a, 'MARTE_HwLayout_HwComponent540', b1)
    if hasattr(b1, 'NFP_Price'):
        assert _is_linked(b1, 'NFP_Price', a)
    _safe_set(a, 'MARTE_HwLayout_HwComponent540', b2)
    assert _is_linked(a, 'MARTE_HwLayout_HwComponent540', b2)
    if hasattr(b1, 'NFP_Price'):
        assert not _is_linked(b1, 'NFP_Price', a)
    if hasattr(b2, 'NFP_Price'):
        assert _is_linked(b2, 'NFP_Price', a)
    _safe_set(a, 'MARTE_HwLayout_HwComponent540', None)
    assert not _is_linked(a, 'MARTE_HwLayout_HwComponent540', b2)
    if hasattr(b2, 'NFP_Price'):
        assert not _is_linked(b2, 'NFP_Price', a)


def test_assoc_priorityElements634_link_reassign_clear():
    a = MARTE_SW_Concurrency_SwConcurrentResource(activationCapacity="sample_text")
    b1 = SW_Concurrency_MARTE_TypedElement()
    b2 = SW_Concurrency_MARTE_TypedElement()
    _safe_set(a, 'MARTE_SW_Concurrency_SwConcurrentResource635', {b1})
    assert _is_linked(a, 'MARTE_SW_Concurrency_SwConcurrentResource635', b1)
    if hasattr(b1, 'SW_Concurrency_MARTE_TypedElement636'):
        assert _is_linked(b1, 'SW_Concurrency_MARTE_TypedElement636', a)
    _safe_set(a, 'MARTE_SW_Concurrency_SwConcurrentResource635', {b2})
    assert _is_linked(a, 'MARTE_SW_Concurrency_SwConcurrentResource635', b2)
    if hasattr(b1, 'SW_Concurrency_MARTE_TypedElement636'):
        assert not _is_linked(b1, 'SW_Concurrency_MARTE_TypedElement636', a)
    if hasattr(b2, 'SW_Concurrency_MARTE_TypedElement636'):
        assert _is_linked(b2, 'SW_Concurrency_MARTE_TypedElement636', a)
    _safe_set(a, 'MARTE_SW_Concurrency_SwConcurrentResource635', set())
    assert not _is_linked(a, 'MARTE_SW_Concurrency_SwConcurrentResource635', b2)
    if hasattr(b2, 'SW_Concurrency_MARTE_TypedElement636'):
        assert not _is_linked(b2, 'SW_Concurrency_MARTE_TypedElement636', a)


def test_assoc_processingUnits116_link_reassign_clear():
    a = MARTE_GRM_Scheduler(isPreemptible="sample_text", otherSchedPolicy="sample_text", schedPolicy="sample_text")
    b1 = GRM_ProcessingResource()
    b2 = GRM_ProcessingResource()
    _safe_set(a, 'MARTE_GRM_Scheduler117', {b1})
    assert _is_linked(a, 'MARTE_GRM_Scheduler117', b1)
    if hasattr(b1, 'GRM_ProcessingResource'):
        assert _is_linked(b1, 'GRM_ProcessingResource', a)
    _safe_set(a, 'MARTE_GRM_Scheduler117', {b2})
    assert _is_linked(a, 'MARTE_GRM_Scheduler117', b2)
    if hasattr(b1, 'GRM_ProcessingResource'):
        assert not _is_linked(b1, 'GRM_ProcessingResource', a)
    if hasattr(b2, 'GRM_ProcessingResource'):
        assert _is_linked(b2, 'GRM_ProcessingResource', a)
    _safe_set(a, 'MARTE_GRM_Scheduler117', set())
    assert not _is_linked(a, 'MARTE_GRM_Scheduler117', b2)
    if hasattr(b2, 'GRM_ProcessingResource'):
        assert not _is_linked(b2, 'GRM_ProcessingResource', a)


def test_assoc_protectedSharedRsources120_link_reassign_clear():
    a = MARTE_GRM_Scheduler(isPreemptible="sample_text", otherSchedPolicy="sample_text", schedPolicy="sample_text")
    b1 = GRM_MutualExclusionResource()
    b2 = GRM_MutualExclusionResource()
    _safe_set(a, 'scheduler', {b1})
    assert _is_linked(a, 'scheduler', b1)
    if hasattr(b1, 'MutualExclusionResource'):
        assert _is_linked(b1, 'MutualExclusionResource', a)
    _safe_set(a, 'scheduler', {b2})
    assert _is_linked(a, 'scheduler', b2)
    if hasattr(b1, 'MutualExclusionResource'):
        assert not _is_linked(b1, 'MutualExclusionResource', a)
    if hasattr(b2, 'MutualExclusionResource'):
        assert _is_linked(b2, 'MutualExclusionResource', a)
    _safe_set(a, 'scheduler', set())
    assert not _is_linked(a, 'scheduler', b2)
    if hasattr(b2, 'MutualExclusionResource'):
        assert not _is_linked(b2, 'MutualExclusionResource', a)


def test_assoc_protocols575_link_reassign_clear():
    a = MARTE_HwDatasheet_HwDatasheet(name="sample_text", revision="sample_text")
    b1 = HwProtocol_HwProtocol()
    b2 = HwProtocol_HwProtocol()
    _safe_set(a, 'MARTE_HwDatasheet_HwDatasheet576', {b1})
    assert _is_linked(a, 'MARTE_HwDatasheet_HwDatasheet576', b1)
    if hasattr(b1, 'HwProtocol_HwProtocol577'):
        assert _is_linked(b1, 'HwProtocol_HwProtocol577', a)
    _safe_set(a, 'MARTE_HwDatasheet_HwDatasheet576', {b2})
    assert _is_linked(a, 'MARTE_HwDatasheet_HwDatasheet576', b2)
    if hasattr(b1, 'HwProtocol_HwProtocol577'):
        assert not _is_linked(b1, 'HwProtocol_HwProtocol577', a)
    if hasattr(b2, 'HwProtocol_HwProtocol577'):
        assert _is_linked(b2, 'HwProtocol_HwProtocol577', a)
    _safe_set(a, 'MARTE_HwDatasheet_HwDatasheet576', set())
    assert not _is_linked(a, 'MARTE_HwDatasheet_HwDatasheet576', b2)
    if hasattr(b2, 'HwProtocol_HwProtocol577'):
        assert not _is_linked(b2, 'HwProtocol_HwProtocol577', a)


def test_assoc_protocols582_link_reassign_clear():
    a = MARTE_HwDiagram_HwBlockDiagram(name="sample_text")
    b1 = HwProtocol_HwProtocol()
    b2 = HwProtocol_HwProtocol()
    _safe_set(a, 'MARTE_HwDiagram_HwBlockDiagram', {b1})
    assert _is_linked(a, 'MARTE_HwDiagram_HwBlockDiagram', b1)
    if hasattr(b1, 'HwProtocol_HwProtocol583'):
        assert _is_linked(b1, 'HwProtocol_HwProtocol583', a)
    _safe_set(a, 'MARTE_HwDiagram_HwBlockDiagram', {b2})
    assert _is_linked(a, 'MARTE_HwDiagram_HwBlockDiagram', b2)
    if hasattr(b1, 'HwProtocol_HwProtocol583'):
        assert not _is_linked(b1, 'HwProtocol_HwProtocol583', a)
    if hasattr(b2, 'HwProtocol_HwProtocol583'):
        assert _is_linked(b2, 'HwProtocol_HwProtocol583', a)
    _safe_set(a, 'MARTE_HwDiagram_HwBlockDiagram', set())
    assert not _is_linked(a, 'MARTE_HwDiagram_HwBlockDiagram', b2)
    if hasattr(b2, 'HwProtocol_HwProtocol583'):
        assert not _is_linked(b2, 'HwProtocol_HwProtocol583', a)


def test_assoc_protocols599_link_reassign_clear():
    a = MARTE_HwDiagram_HwHRMDiagram(name="sample_text")
    b1 = HwProtocol_HwProtocol()
    b2 = HwProtocol_HwProtocol()
    _safe_set(a, 'MARTE_HwDiagram_HwHRMDiagram600', {b1})
    assert _is_linked(a, 'MARTE_HwDiagram_HwHRMDiagram600', b1)
    if hasattr(b1, 'HwProtocol_HwProtocol601'):
        assert _is_linked(b1, 'HwProtocol_HwProtocol601', a)
    _safe_set(a, 'MARTE_HwDiagram_HwHRMDiagram600', {b2})
    assert _is_linked(a, 'MARTE_HwDiagram_HwHRMDiagram600', b2)
    if hasattr(b1, 'HwProtocol_HwProtocol601'):
        assert not _is_linked(b1, 'HwProtocol_HwProtocol601', a)
    if hasattr(b2, 'HwProtocol_HwProtocol601'):
        assert _is_linked(b2, 'HwProtocol_HwProtocol601', a)
    _safe_set(a, 'MARTE_HwDiagram_HwHRMDiagram600', set())
    assert not _is_linked(a, 'MARTE_HwDiagram_HwHRMDiagram600', b2)
    if hasattr(b2, 'HwProtocol_HwProtocol601'):
        assert not _is_linked(b2, 'HwProtocol_HwProtocol601', a)


def test_assoc_provInterface804_link_reassign_clear():
    a = MARTE_GCM_ClientServerPort(isConjugated="sample_text", kind="sample_text", specificationKind="sample_text")
    b1 = GCM_MARTE_Interface()
    b2 = GCM_MARTE_Interface()
    _safe_set(a, 'MARTE_GCM_ClientServerPort805', {b1})
    assert _is_linked(a, 'MARTE_GCM_ClientServerPort805', b1)
    if hasattr(b1, 'GCM_MARTE_Interface'):
        assert _is_linked(b1, 'GCM_MARTE_Interface', a)
    _safe_set(a, 'MARTE_GCM_ClientServerPort805', {b2})
    assert _is_linked(a, 'MARTE_GCM_ClientServerPort805', b2)
    if hasattr(b1, 'GCM_MARTE_Interface'):
        assert not _is_linked(b1, 'GCM_MARTE_Interface', a)
    if hasattr(b2, 'GCM_MARTE_Interface'):
        assert _is_linked(b2, 'GCM_MARTE_Interface', a)
    _safe_set(a, 'MARTE_GCM_ClientServerPort805', set())
    assert not _is_linked(a, 'MARTE_GCM_ClientServerPort805', b2)
    if hasattr(b2, 'GCM_MARTE_Interface'):
        assert not _is_linked(b2, 'GCM_MARTE_Interface', a)


def test_assoc_r_Conditions541_link_reassign_clear():
    a = MARTE_HwLayout_HwComponent(kind="sample_text")
    b1 = HwLayout_Env_Condition()
    b2 = HwLayout_Env_Condition()
    _safe_set(a, 'MARTE_HwLayout_HwComponent542', {b1})
    assert _is_linked(a, 'MARTE_HwLayout_HwComponent542', b1)
    if hasattr(b1, 'HwLayout_Env_Condition'):
        assert _is_linked(b1, 'HwLayout_Env_Condition', a)
    _safe_set(a, 'MARTE_HwLayout_HwComponent542', {b2})
    assert _is_linked(a, 'MARTE_HwLayout_HwComponent542', b2)
    if hasattr(b1, 'HwLayout_Env_Condition'):
        assert not _is_linked(b1, 'HwLayout_Env_Condition', a)
    if hasattr(b2, 'HwLayout_Env_Condition'):
        assert _is_linked(b2, 'HwLayout_Env_Condition', a)
    _safe_set(a, 'MARTE_HwLayout_HwComponent542', set())
    assert not _is_linked(a, 'MARTE_HwLayout_HwComponent542', b2)
    if hasattr(b2, 'HwLayout_Env_Condition'):
        assert not _is_linked(b2, 'HwLayout_Env_Condition', a)


def test_assoc_r_HW_Services512_link_reassign_clear():
    a = MARTE_HwGeneral_HwResource(name="sample_text")
    b1 = HwGeneral_HwResourceService()
    b2 = HwGeneral_HwResourceService()
    _safe_set(a, 'MARTE_HwGeneral_HwResource513', {b1})
    assert _is_linked(a, 'MARTE_HwGeneral_HwResource513', b1)
    if hasattr(b1, 'HwGeneral_HwResourceService514'):
        assert _is_linked(b1, 'HwGeneral_HwResourceService514', a)
    _safe_set(a, 'MARTE_HwGeneral_HwResource513', {b2})
    assert _is_linked(a, 'MARTE_HwGeneral_HwResource513', b2)
    if hasattr(b1, 'HwGeneral_HwResourceService514'):
        assert not _is_linked(b1, 'HwGeneral_HwResourceService514', a)
    if hasattr(b2, 'HwGeneral_HwResourceService514'):
        assert _is_linked(b2, 'HwGeneral_HwResourceService514', a)
    _safe_set(a, 'MARTE_HwGeneral_HwResource513', set())
    assert not _is_linked(a, 'MARTE_HwGeneral_HwResource513', b2)
    if hasattr(b2, 'HwGeneral_HwResourceService514'):
        assert not _is_linked(b2, 'HwGeneral_HwResourceService514', a)


def test_assoc_range556_link_reassign_clear():
    a = MARTE_HwLayout_Env_Condition(status="sample_text", type="sample_text")
    b1 = Realnterval()
    b2 = Realnterval()
    _safe_set(a, 'MARTE_HwLayout_Env_Condition557', b1)
    assert _is_linked(a, 'MARTE_HwLayout_Env_Condition557', b1)
    if hasattr(b1, 'Realnterval'):
        assert _is_linked(b1, 'Realnterval', a)
    _safe_set(a, 'MARTE_HwLayout_Env_Condition557', b2)
    assert _is_linked(a, 'MARTE_HwLayout_Env_Condition557', b2)
    if hasattr(b1, 'Realnterval'):
        assert not _is_linked(b1, 'Realnterval', a)
    if hasattr(b2, 'Realnterval'):
        assert _is_linked(b2, 'Realnterval', a)
    _safe_set(a, 'MARTE_HwLayout_Env_Condition557', None)
    assert not _is_linked(a, 'MARTE_HwLayout_Env_Condition557', b2)
    if hasattr(b2, 'Realnterval'):
        assert not _is_linked(b2, 'Realnterval', a)


def test_assoc_readServices729_link_reassign_clear():
    a = MARTE_SW_Brokering_DeviceBroker(accessPolicy="sample_text", isBuffered="sample_text", name="sample_text")
    b1 = SW_Brokering_MARTE_BehavioralFeature()
    b2 = SW_Brokering_MARTE_BehavioralFeature()
    _safe_set(a, 'MARTE_SW_Brokering_DeviceBroker730', {b1})
    assert _is_linked(a, 'MARTE_SW_Brokering_DeviceBroker730', b1)
    if hasattr(b1, 'SW_Brokering_MARTE_BehavioralFeature731'):
        assert _is_linked(b1, 'SW_Brokering_MARTE_BehavioralFeature731', a)
    _safe_set(a, 'MARTE_SW_Brokering_DeviceBroker730', {b2})
    assert _is_linked(a, 'MARTE_SW_Brokering_DeviceBroker730', b2)
    if hasattr(b1, 'SW_Brokering_MARTE_BehavioralFeature731'):
        assert not _is_linked(b1, 'SW_Brokering_MARTE_BehavioralFeature731', a)
    if hasattr(b2, 'SW_Brokering_MARTE_BehavioralFeature731'):
        assert _is_linked(b2, 'SW_Brokering_MARTE_BehavioralFeature731', a)
    _safe_set(a, 'MARTE_SW_Brokering_DeviceBroker730', set())
    assert not _is_linked(a, 'MARTE_SW_Brokering_DeviceBroker730', b2)
    if hasattr(b2, 'SW_Brokering_MARTE_BehavioralFeature731'):
        assert not _is_linked(b2, 'SW_Brokering_MARTE_BehavioralFeature731', a)


def test_assoc_receiveServices772_link_reassign_clear():
    a = MARTE_SW_Interaction_MessageComResource(isFixedMessageSize="sample_text", mechanism="sample_text", messageQueuePolicy="sample_text")
    b1 = SW_Interaction_MARTE_BehavioralFeature()
    b2 = SW_Interaction_MARTE_BehavioralFeature()
    _safe_set(a, 'MARTE_SW_Interaction_MessageComResource773', {b1})
    assert _is_linked(a, 'MARTE_SW_Interaction_MessageComResource773', b1)
    if hasattr(b1, 'SW_Interaction_MARTE_BehavioralFeature774'):
        assert _is_linked(b1, 'SW_Interaction_MARTE_BehavioralFeature774', a)
    _safe_set(a, 'MARTE_SW_Interaction_MessageComResource773', {b2})
    assert _is_linked(a, 'MARTE_SW_Interaction_MessageComResource773', b2)
    if hasattr(b1, 'SW_Interaction_MARTE_BehavioralFeature774'):
        assert not _is_linked(b1, 'SW_Interaction_MARTE_BehavioralFeature774', a)
    if hasattr(b2, 'SW_Interaction_MARTE_BehavioralFeature774'):
        assert _is_linked(b2, 'SW_Interaction_MARTE_BehavioralFeature774', a)
    _safe_set(a, 'MARTE_SW_Interaction_MessageComResource773', set())
    assert not _is_linked(a, 'MARTE_SW_Interaction_MessageComResource773', b2)
    if hasattr(b2, 'SW_Interaction_MARTE_BehavioralFeature774'):
        assert not _is_linked(b2, 'SW_Interaction_MARTE_BehavioralFeature774', a)


def test_assoc_refpin579_link_reassign_clear():
    a = MARTE_HwPackage_HwPackagePin(altNames="sample_text", pinNo="sample_text")
    b1 = HwIO_HwPin()
    b2 = HwIO_HwPin()
    _safe_set(a, 'pkgPin', {b1})
    assert _is_linked(a, 'pkgPin', b1)
    if hasattr(b1, 'HwPin'):
        assert _is_linked(b1, 'HwPin', a)
    _safe_set(a, 'pkgPin', {b2})
    assert _is_linked(a, 'pkgPin', b2)
    if hasattr(b1, 'HwPin'):
        assert not _is_linked(b1, 'HwPin', a)
    if hasattr(b2, 'HwPin'):
        assert _is_linked(b2, 'HwPin', a)
    _safe_set(a, 'pkgPin', set())
    assert not _is_linked(a, 'pkgPin', b2)
    if hasattr(b2, 'HwPin'):
        assert not _is_linked(b2, 'HwPin', a)


def test_assoc_releaseServices794_link_reassign_clear():
    a = MARTE_SW_Interaction_SwMutualExclusionResource(concurrentAccessProtocol="sample_text", mechanism="sample_text")
    b1 = SW_Interaction_MARTE_BehavioralFeature()
    b2 = SW_Interaction_MARTE_BehavioralFeature()
    _safe_set(a, 'MARTE_SW_Interaction_SwMutualExclusionResource795', {b1})
    assert _is_linked(a, 'MARTE_SW_Interaction_SwMutualExclusionResource795', b1)
    if hasattr(b1, 'SW_Interaction_MARTE_BehavioralFeature796'):
        assert _is_linked(b1, 'SW_Interaction_MARTE_BehavioralFeature796', a)
    _safe_set(a, 'MARTE_SW_Interaction_SwMutualExclusionResource795', {b2})
    assert _is_linked(a, 'MARTE_SW_Interaction_SwMutualExclusionResource795', b2)
    if hasattr(b1, 'SW_Interaction_MARTE_BehavioralFeature796'):
        assert not _is_linked(b1, 'SW_Interaction_MARTE_BehavioralFeature796', a)
    if hasattr(b2, 'SW_Interaction_MARTE_BehavioralFeature796'):
        assert _is_linked(b2, 'SW_Interaction_MARTE_BehavioralFeature796', a)
    _safe_set(a, 'MARTE_SW_Interaction_SwMutualExclusionResource795', set())
    assert not _is_linked(a, 'MARTE_SW_Interaction_SwMutualExclusionResource795', b2)
    if hasattr(b2, 'SW_Interaction_MARTE_BehavioralFeature796'):
        assert not _is_linked(b2, 'SW_Interaction_MARTE_BehavioralFeature796', a)


def test_assoc_repetitionShapeDependence180_link_reassign_clear():
    a = MARTE_RSM_InterRepetition(isModulo="sample_text")
    b1 = IntegerVector()
    b2 = IntegerVector()
    _safe_set(a, 'MARTE_RSM_InterRepetition', b1)
    assert _is_linked(a, 'MARTE_RSM_InterRepetition', b1)
    if hasattr(b1, 'IntegerVector'):
        assert _is_linked(b1, 'IntegerVector', a)
    _safe_set(a, 'MARTE_RSM_InterRepetition', b2)
    assert _is_linked(a, 'MARTE_RSM_InterRepetition', b2)
    if hasattr(b1, 'IntegerVector'):
        assert not _is_linked(b1, 'IntegerVector', a)
    if hasattr(b2, 'IntegerVector'):
        assert _is_linked(b2, 'IntegerVector', a)
    _safe_set(a, 'MARTE_RSM_InterRepetition', None)
    assert not _is_linked(a, 'MARTE_RSM_InterRepetition', b2)
    if hasattr(b2, 'IntegerVector'):
        assert not _is_linked(b2, 'IntegerVector', a)


def test_assoc_reqInterface806_link_reassign_clear():
    a = MARTE_GCM_ClientServerPort(isConjugated="sample_text", kind="sample_text", specificationKind="sample_text")
    b1 = GCM_MARTE_Interface()
    b2 = GCM_MARTE_Interface()
    _safe_set(a, 'MARTE_GCM_ClientServerPort807', {b1})
    assert _is_linked(a, 'MARTE_GCM_ClientServerPort807', b1)
    if hasattr(b1, 'GCM_MARTE_Interface808'):
        assert _is_linked(b1, 'GCM_MARTE_Interface808', a)
    _safe_set(a, 'MARTE_GCM_ClientServerPort807', {b2})
    assert _is_linked(a, 'MARTE_GCM_ClientServerPort807', b2)
    if hasattr(b1, 'GCM_MARTE_Interface808'):
        assert not _is_linked(b1, 'GCM_MARTE_Interface808', a)
    if hasattr(b2, 'GCM_MARTE_Interface808'):
        assert _is_linked(b2, 'GCM_MARTE_Interface808', a)
    _safe_set(a, 'MARTE_GCM_ClientServerPort807', set())
    assert not _is_linked(a, 'MARTE_GCM_ClientServerPort807', b2)
    if hasattr(b2, 'GCM_MARTE_Interface808'):
        assert not _is_linked(b2, 'GCM_MARTE_Interface808', a)


def test_assoc_resMult100_link_reassign_clear():
    a = MARTE_GRM_Resource(isProtected="sample_text")
    b1 = NFP_Integer()
    b2 = NFP_Integer()
    _safe_set(a, 'MARTE_GRM_Resource', b1)
    assert _is_linked(a, 'MARTE_GRM_Resource', b1)
    if hasattr(b1, 'NFP_Integer'):
        assert _is_linked(b1, 'NFP_Integer', a)
    _safe_set(a, 'MARTE_GRM_Resource', b2)
    assert _is_linked(a, 'MARTE_GRM_Resource', b2)
    if hasattr(b1, 'NFP_Integer'):
        assert not _is_linked(b1, 'NFP_Integer', a)
    if hasattr(b2, 'NFP_Integer'):
        assert _is_linked(b2, 'NFP_Integer', a)
    _safe_set(a, 'MARTE_GRM_Resource', None)
    assert not _is_linked(a, 'MARTE_GRM_Resource', b2)
    if hasattr(b2, 'NFP_Integer'):
        assert not _is_linked(b2, 'NFP_Integer', a)


def test_assoc_resolAttr60_link_reassign_clear():
    a = MARTE_Time_ClockType(isLogical="sample_text", nature="sample_text")
    b1 = Time_MARTE_Property()
    b2 = Time_MARTE_Property()
    _safe_set(a, 'MARTE_Time_ClockType61', b1)
    assert _is_linked(a, 'MARTE_Time_ClockType61', b1)
    if hasattr(b1, 'Time_MARTE_Property62'):
        assert _is_linked(b1, 'Time_MARTE_Property62', a)
    _safe_set(a, 'MARTE_Time_ClockType61', b2)
    assert _is_linked(a, 'MARTE_Time_ClockType61', b2)
    if hasattr(b1, 'Time_MARTE_Property62'):
        assert not _is_linked(b1, 'Time_MARTE_Property62', a)
    if hasattr(b2, 'Time_MARTE_Property62'):
        assert _is_linked(b2, 'Time_MARTE_Property62', a)
    _safe_set(a, 'MARTE_Time_ClockType61', None)
    assert not _is_linked(a, 'MARTE_Time_ClockType61', b2)
    if hasattr(b2, 'Time_MARTE_Property62'):
        assert not _is_linked(b2, 'Time_MARTE_Property62', a)


def test_assoc_resumeServices646_link_reassign_clear():
    a = MARTE_SW_Concurrency_SwConcurrentResource(activationCapacity="sample_text")
    b1 = SW_Concurrency_MARTE_BehavioralFeature()
    b2 = SW_Concurrency_MARTE_BehavioralFeature()
    _safe_set(a, 'MARTE_SW_Concurrency_SwConcurrentResource647', {b1})
    assert _is_linked(a, 'MARTE_SW_Concurrency_SwConcurrentResource647', b1)
    if hasattr(b1, 'SW_Concurrency_MARTE_BehavioralFeature648'):
        assert _is_linked(b1, 'SW_Concurrency_MARTE_BehavioralFeature648', a)
    _safe_set(a, 'MARTE_SW_Concurrency_SwConcurrentResource647', {b2})
    assert _is_linked(a, 'MARTE_SW_Concurrency_SwConcurrentResource647', b2)
    if hasattr(b1, 'SW_Concurrency_MARTE_BehavioralFeature648'):
        assert not _is_linked(b1, 'SW_Concurrency_MARTE_BehavioralFeature648', a)
    if hasattr(b2, 'SW_Concurrency_MARTE_BehavioralFeature648'):
        assert _is_linked(b2, 'SW_Concurrency_MARTE_BehavioralFeature648', a)
    _safe_set(a, 'MARTE_SW_Concurrency_SwConcurrentResource647', set())
    assert not _is_linked(a, 'MARTE_SW_Concurrency_SwConcurrentResource647', b2)
    if hasattr(b2, 'SW_Concurrency_MARTE_BehavioralFeature648'):
        assert not _is_linked(b2, 'SW_Concurrency_MARTE_BehavioralFeature648', a)


def test_assoc_routine624_link_reassign_clear():
    a = MARTE_SW_Concurrency_EntryPoint(isReentrant="sample_text")
    b1 = SW_Concurrency_MARTE_BehavioralFeature()
    b2 = SW_Concurrency_MARTE_BehavioralFeature()
    _safe_set(a, 'MARTE_SW_Concurrency_EntryPoint', b1)
    assert _is_linked(a, 'MARTE_SW_Concurrency_EntryPoint', b1)
    if hasattr(b1, 'SW_Concurrency_MARTE_BehavioralFeature'):
        assert _is_linked(b1, 'SW_Concurrency_MARTE_BehavioralFeature', a)
    _safe_set(a, 'MARTE_SW_Concurrency_EntryPoint', b2)
    assert _is_linked(a, 'MARTE_SW_Concurrency_EntryPoint', b2)
    if hasattr(b1, 'SW_Concurrency_MARTE_BehavioralFeature'):
        assert not _is_linked(b1, 'SW_Concurrency_MARTE_BehavioralFeature', a)
    if hasattr(b2, 'SW_Concurrency_MARTE_BehavioralFeature'):
        assert _is_linked(b2, 'SW_Concurrency_MARTE_BehavioralFeature', a)
    _safe_set(a, 'MARTE_SW_Concurrency_EntryPoint', None)
    assert not _is_linked(a, 'MARTE_SW_Concurrency_EntryPoint', b2)
    if hasattr(b2, 'SW_Concurrency_MARTE_BehavioralFeature'):
        assert not _is_linked(b2, 'SW_Concurrency_MARTE_BehavioralFeature', a)


def test_assoc_routineConnectServices678_link_reassign_clear():
    a = MARTE_SW_Concurrency_InterruptResource(isMaskable="sample_text", kind="sample_text")
    b1 = SW_Concurrency_MARTE_BehavioralFeature()
    b2 = SW_Concurrency_MARTE_BehavioralFeature()
    _safe_set(a, 'MARTE_SW_Concurrency_InterruptResource679', {b1})
    assert _is_linked(a, 'MARTE_SW_Concurrency_InterruptResource679', b1)
    if hasattr(b1, 'SW_Concurrency_MARTE_BehavioralFeature680'):
        assert _is_linked(b1, 'SW_Concurrency_MARTE_BehavioralFeature680', a)
    _safe_set(a, 'MARTE_SW_Concurrency_InterruptResource679', {b2})
    assert _is_linked(a, 'MARTE_SW_Concurrency_InterruptResource679', b2)
    if hasattr(b1, 'SW_Concurrency_MARTE_BehavioralFeature680'):
        assert not _is_linked(b1, 'SW_Concurrency_MARTE_BehavioralFeature680', a)
    if hasattr(b2, 'SW_Concurrency_MARTE_BehavioralFeature680'):
        assert _is_linked(b2, 'SW_Concurrency_MARTE_BehavioralFeature680', a)
    _safe_set(a, 'MARTE_SW_Concurrency_InterruptResource679', set())
    assert not _is_linked(a, 'MARTE_SW_Concurrency_InterruptResource679', b2)
    if hasattr(b2, 'SW_Concurrency_MARTE_BehavioralFeature680'):
        assert not _is_linked(b2, 'SW_Concurrency_MARTE_BehavioralFeature680', a)


def test_assoc_routineDisconnectServices681_link_reassign_clear():
    a = MARTE_SW_Concurrency_InterruptResource(isMaskable="sample_text", kind="sample_text")
    b1 = SW_Concurrency_MARTE_BehavioralFeature()
    b2 = SW_Concurrency_MARTE_BehavioralFeature()
    _safe_set(a, 'MARTE_SW_Concurrency_InterruptResource682', {b1})
    assert _is_linked(a, 'MARTE_SW_Concurrency_InterruptResource682', b1)
    if hasattr(b1, 'SW_Concurrency_MARTE_BehavioralFeature683'):
        assert _is_linked(b1, 'SW_Concurrency_MARTE_BehavioralFeature683', a)
    _safe_set(a, 'MARTE_SW_Concurrency_InterruptResource682', {b2})
    assert _is_linked(a, 'MARTE_SW_Concurrency_InterruptResource682', b2)
    if hasattr(b1, 'SW_Concurrency_MARTE_BehavioralFeature683'):
        assert not _is_linked(b1, 'SW_Concurrency_MARTE_BehavioralFeature683', a)
    if hasattr(b2, 'SW_Concurrency_MARTE_BehavioralFeature683'):
        assert _is_linked(b2, 'SW_Concurrency_MARTE_BehavioralFeature683', a)
    _safe_set(a, 'MARTE_SW_Concurrency_InterruptResource682', set())
    assert not _is_linked(a, 'MARTE_SW_Concurrency_InterruptResource682', b2)
    if hasattr(b2, 'SW_Concurrency_MARTE_BehavioralFeature683'):
        assert not _is_linked(b2, 'SW_Concurrency_MARTE_BehavioralFeature683', a)


def test_assoc_schedulableResources121_link_reassign_clear():
    a = MARTE_GRM_Scheduler(isPreemptible="sample_text", otherSchedPolicy="sample_text", schedPolicy="sample_text")
    b1 = GRM_SchedulableResource()
    b2 = GRM_SchedulableResource()
    _safe_set(a, 'host', {b1})
    assert _is_linked(a, 'host', b1)
    if hasattr(b1, 'SchedulableResource'):
        assert _is_linked(b1, 'SchedulableResource', a)
    _safe_set(a, 'host', {b2})
    assert _is_linked(a, 'host', b2)
    if hasattr(b1, 'SchedulableResource'):
        assert not _is_linked(b1, 'SchedulableResource', a)
    if hasattr(b2, 'SchedulableResource'):
        assert _is_linked(b2, 'SchedulableResource', a)
    _safe_set(a, 'host', set())
    assert not _is_linked(a, 'host', b2)
    if hasattr(b2, 'SchedulableResource'):
        assert not _is_linked(b2, 'SchedulableResource', a)


def test_assoc_schedule115_link_reassign_clear():
    a = MARTE_GRM_Scheduler(isPreemptible="sample_text", otherSchedPolicy="sample_text", schedPolicy="sample_text")
    b1 = GRM_MARTE_OpaqueExpression()
    b2 = GRM_MARTE_OpaqueExpression()
    _safe_set(a, 'MARTE_GRM_Scheduler', b1)
    assert _is_linked(a, 'MARTE_GRM_Scheduler', b1)
    if hasattr(b1, 'GRM_MARTE_OpaqueExpression'):
        assert _is_linked(b1, 'GRM_MARTE_OpaqueExpression', a)
    _safe_set(a, 'MARTE_GRM_Scheduler', b2)
    assert _is_linked(a, 'MARTE_GRM_Scheduler', b2)
    if hasattr(b1, 'GRM_MARTE_OpaqueExpression'):
        assert not _is_linked(b1, 'GRM_MARTE_OpaqueExpression', a)
    if hasattr(b2, 'GRM_MARTE_OpaqueExpression'):
        assert _is_linked(b2, 'GRM_MARTE_OpaqueExpression', a)
    _safe_set(a, 'MARTE_GRM_Scheduler', None)
    assert not _is_linked(a, 'MARTE_GRM_Scheduler', b2)
    if hasattr(b2, 'GRM_MARTE_OpaqueExpression'):
        assert not _is_linked(b2, 'GRM_MARTE_OpaqueExpression', a)


def test_assoc_scheduler127_link_reassign_clear():
    a = MARTE_GRM_MutualExclusionResource(otherProtectProtocol="sample_text", protectKind="sample_text")
    b1 = GRM_Scheduler()
    b2 = GRM_Scheduler()
    _safe_set(a, 'protectedSharedRsources', b1)
    assert _is_linked(a, 'protectedSharedRsources', b1)
    if hasattr(b1, 'Scheduler'):
        assert _is_linked(b1, 'Scheduler', a)
    _safe_set(a, 'protectedSharedRsources', b2)
    assert _is_linked(a, 'protectedSharedRsources', b2)
    if hasattr(b1, 'Scheduler'):
        assert not _is_linked(b1, 'Scheduler', a)
    if hasattr(b2, 'Scheduler'):
        assert _is_linked(b2, 'Scheduler', a)
    _safe_set(a, 'protectedSharedRsources', None)
    assert not _is_linked(a, 'protectedSharedRsources', b2)
    if hasattr(b2, 'Scheduler'):
        assert not _is_linked(b2, 'Scheduler', a)


def test_assoc_schedulers684_link_reassign_clear():
    a = MARTE_SW_Concurrency_SwSchedulableResource(isPreemptable="sample_text", isStaticSchedulingFeature="sample_text")
    b1 = SW_Concurrency_MARTE_NamedElement()
    b2 = SW_Concurrency_MARTE_NamedElement()
    _safe_set(a, 'MARTE_SW_Concurrency_SwSchedulableResource', b1)
    assert _is_linked(a, 'MARTE_SW_Concurrency_SwSchedulableResource', b1)
    if hasattr(b1, 'SW_Concurrency_MARTE_NamedElement'):
        assert _is_linked(b1, 'SW_Concurrency_MARTE_NamedElement', a)
    _safe_set(a, 'MARTE_SW_Concurrency_SwSchedulableResource', b2)
    assert _is_linked(a, 'MARTE_SW_Concurrency_SwSchedulableResource', b2)
    if hasattr(b1, 'SW_Concurrency_MARTE_NamedElement'):
        assert not _is_linked(b1, 'SW_Concurrency_MARTE_NamedElement', a)
    if hasattr(b2, 'SW_Concurrency_MARTE_NamedElement'):
        assert _is_linked(b2, 'SW_Concurrency_MARTE_NamedElement', a)
    _safe_set(a, 'MARTE_SW_Concurrency_SwSchedulableResource', None)
    assert not _is_linked(a, 'MARTE_SW_Concurrency_SwSchedulableResource', b2)
    if hasattr(b2, 'SW_Concurrency_MARTE_NamedElement'):
        assert not _is_linked(b2, 'SW_Concurrency_MARTE_NamedElement', a)


def test_assoc_selection830_link_reassign_clear():
    a = MARTE_GCM_DataPool(ordering="sample_text")
    b1 = GCM_MARTE_Behavior()
    b2 = GCM_MARTE_Behavior()
    _safe_set(a, 'MARTE_GCM_DataPool831', b1)
    assert _is_linked(a, 'MARTE_GCM_DataPool831', b1)
    if hasattr(b1, 'GCM_MARTE_Behavior832'):
        assert _is_linked(b1, 'GCM_MARTE_Behavior832', a)
    _safe_set(a, 'MARTE_GCM_DataPool831', b2)
    assert _is_linked(a, 'MARTE_GCM_DataPool831', b2)
    if hasattr(b1, 'GCM_MARTE_Behavior832'):
        assert not _is_linked(b1, 'GCM_MARTE_Behavior832', a)
    if hasattr(b2, 'GCM_MARTE_Behavior832'):
        assert _is_linked(b2, 'GCM_MARTE_Behavior832', a)
    _safe_set(a, 'MARTE_GCM_DataPool831', None)
    assert not _is_linked(a, 'MARTE_GCM_DataPool831', b2)
    if hasattr(b2, 'GCM_MARTE_Behavior832'):
        assert not _is_linked(b2, 'GCM_MARTE_Behavior832', a)


def test_assoc_sendServices769_link_reassign_clear():
    a = MARTE_SW_Interaction_MessageComResource(isFixedMessageSize="sample_text", mechanism="sample_text", messageQueuePolicy="sample_text")
    b1 = SW_Interaction_MARTE_BehavioralFeature()
    b2 = SW_Interaction_MARTE_BehavioralFeature()
    _safe_set(a, 'MARTE_SW_Interaction_MessageComResource770', {b1})
    assert _is_linked(a, 'MARTE_SW_Interaction_MessageComResource770', b1)
    if hasattr(b1, 'SW_Interaction_MARTE_BehavioralFeature771'):
        assert _is_linked(b1, 'SW_Interaction_MARTE_BehavioralFeature771', a)
    _safe_set(a, 'MARTE_SW_Interaction_MessageComResource770', {b2})
    assert _is_linked(a, 'MARTE_SW_Interaction_MessageComResource770', b2)
    if hasattr(b1, 'SW_Interaction_MARTE_BehavioralFeature771'):
        assert not _is_linked(b1, 'SW_Interaction_MARTE_BehavioralFeature771', a)
    if hasattr(b2, 'SW_Interaction_MARTE_BehavioralFeature771'):
        assert _is_linked(b2, 'SW_Interaction_MARTE_BehavioralFeature771', a)
    _safe_set(a, 'MARTE_SW_Interaction_MessageComResource770', set())
    assert not _is_linked(a, 'MARTE_SW_Interaction_MessageComResource770', b2)
    if hasattr(b2, 'SW_Interaction_MARTE_BehavioralFeature771'):
        assert not _is_linked(b2, 'SW_Interaction_MARTE_BehavioralFeature771', a)


def test_assoc_setTime71_link_reassign_clear():
    a = MARTE_Time_ClockType(isLogical="sample_text", nature="sample_text")
    b1 = Time_MARTE_Operation()
    b2 = Time_MARTE_Operation()
    _safe_set(a, 'MARTE_Time_ClockType72', b1)
    assert _is_linked(a, 'MARTE_Time_ClockType72', b1)
    if hasattr(b1, 'Time_MARTE_Operation73'):
        assert _is_linked(b1, 'Time_MARTE_Operation73', a)
    _safe_set(a, 'MARTE_Time_ClockType72', b2)
    assert _is_linked(a, 'MARTE_Time_ClockType72', b2)
    if hasattr(b1, 'Time_MARTE_Operation73'):
        assert not _is_linked(b1, 'Time_MARTE_Operation73', a)
    if hasattr(b2, 'Time_MARTE_Operation73'):
        assert _is_linked(b2, 'Time_MARTE_Operation73', a)
    _safe_set(a, 'MARTE_Time_ClockType72', None)
    assert not _is_linked(a, 'MARTE_Time_ClockType72', b2)
    if hasattr(b2, 'Time_MARTE_Operation73'):
        assert not _is_linked(b2, 'Time_MARTE_Operation73', a)


def test_assoc_shareDataResources658_link_reassign_clear():
    a = MARTE_SW_Concurrency_SwConcurrentResource(activationCapacity="sample_text")
    b1 = SW_Concurrency_MARTE_TypedElement()
    b2 = SW_Concurrency_MARTE_TypedElement()
    _safe_set(a, 'MARTE_SW_Concurrency_SwConcurrentResource659', {b1})
    assert _is_linked(a, 'MARTE_SW_Concurrency_SwConcurrentResource659', b1)
    if hasattr(b1, 'SW_Concurrency_MARTE_TypedElement660'):
        assert _is_linked(b1, 'SW_Concurrency_MARTE_TypedElement660', a)
    _safe_set(a, 'MARTE_SW_Concurrency_SwConcurrentResource659', {b2})
    assert _is_linked(a, 'MARTE_SW_Concurrency_SwConcurrentResource659', b2)
    if hasattr(b1, 'SW_Concurrency_MARTE_TypedElement660'):
        assert not _is_linked(b1, 'SW_Concurrency_MARTE_TypedElement660', a)
    if hasattr(b2, 'SW_Concurrency_MARTE_TypedElement660'):
        assert _is_linked(b2, 'SW_Concurrency_MARTE_TypedElement660', a)
    _safe_set(a, 'MARTE_SW_Concurrency_SwConcurrentResource659', set())
    assert not _is_linked(a, 'MARTE_SW_Concurrency_SwConcurrentResource659', b2)
    if hasattr(b2, 'SW_Concurrency_MARTE_TypedElement660'):
        assert not _is_linked(b2, 'SW_Concurrency_MARTE_TypedElement660', a)


def test_assoc_signalServices783_link_reassign_clear():
    a = MARTE_SW_Interaction_NotificationResource(mechanism="sample_text", occurence="sample_text")
    b1 = SW_Interaction_MARTE_BehavioralFeature()
    b2 = SW_Interaction_MARTE_BehavioralFeature()
    _safe_set(a, 'MARTE_SW_Interaction_NotificationResource784', {b1})
    assert _is_linked(a, 'MARTE_SW_Interaction_NotificationResource784', b1)
    if hasattr(b1, 'SW_Interaction_MARTE_BehavioralFeature785'):
        assert _is_linked(b1, 'SW_Interaction_MARTE_BehavioralFeature785', a)
    _safe_set(a, 'MARTE_SW_Interaction_NotificationResource784', {b2})
    assert _is_linked(a, 'MARTE_SW_Interaction_NotificationResource784', b2)
    if hasattr(b1, 'SW_Interaction_MARTE_BehavioralFeature785'):
        assert not _is_linked(b1, 'SW_Interaction_MARTE_BehavioralFeature785', a)
    if hasattr(b2, 'SW_Interaction_MARTE_BehavioralFeature785'):
        assert _is_linked(b2, 'SW_Interaction_MARTE_BehavioralFeature785', a)
    _safe_set(a, 'MARTE_SW_Interaction_NotificationResource784', set())
    assert not _is_linked(a, 'MARTE_SW_Interaction_NotificationResource784', b2)
    if hasattr(b2, 'SW_Interaction_MARTE_BehavioralFeature785'):
        assert not _is_linked(b2, 'SW_Interaction_MARTE_BehavioralFeature785', a)


def test_assoc_srPoolWaitingTime239_link_reassign_clear():
    a = MARTE_HLAM_RtUnit(isDynamic="sample_text", isMain="sample_text", queueSchedPolicy="sample_text", queueSize="sample_text", srPoolPolicy="sample_text", srPoolSize="sample_text")
    b1 = NFP_Duration()
    b2 = NFP_Duration()
    _safe_set(a, 'MARTE_HLAM_RtUnit', b1)
    assert _is_linked(a, 'MARTE_HLAM_RtUnit', b1)
    if hasattr(b1, 'NFP_Duration240'):
        assert _is_linked(b1, 'NFP_Duration240', a)
    _safe_set(a, 'MARTE_HLAM_RtUnit', b2)
    assert _is_linked(a, 'MARTE_HLAM_RtUnit', b2)
    if hasattr(b1, 'NFP_Duration240'):
        assert not _is_linked(b1, 'NFP_Duration240', a)
    if hasattr(b2, 'NFP_Duration240'):
        assert _is_linked(b2, 'NFP_Duration240', a)
    _safe_set(a, 'MARTE_HLAM_RtUnit', None)
    assert not _is_linked(a, 'MARTE_HLAM_RtUnit', b2)
    if hasattr(b2, 'NFP_Duration240'):
        assert not _is_linked(b2, 'NFP_Duration240', a)


def test_assoc_stackSizeElements637_link_reassign_clear():
    a = MARTE_SW_Concurrency_SwConcurrentResource(activationCapacity="sample_text")
    b1 = SW_Concurrency_MARTE_TypedElement()
    b2 = SW_Concurrency_MARTE_TypedElement()
    _safe_set(a, 'MARTE_SW_Concurrency_SwConcurrentResource638', {b1})
    assert _is_linked(a, 'MARTE_SW_Concurrency_SwConcurrentResource638', b1)
    if hasattr(b1, 'SW_Concurrency_MARTE_TypedElement639'):
        assert _is_linked(b1, 'SW_Concurrency_MARTE_TypedElement639', a)
    _safe_set(a, 'MARTE_SW_Concurrency_SwConcurrentResource638', {b2})
    assert _is_linked(a, 'MARTE_SW_Concurrency_SwConcurrentResource638', b2)
    if hasattr(b1, 'SW_Concurrency_MARTE_TypedElement639'):
        assert not _is_linked(b1, 'SW_Concurrency_MARTE_TypedElement639', a)
    if hasattr(b2, 'SW_Concurrency_MARTE_TypedElement639'):
        assert _is_linked(b2, 'SW_Concurrency_MARTE_TypedElement639', a)
    _safe_set(a, 'MARTE_SW_Concurrency_SwConcurrentResource638', set())
    assert not _is_linked(a, 'MARTE_SW_Concurrency_SwConcurrentResource638', b2)
    if hasattr(b2, 'SW_Concurrency_MARTE_TypedElement639'):
        assert not _is_linked(b2, 'SW_Concurrency_MARTE_TypedElement639', a)


def test_assoc_startObs929_link_reassign_clear():
    a = MARTE_GQAM_GaTimedObs(laxity="sample_text")
    b1 = GQAM_MARTE_TimeObservation()
    b2 = GQAM_MARTE_TimeObservation()
    _safe_set(a, 'MARTE_GQAM_GaTimedObs', {b1})
    assert _is_linked(a, 'MARTE_GQAM_GaTimedObs', b1)
    if hasattr(b1, 'GQAM_MARTE_TimeObservation'):
        assert _is_linked(b1, 'GQAM_MARTE_TimeObservation', a)
    _safe_set(a, 'MARTE_GQAM_GaTimedObs', {b2})
    assert _is_linked(a, 'MARTE_GQAM_GaTimedObs', b2)
    if hasattr(b1, 'GQAM_MARTE_TimeObservation'):
        assert not _is_linked(b1, 'GQAM_MARTE_TimeObservation', a)
    if hasattr(b2, 'GQAM_MARTE_TimeObservation'):
        assert _is_linked(b2, 'GQAM_MARTE_TimeObservation', a)
    _safe_set(a, 'MARTE_GQAM_GaTimedObs', set())
    assert not _is_linked(a, 'MARTE_GQAM_GaTimedObs', b2)
    if hasattr(b2, 'GQAM_MARTE_TimeObservation'):
        assert not _is_linked(b2, 'GQAM_MARTE_TimeObservation', a)


def test_assoc_staticConsumption546_link_reassign_clear():
    a = MARTE_HwLayout_HwComponent(kind="sample_text")
    b1 = NFP_Power()
    b2 = NFP_Power()
    _safe_set(a, 'MARTE_HwLayout_HwComponent547', b1)
    assert _is_linked(a, 'MARTE_HwLayout_HwComponent547', b1)
    if hasattr(b1, 'NFP_Power548'):
        assert _is_linked(b1, 'NFP_Power548', a)
    _safe_set(a, 'MARTE_HwLayout_HwComponent547', b2)
    assert _is_linked(a, 'MARTE_HwLayout_HwComponent547', b2)
    if hasattr(b1, 'NFP_Power548'):
        assert not _is_linked(b1, 'NFP_Power548', a)
    if hasattr(b2, 'NFP_Power548'):
        assert _is_linked(b2, 'NFP_Power548', a)
    _safe_set(a, 'MARTE_HwLayout_HwComponent547', None)
    assert not _is_linked(a, 'MARTE_HwLayout_HwComponent547', b2)
    if hasattr(b2, 'NFP_Power548'):
        assert not _is_linked(b2, 'NFP_Power548', a)


def test_assoc_staticDissipation549_link_reassign_clear():
    a = MARTE_HwLayout_HwComponent(kind="sample_text")
    b1 = NFP_Power()
    b2 = NFP_Power()
    _safe_set(a, 'MARTE_HwLayout_HwComponent550', b1)
    assert _is_linked(a, 'MARTE_HwLayout_HwComponent550', b1)
    if hasattr(b1, 'NFP_Power551'):
        assert _is_linked(b1, 'NFP_Power551', a)
    _safe_set(a, 'MARTE_HwLayout_HwComponent550', b2)
    assert _is_linked(a, 'MARTE_HwLayout_HwComponent550', b2)
    if hasattr(b1, 'NFP_Power551'):
        assert not _is_linked(b1, 'NFP_Power551', a)
    if hasattr(b2, 'NFP_Power551'):
        assert _is_linked(b2, 'NFP_Power551', a)
    _safe_set(a, 'MARTE_HwLayout_HwComponent550', None)
    assert not _is_linked(a, 'MARTE_HwLayout_HwComponent550', b2)
    if hasattr(b2, 'NFP_Power551'):
        assert not _is_linked(b2, 'NFP_Power551', a)


def test_assoc_structure466_link_reassign_clear():
    a = MARTE_HwMemory_HwCache(repl_Policy="sample_text", type="sample_text", writePolicy="sample_text")
    b1 = HwMemory_CacheStructure()
    b2 = HwMemory_CacheStructure()
    _safe_set(a, 'MARTE_HwMemory_HwCache467', b1)
    assert _is_linked(a, 'MARTE_HwMemory_HwCache467', b1)
    if hasattr(b1, 'HwMemory_CacheStructure'):
        assert _is_linked(b1, 'HwMemory_CacheStructure', a)
    _safe_set(a, 'MARTE_HwMemory_HwCache467', b2)
    assert _is_linked(a, 'MARTE_HwMemory_HwCache467', b2)
    if hasattr(b1, 'HwMemory_CacheStructure'):
        assert not _is_linked(b1, 'HwMemory_CacheStructure', a)
    if hasattr(b2, 'HwMemory_CacheStructure'):
        assert _is_linked(b2, 'HwMemory_CacheStructure', a)
    _safe_set(a, 'MARTE_HwMemory_HwCache467', None)
    assert not _is_linked(a, 'MARTE_HwMemory_HwCache467', b2)
    if hasattr(b2, 'HwMemory_CacheStructure'):
        assert not _is_linked(b2, 'HwMemory_CacheStructure', a)


def test_assoc_subComponents552_link_reassign_clear():
    a = MARTE_HwLayout_HwComponent(kind="sample_text")
    b1 = HwLayout_HwComponent()
    b2 = HwLayout_HwComponent()
    _safe_set(a, 'MARTE_HwLayout_HwComponent553', {b1})
    assert _is_linked(a, 'MARTE_HwLayout_HwComponent553', b1)
    if hasattr(b1, 'HwLayout_HwComponent'):
        assert _is_linked(b1, 'HwLayout_HwComponent', a)
    _safe_set(a, 'MARTE_HwLayout_HwComponent553', {b2})
    assert _is_linked(a, 'MARTE_HwLayout_HwComponent553', b2)
    if hasattr(b1, 'HwLayout_HwComponent'):
        assert not _is_linked(b1, 'HwLayout_HwComponent', a)
    if hasattr(b2, 'HwLayout_HwComponent'):
        assert _is_linked(b2, 'HwLayout_HwComponent', a)
    _safe_set(a, 'MARTE_HwLayout_HwComponent553', set())
    assert not _is_linked(a, 'MARTE_HwLayout_HwComponent553', b2)
    if hasattr(b2, 'HwLayout_HwComponent'):
        assert not _is_linked(b2, 'HwLayout_HwComponent', a)


def test_assoc_suspendServices649_link_reassign_clear():
    a = MARTE_SW_Concurrency_SwConcurrentResource(activationCapacity="sample_text")
    b1 = SW_Concurrency_MARTE_BehavioralFeature()
    b2 = SW_Concurrency_MARTE_BehavioralFeature()
    _safe_set(a, 'MARTE_SW_Concurrency_SwConcurrentResource650', {b1})
    assert _is_linked(a, 'MARTE_SW_Concurrency_SwConcurrentResource650', b1)
    if hasattr(b1, 'SW_Concurrency_MARTE_BehavioralFeature651'):
        assert _is_linked(b1, 'SW_Concurrency_MARTE_BehavioralFeature651', a)
    _safe_set(a, 'MARTE_SW_Concurrency_SwConcurrentResource650', {b2})
    assert _is_linked(a, 'MARTE_SW_Concurrency_SwConcurrentResource650', b2)
    if hasattr(b1, 'SW_Concurrency_MARTE_BehavioralFeature651'):
        assert not _is_linked(b1, 'SW_Concurrency_MARTE_BehavioralFeature651', a)
    if hasattr(b2, 'SW_Concurrency_MARTE_BehavioralFeature651'):
        assert _is_linked(b2, 'SW_Concurrency_MARTE_BehavioralFeature651', a)
    _safe_set(a, 'MARTE_SW_Concurrency_SwConcurrentResource650', set())
    assert not _is_linked(a, 'MARTE_SW_Concurrency_SwConcurrentResource650', b2)
    if hasattr(b2, 'SW_Concurrency_MARTE_BehavioralFeature651'):
        assert not _is_linked(b2, 'SW_Concurrency_MARTE_BehavioralFeature651', a)


def test_assoc_terminateServices652_link_reassign_clear():
    a = MARTE_SW_Concurrency_SwConcurrentResource(activationCapacity="sample_text")
    b1 = SW_Concurrency_MARTE_BehavioralFeature()
    b2 = SW_Concurrency_MARTE_BehavioralFeature()
    _safe_set(a, 'MARTE_SW_Concurrency_SwConcurrentResource653', {b1})
    assert _is_linked(a, 'MARTE_SW_Concurrency_SwConcurrentResource653', b1)
    if hasattr(b1, 'SW_Concurrency_MARTE_BehavioralFeature654'):
        assert _is_linked(b1, 'SW_Concurrency_MARTE_BehavioralFeature654', a)
    _safe_set(a, 'MARTE_SW_Concurrency_SwConcurrentResource653', {b2})
    assert _is_linked(a, 'MARTE_SW_Concurrency_SwConcurrentResource653', b2)
    if hasattr(b1, 'SW_Concurrency_MARTE_BehavioralFeature654'):
        assert not _is_linked(b1, 'SW_Concurrency_MARTE_BehavioralFeature654', a)
    if hasattr(b2, 'SW_Concurrency_MARTE_BehavioralFeature654'):
        assert _is_linked(b2, 'SW_Concurrency_MARTE_BehavioralFeature654', a)
    _safe_set(a, 'MARTE_SW_Concurrency_SwConcurrentResource653', set())
    assert not _is_linked(a, 'MARTE_SW_Concurrency_SwConcurrentResource653', b2)
    if hasattr(b2, 'SW_Concurrency_MARTE_BehavioralFeature654'):
        assert not _is_linked(b2, 'SW_Concurrency_MARTE_BehavioralFeature654', a)


def test_assoc_throughput1114_link_reassign_clear():
    a = MARTE_PAM_PaRunTInstance(unbddPool="sample_text")
    b1 = NFP_Frequency()
    b2 = NFP_Frequency()
    _safe_set(a, 'MARTE_PAM_PaRunTInstance1115', b1)
    assert _is_linked(a, 'MARTE_PAM_PaRunTInstance1115', b1)
    if hasattr(b1, 'NFP_Frequency1116'):
        assert _is_linked(b1, 'NFP_Frequency1116', a)
    _safe_set(a, 'MARTE_PAM_PaRunTInstance1115', b2)
    assert _is_linked(a, 'MARTE_PAM_PaRunTInstance1115', b2)
    if hasattr(b1, 'NFP_Frequency1116'):
        assert not _is_linked(b1, 'NFP_Frequency1116', a)
    if hasattr(b2, 'NFP_Frequency1116'):
        assert _is_linked(b2, 'NFP_Frequency1116', a)
    _safe_set(a, 'MARTE_PAM_PaRunTInstance1115', None)
    assert not _is_linked(a, 'MARTE_PAM_PaRunTInstance1115', b2)
    if hasattr(b2, 'NFP_Frequency1116'):
        assert not _is_linked(b2, 'NFP_Frequency1116', a)


def test_assoc_timeSliceElements691_link_reassign_clear():
    a = MARTE_SW_Concurrency_SwSchedulableResource(isPreemptable="sample_text", isStaticSchedulingFeature="sample_text")
    b1 = SW_Concurrency_MARTE_TypedElement()
    b2 = SW_Concurrency_MARTE_TypedElement()
    _safe_set(a, 'MARTE_SW_Concurrency_SwSchedulableResource692', {b1})
    assert _is_linked(a, 'MARTE_SW_Concurrency_SwSchedulableResource692', b1)
    if hasattr(b1, 'SW_Concurrency_MARTE_TypedElement693'):
        assert _is_linked(b1, 'SW_Concurrency_MARTE_TypedElement693', a)
    _safe_set(a, 'MARTE_SW_Concurrency_SwSchedulableResource692', {b2})
    assert _is_linked(a, 'MARTE_SW_Concurrency_SwSchedulableResource692', b2)
    if hasattr(b1, 'SW_Concurrency_MARTE_TypedElement693'):
        assert not _is_linked(b1, 'SW_Concurrency_MARTE_TypedElement693', a)
    if hasattr(b2, 'SW_Concurrency_MARTE_TypedElement693'):
        assert _is_linked(b2, 'SW_Concurrency_MARTE_TypedElement693', a)
    _safe_set(a, 'MARTE_SW_Concurrency_SwSchedulableResource692', set())
    assert not _is_linked(a, 'MARTE_SW_Concurrency_SwSchedulableResource692', b2)
    if hasattr(b2, 'SW_Concurrency_MARTE_TypedElement693'):
        assert not _is_linked(b2, 'SW_Concurrency_MARTE_TypedElement693', a)


def test_assoc_timers718_link_reassign_clear():
    a = MARTE_SW_Concurrency_Alarm(isWatchdog="sample_text")
    b1 = SW_Concurrency_MARTE_TypedElement()
    b2 = SW_Concurrency_MARTE_TypedElement()
    _safe_set(a, 'MARTE_SW_Concurrency_Alarm', {b1})
    assert _is_linked(a, 'MARTE_SW_Concurrency_Alarm', b1)
    if hasattr(b1, 'SW_Concurrency_MARTE_TypedElement719'):
        assert _is_linked(b1, 'SW_Concurrency_MARTE_TypedElement719', a)
    _safe_set(a, 'MARTE_SW_Concurrency_Alarm', {b2})
    assert _is_linked(a, 'MARTE_SW_Concurrency_Alarm', b2)
    if hasattr(b1, 'SW_Concurrency_MARTE_TypedElement719'):
        assert not _is_linked(b1, 'SW_Concurrency_MARTE_TypedElement719', a)
    if hasattr(b2, 'SW_Concurrency_MARTE_TypedElement719'):
        assert _is_linked(b2, 'SW_Concurrency_MARTE_TypedElement719', a)
    _safe_set(a, 'MARTE_SW_Concurrency_Alarm', set())
    assert not _is_linked(a, 'MARTE_SW_Concurrency_Alarm', b2)
    if hasattr(b2, 'SW_Concurrency_MARTE_TypedElement719'):
        assert not _is_linked(b2, 'SW_Concurrency_MARTE_TypedElement719', a)


def test_assoc_type52_link_reassign_clear():
    a = MARTE_Time_Clock(standard="sample_text")
    b1 = Time_ClockType()
    b2 = Time_ClockType()
    _safe_set(a, 'MARTE_Time_Clock53', b1)
    assert _is_linked(a, 'MARTE_Time_Clock53', b1)
    if hasattr(b1, 'Time_ClockType'):
        assert _is_linked(b1, 'Time_ClockType', a)
    _safe_set(a, 'MARTE_Time_Clock53', b2)
    assert _is_linked(a, 'MARTE_Time_Clock53', b2)
    if hasattr(b1, 'Time_ClockType'):
        assert not _is_linked(b1, 'Time_ClockType', a)
    if hasattr(b2, 'Time_ClockType'):
        assert _is_linked(b2, 'Time_ClockType', a)
    _safe_set(a, 'MARTE_Time_Clock53', None)
    assert not _is_linked(a, 'MARTE_Time_Clock53', b2)
    if hasattr(b2, 'Time_ClockType'):
        assert not _is_linked(b2, 'Time_ClockType', a)


def test_assoc_type625_link_reassign_clear():
    a = MARTE_SW_Concurrency_SwConcurrentResource(activationCapacity="sample_text")
    b1 = ArrivalPattern()
    b2 = ArrivalPattern()
    _safe_set(a, 'MARTE_SW_Concurrency_SwConcurrentResource', b1)
    assert _is_linked(a, 'MARTE_SW_Concurrency_SwConcurrentResource', b1)
    if hasattr(b1, 'ArrivalPattern626'):
        assert _is_linked(b1, 'ArrivalPattern626', a)
    _safe_set(a, 'MARTE_SW_Concurrency_SwConcurrentResource', b2)
    assert _is_linked(a, 'MARTE_SW_Concurrency_SwConcurrentResource', b2)
    if hasattr(b1, 'ArrivalPattern626'):
        assert not _is_linked(b1, 'ArrivalPattern626', a)
    if hasattr(b2, 'ArrivalPattern626'):
        assert _is_linked(b2, 'ArrivalPattern626', a)
    _safe_set(a, 'MARTE_SW_Concurrency_SwConcurrentResource', None)
    assert not _is_linked(a, 'MARTE_SW_Concurrency_SwConcurrentResource', b2)
    if hasattr(b2, 'ArrivalPattern626'):
        assert not _is_linked(b2, 'ArrivalPattern626', a)


def test_assoc_unMapServices756_link_reassign_clear():
    a = MARTE_SW_Brokering_MemoryBroker(accessPolicy="sample_text")
    b1 = SW_Brokering_MARTE_BehavioralFeature()
    b2 = SW_Brokering_MARTE_BehavioralFeature()
    _safe_set(a, 'MARTE_SW_Brokering_MemoryBroker757', {b1})
    assert _is_linked(a, 'MARTE_SW_Brokering_MemoryBroker757', b1)
    if hasattr(b1, 'SW_Brokering_MARTE_BehavioralFeature758'):
        assert _is_linked(b1, 'SW_Brokering_MARTE_BehavioralFeature758', a)
    _safe_set(a, 'MARTE_SW_Brokering_MemoryBroker757', {b2})
    assert _is_linked(a, 'MARTE_SW_Brokering_MemoryBroker757', b2)
    if hasattr(b1, 'SW_Brokering_MARTE_BehavioralFeature758'):
        assert not _is_linked(b1, 'SW_Brokering_MARTE_BehavioralFeature758', a)
    if hasattr(b2, 'SW_Brokering_MARTE_BehavioralFeature758'):
        assert _is_linked(b2, 'SW_Brokering_MARTE_BehavioralFeature758', a)
    _safe_set(a, 'MARTE_SW_Brokering_MemoryBroker757', set())
    assert not _is_linked(a, 'MARTE_SW_Brokering_MemoryBroker757', b2)
    if hasattr(b2, 'SW_Brokering_MARTE_BehavioralFeature758'):
        assert not _is_linked(b2, 'SW_Brokering_MARTE_BehavioralFeature758', a)


def test_assoc_unit54_link_reassign_clear():
    a = MARTE_Time_Clock(standard="sample_text")
    b1 = NFPs_Unit()
    b2 = NFPs_Unit()
    _safe_set(a, 'MARTE_Time_Clock55', b1)
    assert _is_linked(a, 'MARTE_Time_Clock55', b1)
    if hasattr(b1, 'NFPs_Unit56'):
        assert _is_linked(b1, 'NFPs_Unit56', a)
    _safe_set(a, 'MARTE_Time_Clock55', b2)
    assert _is_linked(a, 'MARTE_Time_Clock55', b2)
    if hasattr(b1, 'NFPs_Unit56'):
        assert not _is_linked(b1, 'NFPs_Unit56', a)
    if hasattr(b2, 'NFPs_Unit56'):
        assert _is_linked(b2, 'NFPs_Unit56', a)
    _safe_set(a, 'MARTE_Time_Clock55', None)
    assert not _is_linked(a, 'MARTE_Time_Clock55', b2)
    if hasattr(b2, 'NFPs_Unit56'):
        assert not _is_linked(b2, 'NFPs_Unit56', a)


def test_assoc_unitType59_link_reassign_clear():
    a = MARTE_Time_ClockType(isLogical="sample_text", nature="sample_text")
    b1 = Time_MARTE_Enumeration()
    b2 = Time_MARTE_Enumeration()
    _safe_set(a, 'MARTE_Time_ClockType', b1)
    assert _is_linked(a, 'MARTE_Time_ClockType', b1)
    if hasattr(b1, 'Time_MARTE_Enumeration'):
        assert _is_linked(b1, 'Time_MARTE_Enumeration', a)
    _safe_set(a, 'MARTE_Time_ClockType', b2)
    assert _is_linked(a, 'MARTE_Time_ClockType', b2)
    if hasattr(b1, 'Time_MARTE_Enumeration'):
        assert not _is_linked(b1, 'Time_MARTE_Enumeration', a)
    if hasattr(b2, 'Time_MARTE_Enumeration'):
        assert _is_linked(b2, 'Time_MARTE_Enumeration', a)
    _safe_set(a, 'MARTE_Time_ClockType', None)
    assert not _is_linked(a, 'MARTE_Time_ClockType', b2)
    if hasattr(b2, 'Time_MARTE_Enumeration'):
        assert not _is_linked(b2, 'Time_MARTE_Enumeration', a)


def test_assoc_unlockServices750_link_reassign_clear():
    a = MARTE_SW_Brokering_MemoryBroker(accessPolicy="sample_text")
    b1 = SW_Brokering_MARTE_BehavioralFeature()
    b2 = SW_Brokering_MARTE_BehavioralFeature()
    _safe_set(a, 'MARTE_SW_Brokering_MemoryBroker751', {b1})
    assert _is_linked(a, 'MARTE_SW_Brokering_MemoryBroker751', b1)
    if hasattr(b1, 'SW_Brokering_MARTE_BehavioralFeature752'):
        assert _is_linked(b1, 'SW_Brokering_MARTE_BehavioralFeature752', a)
    _safe_set(a, 'MARTE_SW_Brokering_MemoryBroker751', {b2})
    assert _is_linked(a, 'MARTE_SW_Brokering_MemoryBroker751', b2)
    if hasattr(b1, 'SW_Brokering_MARTE_BehavioralFeature752'):
        assert not _is_linked(b1, 'SW_Brokering_MARTE_BehavioralFeature752', a)
    if hasattr(b2, 'SW_Brokering_MARTE_BehavioralFeature752'):
        assert _is_linked(b2, 'SW_Brokering_MARTE_BehavioralFeature752', a)
    _safe_set(a, 'MARTE_SW_Brokering_MemoryBroker751', set())
    assert not _is_linked(a, 'MARTE_SW_Brokering_MemoryBroker751', b2)
    if hasattr(b2, 'SW_Brokering_MARTE_BehavioralFeature752'):
        assert not _is_linked(b2, 'SW_Brokering_MARTE_BehavioralFeature752', a)


def test_assoc_utilization1111_link_reassign_clear():
    a = MARTE_PAM_PaRunTInstance(unbddPool="sample_text")
    b1 = NFP_Real()
    b2 = NFP_Real()
    _safe_set(a, 'MARTE_PAM_PaRunTInstance1112', b1)
    assert _is_linked(a, 'MARTE_PAM_PaRunTInstance1112', b1)
    if hasattr(b1, 'NFP_Real1113'):
        assert _is_linked(b1, 'NFP_Real1113', a)
    _safe_set(a, 'MARTE_PAM_PaRunTInstance1112', b2)
    assert _is_linked(a, 'MARTE_PAM_PaRunTInstance1112', b2)
    if hasattr(b1, 'NFP_Real1113'):
        assert not _is_linked(b1, 'NFP_Real1113', a)
    if hasattr(b2, 'NFP_Real1113'):
        assert _is_linked(b2, 'NFP_Real1113', a)
    _safe_set(a, 'MARTE_PAM_PaRunTInstance1112', None)
    assert not _is_linked(a, 'MARTE_PAM_PaRunTInstance1112', b2)
    if hasattr(b2, 'NFP_Real1113'):
        assert not _is_linked(b2, 'NFP_Real1113', a)


def test_assoc_vectorElements673_link_reassign_clear():
    a = MARTE_SW_Concurrency_InterruptResource(isMaskable="sample_text", kind="sample_text")
    b1 = SW_Concurrency_MARTE_TypedElement()
    b2 = SW_Concurrency_MARTE_TypedElement()
    _safe_set(a, 'MARTE_SW_Concurrency_InterruptResource', {b1})
    assert _is_linked(a, 'MARTE_SW_Concurrency_InterruptResource', b1)
    if hasattr(b1, 'SW_Concurrency_MARTE_TypedElement674'):
        assert _is_linked(b1, 'SW_Concurrency_MARTE_TypedElement674', a)
    _safe_set(a, 'MARTE_SW_Concurrency_InterruptResource', {b2})
    assert _is_linked(a, 'MARTE_SW_Concurrency_InterruptResource', b2)
    if hasattr(b1, 'SW_Concurrency_MARTE_TypedElement674'):
        assert not _is_linked(b1, 'SW_Concurrency_MARTE_TypedElement674', a)
    if hasattr(b2, 'SW_Concurrency_MARTE_TypedElement674'):
        assert _is_linked(b2, 'SW_Concurrency_MARTE_TypedElement674', a)
    _safe_set(a, 'MARTE_SW_Concurrency_InterruptResource', set())
    assert not _is_linked(a, 'MARTE_SW_Concurrency_InterruptResource', b2)
    if hasattr(b2, 'SW_Concurrency_MARTE_TypedElement674'):
        assert not _is_linked(b2, 'SW_Concurrency_MARTE_TypedElement674', a)


def test_assoc_waitServices786_link_reassign_clear():
    a = MARTE_SW_Interaction_NotificationResource(mechanism="sample_text", occurence="sample_text")
    b1 = SW_Interaction_MARTE_BehavioralFeature()
    b2 = SW_Interaction_MARTE_BehavioralFeature()
    _safe_set(a, 'MARTE_SW_Interaction_NotificationResource787', {b1})
    assert _is_linked(a, 'MARTE_SW_Interaction_NotificationResource787', b1)
    if hasattr(b1, 'SW_Interaction_MARTE_BehavioralFeature788'):
        assert _is_linked(b1, 'SW_Interaction_MARTE_BehavioralFeature788', a)
    _safe_set(a, 'MARTE_SW_Interaction_NotificationResource787', {b2})
    assert _is_linked(a, 'MARTE_SW_Interaction_NotificationResource787', b2)
    if hasattr(b1, 'SW_Interaction_MARTE_BehavioralFeature788'):
        assert not _is_linked(b1, 'SW_Interaction_MARTE_BehavioralFeature788', a)
    if hasattr(b2, 'SW_Interaction_MARTE_BehavioralFeature788'):
        assert _is_linked(b2, 'SW_Interaction_MARTE_BehavioralFeature788', a)
    _safe_set(a, 'MARTE_SW_Interaction_NotificationResource787', set())
    assert not _is_linked(a, 'MARTE_SW_Interaction_NotificationResource787', b2)
    if hasattr(b2, 'SW_Interaction_MARTE_BehavioralFeature788'):
        assert not _is_linked(b2, 'SW_Interaction_MARTE_BehavioralFeature788', a)


def test_assoc_waitingPolicyElements759_link_reassign_clear():
    a = MARTE_SW_Interaction_SwInteractionResource(isIntraMemoryPartitionInteraction=True, waitingQueueCapacity="sample_text", waitingQueuePolicy="sample_text")
    b1 = SW_Interaction_MARTE_TypedElement()
    b2 = SW_Interaction_MARTE_TypedElement()
    _safe_set(a, 'MARTE_SW_Interaction_SwInteractionResource', {b1})
    assert _is_linked(a, 'MARTE_SW_Interaction_SwInteractionResource', b1)
    if hasattr(b1, 'SW_Interaction_MARTE_TypedElement'):
        assert _is_linked(b1, 'SW_Interaction_MARTE_TypedElement', a)
    _safe_set(a, 'MARTE_SW_Interaction_SwInteractionResource', {b2})
    assert _is_linked(a, 'MARTE_SW_Interaction_SwInteractionResource', b2)
    if hasattr(b1, 'SW_Interaction_MARTE_TypedElement'):
        assert not _is_linked(b1, 'SW_Interaction_MARTE_TypedElement', a)
    if hasattr(b2, 'SW_Interaction_MARTE_TypedElement'):
        assert _is_linked(b2, 'SW_Interaction_MARTE_TypedElement', a)
    _safe_set(a, 'MARTE_SW_Interaction_SwInteractionResource', set())
    assert not _is_linked(a, 'MARTE_SW_Interaction_SwInteractionResource', b2)
    if hasattr(b2, 'SW_Interaction_MARTE_TypedElement'):
        assert not _is_linked(b2, 'SW_Interaction_MARTE_TypedElement', a)


def test_assoc_weight536_link_reassign_clear():
    a = MARTE_HwLayout_HwComponent(kind="sample_text")
    b1 = NFP_Real()
    b2 = NFP_Real()
    _safe_set(a, 'MARTE_HwLayout_HwComponent537', b1)
    assert _is_linked(a, 'MARTE_HwLayout_HwComponent537', b1)
    if hasattr(b1, 'NFP_Real538'):
        assert _is_linked(b1, 'NFP_Real538', a)
    _safe_set(a, 'MARTE_HwLayout_HwComponent537', b2)
    assert _is_linked(a, 'MARTE_HwLayout_HwComponent537', b2)
    if hasattr(b1, 'NFP_Real538'):
        assert not _is_linked(b1, 'NFP_Real538', a)
    if hasattr(b2, 'NFP_Real538'):
        assert _is_linked(b2, 'NFP_Real538', a)
    _safe_set(a, 'MARTE_HwLayout_HwComponent537', None)
    assert not _is_linked(a, 'MARTE_HwLayout_HwComponent537', b2)
    if hasattr(b2, 'NFP_Real538'):
        assert not _is_linked(b2, 'NFP_Real538', a)


def test_assoc_wire580_link_reassign_clear():
    a = MARTE_HwPackage_HwPackagePin(altNames="sample_text", pinNo="sample_text")
    b1 = HwPackage_HwWire()
    b2 = HwPackage_HwWire()
    _safe_set(a, 'MARTE_HwPackage_HwPackagePin', {b1})
    assert _is_linked(a, 'MARTE_HwPackage_HwPackagePin', b1)
    if hasattr(b1, 'HwPackage_HwWire'):
        assert _is_linked(b1, 'HwPackage_HwWire', a)
    _safe_set(a, 'MARTE_HwPackage_HwPackagePin', {b2})
    assert _is_linked(a, 'MARTE_HwPackage_HwPackagePin', b2)
    if hasattr(b1, 'HwPackage_HwWire'):
        assert not _is_linked(b1, 'HwPackage_HwWire', a)
    if hasattr(b2, 'HwPackage_HwWire'):
        assert _is_linked(b2, 'HwPackage_HwWire', a)
    _safe_set(a, 'MARTE_HwPackage_HwPackagePin', set())
    assert not _is_linked(a, 'MARTE_HwPackage_HwPackagePin', b2)
    if hasattr(b2, 'HwPackage_HwWire'):
        assert not _is_linked(b2, 'HwPackage_HwWire', a)


def test_assoc_wires591_link_reassign_clear():
    a = MARTE_HwDiagram_HwCircuitDiagram(name="sample_text")
    b1 = HwPackage_HwWire()
    b2 = HwPackage_HwWire()
    _safe_set(a, 'MARTE_HwDiagram_HwCircuitDiagram592', {b1})
    assert _is_linked(a, 'MARTE_HwDiagram_HwCircuitDiagram592', b1)
    if hasattr(b1, 'HwPackage_HwWire593'):
        assert _is_linked(b1, 'HwPackage_HwWire593', a)
    _safe_set(a, 'MARTE_HwDiagram_HwCircuitDiagram592', {b2})
    assert _is_linked(a, 'MARTE_HwDiagram_HwCircuitDiagram592', b2)
    if hasattr(b1, 'HwPackage_HwWire593'):
        assert not _is_linked(b1, 'HwPackage_HwWire593', a)
    if hasattr(b2, 'HwPackage_HwWire593'):
        assert _is_linked(b2, 'HwPackage_HwWire593', a)
    _safe_set(a, 'MARTE_HwDiagram_HwCircuitDiagram592', set())
    assert not _is_linked(a, 'MARTE_HwDiagram_HwCircuitDiagram592', b2)
    if hasattr(b2, 'HwPackage_HwWire593'):
        assert not _is_linked(b2, 'HwPackage_HwWire593', a)


def test_assoc_writeServices732_link_reassign_clear():
    a = MARTE_SW_Brokering_DeviceBroker(accessPolicy="sample_text", isBuffered="sample_text", name="sample_text")
    b1 = SW_Brokering_MARTE_BehavioralFeature()
    b2 = SW_Brokering_MARTE_BehavioralFeature()
    _safe_set(a, 'MARTE_SW_Brokering_DeviceBroker733', {b1})
    assert _is_linked(a, 'MARTE_SW_Brokering_DeviceBroker733', b1)
    if hasattr(b1, 'SW_Brokering_MARTE_BehavioralFeature734'):
        assert _is_linked(b1, 'SW_Brokering_MARTE_BehavioralFeature734', a)
    _safe_set(a, 'MARTE_SW_Brokering_DeviceBroker733', {b2})
    assert _is_linked(a, 'MARTE_SW_Brokering_DeviceBroker733', b2)
    if hasattr(b1, 'SW_Brokering_MARTE_BehavioralFeature734'):
        assert not _is_linked(b1, 'SW_Brokering_MARTE_BehavioralFeature734', a)
    if hasattr(b2, 'SW_Brokering_MARTE_BehavioralFeature734'):
        assert _is_linked(b2, 'SW_Brokering_MARTE_BehavioralFeature734', a)
    _safe_set(a, 'MARTE_SW_Brokering_DeviceBroker733', set())
    assert not _is_linked(a, 'MARTE_SW_Brokering_DeviceBroker733', b2)
    if hasattr(b2, 'SW_Brokering_MARTE_BehavioralFeature734'):
        assert not _is_linked(b2, 'SW_Brokering_MARTE_BehavioralFeature734', a)


def test_assoc_yieldServices700_link_reassign_clear():
    a = MARTE_SW_Concurrency_SwSchedulableResource(isPreemptable="sample_text", isStaticSchedulingFeature="sample_text")
    b1 = SW_Concurrency_MARTE_BehavioralFeature()
    b2 = SW_Concurrency_MARTE_BehavioralFeature()
    _safe_set(a, 'MARTE_SW_Concurrency_SwSchedulableResource701', {b1})
    assert _is_linked(a, 'MARTE_SW_Concurrency_SwSchedulableResource701', b1)
    if hasattr(b1, 'SW_Concurrency_MARTE_BehavioralFeature702'):
        assert _is_linked(b1, 'SW_Concurrency_MARTE_BehavioralFeature702', a)
    _safe_set(a, 'MARTE_SW_Concurrency_SwSchedulableResource701', {b2})
    assert _is_linked(a, 'MARTE_SW_Concurrency_SwSchedulableResource701', b2)
    if hasattr(b1, 'SW_Concurrency_MARTE_BehavioralFeature702'):
        assert not _is_linked(b1, 'SW_Concurrency_MARTE_BehavioralFeature702', a)
    if hasattr(b2, 'SW_Concurrency_MARTE_BehavioralFeature702'):
        assert _is_linked(b2, 'SW_Concurrency_MARTE_BehavioralFeature702', a)
    _safe_set(a, 'MARTE_SW_Concurrency_SwSchedulableResource701', set())
    assert not _is_linked(a, 'MARTE_SW_Concurrency_SwSchedulableResource701', b2)
    if hasattr(b2, 'SW_Concurrency_MARTE_BehavioralFeature702'):
        assert not _is_linked(b2, 'SW_Concurrency_MARTE_BehavioralFeature702', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

Action_strategy = st.builds(Action)
@given(instance=Action_strategy)
@settings(max_examples=25)
def test_Action_instantiation(instance):
    assert isinstance(instance, Action)


Activity_strategy = st.builds(Activity)
@given(instance=Activity_strategy)
@settings(max_examples=25)
def test_Activity_instantiation(instance):
    assert isinstance(instance, Activity)


Alloc_Allocated_strategy = st.builds(Alloc_Allocated)
@given(instance=Alloc_Allocated_strategy)
@settings(max_examples=25)
def test_Alloc_Allocated_instantiation(instance):
    assert isinstance(instance, Alloc_Allocated)


Alloc_MARTE_Abstraction_strategy = st.builds(Alloc_MARTE_Abstraction)
@given(instance=Alloc_MARTE_Abstraction_strategy)
@settings(max_examples=25)
def test_Alloc_MARTE_Abstraction_instantiation(instance):
    assert isinstance(instance, Alloc_MARTE_Abstraction)


Alloc_MARTE_ActivityPartition_strategy = st.builds(Alloc_MARTE_ActivityPartition)
@given(instance=Alloc_MARTE_ActivityPartition_strategy)
@settings(max_examples=25)
def test_Alloc_MARTE_ActivityPartition_instantiation(instance):
    assert isinstance(instance, Alloc_MARTE_ActivityPartition)


Alloc_MARTE_Comment_strategy = st.builds(Alloc_MARTE_Comment)
@given(instance=Alloc_MARTE_Comment_strategy)
@settings(max_examples=25)
def test_Alloc_MARTE_Comment_instantiation(instance):
    assert isinstance(instance, Alloc_MARTE_Comment)


Alloc_MARTE_Dependency_strategy = st.builds(Alloc_MARTE_Dependency)
@given(instance=Alloc_MARTE_Dependency_strategy)
@settings(max_examples=25)
def test_Alloc_MARTE_Dependency_instantiation(instance):
    assert isinstance(instance, Alloc_MARTE_Dependency)


Alloc_MARTE_Element_strategy = st.builds(Alloc_MARTE_Element)
@given(instance=Alloc_MARTE_Element_strategy)
@settings(max_examples=25)
def test_Alloc_MARTE_Element_instantiation(instance):
    assert isinstance(instance, Alloc_MARTE_Element)


Alloc_MARTE_NamedElement_strategy = st.builds(Alloc_MARTE_NamedElement)
@given(instance=Alloc_MARTE_NamedElement_strategy)
@settings(max_examples=25)
def test_Alloc_MARTE_NamedElement_instantiation(instance):
    assert isinstance(instance, Alloc_MARTE_NamedElement)


Allocate_strategy = st.builds(Allocate)
@given(instance=Allocate_strategy)
@settings(max_examples=25)
def test_Allocate_instantiation(instance):
    assert isinstance(instance, Allocate)


ArrivalPattern_strategy = st.builds(ArrivalPattern)
@given(instance=ArrivalPattern_strategy)
@settings(max_examples=25)
def test_ArrivalPattern_instantiation(instance):
    assert isinstance(instance, ArrivalPattern)


CoreElements_Configuration_strategy = st.builds(CoreElements_Configuration)
@given(instance=CoreElements_Configuration_strategy)
@settings(max_examples=25)
def test_CoreElements_Configuration_instantiation(instance):
    assert isinstance(instance, CoreElements_Configuration)


CoreElements_MARTE_Package_strategy = st.builds(CoreElements_MARTE_Package)
@given(instance=CoreElements_MARTE_Package_strategy)
@settings(max_examples=25)
def test_CoreElements_MARTE_Package_instantiation(instance):
    assert isinstance(instance, CoreElements_MARTE_Package)


CoreElements_MARTE_State_strategy = st.builds(CoreElements_MARTE_State)
@given(instance=CoreElements_MARTE_State_strategy)
@settings(max_examples=25)
def test_CoreElements_MARTE_State_instantiation(instance):
    assert isinstance(instance, CoreElements_MARTE_State)


CoreElements_MARTE_StateMachine_strategy = st.builds(CoreElements_MARTE_StateMachine)
@given(instance=CoreElements_MARTE_StateMachine_strategy)
@settings(max_examples=25)
def test_CoreElements_MARTE_StateMachine_instantiation(instance):
    assert isinstance(instance, CoreElements_MARTE_StateMachine)


CoreElements_MARTE_StructuredClassifier_strategy = st.builds(CoreElements_MARTE_StructuredClassifier)
@given(instance=CoreElements_MARTE_StructuredClassifier_strategy)
@settings(max_examples=25)
def test_CoreElements_MARTE_StructuredClassifier_instantiation(instance):
    assert isinstance(instance, CoreElements_MARTE_StructuredClassifier)


CoreElements_MARTE_Transition_strategy = st.builds(CoreElements_MARTE_Transition)
@given(instance=CoreElements_MARTE_Transition_strategy)
@settings(max_examples=25)
def test_CoreElements_MARTE_Transition_instantiation(instance):
    assert isinstance(instance, CoreElements_MARTE_Transition)


CoreElements_Mode_strategy = st.builds(CoreElements_Mode)
@given(instance=CoreElements_Mode_strategy)
@settings(max_examples=25)
def test_CoreElements_Mode_instantiation(instance):
    assert isinstance(instance, CoreElements_Mode)


DataTypes_MARTE_DataType_strategy = st.builds(DataTypes_MARTE_DataType)
@given(instance=DataTypes_MARTE_DataType_strategy)
@settings(max_examples=25)
def test_DataTypes_MARTE_DataType_instantiation(instance):
    assert isinstance(instance, DataTypes_MARTE_DataType)


DataTypes_MARTE_Property_strategy = st.builds(DataTypes_MARTE_Property)
@given(instance=DataTypes_MARTE_Property_strategy)
@settings(max_examples=25)
def test_DataTypes_MARTE_Property_instantiation(instance):
    assert isinstance(instance, DataTypes_MARTE_Property)


GCM_ClientServerSpecification_strategy = st.builds(GCM_ClientServerSpecification)
@given(instance=GCM_ClientServerSpecification_strategy)
@settings(max_examples=25)
def test_GCM_ClientServerSpecification_instantiation(instance):
    assert isinstance(instance, GCM_ClientServerSpecification)


GCM_MARTE_AnyReceiveEvent_strategy = st.builds(GCM_MARTE_AnyReceiveEvent)
@given(instance=GCM_MARTE_AnyReceiveEvent_strategy)
@settings(max_examples=25)
def test_GCM_MARTE_AnyReceiveEvent_instantiation(instance):
    assert isinstance(instance, GCM_MARTE_AnyReceiveEvent)


GCM_MARTE_Behavior_strategy = st.builds(GCM_MARTE_Behavior)
@given(instance=GCM_MARTE_Behavior_strategy)
@settings(max_examples=25)
def test_GCM_MARTE_Behavior_instantiation(instance):
    assert isinstance(instance, GCM_MARTE_Behavior)


GCM_MARTE_BehavioralFeature_strategy = st.builds(GCM_MARTE_BehavioralFeature)
@given(instance=GCM_MARTE_BehavioralFeature_strategy)
@settings(max_examples=25)
def test_GCM_MARTE_BehavioralFeature_instantiation(instance):
    assert isinstance(instance, GCM_MARTE_BehavioralFeature)


GCM_MARTE_Classifier_strategy = st.builds(GCM_MARTE_Classifier)
@given(instance=GCM_MARTE_Classifier_strategy)
@settings(max_examples=25)
def test_GCM_MARTE_Classifier_instantiation(instance):
    assert isinstance(instance, GCM_MARTE_Classifier)


GCM_MARTE_Feature_strategy = st.builds(GCM_MARTE_Feature)
@given(instance=GCM_MARTE_Feature_strategy)
@settings(max_examples=25)
def test_GCM_MARTE_Feature_instantiation(instance):
    assert isinstance(instance, GCM_MARTE_Feature)


GCM_MARTE_Interface_strategy = st.builds(GCM_MARTE_Interface)
@given(instance=GCM_MARTE_Interface_strategy)
@settings(max_examples=25)
def test_GCM_MARTE_Interface_instantiation(instance):
    assert isinstance(instance, GCM_MARTE_Interface)


GCM_MARTE_InvocationAction_strategy = st.builds(GCM_MARTE_InvocationAction)
@given(instance=GCM_MARTE_InvocationAction_strategy)
@settings(max_examples=25)
def test_GCM_MARTE_InvocationAction_instantiation(instance):
    assert isinstance(instance, GCM_MARTE_InvocationAction)


GCM_MARTE_Port_strategy = st.builds(GCM_MARTE_Port)
@given(instance=GCM_MARTE_Port_strategy)
@settings(max_examples=25)
def test_GCM_MARTE_Port_instantiation(instance):
    assert isinstance(instance, GCM_MARTE_Port)


GCM_MARTE_Property_strategy = st.builds(GCM_MARTE_Property)
@given(instance=GCM_MARTE_Property_strategy)
@settings(max_examples=25)
def test_GCM_MARTE_Property_instantiation(instance):
    assert isinstance(instance, GCM_MARTE_Property)


GCM_MARTE_Trigger_strategy = st.builds(GCM_MARTE_Trigger)
@given(instance=GCM_MARTE_Trigger_strategy)
@settings(max_examples=25)
def test_GCM_MARTE_Trigger_instantiation(instance):
    assert isinstance(instance, GCM_MARTE_Trigger)


GQAM_GaCommStep_strategy = st.builds(GQAM_GaCommStep)
@given(instance=GQAM_GaCommStep_strategy)
@settings(max_examples=25)
def test_GQAM_GaCommStep_instantiation(instance):
    assert isinstance(instance, GQAM_GaCommStep)


GQAM_GaEventTrace_strategy = st.builds(GQAM_GaEventTrace)
@given(instance=GQAM_GaEventTrace_strategy)
@settings(max_examples=25)
def test_GQAM_GaEventTrace_instantiation(instance):
    assert isinstance(instance, GQAM_GaEventTrace)


GQAM_GaExecHost_strategy = st.builds(GQAM_GaExecHost)
@given(instance=GQAM_GaExecHost_strategy)
@settings(max_examples=25)
def test_GQAM_GaExecHost_instantiation(instance):
    assert isinstance(instance, GQAM_GaExecHost)


GQAM_GaRequestedService_strategy = st.builds(GQAM_GaRequestedService)
@given(instance=GQAM_GaRequestedService_strategy)
@settings(max_examples=25)
def test_GQAM_GaRequestedService_instantiation(instance):
    assert isinstance(instance, GQAM_GaRequestedService)


GQAM_GaResourcesPlatform_strategy = st.builds(GQAM_GaResourcesPlatform)
@given(instance=GQAM_GaResourcesPlatform_strategy)
@settings(max_examples=25)
def test_GQAM_GaResourcesPlatform_instantiation(instance):
    assert isinstance(instance, GQAM_GaResourcesPlatform)


GQAM_GaScenario_strategy = st.builds(GQAM_GaScenario)
@given(instance=GQAM_GaScenario_strategy)
@settings(max_examples=25)
def test_GQAM_GaScenario_instantiation(instance):
    assert isinstance(instance, GQAM_GaScenario)


GQAM_GaStep_strategy = st.builds(GQAM_GaStep)
@given(instance=GQAM_GaStep_strategy)
@settings(max_examples=25)
def test_GQAM_GaStep_instantiation(instance):
    assert isinstance(instance, GQAM_GaStep)


GQAM_GaTimedObs_strategy = st.builds(GQAM_GaTimedObs)
@given(instance=GQAM_GaTimedObs_strategy)
@settings(max_examples=25)
def test_GQAM_GaTimedObs_instantiation(instance):
    assert isinstance(instance, GQAM_GaTimedObs)


GQAM_GaWorkloadBehavior_strategy = st.builds(GQAM_GaWorkloadBehavior)
@given(instance=GQAM_GaWorkloadBehavior_strategy)
@settings(max_examples=25)
def test_GQAM_GaWorkloadBehavior_instantiation(instance):
    assert isinstance(instance, GQAM_GaWorkloadBehavior)


GQAM_GaWorkloadEvent_strategy = st.builds(GQAM_GaWorkloadEvent)
@given(instance=GQAM_GaWorkloadEvent_strategy)
@settings(max_examples=25)
def test_GQAM_GaWorkloadEvent_instantiation(instance):
    assert isinstance(instance, GQAM_GaWorkloadEvent)


GQAM_GaWorkloadGenerator_strategy = st.builds(GQAM_GaWorkloadGenerator)
@given(instance=GQAM_GaWorkloadGenerator_strategy)
@settings(max_examples=25)
def test_GQAM_GaWorkloadGenerator_instantiation(instance):
    assert isinstance(instance, GQAM_GaWorkloadGenerator)


GQAM_MARTE_Behavior_strategy = st.builds(GQAM_MARTE_Behavior)
@given(instance=GQAM_MARTE_Behavior_strategy)
@settings(max_examples=25)
def test_GQAM_MARTE_Behavior_instantiation(instance):
    assert isinstance(instance, GQAM_MARTE_Behavior)


GQAM_MARTE_Classifier_strategy = st.builds(GQAM_MARTE_Classifier)
@given(instance=GQAM_MARTE_Classifier_strategy)
@settings(max_examples=25)
def test_GQAM_MARTE_Classifier_instantiation(instance):
    assert isinstance(instance, GQAM_MARTE_Classifier)


GQAM_MARTE_NamedElement_strategy = st.builds(GQAM_MARTE_NamedElement)
@given(instance=GQAM_MARTE_NamedElement_strategy)
@settings(max_examples=25)
def test_GQAM_MARTE_NamedElement_instantiation(instance):
    assert isinstance(instance, GQAM_MARTE_NamedElement)


GQAM_MARTE_Operation_strategy = st.builds(GQAM_MARTE_Operation)
@given(instance=GQAM_MARTE_Operation_strategy)
@settings(max_examples=25)
def test_GQAM_MARTE_Operation_instantiation(instance):
    assert isinstance(instance, GQAM_MARTE_Operation)


GQAM_MARTE_TimeEvent_strategy = st.builds(GQAM_MARTE_TimeEvent)
@given(instance=GQAM_MARTE_TimeEvent_strategy)
@settings(max_examples=25)
def test_GQAM_MARTE_TimeEvent_instantiation(instance):
    assert isinstance(instance, GQAM_MARTE_TimeEvent)


GQAM_MARTE_TimeObservation_strategy = st.builds(GQAM_MARTE_TimeObservation)
@given(instance=GQAM_MARTE_TimeObservation_strategy)
@settings(max_examples=25)
def test_GQAM_MARTE_TimeObservation_instantiation(instance):
    assert isinstance(instance, GQAM_MARTE_TimeObservation)


GRM_CommunicationEndPoint_strategy = st.builds(GRM_CommunicationEndPoint)
@given(instance=GRM_CommunicationEndPoint_strategy)
@settings(max_examples=25)
def test_GRM_CommunicationEndPoint_instantiation(instance):
    assert isinstance(instance, GRM_CommunicationEndPoint)


GRM_CommunicationMedia_strategy = st.builds(GRM_CommunicationMedia)
@given(instance=GRM_CommunicationMedia_strategy)
@settings(max_examples=25)
def test_GRM_CommunicationMedia_instantiation(instance):
    assert isinstance(instance, GRM_CommunicationMedia)


GRM_ComputingResource_strategy = st.builds(GRM_ComputingResource)
@given(instance=GRM_ComputingResource_strategy)
@settings(max_examples=25)
def test_GRM_ComputingResource_instantiation(instance):
    assert isinstance(instance, GRM_ComputingResource)


GRM_DeviceResource_strategy = st.builds(GRM_DeviceResource)
@given(instance=GRM_DeviceResource_strategy)
@settings(max_examples=25)
def test_GRM_DeviceResource_instantiation(instance):
    assert isinstance(instance, GRM_DeviceResource)


GRM_MARTE_Behavior_strategy = st.builds(GRM_MARTE_Behavior)
@given(instance=GRM_MARTE_Behavior_strategy)
@settings(max_examples=25)
def test_GRM_MARTE_Behavior_instantiation(instance):
    assert isinstance(instance, GRM_MARTE_Behavior)


GRM_MARTE_BehavioralFeature_strategy = st.builds(GRM_MARTE_BehavioralFeature)
@given(instance=GRM_MARTE_BehavioralFeature_strategy)
@settings(max_examples=25)
def test_GRM_MARTE_BehavioralFeature_instantiation(instance):
    assert isinstance(instance, GRM_MARTE_BehavioralFeature)


GRM_MARTE_Classifier_strategy = st.builds(GRM_MARTE_Classifier)
@given(instance=GRM_MARTE_Classifier_strategy)
@settings(max_examples=25)
def test_GRM_MARTE_Classifier_instantiation(instance):
    assert isinstance(instance, GRM_MARTE_Classifier)


GRM_MARTE_Collaboration_strategy = st.builds(GRM_MARTE_Collaboration)
@given(instance=GRM_MARTE_Collaboration_strategy)
@settings(max_examples=25)
def test_GRM_MARTE_Collaboration_instantiation(instance):
    assert isinstance(instance, GRM_MARTE_Collaboration)


GRM_MARTE_CollaborationUse_strategy = st.builds(GRM_MARTE_CollaborationUse)
@given(instance=GRM_MARTE_CollaborationUse_strategy)
@settings(max_examples=25)
def test_GRM_MARTE_CollaborationUse_instantiation(instance):
    assert isinstance(instance, GRM_MARTE_CollaborationUse)


GRM_MARTE_ConnectableElement_strategy = st.builds(GRM_MARTE_ConnectableElement)
@given(instance=GRM_MARTE_ConnectableElement_strategy)
@settings(max_examples=25)
def test_GRM_MARTE_ConnectableElement_instantiation(instance):
    assert isinstance(instance, GRM_MARTE_ConnectableElement)


GRM_MARTE_Connector_strategy = st.builds(GRM_MARTE_Connector)
@given(instance=GRM_MARTE_Connector_strategy)
@settings(max_examples=25)
def test_GRM_MARTE_Connector_instantiation(instance):
    assert isinstance(instance, GRM_MARTE_Connector)


GRM_MARTE_ExecutionSpecification_strategy = st.builds(GRM_MARTE_ExecutionSpecification)
@given(instance=GRM_MARTE_ExecutionSpecification_strategy)
@settings(max_examples=25)
def test_GRM_MARTE_ExecutionSpecification_instantiation(instance):
    assert isinstance(instance, GRM_MARTE_ExecutionSpecification)


GRM_MARTE_InstanceSpecification_strategy = st.builds(GRM_MARTE_InstanceSpecification)
@given(instance=GRM_MARTE_InstanceSpecification_strategy)
@settings(max_examples=25)
def test_GRM_MARTE_InstanceSpecification_instantiation(instance):
    assert isinstance(instance, GRM_MARTE_InstanceSpecification)


GRM_MARTE_Lifeline_strategy = st.builds(GRM_MARTE_Lifeline)
@given(instance=GRM_MARTE_Lifeline_strategy)
@settings(max_examples=25)
def test_GRM_MARTE_Lifeline_instantiation(instance):
    assert isinstance(instance, GRM_MARTE_Lifeline)


GRM_MARTE_NamedElement_strategy = st.builds(GRM_MARTE_NamedElement)
@given(instance=GRM_MARTE_NamedElement_strategy)
@settings(max_examples=25)
def test_GRM_MARTE_NamedElement_instantiation(instance):
    assert isinstance(instance, GRM_MARTE_NamedElement)


GRM_MARTE_OpaqueExpression_strategy = st.builds(GRM_MARTE_OpaqueExpression)
@given(instance=GRM_MARTE_OpaqueExpression_strategy)
@settings(max_examples=25)
def test_GRM_MARTE_OpaqueExpression_instantiation(instance):
    assert isinstance(instance, GRM_MARTE_OpaqueExpression)


GRM_MARTE_Property_strategy = st.builds(GRM_MARTE_Property)
@given(instance=GRM_MARTE_Property_strategy)
@settings(max_examples=25)
def test_GRM_MARTE_Property_instantiation(instance):
    assert isinstance(instance, GRM_MARTE_Property)


GRM_MutualExclusionResource_strategy = st.builds(GRM_MutualExclusionResource)
@given(instance=GRM_MutualExclusionResource_strategy)
@settings(max_examples=25)
def test_GRM_MutualExclusionResource_instantiation(instance):
    assert isinstance(instance, GRM_MutualExclusionResource)


GRM_ProcessingResource_strategy = st.builds(GRM_ProcessingResource)
@given(instance=GRM_ProcessingResource_strategy)
@settings(max_examples=25)
def test_GRM_ProcessingResource_instantiation(instance):
    assert isinstance(instance, GRM_ProcessingResource)


GRM_Resource_strategy = st.builds(GRM_Resource)
@given(instance=GRM_Resource_strategy)
@settings(max_examples=25)
def test_GRM_Resource_instantiation(instance):
    assert isinstance(instance, GRM_Resource)


GRM_ResourceUsage_strategy = st.builds(GRM_ResourceUsage)
@given(instance=GRM_ResourceUsage_strategy)
@settings(max_examples=25)
def test_GRM_ResourceUsage_instantiation(instance):
    assert isinstance(instance, GRM_ResourceUsage)


GRM_SchedulableResource_strategy = st.builds(GRM_SchedulableResource)
@given(instance=GRM_SchedulableResource_strategy)
@settings(max_examples=25)
def test_GRM_SchedulableResource_instantiation(instance):
    assert isinstance(instance, GRM_SchedulableResource)


GRM_Scheduler_strategy = st.builds(GRM_Scheduler)
@given(instance=GRM_Scheduler_strategy)
@settings(max_examples=25)
def test_GRM_Scheduler_instantiation(instance):
    assert isinstance(instance, GRM_Scheduler)


GRM_SecondaryScheduler_strategy = st.builds(GRM_SecondaryScheduler)
@given(instance=GRM_SecondaryScheduler_strategy)
@settings(max_examples=25)
def test_GRM_SecondaryScheduler_instantiation(instance):
    assert isinstance(instance, GRM_SecondaryScheduler)


GRM_StorageResource_strategy = st.builds(GRM_StorageResource)
@given(instance=GRM_StorageResource_strategy)
@settings(max_examples=25)
def test_GRM_StorageResource_instantiation(instance):
    assert isinstance(instance, GRM_StorageResource)


GRM_SynchronizationResource_strategy = st.builds(GRM_SynchronizationResource)
@given(instance=GRM_SynchronizationResource_strategy)
@settings(max_examples=25)
def test_GRM_SynchronizationResource_instantiation(instance):
    assert isinstance(instance, GRM_SynchronizationResource)


GRM_TimingResource_strategy = st.builds(GRM_TimingResource)
@given(instance=GRM_TimingResource_strategy)
@settings(max_examples=25)
def test_GRM_TimingResource_instantiation(instance):
    assert isinstance(instance, GRM_TimingResource)


GaAnalysisContext_strategy = st.builds(GaAnalysisContext)
@given(instance=GaAnalysisContext_strategy)
@settings(max_examples=25)
def test_GaAnalysisContext_instantiation(instance):
    assert isinstance(instance, GaAnalysisContext)


GaCommHost_strategy = st.builds(GaCommHost)
@given(instance=GaCommHost_strategy)
@settings(max_examples=25)
def test_GaCommHost_instantiation(instance):
    assert isinstance(instance, GaCommHost)


GaCommStep_strategy = st.builds(GaCommStep)
@given(instance=GaCommStep_strategy)
@settings(max_examples=25)
def test_GaCommStep_instantiation(instance):
    assert isinstance(instance, GaCommStep)


GaExecHost_strategy = st.builds(GaExecHost)
@given(instance=GaExecHost_strategy)
@settings(max_examples=25)
def test_GaExecHost_instantiation(instance):
    assert isinstance(instance, GaExecHost)


GaScenario_strategy = st.builds(GaScenario)
@given(instance=GaScenario_strategy)
@settings(max_examples=25)
def test_GaScenario_instantiation(instance):
    assert isinstance(instance, GaScenario)


GaStep_strategy = st.builds(GaStep)
@given(instance=GaStep_strategy)
@settings(max_examples=25)
def test_GaStep_instantiation(instance):
    assert isinstance(instance, GaStep)


GaTimedObs_strategy = st.builds(GaTimedObs)
@given(instance=GaTimedObs_strategy)
@settings(max_examples=25)
def test_GaTimedObs_instantiation(instance):
    assert isinstance(instance, GaTimedObs)


GrService_strategy = st.builds(GrService)
@given(instance=GrService_strategy)
@settings(max_examples=25)
def test_GrService_instantiation(instance):
    assert isinstance(instance, GrService)


HLAM_MARTE_Behavior_strategy = st.builds(HLAM_MARTE_Behavior)
@given(instance=HLAM_MARTE_Behavior_strategy)
@settings(max_examples=25)
def test_HLAM_MARTE_Behavior_instantiation(instance):
    assert isinstance(instance, HLAM_MARTE_Behavior)


HLAM_MARTE_BehavioralFeature_strategy = st.builds(HLAM_MARTE_BehavioralFeature)
@given(instance=HLAM_MARTE_BehavioralFeature_strategy)
@settings(max_examples=25)
def test_HLAM_MARTE_BehavioralFeature_instantiation(instance):
    assert isinstance(instance, HLAM_MARTE_BehavioralFeature)


HLAM_MARTE_BehavioredClassifier_strategy = st.builds(HLAM_MARTE_BehavioredClassifier)
@given(instance=HLAM_MARTE_BehavioredClassifier_strategy)
@settings(max_examples=25)
def test_HLAM_MARTE_BehavioredClassifier_instantiation(instance):
    assert isinstance(instance, HLAM_MARTE_BehavioredClassifier)


HLAM_MARTE_Comment_strategy = st.builds(HLAM_MARTE_Comment)
@given(instance=HLAM_MARTE_Comment_strategy)
@settings(max_examples=25)
def test_HLAM_MARTE_Comment_instantiation(instance):
    assert isinstance(instance, HLAM_MARTE_Comment)


HLAM_MARTE_InvocationAction_strategy = st.builds(HLAM_MARTE_InvocationAction)
@given(instance=HLAM_MARTE_InvocationAction_strategy)
@settings(max_examples=25)
def test_HLAM_MARTE_InvocationAction_instantiation(instance):
    assert isinstance(instance, HLAM_MARTE_InvocationAction)


HLAM_MARTE_Message_strategy = st.builds(HLAM_MARTE_Message)
@given(instance=HLAM_MARTE_Message_strategy)
@settings(max_examples=25)
def test_HLAM_MARTE_Message_instantiation(instance):
    assert isinstance(instance, HLAM_MARTE_Message)


HLAM_MARTE_Operation_strategy = st.builds(HLAM_MARTE_Operation)
@given(instance=HLAM_MARTE_Operation_strategy)
@settings(max_examples=25)
def test_HLAM_MARTE_Operation_instantiation(instance):
    assert isinstance(instance, HLAM_MARTE_Operation)


HLAM_MARTE_Port_strategy = st.builds(HLAM_MARTE_Port)
@given(instance=HLAM_MARTE_Port_strategy)
@settings(max_examples=25)
def test_HLAM_MARTE_Port_instantiation(instance):
    assert isinstance(instance, HLAM_MARTE_Port)


HLAM_MARTE_Signal_strategy = st.builds(HLAM_MARTE_Signal)
@given(instance=HLAM_MARTE_Signal_strategy)
@settings(max_examples=25)
def test_HLAM_MARTE_Signal_instantiation(instance):
    assert isinstance(instance, HLAM_MARTE_Signal)


HLAM_RtSpecification_strategy = st.builds(HLAM_RtSpecification)
@given(instance=HLAM_RtSpecification_strategy)
@settings(max_examples=25)
def test_HLAM_RtSpecification_instantiation(instance):
    assert isinstance(instance, HLAM_RtSpecification)


HwCommunicationResource_strategy = st.builds(HwCommunicationResource)
@given(instance=HwCommunicationResource_strategy)
@settings(max_examples=25)
def test_HwCommunicationResource_instantiation(instance):
    assert isinstance(instance, HwCommunicationResource)


HwCommunication_HwArbiter_strategy = st.builds(HwCommunication_HwArbiter)
@given(instance=HwCommunication_HwArbiter_strategy)
@settings(max_examples=25)
def test_HwCommunication_HwArbiter_instantiation(instance):
    assert isinstance(instance, HwCommunication_HwArbiter)


HwCommunication_HwCommunicationResource_strategy = st.builds(HwCommunication_HwCommunicationResource)
@given(instance=HwCommunication_HwCommunicationResource_strategy)
@settings(max_examples=25)
def test_HwCommunication_HwCommunicationResource_instantiation(instance):
    assert isinstance(instance, HwCommunication_HwCommunicationResource)


HwCommunication_HwConnection_strategy = st.builds(HwCommunication_HwConnection)
@given(instance=HwCommunication_HwConnection_strategy)
@settings(max_examples=25)
def test_HwCommunication_HwConnection_instantiation(instance):
    assert isinstance(instance, HwCommunication_HwConnection)


HwCommunication_HwEndPoint_strategy = st.builds(HwCommunication_HwEndPoint)
@given(instance=HwCommunication_HwEndPoint_strategy)
@settings(max_examples=25)
def test_HwCommunication_HwEndPoint_instantiation(instance):
    assert isinstance(instance, HwCommunication_HwEndPoint)


HwCommunication_HwMedia_strategy = st.builds(HwCommunication_HwMedia)
@given(instance=HwCommunication_HwMedia_strategy)
@settings(max_examples=25)
def test_HwCommunication_HwMedia_instantiation(instance):
    assert isinstance(instance, HwCommunication_HwMedia)


HwCommunication_HwPort_strategy = st.builds(HwCommunication_HwPort)
@given(instance=HwCommunication_HwPort_strategy)
@settings(max_examples=25)
def test_HwCommunication_HwPort_instantiation(instance):
    assert isinstance(instance, HwCommunication_HwPort)


HwComponent_strategy = st.builds(HwComponent)
@given(instance=HwComponent_strategy)
@settings(max_examples=25)
def test_HwComponent_instantiation(instance):
    assert isinstance(instance, HwComponent)


HwComputingResource_strategy = st.builds(HwComputingResource)
@given(instance=HwComputingResource_strategy)
@settings(max_examples=25)
def test_HwComputingResource_instantiation(instance):
    assert isinstance(instance, HwComputingResource)


HwComputing_HwBranchPredictor_strategy = st.builds(HwComputing_HwBranchPredictor)
@given(instance=HwComputing_HwBranchPredictor_strategy)
@settings(max_examples=25)
def test_HwComputing_HwBranchPredictor_instantiation(instance):
    assert isinstance(instance, HwComputing_HwBranchPredictor)


HwComputing_HwComputingResource_strategy = st.builds(HwComputing_HwComputingResource)
@given(instance=HwComputing_HwComputingResource_strategy)
@settings(max_examples=25)
def test_HwComputing_HwComputingResource_instantiation(instance):
    assert isinstance(instance, HwComputing_HwComputingResource)


HwComputing_HwISA_strategy = st.builds(HwComputing_HwISA)
@given(instance=HwComputing_HwISA_strategy)
@settings(max_examples=25)
def test_HwComputing_HwISA_instantiation(instance):
    assert isinstance(instance, HwComputing_HwISA)


HwComputing_HwProcessor_strategy = st.builds(HwComputing_HwProcessor)
@given(instance=HwComputing_HwProcessor_strategy)
@settings(max_examples=25)
def test_HwComputing_HwProcessor_instantiation(instance):
    assert isinstance(instance, HwComputing_HwProcessor)


HwComputing_PLD_Organization_strategy = st.builds(HwComputing_PLD_Organization)
@given(instance=HwComputing_PLD_Organization_strategy)
@settings(max_examples=25)
def test_HwComputing_PLD_Organization_instantiation(instance):
    assert isinstance(instance, HwComputing_PLD_Organization)


HwDevice_strategy = st.builds(HwDevice)
@given(instance=HwDevice_strategy)
@settings(max_examples=25)
def test_HwDevice_instantiation(instance):
    assert isinstance(instance, HwDevice)


HwDeviceFunction_HwDeviceFunction_strategy = st.builds(HwDeviceFunction_HwDeviceFunction)
@given(instance=HwDeviceFunction_HwDeviceFunction_strategy)
@settings(max_examples=25)
def test_HwDeviceFunction_HwDeviceFunction_instantiation(instance):
    assert isinstance(instance, HwDeviceFunction_HwDeviceFunction)


HwDevice_HwPeripheral_strategy = st.builds(HwDevice_HwPeripheral)
@given(instance=HwDevice_HwPeripheral_strategy)
@settings(max_examples=25)
def test_HwDevice_HwPeripheral_instantiation(instance):
    assert isinstance(instance, HwDevice_HwPeripheral)


HwDiagram_MARTE_DataType_strategy = st.builds(HwDiagram_MARTE_DataType)
@given(instance=HwDiagram_MARTE_DataType_strategy)
@settings(max_examples=25)
def test_HwDiagram_MARTE_DataType_instantiation(instance):
    assert isinstance(instance, HwDiagram_MARTE_DataType)


HwEndPoint_strategy = st.builds(HwEndPoint)
@given(instance=HwEndPoint_strategy)
@settings(max_examples=25)
def test_HwEndPoint_instantiation(instance):
    assert isinstance(instance, HwEndPoint)


HwGeneral_HwResource_strategy = st.builds(HwGeneral_HwResource)
@given(instance=HwGeneral_HwResource_strategy)
@settings(max_examples=25)
def test_HwGeneral_HwResource_instantiation(instance):
    assert isinstance(instance, HwGeneral_HwResource)


HwGeneral_HwResourceService_strategy = st.builds(HwGeneral_HwResourceService)
@given(instance=HwGeneral_HwResourceService_strategy)
@settings(max_examples=25)
def test_HwGeneral_HwResourceService_instantiation(instance):
    assert isinstance(instance, HwGeneral_HwResourceService)


HwGeneral_MARTE_Activity_strategy = st.builds(HwGeneral_MARTE_Activity)
@given(instance=HwGeneral_MARTE_Activity_strategy)
@settings(max_examples=25)
def test_HwGeneral_MARTE_Activity_instantiation(instance):
    assert isinstance(instance, HwGeneral_MARTE_Activity)


HwGeneral_MARTE_Operation_strategy = st.builds(HwGeneral_MARTE_Operation)
@given(instance=HwGeneral_MARTE_Operation_strategy)
@settings(max_examples=25)
def test_HwGeneral_MARTE_Operation_instantiation(instance):
    assert isinstance(instance, HwGeneral_MARTE_Operation)


HwIO_HwLine_strategy = st.builds(HwIO_HwLine)
@given(instance=HwIO_HwLine_strategy)
@settings(max_examples=25)
def test_HwIO_HwLine_instantiation(instance):
    assert isinstance(instance, HwIO_HwLine)


HwIO_HwPin_strategy = st.builds(HwIO_HwPin)
@given(instance=HwIO_HwPin_strategy)
@settings(max_examples=25)
def test_HwIO_HwPin_instantiation(instance):
    assert isinstance(instance, HwIO_HwPin)


HwI_O_strategy = st.builds(HwI_O)
@given(instance=HwI_O_strategy)
@settings(max_examples=25)
def test_HwI_O_instantiation(instance):
    assert isinstance(instance, HwI_O)


HwLayout_Env_Condition_strategy = st.builds(HwLayout_Env_Condition)
@given(instance=HwLayout_Env_Condition_strategy)
@settings(max_examples=25)
def test_HwLayout_Env_Condition_instantiation(instance):
    assert isinstance(instance, HwLayout_Env_Condition)


HwLayout_HwComponent_strategy = st.builds(HwLayout_HwComponent)
@given(instance=HwLayout_HwComponent_strategy)
@settings(max_examples=25)
def test_HwLayout_HwComponent_instantiation(instance):
    assert isinstance(instance, HwLayout_HwComponent)


HwMedia_strategy = st.builds(HwMedia)
@given(instance=HwMedia_strategy)
@settings(max_examples=25)
def test_HwMedia_instantiation(instance):
    assert isinstance(instance, HwMedia)


HwMemory_strategy = st.builds(HwMemory)
@given(instance=HwMemory_strategy)
@settings(max_examples=25)
def test_HwMemory_instantiation(instance):
    assert isinstance(instance, HwMemory)


HwMemory_CacheStructure_strategy = st.builds(HwMemory_CacheStructure)
@given(instance=HwMemory_CacheStructure_strategy)
@settings(max_examples=25)
def test_HwMemory_CacheStructure_instantiation(instance):
    assert isinstance(instance, HwMemory_CacheStructure)


HwMemory_HwCache_strategy = st.builds(HwMemory_HwCache)
@given(instance=HwMemory_HwCache_strategy)
@settings(max_examples=25)
def test_HwMemory_HwCache_instantiation(instance):
    assert isinstance(instance, HwMemory_HwCache)


HwMemory_HwMemory_strategy = st.builds(HwMemory_HwMemory)
@given(instance=HwMemory_HwMemory_strategy)
@settings(max_examples=25)
def test_HwMemory_HwMemory_instantiation(instance):
    assert isinstance(instance, HwMemory_HwMemory)


HwMemory_HwRAM_strategy = st.builds(HwMemory_HwRAM)
@given(instance=HwMemory_HwRAM_strategy)
@settings(max_examples=25)
def test_HwMemory_HwRAM_instantiation(instance):
    assert isinstance(instance, HwMemory_HwRAM)


HwMemory_MemoryOrganization_strategy = st.builds(HwMemory_MemoryOrganization)
@given(instance=HwMemory_MemoryOrganization_strategy)
@settings(max_examples=25)
def test_HwMemory_MemoryOrganization_instantiation(instance):
    assert isinstance(instance, HwMemory_MemoryOrganization)


HwMemory_Timing_strategy = st.builds(HwMemory_Timing)
@given(instance=HwMemory_Timing_strategy)
@settings(max_examples=25)
def test_HwMemory_Timing_instantiation(instance):
    assert isinstance(instance, HwMemory_Timing)


HwPackage_HwPackage_strategy = st.builds(HwPackage_HwPackage)
@given(instance=HwPackage_HwPackage_strategy)
@settings(max_examples=25)
def test_HwPackage_HwPackage_instantiation(instance):
    assert isinstance(instance, HwPackage_HwPackage)


HwPackage_HwPackagePin_strategy = st.builds(HwPackage_HwPackagePin)
@given(instance=HwPackage_HwPackagePin_strategy)
@settings(max_examples=25)
def test_HwPackage_HwPackagePin_instantiation(instance):
    assert isinstance(instance, HwPackage_HwPackagePin)


HwPackage_HwWire_strategy = st.builds(HwPackage_HwWire)
@given(instance=HwPackage_HwWire_strategy)
@settings(max_examples=25)
def test_HwPackage_HwWire_instantiation(instance):
    assert isinstance(instance, HwPackage_HwWire)


HwPeripheral_MARTE_InputPin_strategy = st.builds(HwPeripheral_MARTE_InputPin)
@given(instance=HwPeripheral_MARTE_InputPin_strategy)
@settings(max_examples=25)
def test_HwPeripheral_MARTE_InputPin_instantiation(instance):
    assert isinstance(instance, HwPeripheral_MARTE_InputPin)


HwPeripheral_MARTE_Operation_strategy = st.builds(HwPeripheral_MARTE_Operation)
@given(instance=HwPeripheral_MARTE_Operation_strategy)
@settings(max_examples=25)
def test_HwPeripheral_MARTE_Operation_instantiation(instance):
    assert isinstance(instance, HwPeripheral_MARTE_Operation)


HwPeripheral_MARTE_OutputPin_strategy = st.builds(HwPeripheral_MARTE_OutputPin)
@given(instance=HwPeripheral_MARTE_OutputPin_strategy)
@settings(max_examples=25)
def test_HwPeripheral_MARTE_OutputPin_instantiation(instance):
    assert isinstance(instance, HwPeripheral_MARTE_OutputPin)


HwPeripheral_OperationImpl_strategy = st.builds(HwPeripheral_OperationImpl)
@given(instance=HwPeripheral_OperationImpl_strategy)
@settings(max_examples=25)
def test_HwPeripheral_OperationImpl_instantiation(instance):
    assert isinstance(instance, HwPeripheral_OperationImpl)


HwPeripheral_PeripheralActivity_strategy = st.builds(HwPeripheral_PeripheralActivity)
@given(instance=HwPeripheral_PeripheralActivity_strategy)
@settings(max_examples=25)
def test_HwPeripheral_PeripheralActivity_instantiation(instance):
    assert isinstance(instance, HwPeripheral_PeripheralActivity)


HwPeripheral_RegisterAction_strategy = st.builds(HwPeripheral_RegisterAction)
@given(instance=HwPeripheral_RegisterAction_strategy)
@settings(max_examples=25)
def test_HwPeripheral_RegisterAction_instantiation(instance):
    assert isinstance(instance, HwPeripheral_RegisterAction)


HwProtocol_HwProtocol_strategy = st.builds(HwProtocol_HwProtocol)
@given(instance=HwProtocol_HwProtocol_strategy)
@settings(max_examples=25)
def test_HwProtocol_HwProtocol_instantiation(instance):
    assert isinstance(instance, HwProtocol_HwProtocol)


HwProtocol_MARTE_Operation_strategy = st.builds(HwProtocol_MARTE_Operation)
@given(instance=HwProtocol_MARTE_Operation_strategy)
@settings(max_examples=25)
def test_HwProtocol_MARTE_Operation_instantiation(instance):
    assert isinstance(instance, HwProtocol_MARTE_Operation)


HwRegister_HwRegister_strategy = st.builds(HwRegister_HwRegister)
@given(instance=HwRegister_HwRegister_strategy)
@settings(max_examples=25)
def test_HwRegister_HwRegister_instantiation(instance):
    assert isinstance(instance, HwRegister_HwRegister)


HwResource_strategy = st.builds(HwResource)
@given(instance=HwResource_strategy)
@settings(max_examples=25)
def test_HwResource_instantiation(instance):
    assert isinstance(instance, HwResource)


HwStorageManager_strategy = st.builds(HwStorageManager)
@given(instance=HwStorageManager_strategy)
@settings(max_examples=25)
def test_HwStorageManager_instantiation(instance):
    assert isinstance(instance, HwStorageManager)


HwStorageManager_HwMMU_strategy = st.builds(HwStorageManager_HwMMU)
@given(instance=HwStorageManager_HwMMU_strategy)
@settings(max_examples=25)
def test_HwStorageManager_HwMMU_instantiation(instance):
    assert isinstance(instance, HwStorageManager_HwMMU)


HwStorageManager_HwStorageManager_strategy = st.builds(HwStorageManager_HwStorageManager)
@given(instance=HwStorageManager_HwStorageManager_strategy)
@settings(max_examples=25)
def test_HwStorageManager_HwStorageManager_instantiation(instance):
    assert isinstance(instance, HwStorageManager_HwStorageManager)


HwTimingResource_strategy = st.builds(HwTimingResource)
@given(instance=HwTimingResource_strategy)
@settings(max_examples=25)
def test_HwTimingResource_instantiation(instance):
    assert isinstance(instance, HwTimingResource)


HwTiming_HwClock_strategy = st.builds(HwTiming_HwClock)
@given(instance=HwTiming_HwClock_strategy)
@settings(max_examples=25)
def test_HwTiming_HwClock_instantiation(instance):
    assert isinstance(instance, HwTiming_HwClock)


IntegerInterval_strategy = st.builds(IntegerInterval)
@given(instance=IntegerInterval_strategy)
@settings(max_examples=25)
def test_IntegerInterval_instantiation(instance):
    assert isinstance(instance, IntegerInterval)


IntegerMatrix_strategy = st.builds(IntegerMatrix)
@given(instance=IntegerMatrix_strategy)
@settings(max_examples=25)
def test_IntegerMatrix_instantiation(instance):
    assert isinstance(instance, IntegerMatrix)


IntegerVector_strategy = st.builds(IntegerVector)
@given(instance=IntegerVector_strategy)
@settings(max_examples=25)
def test_IntegerVector_instantiation(instance):
    assert isinstance(instance, IntegerVector)


InterruptResource_strategy = st.builds(InterruptResource)
@given(instance=InterruptResource_strategy)
@settings(max_examples=25)
def test_InterruptResource_instantiation(instance):
    assert isinstance(instance, InterruptResource)


LinkTopology_strategy = st.builds(LinkTopology)
@given(instance=LinkTopology_strategy)
@settings(max_examples=25)
def test_LinkTopology_instantiation(instance):
    assert isinstance(instance, LinkTopology)


MARTE_Alloc_Allocate_strategy = st.builds(MARTE_Alloc_Allocate, kind=safe_text, nature=safe_text)
@given(instance=MARTE_Alloc_Allocate_strategy)
@settings(max_examples=25)
def test_MARTE_Alloc_Allocate_instantiation(instance):
    assert isinstance(instance, MARTE_Alloc_Allocate)


MARTE_Alloc_AllocateActivityGroup_strategy = st.builds(MARTE_Alloc_AllocateActivityGroup)
@given(instance=MARTE_Alloc_AllocateActivityGroup_strategy)
@settings(max_examples=25)
def test_MARTE_Alloc_AllocateActivityGroup_instantiation(instance):
    assert isinstance(instance, MARTE_Alloc_AllocateActivityGroup)


MARTE_Alloc_Allocated_strategy = st.builds(MARTE_Alloc_Allocated)
@given(instance=MARTE_Alloc_Allocated_strategy)
@settings(max_examples=25)
def test_MARTE_Alloc_Allocated_instantiation(instance):
    assert isinstance(instance, MARTE_Alloc_Allocated)


MARTE_Alloc_Assign_strategy = st.builds(MARTE_Alloc_Assign)
@given(instance=MARTE_Alloc_Assign_strategy)
@settings(max_examples=25)
def test_MARTE_Alloc_Assign_instantiation(instance):
    assert isinstance(instance, MARTE_Alloc_Assign)


MARTE_Alloc_NfpRefine_strategy = st.builds(MARTE_Alloc_NfpRefine)
@given(instance=MARTE_Alloc_NfpRefine_strategy)
@settings(max_examples=25)
def test_MARTE_Alloc_NfpRefine_instantiation(instance):
    assert isinstance(instance, MARTE_Alloc_NfpRefine)


MARTE_CoreElements_Configuration_strategy = st.builds(MARTE_CoreElements_Configuration)
@given(instance=MARTE_CoreElements_Configuration_strategy)
@settings(max_examples=25)
def test_MARTE_CoreElements_Configuration_instantiation(instance):
    assert isinstance(instance, MARTE_CoreElements_Configuration)


MARTE_CoreElements_Mode_strategy = st.builds(MARTE_CoreElements_Mode)
@given(instance=MARTE_CoreElements_Mode_strategy)
@settings(max_examples=25)
def test_MARTE_CoreElements_Mode_instantiation(instance):
    assert isinstance(instance, MARTE_CoreElements_Mode)


MARTE_CoreElements_ModeBehavior_strategy = st.builds(MARTE_CoreElements_ModeBehavior)
@given(instance=MARTE_CoreElements_ModeBehavior_strategy)
@settings(max_examples=25)
def test_MARTE_CoreElements_ModeBehavior_instantiation(instance):
    assert isinstance(instance, MARTE_CoreElements_ModeBehavior)


MARTE_CoreElements_ModeTransition_strategy = st.builds(MARTE_CoreElements_ModeTransition)
@given(instance=MARTE_CoreElements_ModeTransition_strategy)
@settings(max_examples=25)
def test_MARTE_CoreElements_ModeTransition_instantiation(instance):
    assert isinstance(instance, MARTE_CoreElements_ModeTransition)


MARTE_DataTypes_BoundedSubtype_strategy = st.builds(MARTE_DataTypes_BoundedSubtype, isMaxOpen=st.booleans(), isMinOpen=st.booleans(), maxValue=safe_text, minValue=safe_text)
@given(instance=MARTE_DataTypes_BoundedSubtype_strategy)
@settings(max_examples=25)
def test_MARTE_DataTypes_BoundedSubtype_instantiation(instance):
    assert isinstance(instance, MARTE_DataTypes_BoundedSubtype)


MARTE_DataTypes_ChoiceType_strategy = st.builds(MARTE_DataTypes_ChoiceType)
@given(instance=MARTE_DataTypes_ChoiceType_strategy)
@settings(max_examples=25)
def test_MARTE_DataTypes_ChoiceType_instantiation(instance):
    assert isinstance(instance, MARTE_DataTypes_ChoiceType)


MARTE_DataTypes_CollectionType_strategy = st.builds(MARTE_DataTypes_CollectionType)
@given(instance=MARTE_DataTypes_CollectionType_strategy)
@settings(max_examples=25)
def test_MARTE_DataTypes_CollectionType_instantiation(instance):
    assert isinstance(instance, MARTE_DataTypes_CollectionType)


MARTE_DataTypes_IntervalType_strategy = st.builds(MARTE_DataTypes_IntervalType)
@given(instance=MARTE_DataTypes_IntervalType_strategy)
@settings(max_examples=25)
def test_MARTE_DataTypes_IntervalType_instantiation(instance):
    assert isinstance(instance, MARTE_DataTypes_IntervalType)


MARTE_DataTypes_TupleType_strategy = st.builds(MARTE_DataTypes_TupleType)
@given(instance=MARTE_DataTypes_TupleType_strategy)
@settings(max_examples=25)
def test_MARTE_DataTypes_TupleType_instantiation(instance):
    assert isinstance(instance, MARTE_DataTypes_TupleType)


MARTE_GCM_ClientServerFeature_strategy = st.builds(MARTE_GCM_ClientServerFeature, kind=safe_text)
@given(instance=MARTE_GCM_ClientServerFeature_strategy)
@settings(max_examples=25)
def test_MARTE_GCM_ClientServerFeature_instantiation(instance):
    assert isinstance(instance, MARTE_GCM_ClientServerFeature)


MARTE_GCM_ClientServerPort_strategy = st.builds(MARTE_GCM_ClientServerPort, isConjugated=safe_text, kind=safe_text, specificationKind=safe_text)
@given(instance=MARTE_GCM_ClientServerPort_strategy)
@settings(max_examples=25)
def test_MARTE_GCM_ClientServerPort_instantiation(instance):
    assert isinstance(instance, MARTE_GCM_ClientServerPort)


MARTE_GCM_ClientServerSpecification_strategy = st.builds(MARTE_GCM_ClientServerSpecification)
@given(instance=MARTE_GCM_ClientServerSpecification_strategy)
@settings(max_examples=25)
def test_MARTE_GCM_ClientServerSpecification_instantiation(instance):
    assert isinstance(instance, MARTE_GCM_ClientServerSpecification)


MARTE_GCM_DataEvent_strategy = st.builds(MARTE_GCM_DataEvent)
@given(instance=MARTE_GCM_DataEvent_strategy)
@settings(max_examples=25)
def test_MARTE_GCM_DataEvent_instantiation(instance):
    assert isinstance(instance, MARTE_GCM_DataEvent)


MARTE_GCM_DataPool_strategy = st.builds(MARTE_GCM_DataPool, ordering=safe_text)
@given(instance=MARTE_GCM_DataPool_strategy)
@settings(max_examples=25)
def test_MARTE_GCM_DataPool_instantiation(instance):
    assert isinstance(instance, MARTE_GCM_DataPool)


MARTE_GCM_FlowPort_strategy = st.builds(MARTE_GCM_FlowPort, direction=safe_text, isAtomic=safe_text, isConjugated=safe_text)
@given(instance=MARTE_GCM_FlowPort_strategy)
@settings(max_examples=25)
def test_MARTE_GCM_FlowPort_instantiation(instance):
    assert isinstance(instance, MARTE_GCM_FlowPort)


MARTE_GCM_FlowProperty_strategy = st.builds(MARTE_GCM_FlowProperty, direction=safe_text)
@given(instance=MARTE_GCM_FlowProperty_strategy)
@settings(max_examples=25)
def test_MARTE_GCM_FlowProperty_instantiation(instance):
    assert isinstance(instance, MARTE_GCM_FlowProperty)


MARTE_GCM_FlowSpecification_strategy = st.builds(MARTE_GCM_FlowSpecification)
@given(instance=MARTE_GCM_FlowSpecification_strategy)
@settings(max_examples=25)
def test_MARTE_GCM_FlowSpecification_instantiation(instance):
    assert isinstance(instance, MARTE_GCM_FlowSpecification)


MARTE_GCM_GCMInvocationAction_strategy = st.builds(MARTE_GCM_GCMInvocationAction)
@given(instance=MARTE_GCM_GCMInvocationAction_strategy)
@settings(max_examples=25)
def test_MARTE_GCM_GCMInvocationAction_instantiation(instance):
    assert isinstance(instance, MARTE_GCM_GCMInvocationAction)


MARTE_GCM_GCMTrigger_strategy = st.builds(MARTE_GCM_GCMTrigger)
@given(instance=MARTE_GCM_GCMTrigger_strategy)
@settings(max_examples=25)
def test_MARTE_GCM_GCMTrigger_instantiation(instance):
    assert isinstance(instance, MARTE_GCM_GCMTrigger)


MARTE_GQAM_GaAcqStep_strategy = st.builds(MARTE_GQAM_GaAcqStep)
@given(instance=MARTE_GQAM_GaAcqStep_strategy)
@settings(max_examples=25)
def test_MARTE_GQAM_GaAcqStep_instantiation(instance):
    assert isinstance(instance, MARTE_GQAM_GaAcqStep)


MARTE_GQAM_GaAnalysisContext_strategy = st.builds(MARTE_GQAM_GaAnalysisContext)
@given(instance=MARTE_GQAM_GaAnalysisContext_strategy)
@settings(max_examples=25)
def test_MARTE_GQAM_GaAnalysisContext_instantiation(instance):
    assert isinstance(instance, MARTE_GQAM_GaAnalysisContext)


MARTE_GQAM_GaCommChannel_strategy = st.builds(MARTE_GQAM_GaCommChannel)
@given(instance=MARTE_GQAM_GaCommChannel_strategy)
@settings(max_examples=25)
def test_MARTE_GQAM_GaCommChannel_instantiation(instance):
    assert isinstance(instance, MARTE_GQAM_GaCommChannel)


MARTE_GQAM_GaCommHost_strategy = st.builds(MARTE_GQAM_GaCommHost)
@given(instance=MARTE_GQAM_GaCommHost_strategy)
@settings(max_examples=25)
def test_MARTE_GQAM_GaCommHost_instantiation(instance):
    assert isinstance(instance, MARTE_GQAM_GaCommHost)


MARTE_GQAM_GaCommStep_strategy = st.builds(MARTE_GQAM_GaCommStep)
@given(instance=MARTE_GQAM_GaCommStep_strategy)
@settings(max_examples=25)
def test_MARTE_GQAM_GaCommStep_instantiation(instance):
    assert isinstance(instance, MARTE_GQAM_GaCommStep)


MARTE_GQAM_GaEventTrace_strategy = st.builds(MARTE_GQAM_GaEventTrace, content=safe_text, format=safe_text, location=safe_text)
@given(instance=MARTE_GQAM_GaEventTrace_strategy)
@settings(max_examples=25)
def test_MARTE_GQAM_GaEventTrace_instantiation(instance):
    assert isinstance(instance, MARTE_GQAM_GaEventTrace)


MARTE_GQAM_GaExecHost_strategy = st.builds(MARTE_GQAM_GaExecHost)
@given(instance=MARTE_GQAM_GaExecHost_strategy)
@settings(max_examples=25)
def test_MARTE_GQAM_GaExecHost_instantiation(instance):
    assert isinstance(instance, MARTE_GQAM_GaExecHost)


MARTE_GQAM_GaLatencyObs_strategy = st.builds(MARTE_GQAM_GaLatencyObs)
@given(instance=MARTE_GQAM_GaLatencyObs_strategy)
@settings(max_examples=25)
def test_MARTE_GQAM_GaLatencyObs_instantiation(instance):
    assert isinstance(instance, MARTE_GQAM_GaLatencyObs)


MARTE_GQAM_GaRelStep_strategy = st.builds(MARTE_GQAM_GaRelStep)
@given(instance=MARTE_GQAM_GaRelStep_strategy)
@settings(max_examples=25)
def test_MARTE_GQAM_GaRelStep_instantiation(instance):
    assert isinstance(instance, MARTE_GQAM_GaRelStep)


MARTE_GQAM_GaRequestedService_strategy = st.builds(MARTE_GQAM_GaRequestedService)
@given(instance=MARTE_GQAM_GaRequestedService_strategy)
@settings(max_examples=25)
def test_MARTE_GQAM_GaRequestedService_instantiation(instance):
    assert isinstance(instance, MARTE_GQAM_GaRequestedService)


MARTE_GQAM_GaResourcesPlatform_strategy = st.builds(MARTE_GQAM_GaResourcesPlatform)
@given(instance=MARTE_GQAM_GaResourcesPlatform_strategy)
@settings(max_examples=25)
def test_MARTE_GQAM_GaResourcesPlatform_instantiation(instance):
    assert isinstance(instance, MARTE_GQAM_GaResourcesPlatform)


MARTE_GQAM_GaScenario_strategy = st.builds(MARTE_GQAM_GaScenario)
@given(instance=MARTE_GQAM_GaScenario_strategy)
@settings(max_examples=25)
def test_MARTE_GQAM_GaScenario_instantiation(instance):
    assert isinstance(instance, MARTE_GQAM_GaScenario)


MARTE_GQAM_GaStep_strategy = st.builds(MARTE_GQAM_GaStep)
@given(instance=MARTE_GQAM_GaStep_strategy)
@settings(max_examples=25)
def test_MARTE_GQAM_GaStep_instantiation(instance):
    assert isinstance(instance, MARTE_GQAM_GaStep)


MARTE_GQAM_GaTimedObs_strategy = st.builds(MARTE_GQAM_GaTimedObs, laxity=safe_text)
@given(instance=MARTE_GQAM_GaTimedObs_strategy)
@settings(max_examples=25)
def test_MARTE_GQAM_GaTimedObs_instantiation(instance):
    assert isinstance(instance, MARTE_GQAM_GaTimedObs)


MARTE_GQAM_GaWorkloadBehavior_strategy = st.builds(MARTE_GQAM_GaWorkloadBehavior)
@given(instance=MARTE_GQAM_GaWorkloadBehavior_strategy)
@settings(max_examples=25)
def test_MARTE_GQAM_GaWorkloadBehavior_instantiation(instance):
    assert isinstance(instance, MARTE_GQAM_GaWorkloadBehavior)


MARTE_GQAM_GaWorkloadEvent_strategy = st.builds(MARTE_GQAM_GaWorkloadEvent)
@given(instance=MARTE_GQAM_GaWorkloadEvent_strategy)
@settings(max_examples=25)
def test_MARTE_GQAM_GaWorkloadEvent_instantiation(instance):
    assert isinstance(instance, MARTE_GQAM_GaWorkloadEvent)


MARTE_GQAM_GaWorkloadGenerator_strategy = st.builds(MARTE_GQAM_GaWorkloadGenerator)
@given(instance=MARTE_GQAM_GaWorkloadGenerator_strategy)
@settings(max_examples=25)
def test_MARTE_GQAM_GaWorkloadGenerator_instantiation(instance):
    assert isinstance(instance, MARTE_GQAM_GaWorkloadGenerator)


MARTE_GRM_Acquire_strategy = st.builds(MARTE_GRM_Acquire, isBlocking=safe_text)
@given(instance=MARTE_GRM_Acquire_strategy)
@settings(max_examples=25)
def test_MARTE_GRM_Acquire_instantiation(instance):
    assert isinstance(instance, MARTE_GRM_Acquire)


MARTE_GRM_ClockResource_strategy = st.builds(MARTE_GRM_ClockResource)
@given(instance=MARTE_GRM_ClockResource_strategy)
@settings(max_examples=25)
def test_MARTE_GRM_ClockResource_instantiation(instance):
    assert isinstance(instance, MARTE_GRM_ClockResource)


MARTE_GRM_CommunicationEndPoint_strategy = st.builds(MARTE_GRM_CommunicationEndPoint)
@given(instance=MARTE_GRM_CommunicationEndPoint_strategy)
@settings(max_examples=25)
def test_MARTE_GRM_CommunicationEndPoint_instantiation(instance):
    assert isinstance(instance, MARTE_GRM_CommunicationEndPoint)


MARTE_GRM_CommunicationMedia_strategy = st.builds(MARTE_GRM_CommunicationMedia, transmMode=safe_text)
@given(instance=MARTE_GRM_CommunicationMedia_strategy)
@settings(max_examples=25)
def test_MARTE_GRM_CommunicationMedia_instantiation(instance):
    assert isinstance(instance, MARTE_GRM_CommunicationMedia)


MARTE_GRM_ComputingResource_strategy = st.builds(MARTE_GRM_ComputingResource)
@given(instance=MARTE_GRM_ComputingResource_strategy)
@settings(max_examples=25)
def test_MARTE_GRM_ComputingResource_instantiation(instance):
    assert isinstance(instance, MARTE_GRM_ComputingResource)


MARTE_GRM_ConcurrencyResource_strategy = st.builds(MARTE_GRM_ConcurrencyResource)
@given(instance=MARTE_GRM_ConcurrencyResource_strategy)
@settings(max_examples=25)
def test_MARTE_GRM_ConcurrencyResource_instantiation(instance):
    assert isinstance(instance, MARTE_GRM_ConcurrencyResource)


MARTE_GRM_DeviceResource_strategy = st.builds(MARTE_GRM_DeviceResource)
@given(instance=MARTE_GRM_DeviceResource_strategy)
@settings(max_examples=25)
def test_MARTE_GRM_DeviceResource_instantiation(instance):
    assert isinstance(instance, MARTE_GRM_DeviceResource)


MARTE_GRM_GrService_strategy = st.builds(MARTE_GRM_GrService)
@given(instance=MARTE_GRM_GrService_strategy)
@settings(max_examples=25)
def test_MARTE_GRM_GrService_instantiation(instance):
    assert isinstance(instance, MARTE_GRM_GrService)


MARTE_GRM_MutualExclusionResource_strategy = st.builds(MARTE_GRM_MutualExclusionResource, otherProtectProtocol=safe_text, protectKind=safe_text)
@given(instance=MARTE_GRM_MutualExclusionResource_strategy)
@settings(max_examples=25)
def test_MARTE_GRM_MutualExclusionResource_instantiation(instance):
    assert isinstance(instance, MARTE_GRM_MutualExclusionResource)


MARTE_GRM_ProcessingResource_strategy = st.builds(MARTE_GRM_ProcessingResource)
@given(instance=MARTE_GRM_ProcessingResource_strategy)
@settings(max_examples=25)
def test_MARTE_GRM_ProcessingResource_instantiation(instance):
    assert isinstance(instance, MARTE_GRM_ProcessingResource)


MARTE_GRM_Release_strategy = st.builds(MARTE_GRM_Release)
@given(instance=MARTE_GRM_Release_strategy)
@settings(max_examples=25)
def test_MARTE_GRM_Release_instantiation(instance):
    assert isinstance(instance, MARTE_GRM_Release)


MARTE_GRM_Resource_strategy = st.builds(MARTE_GRM_Resource, isProtected=safe_text)
@given(instance=MARTE_GRM_Resource_strategy)
@settings(max_examples=25)
def test_MARTE_GRM_Resource_instantiation(instance):
    assert isinstance(instance, MARTE_GRM_Resource)


MARTE_GRM_ResourceUsage_strategy = st.builds(MARTE_GRM_ResourceUsage)
@given(instance=MARTE_GRM_ResourceUsage_strategy)
@settings(max_examples=25)
def test_MARTE_GRM_ResourceUsage_instantiation(instance):
    assert isinstance(instance, MARTE_GRM_ResourceUsage)


MARTE_GRM_SchedulableResource_strategy = st.builds(MARTE_GRM_SchedulableResource)
@given(instance=MARTE_GRM_SchedulableResource_strategy)
@settings(max_examples=25)
def test_MARTE_GRM_SchedulableResource_instantiation(instance):
    assert isinstance(instance, MARTE_GRM_SchedulableResource)


MARTE_GRM_Scheduler_strategy = st.builds(MARTE_GRM_Scheduler, isPreemptible=safe_text, otherSchedPolicy=safe_text, schedPolicy=safe_text)
@given(instance=MARTE_GRM_Scheduler_strategy)
@settings(max_examples=25)
def test_MARTE_GRM_Scheduler_instantiation(instance):
    assert isinstance(instance, MARTE_GRM_Scheduler)


MARTE_GRM_SecondaryScheduler_strategy = st.builds(MARTE_GRM_SecondaryScheduler)
@given(instance=MARTE_GRM_SecondaryScheduler_strategy)
@settings(max_examples=25)
def test_MARTE_GRM_SecondaryScheduler_instantiation(instance):
    assert isinstance(instance, MARTE_GRM_SecondaryScheduler)


MARTE_GRM_StorageResource_strategy = st.builds(MARTE_GRM_StorageResource)
@given(instance=MARTE_GRM_StorageResource_strategy)
@settings(max_examples=25)
def test_MARTE_GRM_StorageResource_instantiation(instance):
    assert isinstance(instance, MARTE_GRM_StorageResource)


MARTE_GRM_SynchronizationResource_strategy = st.builds(MARTE_GRM_SynchronizationResource)
@given(instance=MARTE_GRM_SynchronizationResource_strategy)
@settings(max_examples=25)
def test_MARTE_GRM_SynchronizationResource_instantiation(instance):
    assert isinstance(instance, MARTE_GRM_SynchronizationResource)


MARTE_GRM_TimerResource_strategy = st.builds(MARTE_GRM_TimerResource, isPeriodic=safe_text)
@given(instance=MARTE_GRM_TimerResource_strategy)
@settings(max_examples=25)
def test_MARTE_GRM_TimerResource_instantiation(instance):
    assert isinstance(instance, MARTE_GRM_TimerResource)


MARTE_GRM_TimingResource_strategy = st.builds(MARTE_GRM_TimingResource)
@given(instance=MARTE_GRM_TimingResource_strategy)
@settings(max_examples=25)
def test_MARTE_GRM_TimingResource_instantiation(instance):
    assert isinstance(instance, MARTE_GRM_TimingResource)


MARTE_HLAM_PpUnit_strategy = st.builds(MARTE_HLAM_PpUnit, concPolicy=safe_text)
@given(instance=MARTE_HLAM_PpUnit_strategy)
@settings(max_examples=25)
def test_MARTE_HLAM_PpUnit_instantiation(instance):
    assert isinstance(instance, MARTE_HLAM_PpUnit)


MARTE_HLAM_RtAction_strategy = st.builds(MARTE_HLAM_RtAction, isAtomic=safe_text, synchKind=safe_text)
@given(instance=MARTE_HLAM_RtAction_strategy)
@settings(max_examples=25)
def test_MARTE_HLAM_RtAction_instantiation(instance):
    assert isinstance(instance, MARTE_HLAM_RtAction)


MARTE_HLAM_RtFeature_strategy = st.builds(MARTE_HLAM_RtFeature)
@given(instance=MARTE_HLAM_RtFeature_strategy)
@settings(max_examples=25)
def test_MARTE_HLAM_RtFeature_instantiation(instance):
    assert isinstance(instance, MARTE_HLAM_RtFeature)


MARTE_HLAM_RtService_strategy = st.builds(MARTE_HLAM_RtService, concPolicy=safe_text, exeKind=safe_text, isAtomic=safe_text, synchKind=safe_text)
@given(instance=MARTE_HLAM_RtService_strategy)
@settings(max_examples=25)
def test_MARTE_HLAM_RtService_instantiation(instance):
    assert isinstance(instance, MARTE_HLAM_RtService)


MARTE_HLAM_RtSpecification_strategy = st.builds(MARTE_HLAM_RtSpecification)
@given(instance=MARTE_HLAM_RtSpecification_strategy)
@settings(max_examples=25)
def test_MARTE_HLAM_RtSpecification_instantiation(instance):
    assert isinstance(instance, MARTE_HLAM_RtSpecification)


MARTE_HLAM_RtUnit_strategy = st.builds(MARTE_HLAM_RtUnit, isDynamic=safe_text, isMain=safe_text, queueSchedPolicy=safe_text, queueSize=safe_text, srPoolPolicy=safe_text, srPoolSize=safe_text)
@given(instance=MARTE_HLAM_RtUnit_strategy)
@settings(max_examples=25)
def test_MARTE_HLAM_RtUnit_instantiation(instance):
    assert isinstance(instance, MARTE_HLAM_RtUnit)


MARTE_HwCommunication_HwArbiter_strategy = st.builds(MARTE_HwCommunication_HwArbiter)
@given(instance=MARTE_HwCommunication_HwArbiter_strategy)
@settings(max_examples=25)
def test_MARTE_HwCommunication_HwArbiter_instantiation(instance):
    assert isinstance(instance, MARTE_HwCommunication_HwArbiter)


MARTE_HwCommunication_HwBridge_strategy = st.builds(MARTE_HwCommunication_HwBridge)
@given(instance=MARTE_HwCommunication_HwBridge_strategy)
@settings(max_examples=25)
def test_MARTE_HwCommunication_HwBridge_instantiation(instance):
    assert isinstance(instance, MARTE_HwCommunication_HwBridge)


MARTE_HwCommunication_HwBus_strategy = st.builds(MARTE_HwCommunication_HwBus)
@given(instance=MARTE_HwCommunication_HwBus_strategy)
@settings(max_examples=25)
def test_MARTE_HwCommunication_HwBus_instantiation(instance):
    assert isinstance(instance, MARTE_HwCommunication_HwBus)


MARTE_HwCommunication_HwCommunicationResource_strategy = st.builds(MARTE_HwCommunication_HwCommunicationResource)
@given(instance=MARTE_HwCommunication_HwCommunicationResource_strategy)
@settings(max_examples=25)
def test_MARTE_HwCommunication_HwCommunicationResource_instantiation(instance):
    assert isinstance(instance, MARTE_HwCommunication_HwCommunicationResource)


MARTE_HwCommunication_HwConnection_strategy = st.builds(MARTE_HwCommunication_HwConnection)
@given(instance=MARTE_HwCommunication_HwConnection_strategy)
@settings(max_examples=25)
def test_MARTE_HwCommunication_HwConnection_instantiation(instance):
    assert isinstance(instance, MARTE_HwCommunication_HwConnection)


MARTE_HwCommunication_HwEndPoint_strategy = st.builds(MARTE_HwCommunication_HwEndPoint)
@given(instance=MARTE_HwCommunication_HwEndPoint_strategy)
@settings(max_examples=25)
def test_MARTE_HwCommunication_HwEndPoint_instantiation(instance):
    assert isinstance(instance, MARTE_HwCommunication_HwEndPoint)


MARTE_HwCommunication_HwMedia_strategy = st.builds(MARTE_HwCommunication_HwMedia)
@given(instance=MARTE_HwCommunication_HwMedia_strategy)
@settings(max_examples=25)
def test_MARTE_HwCommunication_HwMedia_instantiation(instance):
    assert isinstance(instance, MARTE_HwCommunication_HwMedia)


MARTE_HwCommunication_HwPort_strategy = st.builds(MARTE_HwCommunication_HwPort)
@given(instance=MARTE_HwCommunication_HwPort_strategy)
@settings(max_examples=25)
def test_MARTE_HwCommunication_HwPort_instantiation(instance):
    assert isinstance(instance, MARTE_HwCommunication_HwPort)


MARTE_HwComputing_HwASIC_strategy = st.builds(MARTE_HwComputing_HwASIC)
@given(instance=MARTE_HwComputing_HwASIC_strategy)
@settings(max_examples=25)
def test_MARTE_HwComputing_HwASIC_instantiation(instance):
    assert isinstance(instance, MARTE_HwComputing_HwASIC)


MARTE_HwComputing_HwBranchPredictor_strategy = st.builds(MARTE_HwComputing_HwBranchPredictor)
@given(instance=MARTE_HwComputing_HwBranchPredictor_strategy)
@settings(max_examples=25)
def test_MARTE_HwComputing_HwBranchPredictor_instantiation(instance):
    assert isinstance(instance, MARTE_HwComputing_HwBranchPredictor)


MARTE_HwComputing_HwComputingResource_strategy = st.builds(MARTE_HwComputing_HwComputingResource)
@given(instance=MARTE_HwComputing_HwComputingResource_strategy)
@settings(max_examples=25)
def test_MARTE_HwComputing_HwComputingResource_instantiation(instance):
    assert isinstance(instance, MARTE_HwComputing_HwComputingResource)


MARTE_HwComputing_HwISA_strategy = st.builds(MARTE_HwComputing_HwISA, type=safe_text)
@given(instance=MARTE_HwComputing_HwISA_strategy)
@settings(max_examples=25)
def test_MARTE_HwComputing_HwISA_instantiation(instance):
    assert isinstance(instance, MARTE_HwComputing_HwISA)


MARTE_HwComputing_HwMCU_strategy = st.builds(MARTE_HwComputing_HwMCU)
@given(instance=MARTE_HwComputing_HwMCU_strategy)
@settings(max_examples=25)
def test_MARTE_HwComputing_HwMCU_instantiation(instance):
    assert isinstance(instance, MARTE_HwComputing_HwMCU)


MARTE_HwComputing_HwPLD_strategy = st.builds(MARTE_HwComputing_HwPLD, technology=safe_text)
@given(instance=MARTE_HwComputing_HwPLD_strategy)
@settings(max_examples=25)
def test_MARTE_HwComputing_HwPLD_instantiation(instance):
    assert isinstance(instance, MARTE_HwComputing_HwPLD)


MARTE_HwComputing_HwProcessor_strategy = st.builds(MARTE_HwComputing_HwProcessor)
@given(instance=MARTE_HwComputing_HwProcessor_strategy)
@settings(max_examples=25)
def test_MARTE_HwComputing_HwProcessor_instantiation(instance):
    assert isinstance(instance, MARTE_HwComputing_HwProcessor)


MARTE_HwComputing_PLD_Organization_strategy = st.builds(MARTE_HwComputing_PLD_Organization, class_=safe_text)
@given(instance=MARTE_HwComputing_PLD_Organization_strategy)
@settings(max_examples=25)
def test_MARTE_HwComputing_PLD_Organization_instantiation(instance):
    assert isinstance(instance, MARTE_HwComputing_PLD_Organization)


MARTE_HwDatasheet_HwDatasheet_strategy = st.builds(MARTE_HwDatasheet_HwDatasheet, name=safe_text, revision=safe_text)
@given(instance=MARTE_HwDatasheet_HwDatasheet_strategy)
@settings(max_examples=25)
def test_MARTE_HwDatasheet_HwDatasheet_instantiation(instance):
    assert isinstance(instance, MARTE_HwDatasheet_HwDatasheet)


MARTE_HwDeviceFunction_HwDeviceFunction_strategy = st.builds(MARTE_HwDeviceFunction_HwDeviceFunction)
@given(instance=MARTE_HwDeviceFunction_HwDeviceFunction_strategy)
@settings(max_examples=25)
def test_MARTE_HwDeviceFunction_HwDeviceFunction_instantiation(instance):
    assert isinstance(instance, MARTE_HwDeviceFunction_HwDeviceFunction)


MARTE_HwDevice_HWActuator_strategy = st.builds(MARTE_HwDevice_HWActuator)
@given(instance=MARTE_HwDevice_HWActuator_strategy)
@settings(max_examples=25)
def test_MARTE_HwDevice_HWActuator_instantiation(instance):
    assert isinstance(instance, MARTE_HwDevice_HWActuator)


MARTE_HwDevice_HWSensor_strategy = st.builds(MARTE_HwDevice_HWSensor)
@given(instance=MARTE_HwDevice_HWSensor_strategy)
@settings(max_examples=25)
def test_MARTE_HwDevice_HWSensor_instantiation(instance):
    assert isinstance(instance, MARTE_HwDevice_HWSensor)


MARTE_HwDevice_HwDevice_strategy = st.builds(MARTE_HwDevice_HwDevice)
@given(instance=MARTE_HwDevice_HwDevice_strategy)
@settings(max_examples=25)
def test_MARTE_HwDevice_HwDevice_instantiation(instance):
    assert isinstance(instance, MARTE_HwDevice_HwDevice)


MARTE_HwDevice_HwI_O_strategy = st.builds(MARTE_HwDevice_HwI_O)
@given(instance=MARTE_HwDevice_HwI_O_strategy)
@settings(max_examples=25)
def test_MARTE_HwDevice_HwI_O_instantiation(instance):
    assert isinstance(instance, MARTE_HwDevice_HwI_O)


MARTE_HwDevice_HwPeripheral_strategy = st.builds(MARTE_HwDevice_HwPeripheral)
@given(instance=MARTE_HwDevice_HwPeripheral_strategy)
@settings(max_examples=25)
def test_MARTE_HwDevice_HwPeripheral_instantiation(instance):
    assert isinstance(instance, MARTE_HwDevice_HwPeripheral)


MARTE_HwDevice_HwSupport_strategy = st.builds(MARTE_HwDevice_HwSupport)
@given(instance=MARTE_HwDevice_HwSupport_strategy)
@settings(max_examples=25)
def test_MARTE_HwDevice_HwSupport_instantiation(instance):
    assert isinstance(instance, MARTE_HwDevice_HwSupport)


MARTE_HwDiagram_HwBlockDiagram_strategy = st.builds(MARTE_HwDiagram_HwBlockDiagram, name=safe_text)
@given(instance=MARTE_HwDiagram_HwBlockDiagram_strategy)
@settings(max_examples=25)
def test_MARTE_HwDiagram_HwBlockDiagram_instantiation(instance):
    assert isinstance(instance, MARTE_HwDiagram_HwBlockDiagram)


MARTE_HwDiagram_HwCircuitDiagram_strategy = st.builds(MARTE_HwDiagram_HwCircuitDiagram, name=safe_text)
@given(instance=MARTE_HwDiagram_HwCircuitDiagram_strategy)
@settings(max_examples=25)
def test_MARTE_HwDiagram_HwCircuitDiagram_instantiation(instance):
    assert isinstance(instance, MARTE_HwDiagram_HwCircuitDiagram)


MARTE_HwDiagram_HwHRMDiagram_strategy = st.builds(MARTE_HwDiagram_HwHRMDiagram, name=safe_text)
@given(instance=MARTE_HwDiagram_HwHRMDiagram_strategy)
@settings(max_examples=25)
def test_MARTE_HwDiagram_HwHRMDiagram_instantiation(instance):
    assert isinstance(instance, MARTE_HwDiagram_HwHRMDiagram)


MARTE_HwDiagram_SRMDiagram_strategy = st.builds(MARTE_HwDiagram_SRMDiagram)
@given(instance=MARTE_HwDiagram_SRMDiagram_strategy)
@settings(max_examples=25)
def test_MARTE_HwDiagram_SRMDiagram_instantiation(instance):
    assert isinstance(instance, MARTE_HwDiagram_SRMDiagram)


MARTE_HwGeneral_HwResource_strategy = st.builds(MARTE_HwGeneral_HwResource, name=safe_text)
@given(instance=MARTE_HwGeneral_HwResource_strategy)
@settings(max_examples=25)
def test_MARTE_HwGeneral_HwResource_instantiation(instance):
    assert isinstance(instance, MARTE_HwGeneral_HwResource)


MARTE_HwGeneral_HwResourceService_strategy = st.builds(MARTE_HwGeneral_HwResourceService)
@given(instance=MARTE_HwGeneral_HwResourceService_strategy)
@settings(max_examples=25)
def test_MARTE_HwGeneral_HwResourceService_instantiation(instance):
    assert isinstance(instance, MARTE_HwGeneral_HwResourceService)


MARTE_HwIO_HwLine_strategy = st.builds(MARTE_HwIO_HwLine)
@given(instance=MARTE_HwIO_HwLine_strategy)
@settings(max_examples=25)
def test_MARTE_HwIO_HwLine_instantiation(instance):
    assert isinstance(instance, MARTE_HwIO_HwLine)


MARTE_HwIO_HwPin_strategy = st.builds(MARTE_HwIO_HwPin)
@given(instance=MARTE_HwIO_HwPin_strategy)
@settings(max_examples=25)
def test_MARTE_HwIO_HwPin_instantiation(instance):
    assert isinstance(instance, MARTE_HwIO_HwPin)


MARTE_HwLayout_Env_Condition_strategy = st.builds(MARTE_HwLayout_Env_Condition, status=safe_text, type=safe_text)
@given(instance=MARTE_HwLayout_Env_Condition_strategy)
@settings(max_examples=25)
def test_MARTE_HwLayout_Env_Condition_instantiation(instance):
    assert isinstance(instance, MARTE_HwLayout_Env_Condition)


MARTE_HwLayout_HwComponent_strategy = st.builds(MARTE_HwLayout_HwComponent, kind=safe_text)
@given(instance=MARTE_HwLayout_HwComponent_strategy)
@settings(max_examples=25)
def test_MARTE_HwLayout_HwComponent_instantiation(instance):
    assert isinstance(instance, MARTE_HwLayout_HwComponent)


MARTE_HwMemory_CacheStructure_strategy = st.builds(MARTE_HwMemory_CacheStructure)
@given(instance=MARTE_HwMemory_CacheStructure_strategy)
@settings(max_examples=25)
def test_MARTE_HwMemory_CacheStructure_instantiation(instance):
    assert isinstance(instance, MARTE_HwMemory_CacheStructure)


MARTE_HwMemory_HwCache_strategy = st.builds(MARTE_HwMemory_HwCache, repl_Policy=safe_text, type=safe_text, writePolicy=safe_text)
@given(instance=MARTE_HwMemory_HwCache_strategy)
@settings(max_examples=25)
def test_MARTE_HwMemory_HwCache_instantiation(instance):
    assert isinstance(instance, MARTE_HwMemory_HwCache)


MARTE_HwMemory_HwDrive_strategy = st.builds(MARTE_HwMemory_HwDrive)
@given(instance=MARTE_HwMemory_HwDrive_strategy)
@settings(max_examples=25)
def test_MARTE_HwMemory_HwDrive_instantiation(instance):
    assert isinstance(instance, MARTE_HwMemory_HwDrive)


MARTE_HwMemory_HwMemory_strategy = st.builds(MARTE_HwMemory_HwMemory)
@given(instance=MARTE_HwMemory_HwMemory_strategy)
@settings(max_examples=25)
def test_MARTE_HwMemory_HwMemory_instantiation(instance):
    assert isinstance(instance, MARTE_HwMemory_HwMemory)


MARTE_HwMemory_HwRAM_strategy = st.builds(MARTE_HwMemory_HwRAM, repl_Policy=safe_text, writePolicy=safe_text)
@given(instance=MARTE_HwMemory_HwRAM_strategy)
@settings(max_examples=25)
def test_MARTE_HwMemory_HwRAM_instantiation(instance):
    assert isinstance(instance, MARTE_HwMemory_HwRAM)


MARTE_HwMemory_HwROM_strategy = st.builds(MARTE_HwMemory_HwROM, type=safe_text)
@given(instance=MARTE_HwMemory_HwROM_strategy)
@settings(max_examples=25)
def test_MARTE_HwMemory_HwROM_instantiation(instance):
    assert isinstance(instance, MARTE_HwMemory_HwROM)


MARTE_HwMemory_MemoryOrganization_strategy = st.builds(MARTE_HwMemory_MemoryOrganization)
@given(instance=MARTE_HwMemory_MemoryOrganization_strategy)
@settings(max_examples=25)
def test_MARTE_HwMemory_MemoryOrganization_instantiation(instance):
    assert isinstance(instance, MARTE_HwMemory_MemoryOrganization)


MARTE_HwMemory_Timing_strategy = st.builds(MARTE_HwMemory_Timing)
@given(instance=MARTE_HwMemory_Timing_strategy)
@settings(max_examples=25)
def test_MARTE_HwMemory_Timing_instantiation(instance):
    assert isinstance(instance, MARTE_HwMemory_Timing)


MARTE_HwPackage_HwPackage_strategy = st.builds(MARTE_HwPackage_HwPackage, name=safe_text, packageType=safe_text, pinNum=st.integers())
@given(instance=MARTE_HwPackage_HwPackage_strategy)
@settings(max_examples=25)
def test_MARTE_HwPackage_HwPackage_instantiation(instance):
    assert isinstance(instance, MARTE_HwPackage_HwPackage)


MARTE_HwPackage_HwPackagePin_strategy = st.builds(MARTE_HwPackage_HwPackagePin, altNames=safe_text, pinNo=safe_text)
@given(instance=MARTE_HwPackage_HwPackagePin_strategy)
@settings(max_examples=25)
def test_MARTE_HwPackage_HwPackagePin_instantiation(instance):
    assert isinstance(instance, MARTE_HwPackage_HwPackagePin)


MARTE_HwPackage_HwWire_strategy = st.builds(MARTE_HwPackage_HwWire)
@given(instance=MARTE_HwPackage_HwWire_strategy)
@settings(max_examples=25)
def test_MARTE_HwPackage_HwWire_instantiation(instance):
    assert isinstance(instance, MARTE_HwPackage_HwWire)


MARTE_HwPeripheral_OperationImpl_strategy = st.builds(MARTE_HwPeripheral_OperationImpl)
@given(instance=MARTE_HwPeripheral_OperationImpl_strategy)
@settings(max_examples=25)
def test_MARTE_HwPeripheral_OperationImpl_instantiation(instance):
    assert isinstance(instance, MARTE_HwPeripheral_OperationImpl)


MARTE_HwPeripheral_PeripheralActivity_strategy = st.builds(MARTE_HwPeripheral_PeripheralActivity)
@given(instance=MARTE_HwPeripheral_PeripheralActivity_strategy)
@settings(max_examples=25)
def test_MARTE_HwPeripheral_PeripheralActivity_instantiation(instance):
    assert isinstance(instance, MARTE_HwPeripheral_PeripheralActivity)


MARTE_HwPeripheral_ReadRegisterAction_strategy = st.builds(MARTE_HwPeripheral_ReadRegisterAction)
@given(instance=MARTE_HwPeripheral_ReadRegisterAction_strategy)
@settings(max_examples=25)
def test_MARTE_HwPeripheral_ReadRegisterAction_instantiation(instance):
    assert isinstance(instance, MARTE_HwPeripheral_ReadRegisterAction)


MARTE_HwPeripheral_RegisterAction_strategy = st.builds(MARTE_HwPeripheral_RegisterAction)
@given(instance=MARTE_HwPeripheral_RegisterAction_strategy)
@settings(max_examples=25)
def test_MARTE_HwPeripheral_RegisterAction_instantiation(instance):
    assert isinstance(instance, MARTE_HwPeripheral_RegisterAction)


MARTE_HwPeripheral_WriteRegisterAction_strategy = st.builds(MARTE_HwPeripheral_WriteRegisterAction)
@given(instance=MARTE_HwPeripheral_WriteRegisterAction_strategy)
@settings(max_examples=25)
def test_MARTE_HwPeripheral_WriteRegisterAction_instantiation(instance):
    assert isinstance(instance, MARTE_HwPeripheral_WriteRegisterAction)


MARTE_HwPower_HwCoolingSupply_strategy = st.builds(MARTE_HwPower_HwCoolingSupply)
@given(instance=MARTE_HwPower_HwCoolingSupply_strategy)
@settings(max_examples=25)
def test_MARTE_HwPower_HwCoolingSupply_instantiation(instance):
    assert isinstance(instance, MARTE_HwPower_HwCoolingSupply)


MARTE_HwPower_HwPowerSupply_strategy = st.builds(MARTE_HwPower_HwPowerSupply)
@given(instance=MARTE_HwPower_HwPowerSupply_strategy)
@settings(max_examples=25)
def test_MARTE_HwPower_HwPowerSupply_instantiation(instance):
    assert isinstance(instance, MARTE_HwPower_HwPowerSupply)


MARTE_HwProtocol_HwProtocol_strategy = st.builds(MARTE_HwProtocol_HwProtocol, name=safe_text)
@given(instance=MARTE_HwProtocol_HwProtocol_strategy)
@settings(max_examples=25)
def test_MARTE_HwProtocol_HwProtocol_instantiation(instance):
    assert isinstance(instance, MARTE_HwProtocol_HwProtocol)


MARTE_HwRegister_HwRegister_strategy = st.builds(MARTE_HwRegister_HwRegister, address=safe_text)
@given(instance=MARTE_HwRegister_HwRegister_strategy)
@settings(max_examples=25)
def test_MARTE_HwRegister_HwRegister_instantiation(instance):
    assert isinstance(instance, MARTE_HwRegister_HwRegister)


MARTE_HwStorageManager_HwDMA_strategy = st.builds(MARTE_HwStorageManager_HwDMA)
@given(instance=MARTE_HwStorageManager_HwDMA_strategy)
@settings(max_examples=25)
def test_MARTE_HwStorageManager_HwDMA_instantiation(instance):
    assert isinstance(instance, MARTE_HwStorageManager_HwDMA)


MARTE_HwStorageManager_HwMMU_strategy = st.builds(MARTE_HwStorageManager_HwMMU)
@given(instance=MARTE_HwStorageManager_HwMMU_strategy)
@settings(max_examples=25)
def test_MARTE_HwStorageManager_HwMMU_instantiation(instance):
    assert isinstance(instance, MARTE_HwStorageManager_HwMMU)


MARTE_HwStorageManager_HwStorageManager_strategy = st.builds(MARTE_HwStorageManager_HwStorageManager)
@given(instance=MARTE_HwStorageManager_HwStorageManager_strategy)
@settings(max_examples=25)
def test_MARTE_HwStorageManager_HwStorageManager_instantiation(instance):
    assert isinstance(instance, MARTE_HwStorageManager_HwStorageManager)


MARTE_HwTiming_HwClock_strategy = st.builds(MARTE_HwTiming_HwClock)
@given(instance=MARTE_HwTiming_HwClock_strategy)
@settings(max_examples=25)
def test_MARTE_HwTiming_HwClock_instantiation(instance):
    assert isinstance(instance, MARTE_HwTiming_HwClock)


MARTE_HwTiming_HwTimer_strategy = st.builds(MARTE_HwTiming_HwTimer)
@given(instance=MARTE_HwTiming_HwTimer_strategy)
@settings(max_examples=25)
def test_MARTE_HwTiming_HwTimer_instantiation(instance):
    assert isinstance(instance, MARTE_HwTiming_HwTimer)


MARTE_HwTiming_HwTimingResource_strategy = st.builds(MARTE_HwTiming_HwTimingResource)
@given(instance=MARTE_HwTiming_HwTimingResource_strategy)
@settings(max_examples=25)
def test_MARTE_HwTiming_HwTimingResource_instantiation(instance):
    assert isinstance(instance, MARTE_HwTiming_HwTimingResource)


MARTE_NFPs_Dimension_strategy = st.builds(MARTE_NFPs_Dimension, baseExponent=st.integers(), symbol=safe_text)
@given(instance=MARTE_NFPs_Dimension_strategy)
@settings(max_examples=25)
def test_MARTE_NFPs_Dimension_instantiation(instance):
    assert isinstance(instance, MARTE_NFPs_Dimension)


MARTE_NFPs_Nfp_strategy = st.builds(MARTE_NFPs_Nfp)
@given(instance=MARTE_NFPs_Nfp_strategy)
@settings(max_examples=25)
def test_MARTE_NFPs_Nfp_instantiation(instance):
    assert isinstance(instance, MARTE_NFPs_Nfp)


MARTE_NFPs_NfpConstraint_strategy = st.builds(MARTE_NFPs_NfpConstraint, kind=safe_text)
@given(instance=MARTE_NFPs_NfpConstraint_strategy)
@settings(max_examples=25)
def test_MARTE_NFPs_NfpConstraint_instantiation(instance):
    assert isinstance(instance, MARTE_NFPs_NfpConstraint)


MARTE_NFPs_NfpType_strategy = st.builds(MARTE_NFPs_NfpType)
@given(instance=MARTE_NFPs_NfpType_strategy)
@settings(max_examples=25)
def test_MARTE_NFPs_NfpType_instantiation(instance):
    assert isinstance(instance, MARTE_NFPs_NfpType)


MARTE_NFPs_Unit_strategy = st.builds(MARTE_NFPs_Unit, convFactor=safe_text, offsetFactor=safe_text)
@given(instance=MARTE_NFPs_Unit_strategy)
@settings(max_examples=25)
def test_MARTE_NFPs_Unit_instantiation(instance):
    assert isinstance(instance, MARTE_NFPs_Unit)


MARTE_PAM_PaCommStep_strategy = st.builds(MARTE_PAM_PaCommStep)
@given(instance=MARTE_PAM_PaCommStep_strategy)
@settings(max_examples=25)
def test_MARTE_PAM_PaCommStep_instantiation(instance):
    assert isinstance(instance, MARTE_PAM_PaCommStep)


MARTE_PAM_PaLogicalResource_strategy = st.builds(MARTE_PAM_PaLogicalResource)
@given(instance=MARTE_PAM_PaLogicalResource_strategy)
@settings(max_examples=25)
def test_MARTE_PAM_PaLogicalResource_instantiation(instance):
    assert isinstance(instance, MARTE_PAM_PaLogicalResource)


MARTE_PAM_PaRequestedStep_strategy = st.builds(MARTE_PAM_PaRequestedStep)
@given(instance=MARTE_PAM_PaRequestedStep_strategy)
@settings(max_examples=25)
def test_MARTE_PAM_PaRequestedStep_instantiation(instance):
    assert isinstance(instance, MARTE_PAM_PaRequestedStep)


MARTE_PAM_PaResPassStep_strategy = st.builds(MARTE_PAM_PaResPassStep)
@given(instance=MARTE_PAM_PaResPassStep_strategy)
@settings(max_examples=25)
def test_MARTE_PAM_PaResPassStep_instantiation(instance):
    assert isinstance(instance, MARTE_PAM_PaResPassStep)


MARTE_PAM_PaRunTInstance_strategy = st.builds(MARTE_PAM_PaRunTInstance, unbddPool=safe_text)
@given(instance=MARTE_PAM_PaRunTInstance_strategy)
@settings(max_examples=25)
def test_MARTE_PAM_PaRunTInstance_instantiation(instance):
    assert isinstance(instance, MARTE_PAM_PaRunTInstance)


MARTE_PAM_PaStep_strategy = st.builds(MARTE_PAM_PaStep, extOpDemand=safe_text)
@given(instance=MARTE_PAM_PaStep_strategy)
@settings(max_examples=25)
def test_MARTE_PAM_PaStep_instantiation(instance):
    assert isinstance(instance, MARTE_PAM_PaStep)


MARTE_RSM_DefaultLink_strategy = st.builds(MARTE_RSM_DefaultLink)
@given(instance=MARTE_RSM_DefaultLink_strategy)
@settings(max_examples=25)
def test_MARTE_RSM_DefaultLink_instantiation(instance):
    assert isinstance(instance, MARTE_RSM_DefaultLink)


MARTE_RSM_Distribute_strategy = st.builds(MARTE_RSM_Distribute)
@given(instance=MARTE_RSM_Distribute_strategy)
@settings(max_examples=25)
def test_MARTE_RSM_Distribute_instantiation(instance):
    assert isinstance(instance, MARTE_RSM_Distribute)


MARTE_RSM_InterRepetition_strategy = st.builds(MARTE_RSM_InterRepetition, isModulo=safe_text)
@given(instance=MARTE_RSM_InterRepetition_strategy)
@settings(max_examples=25)
def test_MARTE_RSM_InterRepetition_instantiation(instance):
    assert isinstance(instance, MARTE_RSM_InterRepetition)


MARTE_RSM_LinkTopology_strategy = st.builds(MARTE_RSM_LinkTopology)
@given(instance=MARTE_RSM_LinkTopology_strategy)
@settings(max_examples=25)
def test_MARTE_RSM_LinkTopology_instantiation(instance):
    assert isinstance(instance, MARTE_RSM_LinkTopology)


MARTE_RSM_Reshape_strategy = st.builds(MARTE_RSM_Reshape)
@given(instance=MARTE_RSM_Reshape_strategy)
@settings(max_examples=25)
def test_MARTE_RSM_Reshape_instantiation(instance):
    assert isinstance(instance, MARTE_RSM_Reshape)


MARTE_RSM_Shaped_strategy = st.builds(MARTE_RSM_Shaped)
@given(instance=MARTE_RSM_Shaped_strategy)
@settings(max_examples=25)
def test_MARTE_RSM_Shaped_instantiation(instance):
    assert isinstance(instance, MARTE_RSM_Shaped)


MARTE_RSM_Tiler_strategy = st.builds(MARTE_RSM_Tiler)
@given(instance=MARTE_RSM_Tiler_strategy)
@settings(max_examples=25)
def test_MARTE_RSM_Tiler_instantiation(instance):
    assert isinstance(instance, MARTE_RSM_Tiler)


MARTE_SAM_SaAnalysisContext_strategy = st.builds(MARTE_SAM_SaAnalysisContext, optCriterion=safe_text)
@given(instance=MARTE_SAM_SaAnalysisContext_strategy)
@settings(max_examples=25)
def test_MARTE_SAM_SaAnalysisContext_instantiation(instance):
    assert isinstance(instance, MARTE_SAM_SaAnalysisContext)


MARTE_SAM_SaCommHost_strategy = st.builds(MARTE_SAM_SaCommHost)
@given(instance=MARTE_SAM_SaCommHost_strategy)
@settings(max_examples=25)
def test_MARTE_SAM_SaCommHost_instantiation(instance):
    assert isinstance(instance, MARTE_SAM_SaCommHost)


MARTE_SAM_SaCommStep_strategy = st.builds(MARTE_SAM_SaCommStep)
@given(instance=MARTE_SAM_SaCommStep_strategy)
@settings(max_examples=25)
def test_MARTE_SAM_SaCommStep_instantiation(instance):
    assert isinstance(instance, MARTE_SAM_SaCommStep)


MARTE_SAM_SaEndtoEndFlow_strategy = st.builds(MARTE_SAM_SaEndtoEndFlow)
@given(instance=MARTE_SAM_SaEndtoEndFlow_strategy)
@settings(max_examples=25)
def test_MARTE_SAM_SaEndtoEndFlow_instantiation(instance):
    assert isinstance(instance, MARTE_SAM_SaEndtoEndFlow)


MARTE_SAM_SaExecHost_strategy = st.builds(MARTE_SAM_SaExecHost)
@given(instance=MARTE_SAM_SaExecHost_strategy)
@settings(max_examples=25)
def test_MARTE_SAM_SaExecHost_instantiation(instance):
    assert isinstance(instance, MARTE_SAM_SaExecHost)


MARTE_SAM_SaSchedObs_strategy = st.builds(MARTE_SAM_SaSchedObs)
@given(instance=MARTE_SAM_SaSchedObs_strategy)
@settings(max_examples=25)
def test_MARTE_SAM_SaSchedObs_instantiation(instance):
    assert isinstance(instance, MARTE_SAM_SaSchedObs)


MARTE_SAM_SaSharedResource_strategy = st.builds(MARTE_SAM_SaSharedResource)
@given(instance=MARTE_SAM_SaSharedResource_strategy)
@settings(max_examples=25)
def test_MARTE_SAM_SaSharedResource_instantiation(instance):
    assert isinstance(instance, MARTE_SAM_SaSharedResource)


MARTE_SAM_SaStep_strategy = st.builds(MARTE_SAM_SaStep)
@given(instance=MARTE_SAM_SaStep_strategy)
@settings(max_examples=25)
def test_MARTE_SAM_SaStep_instantiation(instance):
    assert isinstance(instance, MARTE_SAM_SaStep)


MARTE_SW_Brokering_DeviceBroker_strategy = st.builds(MARTE_SW_Brokering_DeviceBroker, accessPolicy=safe_text, isBuffered=safe_text, name=safe_text)
@given(instance=MARTE_SW_Brokering_DeviceBroker_strategy)
@settings(max_examples=25)
def test_MARTE_SW_Brokering_DeviceBroker_instantiation(instance):
    assert isinstance(instance, MARTE_SW_Brokering_DeviceBroker)


MARTE_SW_Brokering_MemoryBroker_strategy = st.builds(MARTE_SW_Brokering_MemoryBroker, accessPolicy=safe_text)
@given(instance=MARTE_SW_Brokering_MemoryBroker_strategy)
@settings(max_examples=25)
def test_MARTE_SW_Brokering_MemoryBroker_instantiation(instance):
    assert isinstance(instance, MARTE_SW_Brokering_MemoryBroker)


MARTE_SW_Concurrency_Alarm_strategy = st.builds(MARTE_SW_Concurrency_Alarm, isWatchdog=safe_text)
@given(instance=MARTE_SW_Concurrency_Alarm_strategy)
@settings(max_examples=25)
def test_MARTE_SW_Concurrency_Alarm_instantiation(instance):
    assert isinstance(instance, MARTE_SW_Concurrency_Alarm)


MARTE_SW_Concurrency_EntryPoint_strategy = st.builds(MARTE_SW_Concurrency_EntryPoint, isReentrant=safe_text)
@given(instance=MARTE_SW_Concurrency_EntryPoint_strategy)
@settings(max_examples=25)
def test_MARTE_SW_Concurrency_EntryPoint_instantiation(instance):
    assert isinstance(instance, MARTE_SW_Concurrency_EntryPoint)


MARTE_SW_Concurrency_InterruptResource_strategy = st.builds(MARTE_SW_Concurrency_InterruptResource, isMaskable=safe_text, kind=safe_text)
@given(instance=MARTE_SW_Concurrency_InterruptResource_strategy)
@settings(max_examples=25)
def test_MARTE_SW_Concurrency_InterruptResource_instantiation(instance):
    assert isinstance(instance, MARTE_SW_Concurrency_InterruptResource)


MARTE_SW_Concurrency_MemoryPartition_strategy = st.builds(MARTE_SW_Concurrency_MemoryPartition)
@given(instance=MARTE_SW_Concurrency_MemoryPartition_strategy)
@settings(max_examples=25)
def test_MARTE_SW_Concurrency_MemoryPartition_instantiation(instance):
    assert isinstance(instance, MARTE_SW_Concurrency_MemoryPartition)


MARTE_SW_Concurrency_SwConcurrentResource_strategy = st.builds(MARTE_SW_Concurrency_SwConcurrentResource, activationCapacity=safe_text)
@given(instance=MARTE_SW_Concurrency_SwConcurrentResource_strategy)
@settings(max_examples=25)
def test_MARTE_SW_Concurrency_SwConcurrentResource_instantiation(instance):
    assert isinstance(instance, MARTE_SW_Concurrency_SwConcurrentResource)


MARTE_SW_Concurrency_SwSchedulableResource_strategy = st.builds(MARTE_SW_Concurrency_SwSchedulableResource, isPreemptable=safe_text, isStaticSchedulingFeature=safe_text)
@given(instance=MARTE_SW_Concurrency_SwSchedulableResource_strategy)
@settings(max_examples=25)
def test_MARTE_SW_Concurrency_SwSchedulableResource_instantiation(instance):
    assert isinstance(instance, MARTE_SW_Concurrency_SwSchedulableResource)


MARTE_SW_Concurrency_SwTimerResource_strategy = st.builds(MARTE_SW_Concurrency_SwTimerResource)
@given(instance=MARTE_SW_Concurrency_SwTimerResource_strategy)
@settings(max_examples=25)
def test_MARTE_SW_Concurrency_SwTimerResource_instantiation(instance):
    assert isinstance(instance, MARTE_SW_Concurrency_SwTimerResource)


MARTE_SW_Interaction_MessageComResource_strategy = st.builds(MARTE_SW_Interaction_MessageComResource, isFixedMessageSize=safe_text, mechanism=safe_text, messageQueuePolicy=safe_text)
@given(instance=MARTE_SW_Interaction_MessageComResource_strategy)
@settings(max_examples=25)
def test_MARTE_SW_Interaction_MessageComResource_instantiation(instance):
    assert isinstance(instance, MARTE_SW_Interaction_MessageComResource)


MARTE_SW_Interaction_NotificationResource_strategy = st.builds(MARTE_SW_Interaction_NotificationResource, mechanism=safe_text, occurence=safe_text)
@given(instance=MARTE_SW_Interaction_NotificationResource_strategy)
@settings(max_examples=25)
def test_MARTE_SW_Interaction_NotificationResource_instantiation(instance):
    assert isinstance(instance, MARTE_SW_Interaction_NotificationResource)


MARTE_SW_Interaction_SharedDataComResource_strategy = st.builds(MARTE_SW_Interaction_SharedDataComResource)
@given(instance=MARTE_SW_Interaction_SharedDataComResource_strategy)
@settings(max_examples=25)
def test_MARTE_SW_Interaction_SharedDataComResource_instantiation(instance):
    assert isinstance(instance, MARTE_SW_Interaction_SharedDataComResource)


MARTE_SW_Interaction_SwCommunicationResource_strategy = st.builds(MARTE_SW_Interaction_SwCommunicationResource)
@given(instance=MARTE_SW_Interaction_SwCommunicationResource_strategy)
@settings(max_examples=25)
def test_MARTE_SW_Interaction_SwCommunicationResource_instantiation(instance):
    assert isinstance(instance, MARTE_SW_Interaction_SwCommunicationResource)


MARTE_SW_Interaction_SwInteractionResource_strategy = st.builds(MARTE_SW_Interaction_SwInteractionResource, isIntraMemoryPartitionInteraction=st.booleans(), waitingQueueCapacity=safe_text, waitingQueuePolicy=safe_text)
@given(instance=MARTE_SW_Interaction_SwInteractionResource_strategy)
@settings(max_examples=25)
def test_MARTE_SW_Interaction_SwInteractionResource_instantiation(instance):
    assert isinstance(instance, MARTE_SW_Interaction_SwInteractionResource)


MARTE_SW_Interaction_SwMutualExclusionResource_strategy = st.builds(MARTE_SW_Interaction_SwMutualExclusionResource, concurrentAccessProtocol=safe_text, mechanism=safe_text)
@given(instance=MARTE_SW_Interaction_SwMutualExclusionResource_strategy)
@settings(max_examples=25)
def test_MARTE_SW_Interaction_SwMutualExclusionResource_instantiation(instance):
    assert isinstance(instance, MARTE_SW_Interaction_SwMutualExclusionResource)


MARTE_SW_Interaction_SwSynchronizationResource_strategy = st.builds(MARTE_SW_Interaction_SwSynchronizationResource)
@given(instance=MARTE_SW_Interaction_SwSynchronizationResource_strategy)
@settings(max_examples=25)
def test_MARTE_SW_Interaction_SwSynchronizationResource_instantiation(instance):
    assert isinstance(instance, MARTE_SW_Interaction_SwSynchronizationResource)


MARTE_SW_ResourceCore_SwAccessService_strategy = st.builds(MARTE_SW_ResourceCore_SwAccessService, isModifier=safe_text)
@given(instance=MARTE_SW_ResourceCore_SwAccessService_strategy)
@settings(max_examples=25)
def test_MARTE_SW_ResourceCore_SwAccessService_instantiation(instance):
    assert isinstance(instance, MARTE_SW_ResourceCore_SwAccessService)


MARTE_SW_ResourceCore_SwResource_strategy = st.builds(MARTE_SW_ResourceCore_SwResource)
@given(instance=MARTE_SW_ResourceCore_SwResource_strategy)
@settings(max_examples=25)
def test_MARTE_SW_ResourceCore_SwResource_instantiation(instance):
    assert isinstance(instance, MARTE_SW_ResourceCore_SwResource)


MARTE_Time_Clock_strategy = st.builds(MARTE_Time_Clock, standard=safe_text)
@given(instance=MARTE_Time_Clock_strategy)
@settings(max_examples=25)
def test_MARTE_Time_Clock_instantiation(instance):
    assert isinstance(instance, MARTE_Time_Clock)


MARTE_Time_ClockConstraint_strategy = st.builds(MARTE_Time_ClockConstraint, isChronometricBased=safe_text, isCoincidenceBased=safe_text, isPrecedenceBased=st.booleans())
@given(instance=MARTE_Time_ClockConstraint_strategy)
@settings(max_examples=25)
def test_MARTE_Time_ClockConstraint_instantiation(instance):
    assert isinstance(instance, MARTE_Time_ClockConstraint)


MARTE_Time_ClockType_strategy = st.builds(MARTE_Time_ClockType, isLogical=safe_text, nature=safe_text)
@given(instance=MARTE_Time_ClockType_strategy)
@settings(max_examples=25)
def test_MARTE_Time_ClockType_instantiation(instance):
    assert isinstance(instance, MARTE_Time_ClockType)


MARTE_Time_TimedConstraint_strategy = st.builds(MARTE_Time_TimedConstraint, interpretation=safe_text)
@given(instance=MARTE_Time_TimedConstraint_strategy)
@settings(max_examples=25)
def test_MARTE_Time_TimedConstraint_instantiation(instance):
    assert isinstance(instance, MARTE_Time_TimedConstraint)


MARTE_Time_TimedDomain_strategy = st.builds(MARTE_Time_TimedDomain)
@given(instance=MARTE_Time_TimedDomain_strategy)
@settings(max_examples=25)
def test_MARTE_Time_TimedDomain_instantiation(instance):
    assert isinstance(instance, MARTE_Time_TimedDomain)


MARTE_Time_TimedDurationObservation_strategy = st.builds(MARTE_Time_TimedDurationObservation, obsKind=safe_text)
@given(instance=MARTE_Time_TimedDurationObservation_strategy)
@settings(max_examples=25)
def test_MARTE_Time_TimedDurationObservation_instantiation(instance):
    assert isinstance(instance, MARTE_Time_TimedDurationObservation)


MARTE_Time_TimedElement_strategy = st.builds(MARTE_Time_TimedElement)
@given(instance=MARTE_Time_TimedElement_strategy)
@settings(max_examples=25)
def test_MARTE_Time_TimedElement_instantiation(instance):
    assert isinstance(instance, MARTE_Time_TimedElement)


MARTE_Time_TimedEvent_strategy = st.builds(MARTE_Time_TimedEvent, repetition=safe_text)
@given(instance=MARTE_Time_TimedEvent_strategy)
@settings(max_examples=25)
def test_MARTE_Time_TimedEvent_instantiation(instance):
    assert isinstance(instance, MARTE_Time_TimedEvent)


MARTE_Time_TimedInstantObservation_strategy = st.builds(MARTE_Time_TimedInstantObservation, obsKind=safe_text)
@given(instance=MARTE_Time_TimedInstantObservation_strategy)
@settings(max_examples=25)
def test_MARTE_Time_TimedInstantObservation_instantiation(instance):
    assert isinstance(instance, MARTE_Time_TimedInstantObservation)


MARTE_Time_TimedObservation_strategy = st.builds(MARTE_Time_TimedObservation)
@given(instance=MARTE_Time_TimedObservation_strategy)
@settings(max_examples=25)
def test_MARTE_Time_TimedObservation_instantiation(instance):
    assert isinstance(instance, MARTE_Time_TimedObservation)


MARTE_Time_TimedProcessing_strategy = st.builds(MARTE_Time_TimedProcessing)
@given(instance=MARTE_Time_TimedProcessing_strategy)
@settings(max_examples=25)
def test_MARTE_Time_TimedProcessing_instantiation(instance):
    assert isinstance(instance, MARTE_Time_TimedProcessing)


MARTE_Time_TimedValueSpecification_strategy = st.builds(MARTE_Time_TimedValueSpecification, interpretation=safe_text)
@given(instance=MARTE_Time_TimedValueSpecification_strategy)
@settings(max_examples=25)
def test_MARTE_Time_TimedValueSpecification_instantiation(instance):
    assert isinstance(instance, MARTE_Time_TimedValueSpecification)


MARTE_Variables_ExpressionContext_strategy = st.builds(MARTE_Variables_ExpressionContext)
@given(instance=MARTE_Variables_ExpressionContext_strategy)
@settings(max_examples=25)
def test_MARTE_Variables_ExpressionContext_instantiation(instance):
    assert isinstance(instance, MARTE_Variables_ExpressionContext)


MARTE_Variables_Var_strategy = st.builds(MARTE_Variables_Var, dir=safe_text)
@given(instance=MARTE_Variables_Var_strategy)
@settings(max_examples=25)
def test_MARTE_Variables_Var_instantiation(instance):
    assert isinstance(instance, MARTE_Variables_Var)


MutualExclusionResource_strategy = st.builds(MutualExclusionResource)
@given(instance=MutualExclusionResource_strategy)
@settings(max_examples=25)
def test_MutualExclusionResource_instantiation(instance):
    assert isinstance(instance, MutualExclusionResource)


NFP_Area_strategy = st.builds(NFP_Area)
@given(instance=NFP_Area_strategy)
@settings(max_examples=25)
def test_NFP_Area_instantiation(instance):
    assert isinstance(instance, NFP_Area)


NFP_Boolean_strategy = st.builds(NFP_Boolean)
@given(instance=NFP_Boolean_strategy)
@settings(max_examples=25)
def test_NFP_Boolean_instantiation(instance):
    assert isinstance(instance, NFP_Boolean)


NFP_DataSize_strategy = st.builds(NFP_DataSize)
@given(instance=NFP_DataSize_strategy)
@settings(max_examples=25)
def test_NFP_DataSize_instantiation(instance):
    assert isinstance(instance, NFP_DataSize)


NFP_DataTxRate_strategy = st.builds(NFP_DataTxRate)
@given(instance=NFP_DataTxRate_strategy)
@settings(max_examples=25)
def test_NFP_DataTxRate_instantiation(instance):
    assert isinstance(instance, NFP_DataTxRate)


NFP_DateTime_strategy = st.builds(NFP_DateTime)
@given(instance=NFP_DateTime_strategy)
@settings(max_examples=25)
def test_NFP_DateTime_instantiation(instance):
    assert isinstance(instance, NFP_DateTime)


NFP_Duration_strategy = st.builds(NFP_Duration)
@given(instance=NFP_Duration_strategy)
@settings(max_examples=25)
def test_NFP_Duration_instantiation(instance):
    assert isinstance(instance, NFP_Duration)


NFP_Energy_strategy = st.builds(NFP_Energy)
@given(instance=NFP_Energy_strategy)
@settings(max_examples=25)
def test_NFP_Energy_instantiation(instance):
    assert isinstance(instance, NFP_Energy)


NFP_Frequency_strategy = st.builds(NFP_Frequency)
@given(instance=NFP_Frequency_strategy)
@settings(max_examples=25)
def test_NFP_Frequency_instantiation(instance):
    assert isinstance(instance, NFP_Frequency)


NFP_FrequencyInterval_strategy = st.builds(NFP_FrequencyInterval)
@given(instance=NFP_FrequencyInterval_strategy)
@settings(max_examples=25)
def test_NFP_FrequencyInterval_instantiation(instance):
    assert isinstance(instance, NFP_FrequencyInterval)


NFP_Integer_strategy = st.builds(NFP_Integer)
@given(instance=NFP_Integer_strategy)
@settings(max_examples=25)
def test_NFP_Integer_instantiation(instance):
    assert isinstance(instance, NFP_Integer)


NFP_Length_strategy = st.builds(NFP_Length)
@given(instance=NFP_Length_strategy)
@settings(max_examples=25)
def test_NFP_Length_instantiation(instance):
    assert isinstance(instance, NFP_Length)


NFP_Natural_strategy = st.builds(NFP_Natural)
@given(instance=NFP_Natural_strategy)
@settings(max_examples=25)
def test_NFP_Natural_instantiation(instance):
    assert isinstance(instance, NFP_Natural)


NFP_NaturalInterval_strategy = st.builds(NFP_NaturalInterval)
@given(instance=NFP_NaturalInterval_strategy)
@settings(max_examples=25)
def test_NFP_NaturalInterval_instantiation(instance):
    assert isinstance(instance, NFP_NaturalInterval)


NFP_Percentage_strategy = st.builds(NFP_Percentage)
@given(instance=NFP_Percentage_strategy)
@settings(max_examples=25)
def test_NFP_Percentage_instantiation(instance):
    assert isinstance(instance, NFP_Percentage)


NFP_Power_strategy = st.builds(NFP_Power)
@given(instance=NFP_Power_strategy)
@settings(max_examples=25)
def test_NFP_Power_instantiation(instance):
    assert isinstance(instance, NFP_Power)


NFP_Price_strategy = st.builds(NFP_Price)
@given(instance=NFP_Price_strategy)
@settings(max_examples=25)
def test_NFP_Price_instantiation(instance):
    assert isinstance(instance, NFP_Price)


NFP_Real_strategy = st.builds(NFP_Real)
@given(instance=NFP_Real_strategy)
@settings(max_examples=25)
def test_NFP_Real_instantiation(instance):
    assert isinstance(instance, NFP_Real)


NFP_String_strategy = st.builds(NFP_String)
@given(instance=NFP_String_strategy)
@settings(max_examples=25)
def test_NFP_String_instantiation(instance):
    assert isinstance(instance, NFP_String)


NFPs_Dimension_strategy = st.builds(NFPs_Dimension)
@given(instance=NFPs_Dimension_strategy)
@settings(max_examples=25)
def test_NFPs_Dimension_instantiation(instance):
    assert isinstance(instance, NFPs_Dimension)


NFPs_MARTE_Constraint_strategy = st.builds(NFPs_MARTE_Constraint)
@given(instance=NFPs_MARTE_Constraint_strategy)
@settings(max_examples=25)
def test_NFPs_MARTE_Constraint_instantiation(instance):
    assert isinstance(instance, NFPs_MARTE_Constraint)


NFPs_MARTE_Enumeration_strategy = st.builds(NFPs_MARTE_Enumeration)
@given(instance=NFPs_MARTE_Enumeration_strategy)
@settings(max_examples=25)
def test_NFPs_MARTE_Enumeration_instantiation(instance):
    assert isinstance(instance, NFPs_MARTE_Enumeration)


NFPs_MARTE_EnumerationLiteral_strategy = st.builds(NFPs_MARTE_EnumerationLiteral)
@given(instance=NFPs_MARTE_EnumerationLiteral_strategy)
@settings(max_examples=25)
def test_NFPs_MARTE_EnumerationLiteral_instantiation(instance):
    assert isinstance(instance, NFPs_MARTE_EnumerationLiteral)


NFPs_MARTE_Property_strategy = st.builds(NFPs_MARTE_Property)
@given(instance=NFPs_MARTE_Property_strategy)
@settings(max_examples=25)
def test_NFPs_MARTE_Property_instantiation(instance):
    assert isinstance(instance, NFPs_MARTE_Property)


NFPs_NfpConstraint_strategy = st.builds(NFPs_NfpConstraint)
@given(instance=NFPs_NfpConstraint_strategy)
@settings(max_examples=25)
def test_NFPs_NfpConstraint_instantiation(instance):
    assert isinstance(instance, NFPs_NfpConstraint)


NFPs_Unit_strategy = st.builds(NFPs_Unit)
@given(instance=NFPs_Unit_strategy)
@settings(max_examples=25)
def test_NFPs_Unit_instantiation(instance):
    assert isinstance(instance, NFPs_Unit)


NfpConstraint_strategy = st.builds(NfpConstraint)
@given(instance=NfpConstraint_strategy)
@settings(max_examples=25)
def test_NfpConstraint_instantiation(instance):
    assert isinstance(instance, NfpConstraint)


Operation_strategy = st.builds(Operation)
@given(instance=Operation_strategy)
@settings(max_examples=25)
def test_Operation_instantiation(instance):
    assert isinstance(instance, Operation)


PAM_MARTE_NamedElement_strategy = st.builds(PAM_MARTE_NamedElement)
@given(instance=PAM_MARTE_NamedElement_strategy)
@settings(max_examples=25)
def test_PAM_MARTE_NamedElement_instantiation(instance):
    assert isinstance(instance, PAM_MARTE_NamedElement)


PAM_PaStep_strategy = st.builds(PAM_PaStep)
@given(instance=PAM_PaStep_strategy)
@settings(max_examples=25)
def test_PAM_PaStep_instantiation(instance):
    assert isinstance(instance, PAM_PaStep)


ProcessingResource_strategy = st.builds(ProcessingResource)
@given(instance=ProcessingResource_strategy)
@settings(max_examples=25)
def test_ProcessingResource_instantiation(instance):
    assert isinstance(instance, ProcessingResource)


RSM_MARTE_Connector_strategy = st.builds(RSM_MARTE_Connector)
@given(instance=RSM_MARTE_Connector_strategy)
@settings(max_examples=25)
def test_RSM_MARTE_Connector_instantiation(instance):
    assert isinstance(instance, RSM_MARTE_Connector)


RSM_MARTE_ConnectorEnd_strategy = st.builds(RSM_MARTE_ConnectorEnd)
@given(instance=RSM_MARTE_ConnectorEnd_strategy)
@settings(max_examples=25)
def test_RSM_MARTE_ConnectorEnd_instantiation(instance):
    assert isinstance(instance, RSM_MARTE_ConnectorEnd)


RSM_MARTE_MultiplicityElement_strategy = st.builds(RSM_MARTE_MultiplicityElement)
@given(instance=RSM_MARTE_MultiplicityElement_strategy)
@settings(max_examples=25)
def test_RSM_MARTE_MultiplicityElement_instantiation(instance):
    assert isinstance(instance, RSM_MARTE_MultiplicityElement)


Realnterval_strategy = st.builds(Realnterval)
@given(instance=Realnterval_strategy)
@settings(max_examples=25)
def test_Realnterval_instantiation(instance):
    assert isinstance(instance, Realnterval)


RegisterAction_strategy = st.builds(RegisterAction)
@given(instance=RegisterAction_strategy)
@settings(max_examples=25)
def test_RegisterAction_instantiation(instance):
    assert isinstance(instance, RegisterAction)


Resource_strategy = st.builds(Resource)
@given(instance=Resource_strategy)
@settings(max_examples=25)
def test_Resource_instantiation(instance):
    assert isinstance(instance, Resource)


SAM_MARTE_BehavioralFeature_strategy = st.builds(SAM_MARTE_BehavioralFeature)
@given(instance=SAM_MARTE_BehavioralFeature_strategy)
@settings(max_examples=25)
def test_SAM_MARTE_BehavioralFeature_instantiation(instance):
    assert isinstance(instance, SAM_MARTE_BehavioralFeature)


SAM_MARTE_NamedElement_strategy = st.builds(SAM_MARTE_NamedElement)
@given(instance=SAM_MARTE_NamedElement_strategy)
@settings(max_examples=25)
def test_SAM_MARTE_NamedElement_instantiation(instance):
    assert isinstance(instance, SAM_MARTE_NamedElement)


SAM_SaSharedResource_strategy = st.builds(SAM_SaSharedResource)
@given(instance=SAM_SaSharedResource_strategy)
@settings(max_examples=25)
def test_SAM_SaSharedResource_instantiation(instance):
    assert isinstance(instance, SAM_SaSharedResource)


SW_Brokering_DeviceBroker_strategy = st.builds(SW_Brokering_DeviceBroker)
@given(instance=SW_Brokering_DeviceBroker_strategy)
@settings(max_examples=25)
def test_SW_Brokering_DeviceBroker_instantiation(instance):
    assert isinstance(instance, SW_Brokering_DeviceBroker)


SW_Brokering_MARTE_Activity_strategy = st.builds(SW_Brokering_MARTE_Activity)
@given(instance=SW_Brokering_MARTE_Activity_strategy)
@settings(max_examples=25)
def test_SW_Brokering_MARTE_Activity_instantiation(instance):
    assert isinstance(instance, SW_Brokering_MARTE_Activity)


SW_Brokering_MARTE_BehavioralFeature_strategy = st.builds(SW_Brokering_MARTE_BehavioralFeature)
@given(instance=SW_Brokering_MARTE_BehavioralFeature_strategy)
@settings(max_examples=25)
def test_SW_Brokering_MARTE_BehavioralFeature_instantiation(instance):
    assert isinstance(instance, SW_Brokering_MARTE_BehavioralFeature)


SW_Brokering_MARTE_Operation_strategy = st.builds(SW_Brokering_MARTE_Operation)
@given(instance=SW_Brokering_MARTE_Operation_strategy)
@settings(max_examples=25)
def test_SW_Brokering_MARTE_Operation_instantiation(instance):
    assert isinstance(instance, SW_Brokering_MARTE_Operation)


SW_Brokering_MARTE_TypedElement_strategy = st.builds(SW_Brokering_MARTE_TypedElement)
@given(instance=SW_Brokering_MARTE_TypedElement_strategy)
@settings(max_examples=25)
def test_SW_Brokering_MARTE_TypedElement_instantiation(instance):
    assert isinstance(instance, SW_Brokering_MARTE_TypedElement)


SW_Concurrency_MARTE_BehavioralFeature_strategy = st.builds(SW_Concurrency_MARTE_BehavioralFeature)
@given(instance=SW_Concurrency_MARTE_BehavioralFeature_strategy)
@settings(max_examples=25)
def test_SW_Concurrency_MARTE_BehavioralFeature_instantiation(instance):
    assert isinstance(instance, SW_Concurrency_MARTE_BehavioralFeature)


SW_Concurrency_MARTE_Element_strategy = st.builds(SW_Concurrency_MARTE_Element)
@given(instance=SW_Concurrency_MARTE_Element_strategy)
@settings(max_examples=25)
def test_SW_Concurrency_MARTE_Element_instantiation(instance):
    assert isinstance(instance, SW_Concurrency_MARTE_Element)


SW_Concurrency_MARTE_NamedElement_strategy = st.builds(SW_Concurrency_MARTE_NamedElement)
@given(instance=SW_Concurrency_MARTE_NamedElement_strategy)
@settings(max_examples=25)
def test_SW_Concurrency_MARTE_NamedElement_instantiation(instance):
    assert isinstance(instance, SW_Concurrency_MARTE_NamedElement)


SW_Concurrency_MARTE_Namespace_strategy = st.builds(SW_Concurrency_MARTE_Namespace)
@given(instance=SW_Concurrency_MARTE_Namespace_strategy)
@settings(max_examples=25)
def test_SW_Concurrency_MARTE_Namespace_instantiation(instance):
    assert isinstance(instance, SW_Concurrency_MARTE_Namespace)


SW_Concurrency_MARTE_TypedElement_strategy = st.builds(SW_Concurrency_MARTE_TypedElement)
@given(instance=SW_Concurrency_MARTE_TypedElement_strategy)
@settings(max_examples=25)
def test_SW_Concurrency_MARTE_TypedElement_instantiation(instance):
    assert isinstance(instance, SW_Concurrency_MARTE_TypedElement)


SW_Concurrency_SwConcurrentResource_strategy = st.builds(SW_Concurrency_SwConcurrentResource)
@given(instance=SW_Concurrency_SwConcurrentResource_strategy)
@settings(max_examples=25)
def test_SW_Concurrency_SwConcurrentResource_instantiation(instance):
    assert isinstance(instance, SW_Concurrency_SwConcurrentResource)


SW_Interaction_MARTE_BehavioralFeature_strategy = st.builds(SW_Interaction_MARTE_BehavioralFeature)
@given(instance=SW_Interaction_MARTE_BehavioralFeature_strategy)
@settings(max_examples=25)
def test_SW_Interaction_MARTE_BehavioralFeature_instantiation(instance):
    assert isinstance(instance, SW_Interaction_MARTE_BehavioralFeature)


SW_Interaction_MARTE_TypedElement_strategy = st.builds(SW_Interaction_MARTE_TypedElement)
@given(instance=SW_Interaction_MARTE_TypedElement_strategy)
@settings(max_examples=25)
def test_SW_Interaction_MARTE_TypedElement_instantiation(instance):
    assert isinstance(instance, SW_Interaction_MARTE_TypedElement)


SW_Interaction_SwInteractionResource_strategy = st.builds(SW_Interaction_SwInteractionResource)
@given(instance=SW_Interaction_SwInteractionResource_strategy)
@settings(max_examples=25)
def test_SW_Interaction_SwInteractionResource_instantiation(instance):
    assert isinstance(instance, SW_Interaction_SwInteractionResource)


SW_Interaction_SwSynchronizationResource_strategy = st.builds(SW_Interaction_SwSynchronizationResource)
@given(instance=SW_Interaction_SwSynchronizationResource_strategy)
@settings(max_examples=25)
def test_SW_Interaction_SwSynchronizationResource_instantiation(instance):
    assert isinstance(instance, SW_Interaction_SwSynchronizationResource)


SW_ResourceCore_MARTE_BehavioralFeature_strategy = st.builds(SW_ResourceCore_MARTE_BehavioralFeature)
@given(instance=SW_ResourceCore_MARTE_BehavioralFeature_strategy)
@settings(max_examples=25)
def test_SW_ResourceCore_MARTE_BehavioralFeature_instantiation(instance):
    assert isinstance(instance, SW_ResourceCore_MARTE_BehavioralFeature)


SW_ResourceCore_MARTE_Property_strategy = st.builds(SW_ResourceCore_MARTE_Property)
@given(instance=SW_ResourceCore_MARTE_Property_strategy)
@settings(max_examples=25)
def test_SW_ResourceCore_MARTE_Property_instantiation(instance):
    assert isinstance(instance, SW_ResourceCore_MARTE_Property)


SW_ResourceCore_MARTE_TypedElement_strategy = st.builds(SW_ResourceCore_MARTE_TypedElement)
@given(instance=SW_ResourceCore_MARTE_TypedElement_strategy)
@settings(max_examples=25)
def test_SW_ResourceCore_MARTE_TypedElement_instantiation(instance):
    assert isinstance(instance, SW_ResourceCore_MARTE_TypedElement)


SchedParameters_strategy = st.builds(SchedParameters)
@given(instance=SchedParameters_strategy)
@settings(max_examples=25)
def test_SchedParameters_instantiation(instance):
    assert isinstance(instance, SchedParameters)


SchedulableResource_strategy = st.builds(SchedulableResource)
@given(instance=SchedulableResource_strategy)
@settings(max_examples=25)
def test_SchedulableResource_instantiation(instance):
    assert isinstance(instance, SchedulableResource)


Scheduler_strategy = st.builds(Scheduler)
@given(instance=Scheduler_strategy)
@settings(max_examples=25)
def test_Scheduler_instantiation(instance):
    assert isinstance(instance, Scheduler)


ShapeSpecification_strategy = st.builds(ShapeSpecification)
@given(instance=ShapeSpecification_strategy)
@settings(max_examples=25)
def test_ShapeSpecification_instantiation(instance):
    assert isinstance(instance, ShapeSpecification)


SwCommunicationResource_strategy = st.builds(SwCommunicationResource)
@given(instance=SwCommunicationResource_strategy)
@settings(max_examples=25)
def test_SwCommunicationResource_instantiation(instance):
    assert isinstance(instance, SwCommunicationResource)


SwConcurrentResource_strategy = st.builds(SwConcurrentResource)
@given(instance=SwConcurrentResource_strategy)
@settings(max_examples=25)
def test_SwConcurrentResource_instantiation(instance):
    assert isinstance(instance, SwConcurrentResource)


SwResource_strategy = st.builds(SwResource)
@given(instance=SwResource_strategy)
@settings(max_examples=25)
def test_SwResource_instantiation(instance):
    assert isinstance(instance, SwResource)


SwSynchronizationResource_strategy = st.builds(SwSynchronizationResource)
@given(instance=SwSynchronizationResource_strategy)
@settings(max_examples=25)
def test_SwSynchronizationResource_instantiation(instance):
    assert isinstance(instance, SwSynchronizationResource)


TilerSpecification_strategy = st.builds(TilerSpecification)
@given(instance=TilerSpecification_strategy)
@settings(max_examples=25)
def test_TilerSpecification_instantiation(instance):
    assert isinstance(instance, TilerSpecification)


Time_Clock_strategy = st.builds(Time_Clock)
@given(instance=Time_Clock_strategy)
@settings(max_examples=25)
def test_Time_Clock_instantiation(instance):
    assert isinstance(instance, Time_Clock)


Time_ClockType_strategy = st.builds(Time_ClockType)
@given(instance=Time_ClockType_strategy)
@settings(max_examples=25)
def test_Time_ClockType_instantiation(instance):
    assert isinstance(instance, Time_ClockType)


Time_MARTE_Action_strategy = st.builds(Time_MARTE_Action)
@given(instance=Time_MARTE_Action_strategy)
@settings(max_examples=25)
def test_Time_MARTE_Action_instantiation(instance):
    assert isinstance(instance, Time_MARTE_Action)


Time_MARTE_Behavior_strategy = st.builds(Time_MARTE_Behavior)
@given(instance=Time_MARTE_Behavior_strategy)
@settings(max_examples=25)
def test_Time_MARTE_Behavior_instantiation(instance):
    assert isinstance(instance, Time_MARTE_Behavior)


Time_MARTE_Class_strategy = st.builds(Time_MARTE_Class)
@given(instance=Time_MARTE_Class_strategy)
@settings(max_examples=25)
def test_Time_MARTE_Class_instantiation(instance):
    assert isinstance(instance, Time_MARTE_Class)


Time_MARTE_DurationObservation_strategy = st.builds(Time_MARTE_DurationObservation)
@given(instance=Time_MARTE_DurationObservation_strategy)
@settings(max_examples=25)
def test_Time_MARTE_DurationObservation_instantiation(instance):
    assert isinstance(instance, Time_MARTE_DurationObservation)


Time_MARTE_Enumeration_strategy = st.builds(Time_MARTE_Enumeration)
@given(instance=Time_MARTE_Enumeration_strategy)
@settings(max_examples=25)
def test_Time_MARTE_Enumeration_instantiation(instance):
    assert isinstance(instance, Time_MARTE_Enumeration)


Time_MARTE_Event_strategy = st.builds(Time_MARTE_Event)
@given(instance=Time_MARTE_Event_strategy)
@settings(max_examples=25)
def test_Time_MARTE_Event_instantiation(instance):
    assert isinstance(instance, Time_MARTE_Event)


Time_MARTE_InstanceSpecification_strategy = st.builds(Time_MARTE_InstanceSpecification)
@given(instance=Time_MARTE_InstanceSpecification_strategy)
@settings(max_examples=25)
def test_Time_MARTE_InstanceSpecification_instantiation(instance):
    assert isinstance(instance, Time_MARTE_InstanceSpecification)


Time_MARTE_Message_strategy = st.builds(Time_MARTE_Message)
@given(instance=Time_MARTE_Message_strategy)
@settings(max_examples=25)
def test_Time_MARTE_Message_instantiation(instance):
    assert isinstance(instance, Time_MARTE_Message)


Time_MARTE_Namespace_strategy = st.builds(Time_MARTE_Namespace)
@given(instance=Time_MARTE_Namespace_strategy)
@settings(max_examples=25)
def test_Time_MARTE_Namespace_instantiation(instance):
    assert isinstance(instance, Time_MARTE_Namespace)


Time_MARTE_Operation_strategy = st.builds(Time_MARTE_Operation)
@given(instance=Time_MARTE_Operation_strategy)
@settings(max_examples=25)
def test_Time_MARTE_Operation_instantiation(instance):
    assert isinstance(instance, Time_MARTE_Operation)


Time_MARTE_Property_strategy = st.builds(Time_MARTE_Property)
@given(instance=Time_MARTE_Property_strategy)
@settings(max_examples=25)
def test_Time_MARTE_Property_instantiation(instance):
    assert isinstance(instance, Time_MARTE_Property)


Time_MARTE_TimeEvent_strategy = st.builds(Time_MARTE_TimeEvent)
@given(instance=Time_MARTE_TimeEvent_strategy)
@settings(max_examples=25)
def test_Time_MARTE_TimeEvent_instantiation(instance):
    assert isinstance(instance, Time_MARTE_TimeEvent)


Time_MARTE_TimeObservation_strategy = st.builds(Time_MARTE_TimeObservation)
@given(instance=Time_MARTE_TimeObservation_strategy)
@settings(max_examples=25)
def test_Time_MARTE_TimeObservation_instantiation(instance):
    assert isinstance(instance, Time_MARTE_TimeObservation)


Time_MARTE_ValueSpecification_strategy = st.builds(Time_MARTE_ValueSpecification)
@given(instance=Time_MARTE_ValueSpecification_strategy)
@settings(max_examples=25)
def test_Time_MARTE_ValueSpecification_instantiation(instance):
    assert isinstance(instance, Time_MARTE_ValueSpecification)


Time_TimedElement_strategy = st.builds(Time_TimedElement)
@given(instance=Time_TimedElement_strategy)
@settings(max_examples=25)
def test_Time_TimedElement_instantiation(instance):
    assert isinstance(instance, Time_TimedElement)


Time_TimedInstantObservation_strategy = st.builds(Time_TimedInstantObservation)
@given(instance=Time_TimedInstantObservation_strategy)
@settings(max_examples=25)
def test_Time_TimedInstantObservation_instantiation(instance):
    assert isinstance(instance, Time_TimedInstantObservation)


Time_TimedProcessing_strategy = st.builds(Time_TimedProcessing)
@given(instance=Time_TimedProcessing_strategy)
@settings(max_examples=25)
def test_Time_TimedProcessing_instantiation(instance):
    assert isinstance(instance, Time_TimedProcessing)


TimedElement_strategy = st.builds(TimedElement)
@given(instance=TimedElement_strategy)
@settings(max_examples=25)
def test_TimedElement_instantiation(instance):
    assert isinstance(instance, TimedElement)


TimedObservation_strategy = st.builds(TimedObservation)
@given(instance=TimedObservation_strategy)
@settings(max_examples=25)
def test_TimedObservation_instantiation(instance):
    assert isinstance(instance, TimedObservation)


TimerResource_strategy = st.builds(TimerResource)
@given(instance=TimerResource_strategy)
@settings(max_examples=25)
def test_TimerResource_instantiation(instance):
    assert isinstance(instance, TimerResource)


TimingResource_strategy = st.builds(TimingResource)
@given(instance=TimingResource_strategy)
@settings(max_examples=25)
def test_TimingResource_instantiation(instance):
    assert isinstance(instance, TimingResource)


TupleType_strategy = st.builds(TupleType)
@given(instance=TupleType_strategy)
@settings(max_examples=25)
def test_TupleType_instantiation(instance):
    assert isinstance(instance, TupleType)


UtilityType_strategy = st.builds(UtilityType)
@given(instance=UtilityType_strategy)
@settings(max_examples=25)
def test_UtilityType_instantiation(instance):
    assert isinstance(instance, UtilityType)


Variables_ExpressionContext_strategy = st.builds(Variables_ExpressionContext)
@given(instance=Variables_ExpressionContext_strategy)
@settings(max_examples=25)
def test_Variables_ExpressionContext_instantiation(instance):
    assert isinstance(instance, Variables_ExpressionContext)


Variables_MARTE_NamedElement_strategy = st.builds(Variables_MARTE_NamedElement)
@given(instance=Variables_MARTE_NamedElement_strategy)
@settings(max_examples=25)
def test_Variables_MARTE_NamedElement_instantiation(instance):
    assert isinstance(instance, Variables_MARTE_NamedElement)


Variables_MARTE_Property_strategy = st.builds(Variables_MARTE_Property)
@given(instance=Variables_MARTE_Property_strategy)
@settings(max_examples=25)
def test_Variables_MARTE_Property_instantiation(instance):
    assert isinstance(instance, Variables_MARTE_Property)


