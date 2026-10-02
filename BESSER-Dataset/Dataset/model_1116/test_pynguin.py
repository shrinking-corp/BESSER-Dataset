#  This file is part of Pynguin.
#
#  SPDX-FileCopyrightText: 2019�2026 Pynguin Contributors
#
#  SPDX-License-Identifier: MIT
#
#  This file was automatically generated using Pynguin.

import sys
import python_code

python_code_ = sys.modules["python_code"]
from python_code import (
    ABC,
    AccessData,
    ActionBottlenecksData,
    ActionBottlenecksWithSchedulingData,
    ActionDynamicData,
    ActionMemoryProfilingData,
    ActionToDoubleMap,
    ActionToLongMap,
    ActionToStatisticalDataMap,
    ActionVariablePipeliningData,
    ActionsVariablePipeliningReport,
    ActorDynamicData,
    ActorFire,
    ActorSelectionSchedule,
    ActorToLongMap,
    ActorToStatisticalDataMap,
    AnalysisReport,
    BalancedPipelinePartition,
    BottlenecksReport,
    BottlenecksWithSchedulingReport,
    BoundedBufferData,
    BoundedBuffersReport,
    BufferDynamicData,
    BufferToDoubleMap,
    BufferToIntegerMap,
    BufferToLongMap,
    BufferToStatisticalDataMap,
    CodeData,
    ComCostPartition,
    ComparedAction,
    ComparedTrace,
    ComplexCodeData,
    ComplexDynamicData,
    CompressedDependency,
    CompressedStep,
    CompressedTraceReport,
    DoubleToBottlenecksReportMap,
    DoubleToBottlenecksWithSchedulingReportMap,
    DoubleToDoubleMap,
    EOperatorToStatisticalDataMap,
    Enum,
    FSMCombination,
    FSMCombinator,
    FSMComparator,
    FSMCondition,
    FSMOp,
    FSMOperation,
    FSMState,
    FSMTransition,
    FSMVar,
    FSMVarUpdate,
    GuardToLongMap,
    ImpactAnalysisData,
    IntraActionCommunicationData,
    IntraActorCommunicationData,
    MarkovModelActionData,
    MarkovPartitionScheduler,
    MarkovSchedulingState,
    MarkovSchedulingTransition,
    MemoryAccessData,
    OptimalBufferData,
    Optimizer,
    PartitionToActorSelectionScheduleMap,
    PortToLongMap,
    PostProcessingData,
    ProcedureToComplexDynamicDataMap,
    ProcedureToStatisticalDataMap,
    ProfilingStatsActorData,
    ScheduledImpactAnalysisData,
    SchedulerChecksPartition,
    Sequence,
    StatisticalActorPartition,
    StringToAccessDataMap,
    StringToDoubleMap,
    StringToIntegerMap,
    StringToLongMap,
    StringToStringMap,
    TableRow,
    VariableToLongMap,
    VariableToStatisticalDataMap,
    WorkloadBalancePartition,
    abstractmethod,
    analysis_AnalysisReport,
    analysis_bottlenecks_ActionBottlenecksData,
    analysis_bottlenecks_ActionBottlenecksWithSchedulingData,
    analysis_bottlenecks_BottlenecksReport,
    analysis_bottlenecks_BottlenecksWithSchedulingReport,
    analysis_bottlenecks_DoubleToBottlenecksReportMap,
    analysis_bottlenecks_DoubleToBottlenecksWithSchedulingReportMap,
    analysis_bottlenecks_ImpactAnalysisData,
    analysis_bottlenecks_ImpactAnalysisReport,
    analysis_bottlenecks_ScheduledImpactAnalysisData,
    analysis_bottlenecks_ScheduledImpactAnalysisReport,
    analysis_buffers_BoundedBufferData,
    analysis_buffers_BoundedBuffersReport,
    analysis_buffers_OptimalBufferData,
    analysis_buffers_OptimalBuffersReport,
    analysis_caseoptimal_CaseOptimalActorSelectionSchedule,
    analysis_caseoptimal_CaseOptimalScheduleReport,
    analysis_map_ActionToDoubleMap,
    analysis_map_ActionToLongMap,
    analysis_map_ActionToStatisticalDataMap,
    analysis_map_ActorClassToStatisticalDataMap,
    analysis_map_ActorToLongMap,
    analysis_map_ActorToStatisticalDataMap,
    analysis_map_BufferToDoubleMap,
    analysis_map_BufferToIntegerMap,
    analysis_map_BufferToLongMap,
    analysis_map_BufferToStatisticalDataMap,
    analysis_map_DoubleToDoubleMap,
    analysis_map_EOperatorToStatisticalDataMap,
    analysis_map_GuardToLongMap,
    analysis_map_PartitionToActorSelectionScheduleMap,
    analysis_map_PortToLongMap,
    analysis_map_ProcedureToStatisticalDataMap,
    analysis_map_StringToDoubleMap,
    analysis_map_StringToIntegerMap,
    analysis_map_StringToLongMap,
    analysis_map_StringToStringMap,
    analysis_map_VariableToLongMap,
    analysis_map_VariableToStatisticalDataMap,
    analysis_partitioning_BalancedPipelinePartition,
    analysis_partitioning_BalancedPipelinePartitioningReport,
    analysis_partitioning_ComCostPartition,
    analysis_partitioning_ComCostPartitioningReport,
    analysis_partitioning_WorkloadBalancePartition,
    analysis_partitioning_WorkloadBalancePartitioningReport,
    analysis_pipelining_ActionVariablePipeliningData,
    analysis_pipelining_ActionsVariablePipeliningReport,
    analysis_pipelining_ImpactAnalysisData,
    analysis_pipelining_ImpactAnalysisReport,
    analysis_postprocessing_ActionStatisticsReport,
    analysis_postprocessing_ActorStatisticsReport,
    analysis_postprocessing_BufferBlockingReport,
    analysis_postprocessing_PostProcessingData,
    analysis_postprocessing_PostProcessingReport,
    analysis_postprocessing_SchedulerChecksPartition,
    analysis_postprocessing_SchedulerChecksReport,
    analysis_postprocessing_StatisticalActorPartition,
    analysis_profiler_AccessData,
    analysis_profiler_ActionDynamicData,
    analysis_profiler_ActionMemoryProfilingData,
    analysis_profiler_ActorDynamicData,
    analysis_profiler_BenchmarkReport,
    analysis_profiler_BufferAccessData,
    analysis_profiler_BufferDynamicData,
    analysis_profiler_CodeData,
    analysis_profiler_CodeProfilingReport,
    analysis_profiler_ComplexCodeData,
    analysis_profiler_ComplexDynamicData,
    analysis_profiler_DynamicProfilingReport,
    analysis_profiler_LocalVariableAccessData,
    analysis_profiler_MemoryAccessData,
    analysis_profiler_MemoryProfilingReport,
    analysis_profiler_ProcedureToComplexDynamicDataMap,
    analysis_profiler_SharedVariableAccessData,
    analysis_profiler_StateVariableAccessData,
    analysis_profiler_StringToAccessDataMap,
    analysis_profiler_TableRow,
    analysis_profiling_IntraActionCommunicationData,
    analysis_profiling_IntraActionCommunicationReport,
    analysis_profiling_IntraActorCommunicationData,
    analysis_profiling_ProfilingStatsActorData,
    analysis_profiling_ProfilingStatsReport,
    analysis_scheduling_ActorFire,
    analysis_scheduling_ActorSelectionSchedule,
    analysis_scheduling_FSM,
    analysis_scheduling_FSMCombination,
    analysis_scheduling_FSMCondition,
    analysis_scheduling_FSMOperation,
    analysis_scheduling_FSMState,
    analysis_scheduling_FSMTransition,
    analysis_scheduling_FSMTransitionWithState,
    analysis_scheduling_FSMVar,
    analysis_scheduling_FSMVarUpdate,
    analysis_scheduling_MarkovPartitionScheduler,
    analysis_scheduling_MarkovSchedulingState,
    analysis_scheduling_MarkovSchedulingTransition,
    analysis_scheduling_MarkovSimpleSchedulerReport,
    analysis_scheduling_PartitionedActorFire,
    analysis_scheduling_Sequence,
    analysis_trace_ComparedAction,
    analysis_trace_ComparedTrace,
    analysis_trace_CompressedDependency,
    analysis_trace_CompressedFsmDependency,
    analysis_trace_CompressedGuardDependency,
    analysis_trace_CompressedPortDependency,
    analysis_trace_CompressedStep,
    analysis_trace_CompressedTokensDependency,
    analysis_trace_CompressedTraceReport,
    analysis_trace_CompressedVariableDependency,
    analysis_trace_MarkovModelActionData,
    analysis_trace_MarkowModelTraceReport,
    analysis_trace_TraceComparatorReport,
    analysis_trace_TraceSizeReport,
    bottlenecks_analysis_Action,
    bottlenecks_analysis_ActorClass,
    bottlenecks_analysis_Network,
    buffers_analysis_Buffer,
    buffers_analysis_Network,
    date,
    datetime,
    map_analysis_Action,
    map_analysis_Actor,
    map_analysis_ActorClass,
    map_analysis_Buffer,
    map_analysis_Guard,
    map_analysis_Port,
    map_analysis_Procedure,
    map_analysis_StatisticalData,
    map_analysis_Variable,
    partitioning_analysis_Actor,
    partitioning_analysis_Network,
    pipelining_analysis_Action,
    pipelining_analysis_ActorClass,
    pipelining_analysis_Network,
    pipelining_analysis_StatisticalData,
    postprocessing_PostProcessingData,
    postprocessing_analysis_Actor,
    postprocessing_analysis_Network,
    postprocessing_analysis_StatisticalData,
    profiler_analysis_Action,
    profiler_analysis_Actor,
    profiler_analysis_Buffer,
    profiler_analysis_Network,
    profiler_analysis_Procedure,
    profiler_analysis_StatisticalData,
    profiling_analysis_Action,
    profiling_analysis_Actor,
    profiling_analysis_Network,
    profiling_analysis_StatisticalData,
    scheduling_analysis_Actor,
    scheduling_analysis_Network,
    time,
    trace_analysis_Action,
    trace_analysis_Network,
)


def test_0():
    var_1 = python_code_.FSMTransition()
    python_code_.analysis_map_ActionToDoubleMap(value=1)
    var_5 = lambda *args, **kwargs: True
    var_6 = python_code_.analysis_scheduling_MarkovPartitionScheduler(partitionId=var_1)
    assert isinstance(var_6, python_code_.analysis_scheduling_MarkovPartitionScheduler)
    var_7 = var_6.getAssociatedState(analysis_actor=var_1)
    var_8 = python_code_.analysis_profiler_ActionMemoryProfilingData(
        actor=None, action=var_5, analysis_profiler_ActionMemoryProfilingData67=var_7
    )
    var_8.getReadSharedVariableData(analysis_variable=var_6)


def test_1():
    var_3 = python_code_.analysis_trace_CompressedTraceReport
    python_code_.analysis_scheduling_FSMCombination(combinator=var_3)
    python_code_.analysis_map_ActionToDoubleMap(value=b"\xbc\x04\xe6\x99;\xed\xcf\xf5")


def test_2():
    var_0 = python_code_.partitioning_analysis_Network()
    var_1 = python_code_.analysis_partitioning_ComCostPartitioningReport(
        bitAccurate=complex(-3753.0263359, -1820.5),
        analysis_partitioning_ComCostPartitioningReport=var_0,
    )
    assert isinstance(
        var_1, python_code_.analysis_partitioning_ComCostPartitioningReport
    )
    var_4 = python_code_.FSMCondition()
    var_5 = python_code_.Sequence()
    python_code_.analysis_scheduling_FSMTransition(
        targetStateEnumName=None,
        sourceStateEnumName=[464.72],
        analysis_scheduling_FSMTransition=var_4,
        analysis_scheduling_FSMTransition428=var_5,
    )


def test_3():
    var_0 = python_code_.ActionMemoryProfilingData()
    var_1 = python_code_.ActionBottlenecksWithSchedulingData
    var_2 = python_code_.analysis_profiler_ActionMemoryProfilingData(
        actor='x;g} 5=|tC";e!3\\\x0b',
        action=var_1,
        analysis_profiler_ActionMemoryProfilingData=set(),
    )
    var_2.getReadBufferData(
        analysis_targetActor=var_2,
        analysis_sourceActor=b"\xae\x9dPj",
        analysis_sourcePort=var_1,
        analysis_targetPort=var_0,
    )
    var_7 = "JRdv{\rqJ>c"
    var_8 = python_code_.analysis_profiler_LocalVariableAccessData(name=var_7)
    assert isinstance(var_8, python_code_.analysis_profiler_LocalVariableAccessData)
    python_code_.analysis_map_ActorToLongMap(value=())
    var_11 = python_code_.analysis_profiler_ComplexCodeData()
    var_12 = python_code_.analysis_profiler_ComplexCodeData(CodeData13=var_11)
    assert isinstance(var_12, python_code_.analysis_profiler_ComplexCodeData)
    var_14 = python_code_.map_analysis_Guard()
    python_code_.analysis_map_GuardToLongMap(
        value=True, analysis_map_GuardToLongMap=var_14
    )
    python_code_.analysis_bottlenecks_DoubleToBottlenecksWithSchedulingReportMap(
        key=var_14,
        analysis_bottlenecks_DoubleToBottlenecksWithSchedulingReportMap=var_1,
    )


def test_4():
    var_0 = "YK\x0ca{N_p_odx|q"
    var_1 = python_code_.analysis_caseoptimal_CaseOptimalScheduleReport(
        traceFile=886, pipeline=(), partitionFilePath=var_0
    )
    assert isinstance(
        var_1, python_code_.analysis_caseoptimal_CaseOptimalScheduleReport
    )
    var_4 = "|"
    var_5 = ",y"
    var_6 = python_code_.CompressedDependency
    var_7 = python_code_.analysis_profiler_ActionMemoryProfilingData(
        actor=var_5, action=var_6
    )
    var_8 = var_7.getWriteSharedVariableData(
        analysis_variable=complex(-1768.6, -2298.0)
    )
    var_9 = python_code_.analysis_profiler_ActionMemoryProfilingData(
        actor=var_4, action=var_4, analysis_profiler_ActionMemoryProfilingData=var_8
    )
    var_7.getWriteLocalVariableData(analysis_variable=var_9)
    var_12 = python_code_.ProfilingStatsActorData()
    var_14 = python_code_.analysis_map_PartitionToActorSelectionScheduleMap(key=var_6)
    var_16 = python_code_.BoundedBuffersReport()
    var_17 = python_code_.analysis_buffers_OptimalBuffersReport(
        pow2={"x\r-Oy&,+2n/}": -660.86},
        bitAccurate=var_6,
        analysis_buffers_OptimalBuffersReport267=var_16,
        analysis_buffers_OptimalBuffersReport269=var_14,
    )
    assert isinstance(var_17, python_code_.analysis_buffers_OptimalBuffersReport)
    var_20 = 1962.33
    var_21 = python_code_.analysis_bottlenecks_BottlenecksReport(
        cpWeight=var_6,
        cpVariance=True,
        totalWeight=var_12,
        totalVariance=var_20,
        cpFirings=var_4,
        totalFirings="06id4,F(Y",
    )
    assert isinstance(var_21, python_code_.analysis_bottlenecks_BottlenecksReport)
    var_25 = python_code_.analysis_profiler_MemoryProfilingReport(networkName=var_17)
    assert isinstance(var_25, python_code_.analysis_profiler_MemoryProfilingReport)
    var_25.getActionData(analysis_actor=var_6, analysis_action=var_6)


def test_5():
    var_0 = python_code_.BoundedBuffersReport
    var_1 = (
        "_analysis_profiler_BufferDynamicData__analysis_profiler_BufferDynamicData28"
    )
    var_2 = ""
    var_3 = python_code_.analysis_profiler_ActionMemoryProfilingData(
        actor=var_1, action=var_2, analysis_profiler_ActionMemoryProfilingData67=var_1
    )
    var_4 = python_code_.analysis_profiler_LocalVariableAccessData(
        name=[], MemoryAccessData68=var_0, MemoryAccessData=var_3
    )
    assert isinstance(var_4, python_code_.analysis_profiler_LocalVariableAccessData)
    var_3.getReadStateVariableData(analysis_variable=var_2)


def test_6():
    var_0 = 1126.43
    var_1 = python_code_.MemoryAccessData
    var_2 = python_code_.analysis_bottlenecks_BottlenecksReport(
        cpWeight=[],
        cpVariance=complex(-2444.0, 2678.39),
        totalWeight=4466,
        totalVariance=var_0,
        cpFirings=50,
        totalFirings=var_1,
    )
    assert isinstance(var_2, python_code_.analysis_bottlenecks_BottlenecksReport)
    var_3 = "5U+\no}F\t"
    python_code_.analysis_map_StringToLongMap(key=var_3, value=var_1)
    var_6 = python_code_.MarkovSchedulingTransition
    python_code_.analysis_map_DoubleToDoubleMap(key=var_1, value=var_6)


def test_7():
    var_0 = "kvs)L7/qSqx`="
    var_1 = "trace_analysis_Network._analysis_profiler_BufferDynamicData__analysis_profiler_BufferDynamicData31._analysis_profiler_BufferDynamicData__analysis_profiler_BufferDynamicData28._analysis_trace_MarkowModelTraceReport__analysis_trace_MarkowModelTraceReport196"
    var_2 = python_code_.analysis_profiler_ActionMemoryProfilingData(
        actor=var_0, action=var_1
    )
    var_3 = var_2.getReadSharedVariableData(analysis_variable=var_0)
    var_5 = python_code_.scheduling_analysis_Network
    var_6 = var_2.getWriteStateVariableData(analysis_variable=var_5)
    var_7 = python_code_.analysis_trace_CompressedTraceReport(
        traceFile=var_0, analysis_trace_CompressedTraceReport138=var_6
    )
    assert isinstance(var_7, python_code_.analysis_trace_CompressedTraceReport)
    var_7.getSteps(analysis_actor=var_3)


def test_8():
    var_0 = python_code_.map_analysis_Port()
    var_4 = ""
    var_5 = "wJ`XXy "
    var_6 = python_code_.analysis_profiler_BufferAccessData(
        sourceActor=var_0,
        sourcePort=var_4,
        targetActor=var_5,
        targetPort=None,
        MemoryAccessData68=var_4,
    )
    assert isinstance(var_6, python_code_.analysis_profiler_BufferAccessData)


def test_9():
    var_0 = python_code_.analysis_profiler_ComplexCodeData()
    var_0.getProcedureData(analysis_procedure=var_0)
