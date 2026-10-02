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
    HwCommunication_HwEndPoint,
    HwCommunication_HwMedia,
    HwComponent,
    HwComputingResource,
    HwComputing_HwBranchPredictor,
    HwComputing_HwComputingResource,
    HwComputing_HwISA,
    HwComputing_HwProcessor,
    HwDevice,
    HwGeneral_HwResource,
    HwGeneral_HwResourceService,
    HwI_O,
    HwLayout_HwComponent,
    HwMedia,
    HwMemory,
    HwMemory_HwCache,
    HwMemory_HwMemory,
    HwMemory_HwRAM,
    HwResource,
    HwStorageManager,
    HwStorageManager_HwMMU,
    HwStorageManager_HwStorageManager,
    HwTimingResource,
    HwTiming_HwClock,
    ISA_Type,
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
    MARTE_GCM_GCMInvocatingBehavior,
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
    MARTE_HwCommunication_HwEndPoint,
    MARTE_HwCommunication_HwMedia,
    MARTE_HwComputing_HwASIC,
    MARTE_HwComputing_HwBranchPredictor,
    MARTE_HwComputing_HwComputingResource,
    MARTE_HwComputing_HwISA,
    MARTE_HwComputing_HwPLD,
    MARTE_HwComputing_HwProcessor,
    MARTE_HwDevice_HWActuator,
    MARTE_HwDevice_HWSensor,
    MARTE_HwDevice_HwDevice,
    MARTE_HwDevice_HwI_O,
    MARTE_HwDevice_HwSupport,
    MARTE_HwGeneral_HwResource,
    MARTE_HwGeneral_HwResourceService,
    MARTE_HwLayout_HwComponent,
    MARTE_HwMemory_HwCache,
    MARTE_HwMemory_HwDrive,
    MARTE_HwMemory_HwMemory,
    MARTE_HwMemory_HwRAM,
    MARTE_HwMemory_HwROM,
    MARTE_HwPower_HwCoolingSupply,
    MARTE_HwPower_HwPowerSupply,
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
    MARTE_Operators_Operator,
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
    MARTE_Time_TimedProcessing,
    MARTE_Time_TimedValueSpecification,
    MARTE_Variables_ExpressionContext,
    MARTE_Variables_Var,
    MessageResourceKind,
    MutualExclusionResource,
    MutualExclusionResourceKind,
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
    Operators_MARTE_Behavior,
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
    Repl_Policy,
    Resource,
    SAM_MARTE_BehavioralFeature,
    SAM_MARTE_NamedElement,
    SAM_SaSharedResource,
    SW_Brokering_MARTE_BehavioralFeature,
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
    SchedulableResource,
    Scheduler,
    SwCommunicationResource,
    SwConcurrentResource,
    SwResource,
    SwSynchronizationResource,
    SynchronizationKind,
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
    TimerResource,
    TimingResource,
    TupleType,
    VariableDirectionKind,
    Variables_ExpressionContext,
    Variables_MARTE_NamedElement,
    Variables_MARTE_Property,
    WritePolicy,
    abstractmethod,
    date,
    datetime,
    dummy,
    time,
)


def test_0():
    var_7 = python_code_.Time_ClockType()
    var_8 = python_code_.Time_MARTE_Event()
    python_code_.MARTE_Time_Clock(
        standard=b"\x9d7\xa1\xa9Iq\xcb,\xe2V\x04K",
        MARTE_Time_Clock53=var_7,
        MARTE_Time_Clock60=var_8,
    )
    var_10 = python_code_.MARTE_Time_TimedValueSpecification(interpretation=var_7)
    assert isinstance(var_10, python_code_.MARTE_Time_TimedValueSpecification)
    var_12 = "k?o}"
    var_13 = "(a)T\t4bA\n"
    python_code_.MARTE_PAM_PaRunTInstance(
        poolSize=set(), unbddPool=var_12, utilization=var_13, throughput=var_13
    )


def test_1():
    var_5 = "8}(dA7q(]%y_y6ff#"
    var_6 = lambda *args, **kwargs: "^nD0WCnBg*e"
    var_7 = "SW_Concurrency_MARTE_BehavioralFeature327"
    var_8 = python_code_.MARTE_SAM_SaCommStep(
        deadline=var_5,
        spareCap=var_6,
        schSlack=var_7,
        MARTE_SAM_SaCommStep=complex(1529.4, -1706.0),
    )
    assert isinstance(var_8, python_code_.MARTE_SAM_SaCommStep)
    python_code_.MARTE_GQAM_GaWorkloadGenerator(pop=var_6)
    var_14 = python_code_.MARTE_GQAM_GaTimedObs
    var_15 = "x=v~@&`&g\rzR#6[R"
    var_16 = "\n@@ust6~xcM'Ea]T"
    var_17 = "tG|Tn\r!RB`(Jy13+hT"
    var_18 = "~Gy'kRbq7j?m\t}n|"
    var_19 = python_code_.GRM_SchedulableResource()
    var_20 = python_code_.MARTE_GQAM_GaStep(
        isAtomic=var_5,
        blockT=var_14,
        rep=var_15,
        prob=var_16,
        priority=var_14,
        servCount=var_17,
        selfDelay=var_18,
        MARTE_GQAM_GaStep=var_19,
    )
    assert isinstance(var_20, python_code_.MARTE_GQAM_GaStep)
    var_22 = "[+8;gs;!dA"
    var_23 = python_code_.MARTE_Time_TimedConstraint(
        interpretation=var_22, NFPs_NfpConstraint49=None
    )
    assert isinstance(var_23, python_code_.MARTE_Time_TimedConstraint)


@pytest.mark.xfail(strict=True)
def test_2():
    var_1 = python_code_.RSM_MARTE_MultiplicityElement()
    var_2 = "2IM{`a"
    var_3 = "HwComputing_HwISA"
    var_4 = python_code_.HwComputing_HwBranchPredictor()
    var_5 = {var_4, var_4}
    python_code_.MARTE_HwComputing_HwProcessor(
        architecture=var_1,
        mips=b'\x81\xb0j\x13"\xc4\xc7Kel\xb6h\xcf',
        ipc=(-482.79, -5217.55),
        nbCores=var_2,
        nbPipelines=var_2,
        nbStages=var_2,
        nbALUs=var_3,
        nbFPUs={},
        MARTE_HwComputing_HwProcessor207=var_5,
        MARTE_HwComputing_HwProcessor209=var_5,
    )
    var_7 = "49VBN5SR2-D)1g8]"
    python_code_.MARTE_GQAM_GaTimedObs(
        laxity=var_7, MARTE_GQAM_GaTimedObs499=var_4, MARTE_GQAM_GaTimedObs=var_7
    )


def test_3():
    var_0 = python_code_.GaCommHost()
    var_1 = python_code_.CoreElements_MARTE_Transition()
    var_3 = python_code_.InterruptKind
    var_4 = "Xv"
    var_5 = "`o/)#$R'v;J;>ALH?"
    var_6 = '46x"\nkp_VxXQ'
    var_7 = python_code_.MARTE_GRM_Scheduler(
        isPreemptible={
            "\nQYGcS": -606.27,
            "_MARTE_GQAM_GaWorkloadEvent__MARTE_GQAM_GaWorkloadEvent476": -918,
        },
        schedPolicy=var_4,
        otherSchedPolicy=(),
        schedule=set(),
        MARTE_GRM_Scheduler=var_4,
    )
    assert isinstance(var_7, python_code_.MARTE_GRM_Scheduler)
    var_8 = python_code_.MARTE_SW_Interaction_SwMutualExclusionResource(
        mechanism=var_4,
        concurrentAccessProtocol=var_6,
        MARTE_SW_Interaction_SwMutualExclusionResource422=var_5,
        MutualExclusionResource=var_7,
    )
    assert isinstance(
        var_8, python_code_.MARTE_SW_Interaction_SwMutualExclusionResource
    )
    var_9 = python_code_.SW_Interaction_MARTE_BehavioralFeature()
    var_10 = {var_9}
    var_11 = python_code_.MARTE_SW_Interaction_SwMutualExclusionResource(
        mechanism=var_1,
        concurrentAccessProtocol=var_3,
        MARTE_SW_Interaction_SwMutualExclusionResource=b"{M\xf3\xa2",
        MARTE_SW_Interaction_SwMutualExclusionResource419=var_10,
        MARTE_SW_Interaction_SwMutualExclusionResource422=var_10,
    )
    var_12 = {var_8, var_8, var_8, var_11, var_8}
    python_code_.MARTE_GRM_Scheduler(
        isPreemptible=var_4,
        schedPolicy=var_4,
        otherSchedPolicy=-1620,
        schedule=var_5,
        MARTE_GRM_Scheduler=var_3,
        scheduler=var_12,
    )
    var_14 = python_code_.MARTE_GQAM_GaExecHost(
        commTxOvh=var_3,
        commRcvOvh=var_3,
        cntxtSwT=var_1,
        clockOvh=var_1,
        schedPriRange=var_1,
        memSize=var_4,
        utilization=var_5,
        throughput=var_4,
        GRM_ComputingResource=var_7,
        Scheduler=complex(2716.0, 1833.2838),
    )
    assert isinstance(var_14, python_code_.MARTE_GQAM_GaExecHost)
    var_17 = "<h@{^^1iIM/I"
    var_18 = python_code_.MARTE_RSM_Reshape(patternShape=var_17, repetitonShape=var_0)
    assert isinstance(var_18, python_code_.MARTE_RSM_Reshape)
    var_23 = "EPFJ*vVV\x0b2@vnbs9x~Z"
    var_24 = "+|.;91\x0baXhEIzji0F"
    python_code_.MARTE_HwStorageManager_HwMMU(
        virtualAddrSpace=var_4,
        physicalAddrSpace=var_23,
        memoryProtection=var_24,
        nbEntries=var_8,
        MARTE_HwStorageManager_HwMMU=var_12,
    )
    python_code_.MARTE_Alloc_Assign(kind=var_23, nature={-1507.35, 0})


def test_4():
    var_2 = "_MARTE_SAM_SaEndtoEndFlow__MARTE_SAM_SaEndtoEndFlow523"
    var_3 = "MARTE_GRM_ProcessingResource:HLAM_MARTE_BehavioralFeature204:SW_Concurrency_MARTE_TypedElement264"
    var_4 = python_code_.GRM_MARTE_Lifeline()
    python_code_.MARTE_GRM_Resource(
        resMult=1393,
        isProtected=var_2,
        isActive=var_3,
        MARTE_GRM_Resource=var_3,
        MARTE_GRM_Resource109=var_4,
        MARTE_GRM_Resource111=-1488,
    )


def test_5():
    var_5 = python_code_.PoolMgtPolicyKind.timedWait
    var_7 = "!OWud|)_TNR+>W7{\n\t"
    var_8 = lambda *args, **kwargs: []
    var_9 = "HwComputing_HwISA:SW_Interaction_MARTE_BehavioralFeature423:_MARTE_Time_TimedValueSpecification__MARTE_Time_TimedValueSpecification"
    var_10 = python_code_.HLAM_MARTE_Behavior()
    var_11 = python_code_.MARTE_HLAM_RtUnit(
        queueSchedPolicy=[
            807.08,
            "_MARTE_GQAM_GaStep__MARTE_GQAM_GaStep _MARTE_GRM_ProcessingResource__MARTE_GRM_ProcessingResource",
        ],
        isDynamic=var_7,
        isMain=var_8,
        srPoolSize=False,
        srPoolPolicy=var_8,
        srPoolWaitingTime=var_7,
        memorySize=var_8,
        queueSize=var_9,
        msgMaxSize=3506,
        MARTE_HLAM_RtUnit=var_10,
        MARTE_HLAM_RtUnit176=" [\x0bP2^o",
    )
    var_12 = python_code_.MARTE_HwMemory_HwDrive(
        sectorSize=["=tVT"], MARTE_HwMemory_HwDrive=var_11
    )
    assert isinstance(var_12, python_code_.MARTE_HwMemory_HwDrive)
    var_13 = python_code_.MARTE_SAM_SaSharedResource(
        releaseT=None, capacity=-1107, isPreemp=var_5, isConsum=var_7, acquisT=set()
    )
    assert isinstance(var_13, python_code_.MARTE_SAM_SaSharedResource)
    var_18 = python_code_.GRM_MARTE_Property()
    var_19 = python_code_.NfpConstraint
    python_code_.MARTE_GRM_Resource(
        resMult=None,
        isProtected=[2833.82],
        isActive=var_8,
        MARTE_GRM_Resource=var_18,
        MARTE_GRM_Resource109=var_19,
    )


def test_6():
    var_1 = "s(Q"
    var_2 = python_code_.SW_Concurrency_MARTE_TypedElement()
    var_3 = {var_2}
    var_4 = python_code_.MARTE_SW_Concurrency_InterruptResource(
        kind=var_1,
        isMaskable=("B!_w", True, 2059),
        MARTE_SW_Concurrency_InterruptResource304=var_3,
    )
    assert isinstance(var_4, python_code_.MARTE_SW_Concurrency_InterruptResource)


@pytest.mark.xfail(strict=True)
def test_7():
    var_0 = python_code_.Time_MARTE_Class()
    var_2 = "V<:nxJx7&C8oB"
    var_3 = "zI9ClXX!rM}Sn;q&]"
    var_4 = python_code_.MARTE_GCM_ClientServerPort
    var_5 = "@R3ns.:"
    python_code_.MARTE_HwLayout_HwComponent(
        grid=var_2,
        nbPins=var_2,
        weight=var_0,
        kind=var_3,
        dimensions=var_3,
        area=var_2,
        position={},
        price=var_4,
        r_Conditions=var_4,
        staticConsumption=var_5,
        staticDissipation=var_2,
    )
    var_10 = python_code_.HwMemory_HwRAM()
    var_11 = python_code_.MARTE_HwMemory_HwDrive(
        sectorSize=var_5, MARTE_HwMemory_HwDrive=var_10
    )
    assert isinstance(var_11, python_code_.MARTE_HwMemory_HwDrive)
    var_15 = python_code_.GRM_Resource()
    var_17 = set()
    python_code_.MARTE_SW_Brokering_MemoryBroker(
        accessPolicy=var_3,
        MARTE_SW_Brokering_MemoryBroker=var_15,
        MARTE_SW_Brokering_MemoryBroker366=var_17,
    )


def test_8():
    python_code_.SwSynchronizationResource()
