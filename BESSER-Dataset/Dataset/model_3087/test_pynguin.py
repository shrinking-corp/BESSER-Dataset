#  This file is part of Pynguin.
#
#  SPDX-FileCopyrightText: 2019�2026 Pynguin Contributors
#
#  SPDX-License-Identifier: MIT
#
#  This file was automatically generated using Pynguin.

import pytest
import sys
import python_code

python_code_ = sys.modules["python_code"]
from python_code import (
    ABC,
    AccessPolicyKind,
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
    AllocationEndKind,
    AllocationKind,
    AllocationNature,
    ArrivalPattern,
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
    CoreElements_Configuration,
    CoreElements_MARTE_Package,
    CoreElements_MARTE_State,
    CoreElements_MARTE_StateMachine,
    CoreElements_MARTE_StructuredClassifier,
    CoreElements_MARTE_Transition,
    CoreElements_Mode,
    DataPoolOrderingKind,
    DataTypes_MARTE_DataType,
    DataTypes_MARTE_Property,
    Enum,
    ExecutionKind,
    FlowDirectionKind,
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
    ISA_Type,
    IntegerInterval,
    IntegerMatrix,
    IntegerVector,
    InterruptKind,
    InterruptResource,
    LaxityKind,
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
    MessageResourceKind,
    MutualExclusionResource,
    MutualExclusionResourceKind,
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
    NotificationKind,
    NotificationResourceKind,
    Operation,
    OptimallityCriterionKind,
    PAM_MARTE_NamedElement,
    PAM_PaStep,
    PLD_Class,
    PLD_Technology,
    PoolMgtPolicyKind,
    PortSpecificationKind,
    ProcessingResource,
    QueuePolicyKind,
    ROM_Type,
    RSM_MARTE_Connector,
    RSM_MARTE_ConnectorEnd,
    RSM_MARTE_MultiplicityElement,
    Realnterval,
    RegisterAction,
    Repl_Policy,
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
    SynchronizationKind,
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
    VariableDirectionKind,
    Variables_ExpressionContext,
    Variables_MARTE_NamedElement,
    Variables_MARTE_Property,
    WritePolicy,
    abstractmethod,
    date,
    datetime,
    time,
)


def test_0():
    var_3 = python_code_.MARTE_NFPs_Nfp()
    var_6 = 'Tj"B~DSq)Q5Z7^;X['
    var_7 = "UDx,ys"
    var_8 = python_code_.MARTE_HwMemory_HwCache(
        type=var_6, repl_Policy=var_7, writePolicy=var_7, MARTE_HwMemory_HwCache=var_3
    )
    assert isinstance(var_8, python_code_.MARTE_HwMemory_HwCache)
    var_9 = "mSTe1G4Z!+]\x0c@$\t:"
    var_10 = "_MARTE_SW_Brokering_MemoryBroker__MARTE_SW_Brokering_MemoryBroker742NFP_Real1113_MARTE_HwMemory_HwROM__MARTE_HwMemory_HwROM"
    python_code_.MARTE_HLAM_RtService(
        concPolicy=None, exeKind=var_9, isAtomic=var_7, synchKind=var_10
    )


@pytest.mark.xfail(strict=True)
def test_1():
    var_2 = python_code_.CoreElements_MARTE_StateMachine()
    python_code_.MARTE_HLAM_PpUnit(concPolicy=var_2)
    var_20 = "Time_MARTE_Operation-GCM_MARTE_Port-_MARTE_HwComputing_PLD_Organization__MARTE_HwComputing_PLD_Organization305-seaOfGates"
    var_21 = lambda *args, **kwargs: False
    var_22 = python_code_.PAM_MARTE_NamedElement()
    var_23 = python_code_.MARTE_PAM_PaRunTInstance(
        unbddPool=complex(-371.84551, 635.20382),
        MARTE_PAM_PaRunTInstance=set(),
        MARTE_PAM_PaRunTInstance1118=var_22,
    )
    assert isinstance(var_23, python_code_.MARTE_PAM_PaRunTInstance)
    python_code_.MARTE_SW_Concurrency_SwSchedulableResource(
        isStaticSchedulingFeature=var_20,
        isPreemptable=var_21,
        MARTE_SW_Concurrency_SwSchedulableResource689=False,
        MARTE_SW_Concurrency_SwSchedulableResource701=var_21,
        MARTE_SW_Concurrency_SwSchedulableResource692="H#Q)?|n",
        GRM_SchedulableResource1107=var_23,
    )


def test_2():
    var_1 = "_MARTE_SW_Concurrency_InterruptResource__MARTE_SW_Concurrency_InterruptResource676flash"
    python_code_.MARTE_GCM_DataPool(ordering=var_1)
    var_11 = python_code_.MARTE_SAM_SaExecHost()
    var_14 = '$\x0c,JD+DP7zFh"-6"\\'
    var_15 = python_code_.SW_Brokering_MARTE_Operation
    var_16 = "Q \t"
    var_17 = "SchedulableResource"
    var_18 = python_code_.NFP_Duration()
    var_19 = python_code_.HLAM_MARTE_Behavior()
    python_code_.MARTE_HLAM_RtUnit(
        queueSchedPolicy=[],
        queueSize=var_14,
        isDynamic=var_15,
        isMain=var_16,
        srPoolSize=var_17,
        srPoolPolicy=var_16,
        MARTE_HLAM_RtUnit244=var_15,
        MARTE_HLAM_RtUnit=var_18,
        MARTE_HLAM_RtUnit242=var_19,
    )
    var_21 = python_code_.MARTE_GRM_TimerResource(isPeriodic=var_11)
    assert isinstance(var_21, python_code_.MARTE_GRM_TimerResource)
    var_26 = python_code_.ProcessingResource()
    python_code_.MARTE_GCM_FlowPort(
        isAtomic=2, isConjugated=var_26, direction=(-792, 1034)
    )
    var_38 = 544
    python_code_.MARTE_HwPackage_HwPackage(pinNum=var_38, packageType=None, name=var_15)


def test_3():
    var_6 = python_code_.GRM_MARTE_NamedElement
    python_code_.MARTE_GCM_ClientServerFeature(
        kind=var_6, MARTE_GCM_ClientServerFeature=var_6
    )


def test_4():
    var_3 = "flash"
    var_4 = "HLAM_MARTE_InvocationAction299"
    var_5 = python_code_.MARTE_GCM_ClientServerPort(
        specificationKind=var_3,
        isConjugated=var_4,
        kind=var_3,
        MARTE_GCM_ClientServerPort805=var_4,
    )
    assert isinstance(var_5, python_code_.MARTE_GCM_ClientServerPort)


def test_5():
    var_25 = python_code_.MARTE_HwCommunication_HwPort()
    var_26 = "_MARTE_GQAM_GaEventTrace__MARTE_GQAM_GaEventTrace"
    var_27 = python_code_.SW_Concurrency_MARTE_BehavioralFeature()
    var_28 = {var_27, var_27, var_27, var_27}
    var_29 = python_code_.MARTE_SW_Concurrency_InterruptResource(
        kind=True, isMaskable=var_26, MARTE_SW_Concurrency_InterruptResource682=var_28
    )
    assert isinstance(var_29, python_code_.MARTE_SW_Concurrency_InterruptResource)
    var_34 = python_code_.MARTE_GRM_MutualExclusionResource(
        protectKind=var_25, otherProtectProtocol=var_26
    )
    assert isinstance(var_34, python_code_.MARTE_GRM_MutualExclusionResource)


@pytest.mark.xfail(strict=True)
def test_6():
    var_0 = "NFP_Natural345._MARTE_Time_TimedEvent__MARTE_Time_TimedEvent85"
    var_1 = python_code_.MARTE_HwMemory_HwMemory()
    var_2 = {var_1, var_1, var_1}
    var_3 = python_code_.MARTE_CoreElements_ModeBehavior
    python_code_.MARTE_HwDiagram_HwHRMDiagram(
        name=var_0,
        MARTE_HwDiagram_HwHRMDiagram=var_2,
        MARTE_HwDiagram_HwHRMDiagram597=var_2,
        MARTE_HwDiagram_HwHRMDiagram600=648,
        MARTE_HwDiagram_HwHRMDiagram603=var_3,
    )


@pytest.mark.xfail(strict=True)
def test_7():
    var_2 = python_code_.ExecutionKind.deferred
    var_5 = python_code_.GRM_MARTE_ConnectableElement()
    var_6 = python_code_.MARTE_GRM_Resource(
        isProtected=var_2, MARTE_GRM_Resource110=var_5
    )
    var_11 = "Time_ClockType"
    python_code_.MARTE_HwProtocol_HwProtocol(
        name=var_11, MARTE_HwProtocol_HwProtocol=var_6
    )


def test_8():
    var_0 = "@2X;|"
    python_code_.MARTE_Time_Clock(standard=var_0)


def test_9():
    python_code_.CallConcurrencyKind.concurrent
