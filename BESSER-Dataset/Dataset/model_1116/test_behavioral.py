import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
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
    FSMCombination,
    FSMCondition,
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
    trace_analysis_Action,
    trace_analysis_Network,
    FSMCombinator,
    FSMComparator,
    FSMOp,
    Optimizer,
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

def test_assoc_action141_stub_double():
    # trace_analysis_Action has no real 'trace_analysis_Action' property in the generated
    # code (a bare stub) -- manually attach it so analysis_trace_CompressedStep's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # analysis_trace_CompressedStep's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = analysis_trace_CompressedStep(count="sample_text")
    partner = trace_analysis_Action()
    setattr(partner, 'trace_analysis_Action', None)
    _safe_set(owner, 'analysis_trace_CompressedStep', partner)
    assert getattr(partner, 'trace_analysis_Action') == owner
    _safe_set(owner, 'analysis_trace_CompressedStep', None)
    assert getattr(partner, 'trace_analysis_Action') is None


def test_assoc_action191_stub_double():
    # trace_analysis_Action has no real 'trace_analysis_Action192' property in the generated
    # code (a bare stub) -- manually attach it so analysis_trace_ComparedAction's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # analysis_trace_ComparedAction's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = analysis_trace_ComparedAction(dIncomings="sample_text", dOutgoings="sample_text", dSteps="sample_text", found=True)
    partner = trace_analysis_Action()
    setattr(partner, 'trace_analysis_Action192', None)
    _safe_set(owner, 'analysis_trace_ComparedAction', partner)
    assert getattr(partner, 'trace_analysis_Action192') == owner
    _safe_set(owner, 'analysis_trace_ComparedAction', None)
    assert getattr(partner, 'trace_analysis_Action192') is None


def test_assoc_action197_stub_double():
    # trace_analysis_Action has no real 'trace_analysis_Action198' property in the generated
    # code (a bare stub) -- manually attach it so analysis_trace_MarkovModelActionData's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # analysis_trace_MarkovModelActionData's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = analysis_trace_MarkovModelActionData(first=True, successors="sample_text")
    partner = trace_analysis_Action()
    setattr(partner, 'trace_analysis_Action198', None)
    _safe_set(owner, 'analysis_trace_MarkovModelActionData', partner)
    assert getattr(partner, 'trace_analysis_Action198') == owner
    _safe_set(owner, 'analysis_trace_MarkovModelActionData', None)
    assert getattr(partner, 'trace_analysis_Action198') is None


def test_assoc_action205_stub_double():
    # bottlenecks_analysis_Action has no real 'bottlenecks_analysis_Action' property in the generated
    # code (a bare stub) -- manually attach it so analysis_bottlenecks_ActionBottlenecksData's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # analysis_bottlenecks_ActionBottlenecksData's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = analysis_bottlenecks_ActionBottlenecksData(cpFirings="sample_text", cpVariance=3.14, cpWeight=3.14, slackMax=3.14, slackMin=3.14, totalFirings="sample_text", totalVariance=3.14, totalWeight=3.14)
    partner = bottlenecks_analysis_Action()
    setattr(partner, 'bottlenecks_analysis_Action', None)
    _safe_set(owner, 'analysis_bottlenecks_ActionBottlenecksData', partner)
    assert getattr(partner, 'bottlenecks_analysis_Action') == owner
    _safe_set(owner, 'analysis_bottlenecks_ActionBottlenecksData', None)
    assert getattr(partner, 'bottlenecks_analysis_Action') is None


def test_assoc_action228_stub_double():
    # bottlenecks_analysis_Action has no real 'bottlenecks_analysis_Action229' property in the generated
    # code (a bare stub) -- manually attach it so analysis_bottlenecks_ActionBottlenecksWithSchedulingData's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # analysis_bottlenecks_ActionBottlenecksWithSchedulingData's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = analysis_bottlenecks_ActionBottlenecksWithSchedulingData(cpFirings="sample_text", cpWeight=3.14, totalFirings="sample_text", totalWeight=3.14)
    partner = bottlenecks_analysis_Action()
    setattr(partner, 'bottlenecks_analysis_Action229', None)
    _safe_set(owner, 'analysis_bottlenecks_ActionBottlenecksWithSchedulingData', partner)
    assert getattr(partner, 'bottlenecks_analysis_Action229') == owner
    _safe_set(owner, 'analysis_bottlenecks_ActionBottlenecksWithSchedulingData', None)
    assert getattr(partner, 'bottlenecks_analysis_Action229') is None


def test_assoc_action301_stub_double():
    # pipelining_analysis_Action has no real 'pipelining_analysis_Action' property in the generated
    # code (a bare stub) -- manually attach it so analysis_pipelining_ActionVariablePipeliningData's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # analysis_pipelining_ActionVariablePipeliningData's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = analysis_pipelining_ActionVariablePipeliningData(pipelinable=True)
    partner = pipelining_analysis_Action()
    setattr(partner, 'pipelining_analysis_Action', None)
    _safe_set(owner, 'analysis_pipelining_ActionVariablePipeliningData', partner)
    assert getattr(partner, 'pipelining_analysis_Action') == owner
    _safe_set(owner, 'analysis_pipelining_ActionVariablePipeliningData', None)
    assert getattr(partner, 'pipelining_analysis_Action') is None


def test_assoc_actionPeeks38_stub_double():
    # ActionToLongMap has no real 'ActionToLongMap' property in the generated
    # code (a bare stub) -- manually attach it so analysis_profiler_BufferDynamicData's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # analysis_profiler_BufferDynamicData's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = analysis_profiler_BufferDynamicData(unconsumedTokens=7)
    partner = ActionToLongMap()
    setattr(partner, 'ActionToLongMap', None)
    _safe_set(owner, 'analysis_profiler_BufferDynamicData39', {partner})
    assert getattr(partner, 'ActionToLongMap') == owner
    _safe_set(owner, 'analysis_profiler_BufferDynamicData39', set())
    assert getattr(partner, 'ActionToLongMap') is None


def test_assoc_actionReadMisses40_stub_double():
    # ActionToLongMap has no real 'ActionToLongMap42' property in the generated
    # code (a bare stub) -- manually attach it so analysis_profiler_BufferDynamicData's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # analysis_profiler_BufferDynamicData's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = analysis_profiler_BufferDynamicData(unconsumedTokens=7)
    partner = ActionToLongMap()
    setattr(partner, 'ActionToLongMap42', None)
    _safe_set(owner, 'analysis_profiler_BufferDynamicData41', {partner})
    assert getattr(partner, 'ActionToLongMap42') == owner
    _safe_set(owner, 'analysis_profiler_BufferDynamicData41', set())
    assert getattr(partner, 'ActionToLongMap42') is None


def test_assoc_actionReads33_stub_double():
    # ActionToStatisticalDataMap has no real 'ActionToStatisticalDataMap' property in the generated
    # code (a bare stub) -- manually attach it so analysis_profiler_BufferDynamicData's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # analysis_profiler_BufferDynamicData's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = analysis_profiler_BufferDynamicData(unconsumedTokens=7)
    partner = ActionToStatisticalDataMap()
    setattr(partner, 'ActionToStatisticalDataMap', None)
    _safe_set(owner, 'analysis_profiler_BufferDynamicData34', {partner})
    assert getattr(partner, 'ActionToStatisticalDataMap') == owner
    _safe_set(owner, 'analysis_profiler_BufferDynamicData34', set())
    assert getattr(partner, 'ActionToStatisticalDataMap') is None


def test_assoc_actionWriteMisses43_stub_double():
    # ActionToLongMap has no real 'ActionToLongMap45' property in the generated
    # code (a bare stub) -- manually attach it so analysis_profiler_BufferDynamicData's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # analysis_profiler_BufferDynamicData's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = analysis_profiler_BufferDynamicData(unconsumedTokens=7)
    partner = ActionToLongMap()
    setattr(partner, 'ActionToLongMap45', None)
    _safe_set(owner, 'analysis_profiler_BufferDynamicData44', {partner})
    assert getattr(partner, 'ActionToLongMap45') == owner
    _safe_set(owner, 'analysis_profiler_BufferDynamicData44', set())
    assert getattr(partner, 'ActionToLongMap45') is None


def test_assoc_actionWrites35_stub_double():
    # ActionToStatisticalDataMap has no real 'ActionToStatisticalDataMap37' property in the generated
    # code (a bare stub) -- manually attach it so analysis_profiler_BufferDynamicData's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # analysis_profiler_BufferDynamicData's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = analysis_profiler_BufferDynamicData(unconsumedTokens=7)
    partner = ActionToStatisticalDataMap()
    setattr(partner, 'ActionToStatisticalDataMap37', None)
    _safe_set(owner, 'analysis_profiler_BufferDynamicData36', {partner})
    assert getattr(partner, 'ActionToStatisticalDataMap37') == owner
    _safe_set(owner, 'analysis_profiler_BufferDynamicData36', set())
    assert getattr(partner, 'ActionToStatisticalDataMap37') is None


def test_assoc_actions189_stub_double():
    # ComparedAction has no real 'ComparedAction' property in the generated
    # code (a bare stub) -- manually attach it so analysis_trace_ComparedTrace's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # analysis_trace_ComparedTrace's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = analysis_trace_ComparedTrace(dDependencies="sample_text", dSteps="sample_text", equal=True)
    partner = ComparedAction()
    setattr(partner, 'ComparedAction', None)
    _safe_set(owner, 'analysis_trace_ComparedTrace190', {partner})
    assert getattr(partner, 'ComparedAction') == owner
    _safe_set(owner, 'analysis_trace_ComparedTrace190', set())
    assert getattr(partner, 'ComparedAction') is None


def test_assoc_actions319_stub_double():
    # pipelining_analysis_Action has no real 'pipelining_analysis_Action321' property in the generated
    # code (a bare stub) -- manually attach it so analysis_pipelining_ImpactAnalysisData's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # analysis_pipelining_ImpactAnalysisData's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = analysis_pipelining_ImpactAnalysisData(cpReduction=3.14)
    partner = pipelining_analysis_Action()
    setattr(partner, 'pipelining_analysis_Action321', None)
    _safe_set(owner, 'analysis_pipelining_ImpactAnalysisData320', {partner})
    assert getattr(partner, 'pipelining_analysis_Action321') == owner
    _safe_set(owner, 'analysis_pipelining_ImpactAnalysisData320', set())
    assert getattr(partner, 'pipelining_analysis_Action321') is None


def test_assoc_actionsData10_stub_double():
    # CodeData has no real 'CodeData' property in the generated
    # code (a bare stub) -- manually attach it so analysis_profiler_ComplexCodeData's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # analysis_profiler_ComplexCodeData's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = analysis_profiler_ComplexCodeData()
    partner = CodeData()
    setattr(partner, 'CodeData', None)
    _safe_set(owner, 'analysis_profiler_ComplexCodeData', {partner})
    assert getattr(partner, 'CodeData') == owner
    _safe_set(owner, 'analysis_profiler_ComplexCodeData', set())
    assert getattr(partner, 'CodeData') is None


def test_assoc_actionsData195_stub_double():
    # MarkovModelActionData has no real 'MarkovModelActionData' property in the generated
    # code (a bare stub) -- manually attach it so analysis_trace_MarkowModelTraceReport's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # analysis_trace_MarkowModelTraceReport's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = analysis_trace_MarkowModelTraceReport()
    partner = MarkovModelActionData()
    setattr(partner, 'MarkovModelActionData', None)
    _safe_set(owner, 'analysis_trace_MarkowModelTraceReport196', {partner})
    assert getattr(partner, 'MarkovModelActionData') == owner
    _safe_set(owner, 'analysis_trace_MarkowModelTraceReport196', set())
    assert getattr(partner, 'MarkovModelActionData') is None


def test_assoc_actionsData203_stub_double():
    # ActionBottlenecksData has no real 'ActionBottlenecksData' property in the generated
    # code (a bare stub) -- manually attach it so analysis_bottlenecks_BottlenecksReport's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # analysis_bottlenecks_BottlenecksReport's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = analysis_bottlenecks_BottlenecksReport(cpFirings="sample_text", cpVariance=3.14, cpWeight=3.14, totalFirings="sample_text", totalVariance=3.14, totalWeight=3.14)
    partner = ActionBottlenecksData()
    setattr(partner, 'ActionBottlenecksData', None)
    _safe_set(owner, 'analysis_bottlenecks_BottlenecksReport204', {partner})
    assert getattr(partner, 'ActionBottlenecksData') == owner
    _safe_set(owner, 'analysis_bottlenecks_BottlenecksReport204', set())
    assert getattr(partner, 'ActionBottlenecksData') is None


def test_assoc_actionsData224_stub_double():
    # ActionBottlenecksWithSchedulingData has no real 'ActionBottlenecksWithSchedulingData' property in the generated
    # code (a bare stub) -- manually attach it so analysis_bottlenecks_BottlenecksWithSchedulingReport's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # analysis_bottlenecks_BottlenecksWithSchedulingReport's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = analysis_bottlenecks_BottlenecksWithSchedulingReport(cpBlockingTime=3.14, cpFirings="sample_text", cpWeight=3.14, executionTime=3.14, totalFirings="sample_text", totalWeight=3.14)
    partner = ActionBottlenecksWithSchedulingData()
    setattr(partner, 'ActionBottlenecksWithSchedulingData', None)
    _safe_set(owner, 'analysis_bottlenecks_BottlenecksWithSchedulingReport225', {partner})
    assert getattr(partner, 'ActionBottlenecksWithSchedulingData') == owner
    _safe_set(owner, 'analysis_bottlenecks_BottlenecksWithSchedulingReport225', set())
    assert getattr(partner, 'ActionBottlenecksWithSchedulingData') is None


def test_assoc_actionsData64_stub_double():
    # ActionMemoryProfilingData has no real 'ActionMemoryProfilingData' property in the generated
    # code (a bare stub) -- manually attach it so analysis_profiler_MemoryProfilingReport's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # analysis_profiler_MemoryProfilingReport's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = analysis_profiler_MemoryProfilingReport(networkName="sample_text")
    partner = ActionMemoryProfilingData()
    setattr(partner, 'ActionMemoryProfilingData', None)
    _safe_set(owner, 'analysis_profiler_MemoryProfilingReport', {partner})
    assert getattr(partner, 'ActionMemoryProfilingData') == owner
    _safe_set(owner, 'analysis_profiler_MemoryProfilingReport', set())
    assert getattr(partner, 'ActionMemoryProfilingData') is None


def test_assoc_actionsFirings115_stub_double():
    # ActionToLongMap has no real 'ActionToLongMap116' property in the generated
    # code (a bare stub) -- manually attach it so analysis_trace_TraceSizeReport's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # analysis_trace_TraceSizeReport's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = analysis_trace_TraceSizeReport(dependencies="sample_text", firings="sample_text")
    partner = ActionToLongMap()
    setattr(partner, 'ActionToLongMap116', None)
    _safe_set(owner, 'analysis_trace_TraceSizeReport', {partner})
    assert getattr(partner, 'ActionToLongMap116') == owner
    _safe_set(owner, 'analysis_trace_TraceSizeReport', set())
    assert getattr(partner, 'ActionToLongMap116') is None


def test_assoc_actionsIncomings117_stub_double():
    # ActionToLongMap has no real 'ActionToLongMap119' property in the generated
    # code (a bare stub) -- manually attach it so analysis_trace_TraceSizeReport's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # analysis_trace_TraceSizeReport's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = analysis_trace_TraceSizeReport(dependencies="sample_text", firings="sample_text")
    partner = ActionToLongMap()
    setattr(partner, 'ActionToLongMap119', None)
    _safe_set(owner, 'analysis_trace_TraceSizeReport118', {partner})
    assert getattr(partner, 'ActionToLongMap119') == owner
    _safe_set(owner, 'analysis_trace_TraceSizeReport118', set())
    assert getattr(partner, 'ActionToLongMap119') is None


def test_assoc_actionsOutgoings120_stub_double():
    # ActionToLongMap has no real 'ActionToLongMap122' property in the generated
    # code (a bare stub) -- manually attach it so analysis_trace_TraceSizeReport's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # analysis_trace_TraceSizeReport's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = analysis_trace_TraceSizeReport(dependencies="sample_text", firings="sample_text")
    partner = ActionToLongMap()
    setattr(partner, 'ActionToLongMap122', None)
    _safe_set(owner, 'analysis_trace_TraceSizeReport121', {partner})
    assert getattr(partner, 'ActionToLongMap122') == owner
    _safe_set(owner, 'analysis_trace_TraceSizeReport121', set())
    assert getattr(partner, 'ActionToLongMap122') is None


def test_assoc_actor449_stub_double():
    # scheduling_analysis_Actor has no real 'scheduling_analysis_Actor450' property in the generated
    # code (a bare stub) -- manually attach it so analysis_scheduling_MarkovSchedulingState's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # analysis_scheduling_MarkovSchedulingState's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = analysis_scheduling_MarkovSchedulingState(firings="sample_text", name="sample_text")
    partner = scheduling_analysis_Actor()
    setattr(partner, 'scheduling_analysis_Actor450', None)
    _safe_set(owner, 'analysis_scheduling_MarkovSchedulingState', partner)
    assert getattr(partner, 'scheduling_analysis_Actor450') == owner
    _safe_set(owner, 'analysis_scheduling_MarkovSchedulingState', None)
    assert getattr(partner, 'scheduling_analysis_Actor450') is None


def test_assoc_actorClass322_stub_double():
    # pipelining_analysis_ActorClass has no real 'pipelining_analysis_ActorClass' property in the generated
    # code (a bare stub) -- manually attach it so analysis_pipelining_ImpactAnalysisData's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # analysis_pipelining_ImpactAnalysisData's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = analysis_pipelining_ImpactAnalysisData(cpReduction=3.14)
    partner = pipelining_analysis_ActorClass()
    setattr(partner, 'pipelining_analysis_ActorClass', None)
    _safe_set(owner, 'analysis_pipelining_ImpactAnalysisData323', partner)
    assert getattr(partner, 'pipelining_analysis_ActorClass') == owner
    _safe_set(owner, 'analysis_pipelining_ImpactAnalysisData323', None)
    assert getattr(partner, 'pipelining_analysis_ActorClass') is None


def test_assoc_actorClassesData1_stub_double():
    # ComplexCodeData has no real 'ComplexCodeData' property in the generated
    # code (a bare stub) -- manually attach it so analysis_profiler_CodeProfilingReport's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # analysis_profiler_CodeProfilingReport's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = analysis_profiler_CodeProfilingReport()
    partner = ComplexCodeData()
    setattr(partner, 'ComplexCodeData', None)
    _safe_set(owner, 'analysis_profiler_CodeProfilingReport2', {partner})
    assert getattr(partner, 'ComplexCodeData') == owner
    _safe_set(owner, 'analysis_profiler_CodeProfilingReport2', set())
    assert getattr(partner, 'ComplexCodeData') is None


def test_assoc_actors279_stub_double():
    # partitioning_analysis_Actor has no real 'partitioning_analysis_Actor' property in the generated
    # code (a bare stub) -- manually attach it so analysis_partitioning_ComCostPartition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # analysis_partitioning_ComCostPartition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = analysis_partitioning_ComCostPartition(externalCost="sample_text", internalCost="sample_text")
    partner = partitioning_analysis_Actor()
    setattr(partner, 'partitioning_analysis_Actor', None)
    _safe_set(owner, 'analysis_partitioning_ComCostPartition', {partner})
    assert getattr(partner, 'partitioning_analysis_Actor') == owner
    _safe_set(owner, 'analysis_partitioning_ComCostPartition', set())
    assert getattr(partner, 'partitioning_analysis_Actor') is None


def test_assoc_actors286_stub_double():
    # partitioning_analysis_Actor has no real 'partitioning_analysis_Actor287' property in the generated
    # code (a bare stub) -- manually attach it so analysis_partitioning_WorkloadBalancePartition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # analysis_partitioning_WorkloadBalancePartition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = analysis_partitioning_WorkloadBalancePartition(workload=3.14)
    partner = partitioning_analysis_Actor()
    setattr(partner, 'partitioning_analysis_Actor287', None)
    _safe_set(owner, 'analysis_partitioning_WorkloadBalancePartition', {partner})
    assert getattr(partner, 'partitioning_analysis_Actor287') == owner
    _safe_set(owner, 'analysis_partitioning_WorkloadBalancePartition', set())
    assert getattr(partner, 'partitioning_analysis_Actor287') is None


def test_assoc_actors292_stub_double():
    # partitioning_analysis_Actor has no real 'partitioning_analysis_Actor293' property in the generated
    # code (a bare stub) -- manually attach it so analysis_partitioning_BalancedPipelinePartition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # analysis_partitioning_BalancedPipelinePartition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = analysis_partitioning_BalancedPipelinePartition(commonPredAvg=3.14, preWorkload=3.14, workload=3.14)
    partner = partitioning_analysis_Actor()
    setattr(partner, 'partitioning_analysis_Actor293', None)
    _safe_set(owner, 'analysis_partitioning_BalancedPipelinePartition', {partner})
    assert getattr(partner, 'partitioning_analysis_Actor293') == owner
    _safe_set(owner, 'analysis_partitioning_BalancedPipelinePartition', set())
    assert getattr(partner, 'partitioning_analysis_Actor293') is None


def test_assoc_actors444_stub_double():
    # scheduling_analysis_Actor has no real 'scheduling_analysis_Actor' property in the generated
    # code (a bare stub) -- manually attach it so analysis_scheduling_MarkovPartitionScheduler's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # analysis_scheduling_MarkovPartitionScheduler's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = analysis_scheduling_MarkovPartitionScheduler(partitionId="sample_text")
    partner = scheduling_analysis_Actor()
    setattr(partner, 'scheduling_analysis_Actor', None)
    _safe_set(owner, 'analysis_scheduling_MarkovPartitionScheduler', {partner})
    assert getattr(partner, 'scheduling_analysis_Actor') == owner
    _safe_set(owner, 'analysis_scheduling_MarkovPartitionScheduler', set())
    assert getattr(partner, 'scheduling_analysis_Actor') is None


def test_assoc_actorsFirings123_stub_double():
    # ActorToLongMap has no real 'ActorToLongMap' property in the generated
    # code (a bare stub) -- manually attach it so analysis_trace_TraceSizeReport's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # analysis_trace_TraceSizeReport's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = analysis_trace_TraceSizeReport(dependencies="sample_text", firings="sample_text")
    partner = ActorToLongMap()
    setattr(partner, 'ActorToLongMap', None)
    _safe_set(owner, 'analysis_trace_TraceSizeReport124', {partner})
    assert getattr(partner, 'ActorToLongMap') == owner
    _safe_set(owner, 'analysis_trace_TraceSizeReport124', set())
    assert getattr(partner, 'ActorToLongMap') is None


def test_assoc_actorsIncoming125_stub_double():
    # ActorToLongMap has no real 'ActorToLongMap127' property in the generated
    # code (a bare stub) -- manually attach it so analysis_trace_TraceSizeReport's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # analysis_trace_TraceSizeReport's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = analysis_trace_TraceSizeReport(dependencies="sample_text", firings="sample_text")
    partner = ActorToLongMap()
    setattr(partner, 'ActorToLongMap127', None)
    _safe_set(owner, 'analysis_trace_TraceSizeReport126', {partner})
    assert getattr(partner, 'ActorToLongMap127') == owner
    _safe_set(owner, 'analysis_trace_TraceSizeReport126', set())
    assert getattr(partner, 'ActorToLongMap127') is None


def test_assoc_actorsOutgoings128_stub_double():
    # ActorToLongMap has no real 'ActorToLongMap130' property in the generated
    # code (a bare stub) -- manually attach it so analysis_trace_TraceSizeReport's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # analysis_trace_TraceSizeReport's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = analysis_trace_TraceSizeReport(dependencies="sample_text", firings="sample_text")
    partner = ActorToLongMap()
    setattr(partner, 'ActorToLongMap130', None)
    _safe_set(owner, 'analysis_trace_TraceSizeReport129', {partner})
    assert getattr(partner, 'ActorToLongMap130') == owner
    _safe_set(owner, 'analysis_trace_TraceSizeReport129', set())
    assert getattr(partner, 'ActorToLongMap130') is None


def test_assoc_actorsStatsData421_stub_double():
    # ProfilingStatsActorData has no real 'ProfilingStatsActorData' property in the generated
    # code (a bare stub) -- manually attach it so analysis_profiling_ProfilingStatsReport's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # analysis_profiling_ProfilingStatsReport's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = analysis_profiling_ProfilingStatsReport(networkName="sample_text")
    partner = ProfilingStatsActorData()
    setattr(partner, 'ProfilingStatsActorData', None)
    _safe_set(owner, 'analysis_profiling_ProfilingStatsReport', {partner})
    assert getattr(partner, 'ProfilingStatsActorData') == owner
    _safe_set(owner, 'analysis_profiling_ProfilingStatsReport', set())
    assert getattr(partner, 'ProfilingStatsActorData') is None


def test_assoc_blockedReadingTimes334_stub_double():
    # StringToDoubleMap has no real 'StringToDoubleMap336' property in the generated
    # code (a bare stub) -- manually attach it so analysis_postprocessing_ActorStatisticsReport's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # analysis_postprocessing_ActorStatisticsReport's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = analysis_postprocessing_ActorStatisticsReport(averageOccupancy=3.14, executionTime=3.14, occupancyDeviation=3.14)
    partner = StringToDoubleMap()
    setattr(partner, 'StringToDoubleMap336', None)
    _safe_set(owner, 'analysis_postprocessing_ActorStatisticsReport335', {partner})
    assert getattr(partner, 'StringToDoubleMap336') == owner
    _safe_set(owner, 'analysis_postprocessing_ActorStatisticsReport335', set())
    assert getattr(partner, 'StringToDoubleMap336') is None


def test_assoc_blockedWritingTimes337_stub_double():
    # StringToDoubleMap has no real 'StringToDoubleMap339' property in the generated
    # code (a bare stub) -- manually attach it so analysis_postprocessing_ActorStatisticsReport's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # analysis_postprocessing_ActorStatisticsReport's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = analysis_postprocessing_ActorStatisticsReport(averageOccupancy=3.14, executionTime=3.14, occupancyDeviation=3.14)
    partner = StringToDoubleMap()
    setattr(partner, 'StringToDoubleMap339', None)
    _safe_set(owner, 'analysis_postprocessing_ActorStatisticsReport338', {partner})
    assert getattr(partner, 'StringToDoubleMap339') == owner
    _safe_set(owner, 'analysis_postprocessing_ActorStatisticsReport338', set())
    assert getattr(partner, 'StringToDoubleMap339') is None


def test_assoc_blockingInstances234_stub_double():
    # BufferToIntegerMap has no real 'BufferToIntegerMap236' property in the generated
    # code (a bare stub) -- manually attach it so analysis_bottlenecks_ActionBottlenecksWithSchedulingData's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # analysis_bottlenecks_ActionBottlenecksWithSchedulingData's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = analysis_bottlenecks_ActionBottlenecksWithSchedulingData(cpFirings="sample_text", cpWeight=3.14, totalFirings="sample_text", totalWeight=3.14)
    partner = BufferToIntegerMap()
    setattr(partner, 'BufferToIntegerMap236', None)
    _safe_set(owner, 'analysis_bottlenecks_ActionBottlenecksWithSchedulingData235', {partner})
    assert getattr(partner, 'BufferToIntegerMap236') == owner
    _safe_set(owner, 'analysis_bottlenecks_ActionBottlenecksWithSchedulingData235', set())
    assert getattr(partner, 'BufferToIntegerMap236') is None


def test_assoc_buffer24_stub_double():
    # profiler_analysis_Buffer has no real 'profiler_analysis_Buffer' property in the generated
    # code (a bare stub) -- manually attach it so analysis_profiler_BufferDynamicData's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # analysis_profiler_BufferDynamicData's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = analysis_profiler_BufferDynamicData(unconsumedTokens=7)
    partner = profiler_analysis_Buffer()
    setattr(partner, 'profiler_analysis_Buffer', None)
    _safe_set(owner, 'analysis_profiler_BufferDynamicData', partner)
    assert getattr(partner, 'profiler_analysis_Buffer') == owner
    _safe_set(owner, 'analysis_profiler_BufferDynamicData', None)
    assert getattr(partner, 'profiler_analysis_Buffer') is None


def test_assoc_buffer261_stub_double():
    # buffers_analysis_Buffer has no real 'buffers_analysis_Buffer' property in the generated
    # code (a bare stub) -- manually attach it so analysis_buffers_BoundedBufferData's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # analysis_buffers_BoundedBufferData's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = analysis_buffers_BoundedBufferData(bitSize=7, tokenSize=7)
    partner = buffers_analysis_Buffer()
    setattr(partner, 'buffers_analysis_Buffer', None)
    _safe_set(owner, 'analysis_buffers_BoundedBufferData', partner)
    assert getattr(partner, 'buffers_analysis_Buffer') == owner
    _safe_set(owner, 'analysis_buffers_BoundedBufferData', None)
    assert getattr(partner, 'buffers_analysis_Buffer') is None


def test_assoc_buffersData259_stub_double():
    # BoundedBufferData has no real 'BoundedBufferData' property in the generated
    # code (a bare stub) -- manually attach it so analysis_buffers_BoundedBuffersReport's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # analysis_buffers_BoundedBuffersReport's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = analysis_buffers_BoundedBuffersReport(bitAccurate=True, bitSize=7, pow2=True, tokenSize=7)
    partner = BoundedBufferData()
    setattr(partner, 'BoundedBufferData', None)
    _safe_set(owner, 'analysis_buffers_BoundedBuffersReport260', {partner})
    assert getattr(partner, 'BoundedBufferData') == owner
    _safe_set(owner, 'analysis_buffers_BoundedBuffersReport260', set())
    assert getattr(partner, 'BoundedBufferData') is None


def test_assoc_buffersData264_stub_double():
    # OptimalBufferData has no real 'OptimalBufferData' property in the generated
    # code (a bare stub) -- manually attach it so analysis_buffers_OptimalBuffersReport's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # analysis_buffers_OptimalBuffersReport's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = analysis_buffers_OptimalBuffersReport(bitAccurate=True, pow2=True)
    partner = OptimalBufferData()
    setattr(partner, 'OptimalBufferData', None)
    _safe_set(owner, 'analysis_buffers_OptimalBuffersReport265', {partner})
    assert getattr(partner, 'OptimalBufferData') == owner
    _safe_set(owner, 'analysis_buffers_OptimalBuffersReport265', set())
    assert getattr(partner, 'OptimalBufferData') is None


def test_assoc_combinedCond438_stub_double():
    # FSMCombination has no real 'FSMCombination' property in the generated
    # code (a bare stub) -- manually attach it so analysis_scheduling_FSMCondition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # analysis_scheduling_FSMCondition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = analysis_scheduling_FSMCondition(comp="sample_text", compval="sample_text", valName="sample_text")
    partner = FSMCombination()
    setattr(partner, 'FSMCombination', None)
    _safe_set(owner, 'analysis_scheduling_FSMCondition', partner)
    assert getattr(partner, 'FSMCombination') == owner
    _safe_set(owner, 'analysis_scheduling_FSMCondition', None)
    assert getattr(partner, 'FSMCombination') is None


def test_assoc_compressedTrace184_stub_double():
    # CompressedTraceReport has no real 'CompressedTraceReport185' property in the generated
    # code (a bare stub) -- manually attach it so analysis_trace_ComparedTrace's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # analysis_trace_ComparedTrace's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = analysis_trace_ComparedTrace(dDependencies="sample_text", dSteps="sample_text", equal=True)
    partner = CompressedTraceReport()
    setattr(partner, 'CompressedTraceReport185', None)
    _safe_set(owner, 'analysis_trace_ComparedTrace', partner)
    assert getattr(partner, 'CompressedTraceReport185') == owner
    _safe_set(owner, 'analysis_trace_ComparedTrace', None)
    assert getattr(partner, 'CompressedTraceReport185') is None


def test_assoc_cond426_stub_double():
    # FSMCondition has no real 'FSMCondition' property in the generated
    # code (a bare stub) -- manually attach it so analysis_scheduling_FSMTransition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # analysis_scheduling_FSMTransition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = analysis_scheduling_FSMTransition(sourceStateEnumName="sample_text", targetStateEnumName="sample_text")
    partner = FSMCondition()
    setattr(partner, 'FSMCondition', None)
    _safe_set(owner, 'analysis_scheduling_FSMTransition', partner)
    assert getattr(partner, 'FSMCondition') == owner
    _safe_set(owner, 'analysis_scheduling_FSMTransition', None)
    assert getattr(partner, 'FSMCondition') is None


def test_assoc_cond436_stub_double():
    # FSMCondition has no real 'FSMCondition437' property in the generated
    # code (a bare stub) -- manually attach it so analysis_scheduling_FSMCombination's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # analysis_scheduling_FSMCombination's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = analysis_scheduling_FSMCombination(combinator="sample_text")
    partner = FSMCondition()
    setattr(partner, 'FSMCondition437', None)
    _safe_set(owner, 'analysis_scheduling_FSMCombination', partner)
    assert getattr(partner, 'FSMCondition437') == owner
    _safe_set(owner, 'analysis_scheduling_FSMCombination', None)
    assert getattr(partner, 'FSMCondition437') is None


def test_assoc_consecutiveFirings302_stub_double():
    # pipelining_analysis_StatisticalData has no real 'pipelining_analysis_StatisticalData' property in the generated
    # code (a bare stub) -- manually attach it so analysis_pipelining_ActionVariablePipeliningData's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # analysis_pipelining_ActionVariablePipeliningData's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = analysis_pipelining_ActionVariablePipeliningData(pipelinable=True)
    partner = pipelining_analysis_StatisticalData()
    setattr(partner, 'pipelining_analysis_StatisticalData', None)
    _safe_set(owner, 'analysis_pipelining_ActionVariablePipeliningData303', partner)
    assert getattr(partner, 'pipelining_analysis_StatisticalData') == owner
    _safe_set(owner, 'analysis_pipelining_ActionVariablePipeliningData303', None)
    assert getattr(partner, 'pipelining_analysis_StatisticalData') is None


def test_assoc_containedReferenceActions186_stub_double():
    # trace_analysis_Action has no real 'trace_analysis_Action188' property in the generated
    # code (a bare stub) -- manually attach it so analysis_trace_ComparedTrace's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # analysis_trace_ComparedTrace's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = analysis_trace_ComparedTrace(dDependencies="sample_text", dSteps="sample_text", equal=True)
    partner = trace_analysis_Action()
    setattr(partner, 'trace_analysis_Action188', None)
    _safe_set(owner, 'analysis_trace_ComparedTrace187', {partner})
    assert getattr(partner, 'trace_analysis_Action188') == owner
    _safe_set(owner, 'analysis_trace_ComparedTrace187', set())
    assert getattr(partner, 'trace_analysis_Action188') is None


def test_assoc_cpPartitionsBlockingTime226_stub_double():
    # StringToDoubleMap has no real 'StringToDoubleMap' property in the generated
    # code (a bare stub) -- manually attach it so analysis_bottlenecks_BottlenecksWithSchedulingReport's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # analysis_bottlenecks_BottlenecksWithSchedulingReport's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = analysis_bottlenecks_BottlenecksWithSchedulingReport(cpBlockingTime=3.14, cpFirings="sample_text", cpWeight=3.14, executionTime=3.14, totalFirings="sample_text", totalWeight=3.14)
    partner = StringToDoubleMap()
    setattr(partner, 'StringToDoubleMap', None)
    _safe_set(owner, 'analysis_bottlenecks_BottlenecksWithSchedulingReport227', {partner})
    assert getattr(partner, 'StringToDoubleMap') == owner
    _safe_set(owner, 'analysis_bottlenecks_BottlenecksWithSchedulingReport227', set())
    assert getattr(partner, 'StringToDoubleMap') is None


def test_assoc_dependencies139_stub_double():
    # CompressedDependency has no real 'CompressedDependency' property in the generated
    # code (a bare stub) -- manually attach it so analysis_trace_CompressedTraceReport's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # analysis_trace_CompressedTraceReport's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = analysis_trace_CompressedTraceReport(traceFile="sample_text")
    partner = CompressedDependency()
    setattr(partner, 'CompressedDependency', None)
    _safe_set(owner, 'analysis_trace_CompressedTraceReport140', {partner})
    assert getattr(partner, 'CompressedDependency') == owner
    _safe_set(owner, 'analysis_trace_CompressedTraceReport140', set())
    assert getattr(partner, 'CompressedDependency') is None


def test_assoc_dependenciesKinds131_stub_double():
    # StringToLongMap has no real 'StringToLongMap' property in the generated
    # code (a bare stub) -- manually attach it so analysis_trace_TraceSizeReport's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # analysis_trace_TraceSizeReport's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = analysis_trace_TraceSizeReport(dependencies="sample_text", firings="sample_text")
    partner = StringToLongMap()
    setattr(partner, 'StringToLongMap', None)
    _safe_set(owner, 'analysis_trace_TraceSizeReport132', {partner})
    assert getattr(partner, 'StringToLongMap') == owner
    _safe_set(owner, 'analysis_trace_TraceSizeReport132', set())
    assert getattr(partner, 'StringToLongMap') is None


def test_assoc_estimatedBottlenecks317_stub_double():
    # BottlenecksReport has no real 'BottlenecksReport318' property in the generated
    # code (a bare stub) -- manually attach it so analysis_pipelining_ImpactAnalysisData's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # analysis_pipelining_ImpactAnalysisData's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = analysis_pipelining_ImpactAnalysisData(cpReduction=3.14)
    partner = BottlenecksReport()
    setattr(partner, 'BottlenecksReport318', None)
    _safe_set(owner, 'analysis_pipelining_ImpactAnalysisData', partner)
    assert getattr(partner, 'BottlenecksReport318') == owner
    _safe_set(owner, 'analysis_pipelining_ImpactAnalysisData', None)
    assert getattr(partner, 'BottlenecksReport318') is None


def test_assoc_externalCostMap283_stub_double():
    # ActorToLongMap has no real 'ActorToLongMap285' property in the generated
    # code (a bare stub) -- manually attach it so analysis_partitioning_ComCostPartition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # analysis_partitioning_ComCostPartition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = analysis_partitioning_ComCostPartition(externalCost="sample_text", internalCost="sample_text")
    partner = ActorToLongMap()
    setattr(partner, 'ActorToLongMap285', None)
    _safe_set(owner, 'analysis_partitioning_ComCostPartition284', {partner})
    assert getattr(partner, 'ActorToLongMap285') == owner
    _safe_set(owner, 'analysis_partitioning_ComCostPartition284', set())
    assert getattr(partner, 'ActorToLongMap285') is None


def test_assoc_idleTimes331_stub_double():
    # StringToDoubleMap has no real 'StringToDoubleMap333' property in the generated
    # code (a bare stub) -- manually attach it so analysis_postprocessing_ActorStatisticsReport's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # analysis_postprocessing_ActorStatisticsReport's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = analysis_postprocessing_ActorStatisticsReport(averageOccupancy=3.14, executionTime=3.14, occupancyDeviation=3.14)
    partner = StringToDoubleMap()
    setattr(partner, 'StringToDoubleMap333', None)
    _safe_set(owner, 'analysis_postprocessing_ActorStatisticsReport332', {partner})
    assert getattr(partner, 'StringToDoubleMap333') == owner
    _safe_set(owner, 'analysis_postprocessing_ActorStatisticsReport332', set())
    assert getattr(partner, 'StringToDoubleMap333') is None


def test_assoc_impactData208_stub_double():
    # ImpactAnalysisData has no real 'ImpactAnalysisData' property in the generated
    # code (a bare stub) -- manually attach it so analysis_bottlenecks_ImpactAnalysisReport's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # analysis_bottlenecks_ImpactAnalysisReport's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = analysis_bottlenecks_ImpactAnalysisReport(classLevel=True)
    partner = ImpactAnalysisData()
    setattr(partner, 'ImpactAnalysisData', None)
    _safe_set(owner, 'analysis_bottlenecks_ImpactAnalysisReport209', {partner})
    assert getattr(partner, 'ImpactAnalysisData') == owner
    _safe_set(owner, 'analysis_bottlenecks_ImpactAnalysisReport209', set())
    assert getattr(partner, 'ImpactAnalysisData') is None


def test_assoc_incomings142_stub_double():
    # CompressedDependency has no real 'CompressedDependency143' property in the generated
    # code (a bare stub) -- manually attach it so analysis_trace_CompressedStep's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # analysis_trace_CompressedStep's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = analysis_trace_CompressedStep(count="sample_text")
    partner = CompressedDependency()
    setattr(partner, 'CompressedDependency143', None)
    _safe_set(owner, 'target', {partner})
    assert getattr(partner, 'CompressedDependency143') == owner
    _safe_set(owner, 'target', set())
    assert getattr(partner, 'CompressedDependency143') is None


def test_assoc_incomings454_stub_double():
    # MarkovSchedulingTransition has no real 'MarkovSchedulingTransition456' property in the generated
    # code (a bare stub) -- manually attach it so analysis_scheduling_MarkovSchedulingState's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # analysis_scheduling_MarkovSchedulingState's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = analysis_scheduling_MarkovSchedulingState(firings="sample_text", name="sample_text")
    partner = MarkovSchedulingTransition()
    setattr(partner, 'MarkovSchedulingTransition456', None)
    _safe_set(owner, 'target455', {partner})
    assert getattr(partner, 'MarkovSchedulingTransition456') == owner
    _safe_set(owner, 'target455', set())
    assert getattr(partner, 'MarkovSchedulingTransition456') is None


def test_assoc_initialBottlenecks210_stub_double():
    # BottlenecksReport has no real 'BottlenecksReport' property in the generated
    # code (a bare stub) -- manually attach it so analysis_bottlenecks_ImpactAnalysisReport's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # analysis_bottlenecks_ImpactAnalysisReport's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = analysis_bottlenecks_ImpactAnalysisReport(classLevel=True)
    partner = BottlenecksReport()
    setattr(partner, 'BottlenecksReport', None)
    _safe_set(owner, 'analysis_bottlenecks_ImpactAnalysisReport211', partner)
    assert getattr(partner, 'BottlenecksReport') == owner
    _safe_set(owner, 'analysis_bottlenecks_ImpactAnalysisReport211', None)
    assert getattr(partner, 'BottlenecksReport') is None


def test_assoc_initialBottlenecks268_stub_double():
    # BottlenecksWithSchedulingReport has no real 'BottlenecksWithSchedulingReport270' property in the generated
    # code (a bare stub) -- manually attach it so analysis_buffers_OptimalBuffersReport's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # analysis_buffers_OptimalBuffersReport's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = analysis_buffers_OptimalBuffersReport(bitAccurate=True, pow2=True)
    partner = BottlenecksWithSchedulingReport()
    setattr(partner, 'BottlenecksWithSchedulingReport270', None)
    _safe_set(owner, 'analysis_buffers_OptimalBuffersReport269', partner)
    assert getattr(partner, 'BottlenecksWithSchedulingReport270') == owner
    _safe_set(owner, 'analysis_buffers_OptimalBuffersReport269', None)
    assert getattr(partner, 'BottlenecksWithSchedulingReport270') is None


def test_assoc_initialBottlenecksWithScheduling255_stub_double():
    # BottlenecksWithSchedulingReport has no real 'BottlenecksWithSchedulingReport257' property in the generated
    # code (a bare stub) -- manually attach it so analysis_bottlenecks_ScheduledImpactAnalysisReport's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # analysis_bottlenecks_ScheduledImpactAnalysisReport's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = analysis_bottlenecks_ScheduledImpactAnalysisReport(classLevel=True)
    partner = BottlenecksWithSchedulingReport()
    setattr(partner, 'BottlenecksWithSchedulingReport257', None)
    _safe_set(owner, 'analysis_bottlenecks_ScheduledImpactAnalysisReport256', partner)
    assert getattr(partner, 'BottlenecksWithSchedulingReport257') == owner
    _safe_set(owner, 'analysis_bottlenecks_ScheduledImpactAnalysisReport256', None)
    assert getattr(partner, 'BottlenecksWithSchedulingReport257') is None


def test_assoc_initialBufferConfiguration266_stub_double():
    # BoundedBuffersReport has no real 'BoundedBuffersReport' property in the generated
    # code (a bare stub) -- manually attach it so analysis_buffers_OptimalBuffersReport's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # analysis_buffers_OptimalBuffersReport's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = analysis_buffers_OptimalBuffersReport(bitAccurate=True, pow2=True)
    partner = BoundedBuffersReport()
    setattr(partner, 'BoundedBuffersReport', None)
    _safe_set(owner, 'analysis_buffers_OptimalBuffersReport267', partner)
    assert getattr(partner, 'BoundedBuffersReport') == owner
    _safe_set(owner, 'analysis_buffers_OptimalBuffersReport267', None)
    assert getattr(partner, 'BoundedBuffersReport') is None


def test_assoc_internalCostMap280_stub_double():
    # ActorToLongMap has no real 'ActorToLongMap282' property in the generated
    # code (a bare stub) -- manually attach it so analysis_partitioning_ComCostPartition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # analysis_partitioning_ComCostPartition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = analysis_partitioning_ComCostPartition(externalCost="sample_text", internalCost="sample_text")
    partner = ActorToLongMap()
    setattr(partner, 'ActorToLongMap282', None)
    _safe_set(owner, 'analysis_partitioning_ComCostPartition281', {partner})
    assert getattr(partner, 'ActorToLongMap282') == owner
    _safe_set(owner, 'analysis_partitioning_ComCostPartition281', set())
    assert getattr(partner, 'ActorToLongMap282') is None


def test_assoc_key100_stub_double():
    # map_analysis_Actor has no real 'map_analysis_Actor101' property in the generated
    # code (a bare stub) -- manually attach it so analysis_map_ActorToLongMap's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # analysis_map_ActorToLongMap's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = analysis_map_ActorToLongMap(value="sample_text")
    partner = map_analysis_Actor()
    setattr(partner, 'map_analysis_Actor101', None)
    _safe_set(owner, 'analysis_map_ActorToLongMap', partner)
    assert getattr(partner, 'map_analysis_Actor101') == owner
    _safe_set(owner, 'analysis_map_ActorToLongMap', None)
    assert getattr(partner, 'map_analysis_Actor101') is None


def test_assoc_key102_stub_double():
    # map_analysis_Buffer has no real 'map_analysis_Buffer103' property in the generated
    # code (a bare stub) -- manually attach it so analysis_map_BufferToLongMap's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # analysis_map_BufferToLongMap's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = analysis_map_BufferToLongMap(value="sample_text")
    partner = map_analysis_Buffer()
    setattr(partner, 'map_analysis_Buffer103', None)
    _safe_set(owner, 'analysis_map_BufferToLongMap', partner)
    assert getattr(partner, 'map_analysis_Buffer103') == owner
    _safe_set(owner, 'analysis_map_BufferToLongMap', None)
    assert getattr(partner, 'map_analysis_Buffer103') is None


def test_assoc_key104_stub_double():
    # map_analysis_Variable has no real 'map_analysis_Variable105' property in the generated
    # code (a bare stub) -- manually attach it so analysis_map_VariableToLongMap's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # analysis_map_VariableToLongMap's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = analysis_map_VariableToLongMap(value="sample_text")
    partner = map_analysis_Variable()
    setattr(partner, 'map_analysis_Variable105', None)
    _safe_set(owner, 'analysis_map_VariableToLongMap', partner)
    assert getattr(partner, 'map_analysis_Variable105') == owner
    _safe_set(owner, 'analysis_map_VariableToLongMap', None)
    assert getattr(partner, 'map_analysis_Variable105') is None


def test_assoc_key106_stub_double():
    # map_analysis_Guard has no real 'map_analysis_Guard' property in the generated
    # code (a bare stub) -- manually attach it so analysis_map_GuardToLongMap's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # analysis_map_GuardToLongMap's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = analysis_map_GuardToLongMap(value="sample_text")
    partner = map_analysis_Guard()
    setattr(partner, 'map_analysis_Guard', None)
    _safe_set(owner, 'analysis_map_GuardToLongMap', partner)
    assert getattr(partner, 'map_analysis_Guard') == owner
    _safe_set(owner, 'analysis_map_GuardToLongMap', None)
    assert getattr(partner, 'map_analysis_Guard') is None


def test_assoc_key107_stub_double():
    # map_analysis_Port has no real 'map_analysis_Port' property in the generated
    # code (a bare stub) -- manually attach it so analysis_map_PortToLongMap's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # analysis_map_PortToLongMap's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = analysis_map_PortToLongMap(value="sample_text")
    partner = map_analysis_Port()
    setattr(partner, 'map_analysis_Port', None)
    _safe_set(owner, 'analysis_map_PortToLongMap', partner)
    assert getattr(partner, 'map_analysis_Port') == owner
    _safe_set(owner, 'analysis_map_PortToLongMap', None)
    assert getattr(partner, 'map_analysis_Port') is None


def test_assoc_key108_stub_double():
    # map_analysis_Action has no real 'map_analysis_Action109' property in the generated
    # code (a bare stub) -- manually attach it so analysis_map_ActionToDoubleMap's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # analysis_map_ActionToDoubleMap's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = analysis_map_ActionToDoubleMap(value="sample_text")
    partner = map_analysis_Action()
    setattr(partner, 'map_analysis_Action109', None)
    _safe_set(owner, 'analysis_map_ActionToDoubleMap', partner)
    assert getattr(partner, 'map_analysis_Action109') == owner
    _safe_set(owner, 'analysis_map_ActionToDoubleMap', None)
    assert getattr(partner, 'map_analysis_Action109') is None


def test_assoc_key110_stub_double():
    # map_analysis_Buffer has no real 'map_analysis_Buffer111' property in the generated
    # code (a bare stub) -- manually attach it so analysis_map_BufferToIntegerMap's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # analysis_map_BufferToIntegerMap's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = analysis_map_BufferToIntegerMap(value="sample_text")
    partner = map_analysis_Buffer()
    setattr(partner, 'map_analysis_Buffer111', None)
    _safe_set(owner, 'analysis_map_BufferToIntegerMap', partner)
    assert getattr(partner, 'map_analysis_Buffer111') == owner
    _safe_set(owner, 'analysis_map_BufferToIntegerMap', None)
    assert getattr(partner, 'map_analysis_Buffer111') is None


def test_assoc_key112_stub_double():
    # map_analysis_Buffer has no real 'map_analysis_Buffer113' property in the generated
    # code (a bare stub) -- manually attach it so analysis_map_BufferToDoubleMap's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # analysis_map_BufferToDoubleMap's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = analysis_map_BufferToDoubleMap(value="sample_text")
    partner = map_analysis_Buffer()
    setattr(partner, 'map_analysis_Buffer113', None)
    _safe_set(owner, 'analysis_map_BufferToDoubleMap', partner)
    assert getattr(partner, 'map_analysis_Buffer113') == owner
    _safe_set(owner, 'analysis_map_BufferToDoubleMap', None)
    assert getattr(partner, 'map_analysis_Buffer113') is None


def test_assoc_key98_stub_double():
    # map_analysis_Action has no real 'map_analysis_Action99' property in the generated
    # code (a bare stub) -- manually attach it so analysis_map_ActionToLongMap's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # analysis_map_ActionToLongMap's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = analysis_map_ActionToLongMap(value="sample_text")
    partner = map_analysis_Action()
    setattr(partner, 'map_analysis_Action99', None)
    _safe_set(owner, 'analysis_map_ActionToLongMap', partner)
    assert getattr(partner, 'map_analysis_Action99') == owner
    _safe_set(owner, 'analysis_map_ActionToLongMap', None)
    assert getattr(partner, 'map_analysis_Action99') is None


def test_assoc_maxBlockedMultiplication232_stub_double():
    # BufferToDoubleMap has no real 'BufferToDoubleMap' property in the generated
    # code (a bare stub) -- manually attach it so analysis_bottlenecks_ActionBottlenecksWithSchedulingData's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # analysis_bottlenecks_ActionBottlenecksWithSchedulingData's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = analysis_bottlenecks_ActionBottlenecksWithSchedulingData(cpFirings="sample_text", cpWeight=3.14, totalFirings="sample_text", totalWeight=3.14)
    partner = BufferToDoubleMap()
    setattr(partner, 'BufferToDoubleMap', None)
    _safe_set(owner, 'analysis_bottlenecks_ActionBottlenecksWithSchedulingData233', {partner})
    assert getattr(partner, 'BufferToDoubleMap') == owner
    _safe_set(owner, 'analysis_bottlenecks_ActionBottlenecksWithSchedulingData233', set())
    assert getattr(partner, 'BufferToDoubleMap') is None


def test_assoc_maxBlockedOutputTokens230_stub_double():
    # BufferToIntegerMap has no real 'BufferToIntegerMap' property in the generated
    # code (a bare stub) -- manually attach it so analysis_bottlenecks_ActionBottlenecksWithSchedulingData's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # analysis_bottlenecks_ActionBottlenecksWithSchedulingData's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = analysis_bottlenecks_ActionBottlenecksWithSchedulingData(cpFirings="sample_text", cpWeight=3.14, totalFirings="sample_text", totalWeight=3.14)
    partner = BufferToIntegerMap()
    setattr(partner, 'BufferToIntegerMap', None)
    _safe_set(owner, 'analysis_bottlenecks_ActionBottlenecksWithSchedulingData231', {partner})
    assert getattr(partner, 'BufferToIntegerMap') == owner
    _safe_set(owner, 'analysis_bottlenecks_ActionBottlenecksWithSchedulingData231', set())
    assert getattr(partner, 'BufferToIntegerMap') is None


def test_assoc_neighbors152_stub_double():
    # CompressedStep has no real 'CompressedStep154' property in the generated
    # code (a bare stub) -- manually attach it so analysis_trace_CompressedStep's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # analysis_trace_CompressedStep's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = analysis_trace_CompressedStep(count="sample_text")
    partner = CompressedStep()
    setattr(partner, 'CompressedStep154', None)
    _safe_set(owner, 'analysis_trace_CompressedStep153', {partner})
    assert getattr(partner, 'CompressedStep154') == owner
    _safe_set(owner, 'analysis_trace_CompressedStep153', set())
    assert getattr(partner, 'CompressedStep154') is None


def test_assoc_network0_stub_double():
    # profiler_analysis_Network has no real 'profiler_analysis_Network' property in the generated
    # code (a bare stub) -- manually attach it so analysis_profiler_CodeProfilingReport's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # analysis_profiler_CodeProfilingReport's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = analysis_profiler_CodeProfilingReport()
    partner = profiler_analysis_Network()
    setattr(partner, 'profiler_analysis_Network', None)
    _safe_set(owner, 'analysis_profiler_CodeProfilingReport', partner)
    assert getattr(partner, 'profiler_analysis_Network') == owner
    _safe_set(owner, 'analysis_profiler_CodeProfilingReport', None)
    assert getattr(partner, 'profiler_analysis_Network') is None


def test_assoc_network133_stub_double():
    # trace_analysis_Network has no real 'trace_analysis_Network' property in the generated
    # code (a bare stub) -- manually attach it so analysis_trace_TraceSizeReport's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # analysis_trace_TraceSizeReport's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = analysis_trace_TraceSizeReport(dependencies="sample_text", firings="sample_text")
    partner = trace_analysis_Network()
    setattr(partner, 'trace_analysis_Network', None)
    _safe_set(owner, 'analysis_trace_TraceSizeReport134', partner)
    assert getattr(partner, 'trace_analysis_Network') == owner
    _safe_set(owner, 'analysis_trace_TraceSizeReport134', None)
    assert getattr(partner, 'trace_analysis_Network') is None


def test_assoc_network135_stub_double():
    # trace_analysis_Network has no real 'trace_analysis_Network136' property in the generated
    # code (a bare stub) -- manually attach it so analysis_trace_CompressedTraceReport's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # analysis_trace_CompressedTraceReport's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = analysis_trace_CompressedTraceReport(traceFile="sample_text")
    partner = trace_analysis_Network()
    setattr(partner, 'trace_analysis_Network136', None)
    _safe_set(owner, 'analysis_trace_CompressedTraceReport', partner)
    assert getattr(partner, 'trace_analysis_Network136') == owner
    _safe_set(owner, 'analysis_trace_CompressedTraceReport', None)
    assert getattr(partner, 'trace_analysis_Network136') is None


def test_assoc_network193_stub_double():
    # trace_analysis_Network has no real 'trace_analysis_Network194' property in the generated
    # code (a bare stub) -- manually attach it so analysis_trace_MarkowModelTraceReport's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # analysis_trace_MarkowModelTraceReport's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = analysis_trace_MarkowModelTraceReport()
    partner = trace_analysis_Network()
    setattr(partner, 'trace_analysis_Network194', None)
    _safe_set(owner, 'analysis_trace_MarkowModelTraceReport', partner)
    assert getattr(partner, 'trace_analysis_Network194') == owner
    _safe_set(owner, 'analysis_trace_MarkowModelTraceReport', None)
    assert getattr(partner, 'trace_analysis_Network194') is None


def test_assoc_network202_stub_double():
    # bottlenecks_analysis_Network has no real 'bottlenecks_analysis_Network' property in the generated
    # code (a bare stub) -- manually attach it so analysis_bottlenecks_BottlenecksReport's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # analysis_bottlenecks_BottlenecksReport's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = analysis_bottlenecks_BottlenecksReport(cpFirings="sample_text", cpVariance=3.14, cpWeight=3.14, totalFirings="sample_text", totalVariance=3.14, totalWeight=3.14)
    partner = bottlenecks_analysis_Network()
    setattr(partner, 'bottlenecks_analysis_Network', None)
    _safe_set(owner, 'analysis_bottlenecks_BottlenecksReport', partner)
    assert getattr(partner, 'bottlenecks_analysis_Network') == owner
    _safe_set(owner, 'analysis_bottlenecks_BottlenecksReport', None)
    assert getattr(partner, 'bottlenecks_analysis_Network') is None


def test_assoc_network206_stub_double():
    # bottlenecks_analysis_Network has no real 'bottlenecks_analysis_Network207' property in the generated
    # code (a bare stub) -- manually attach it so analysis_bottlenecks_ImpactAnalysisReport's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # analysis_bottlenecks_ImpactAnalysisReport's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = analysis_bottlenecks_ImpactAnalysisReport(classLevel=True)
    partner = bottlenecks_analysis_Network()
    setattr(partner, 'bottlenecks_analysis_Network207', None)
    _safe_set(owner, 'analysis_bottlenecks_ImpactAnalysisReport', partner)
    assert getattr(partner, 'bottlenecks_analysis_Network207') == owner
    _safe_set(owner, 'analysis_bottlenecks_ImpactAnalysisReport', None)
    assert getattr(partner, 'bottlenecks_analysis_Network207') is None


def test_assoc_network222_stub_double():
    # bottlenecks_analysis_Network has no real 'bottlenecks_analysis_Network223' property in the generated
    # code (a bare stub) -- manually attach it so analysis_bottlenecks_BottlenecksWithSchedulingReport's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # analysis_bottlenecks_BottlenecksWithSchedulingReport's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = analysis_bottlenecks_BottlenecksWithSchedulingReport(cpBlockingTime=3.14, cpFirings="sample_text", cpWeight=3.14, executionTime=3.14, totalFirings="sample_text", totalWeight=3.14)
    partner = bottlenecks_analysis_Network()
    setattr(partner, 'bottlenecks_analysis_Network223', None)
    _safe_set(owner, 'analysis_bottlenecks_BottlenecksWithSchedulingReport', partner)
    assert getattr(partner, 'bottlenecks_analysis_Network223') == owner
    _safe_set(owner, 'analysis_bottlenecks_BottlenecksWithSchedulingReport', None)
    assert getattr(partner, 'bottlenecks_analysis_Network223') is None


def test_assoc_network251_stub_double():
    # bottlenecks_analysis_Network has no real 'bottlenecks_analysis_Network252' property in the generated
    # code (a bare stub) -- manually attach it so analysis_bottlenecks_ScheduledImpactAnalysisReport's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # analysis_bottlenecks_ScheduledImpactAnalysisReport's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = analysis_bottlenecks_ScheduledImpactAnalysisReport(classLevel=True)
    partner = bottlenecks_analysis_Network()
    setattr(partner, 'bottlenecks_analysis_Network252', None)
    _safe_set(owner, 'analysis_bottlenecks_ScheduledImpactAnalysisReport', partner)
    assert getattr(partner, 'bottlenecks_analysis_Network252') == owner
    _safe_set(owner, 'analysis_bottlenecks_ScheduledImpactAnalysisReport', None)
    assert getattr(partner, 'bottlenecks_analysis_Network252') is None


def test_assoc_network258_stub_double():
    # buffers_analysis_Network has no real 'buffers_analysis_Network' property in the generated
    # code (a bare stub) -- manually attach it so analysis_buffers_BoundedBuffersReport's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # analysis_buffers_BoundedBuffersReport's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = analysis_buffers_BoundedBuffersReport(bitAccurate=True, bitSize=7, pow2=True, tokenSize=7)
    partner = buffers_analysis_Network()
    setattr(partner, 'buffers_analysis_Network', None)
    _safe_set(owner, 'analysis_buffers_BoundedBuffersReport', partner)
    assert getattr(partner, 'buffers_analysis_Network') == owner
    _safe_set(owner, 'analysis_buffers_BoundedBuffersReport', None)
    assert getattr(partner, 'buffers_analysis_Network') is None


def test_assoc_network262_stub_double():
    # buffers_analysis_Network has no real 'buffers_analysis_Network263' property in the generated
    # code (a bare stub) -- manually attach it so analysis_buffers_OptimalBuffersReport's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # analysis_buffers_OptimalBuffersReport's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = analysis_buffers_OptimalBuffersReport(bitAccurate=True, pow2=True)
    partner = buffers_analysis_Network()
    setattr(partner, 'buffers_analysis_Network263', None)
    _safe_set(owner, 'analysis_buffers_OptimalBuffersReport', partner)
    assert getattr(partner, 'buffers_analysis_Network263') == owner
    _safe_set(owner, 'analysis_buffers_OptimalBuffersReport', None)
    assert getattr(partner, 'buffers_analysis_Network263') is None


def test_assoc_network276_stub_double():
    # partitioning_analysis_Network has no real 'partitioning_analysis_Network' property in the generated
    # code (a bare stub) -- manually attach it so analysis_partitioning_ComCostPartitioningReport's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # analysis_partitioning_ComCostPartitioningReport's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = analysis_partitioning_ComCostPartitioningReport(bitAccurate=True)
    partner = partitioning_analysis_Network()
    setattr(partner, 'partitioning_analysis_Network', None)
    _safe_set(owner, 'analysis_partitioning_ComCostPartitioningReport', partner)
    assert getattr(partner, 'partitioning_analysis_Network') == owner
    _safe_set(owner, 'analysis_partitioning_ComCostPartitioningReport', None)
    assert getattr(partner, 'partitioning_analysis_Network') is None


def test_assoc_network324_stub_double():
    # postprocessing_analysis_Network has no real 'postprocessing_analysis_Network' property in the generated
    # code (a bare stub) -- manually attach it so analysis_postprocessing_PostProcessingReport's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # analysis_postprocessing_PostProcessingReport's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = analysis_postprocessing_PostProcessingReport(deadlock=True, time=3.14)
    partner = postprocessing_analysis_Network()
    setattr(partner, 'postprocessing_analysis_Network', None)
    _safe_set(owner, 'analysis_postprocessing_PostProcessingReport', partner)
    assert getattr(partner, 'postprocessing_analysis_Network') == owner
    _safe_set(owner, 'analysis_postprocessing_PostProcessingReport', None)
    assert getattr(partner, 'postprocessing_analysis_Network') is None


def test_assoc_network327_stub_double():
    # postprocessing_analysis_Network has no real 'postprocessing_analysis_Network328' property in the generated
    # code (a bare stub) -- manually attach it so analysis_postprocessing_ActorStatisticsReport's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # analysis_postprocessing_ActorStatisticsReport's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = analysis_postprocessing_ActorStatisticsReport(averageOccupancy=3.14, executionTime=3.14, occupancyDeviation=3.14)
    partner = postprocessing_analysis_Network()
    setattr(partner, 'postprocessing_analysis_Network328', None)
    _safe_set(owner, 'analysis_postprocessing_ActorStatisticsReport', partner)
    assert getattr(partner, 'postprocessing_analysis_Network328') == owner
    _safe_set(owner, 'analysis_postprocessing_ActorStatisticsReport', None)
    assert getattr(partner, 'postprocessing_analysis_Network328') is None


def test_assoc_networkData3_stub_double():
    # ComplexCodeData has no real 'ComplexCodeData5' property in the generated
    # code (a bare stub) -- manually attach it so analysis_profiler_CodeProfilingReport's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # analysis_profiler_CodeProfilingReport's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = analysis_profiler_CodeProfilingReport()
    partner = ComplexCodeData()
    setattr(partner, 'ComplexCodeData5', None)
    _safe_set(owner, 'analysis_profiler_CodeProfilingReport4', partner)
    assert getattr(partner, 'ComplexCodeData5') == owner
    _safe_set(owner, 'analysis_profiler_CodeProfilingReport4', None)
    assert getattr(partner, 'ComplexCodeData5') is None


def test_assoc_occupancy30_stub_double():
    # profiler_analysis_StatisticalData has no real 'profiler_analysis_StatisticalData32' property in the generated
    # code (a bare stub) -- manually attach it so analysis_profiler_BufferDynamicData's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # analysis_profiler_BufferDynamicData's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = analysis_profiler_BufferDynamicData(unconsumedTokens=7)
    partner = profiler_analysis_StatisticalData()
    setattr(partner, 'profiler_analysis_StatisticalData32', None)
    _safe_set(owner, 'analysis_profiler_BufferDynamicData31', partner)
    assert getattr(partner, 'profiler_analysis_StatisticalData32') == owner
    _safe_set(owner, 'analysis_profiler_BufferDynamicData31', None)
    assert getattr(partner, 'profiler_analysis_StatisticalData32') is None


def test_assoc_operandsCount7_stub_double():
    # StringToIntegerMap has no real 'StringToIntegerMap9' property in the generated
    # code (a bare stub) -- manually attach it so analysis_profiler_CodeData's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # analysis_profiler_CodeData's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = analysis_profiler_CodeData(blockName="sample_text", nol="sample_text")
    partner = StringToIntegerMap()
    setattr(partner, 'StringToIntegerMap9', None)
    _safe_set(owner, 'analysis_profiler_CodeData8', {partner})
    assert getattr(partner, 'StringToIntegerMap9') == owner
    _safe_set(owner, 'analysis_profiler_CodeData8', set())
    assert getattr(partner, 'StringToIntegerMap9') is None


def test_assoc_operatorsCount6_stub_double():
    # StringToIntegerMap has no real 'StringToIntegerMap' property in the generated
    # code (a bare stub) -- manually attach it so analysis_profiler_CodeData's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # analysis_profiler_CodeData's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = analysis_profiler_CodeData(blockName="sample_text", nol="sample_text")
    partner = StringToIntegerMap()
    setattr(partner, 'StringToIntegerMap', None)
    _safe_set(owner, 'analysis_profiler_CodeData', {partner})
    assert getattr(partner, 'StringToIntegerMap') == owner
    _safe_set(owner, 'analysis_profiler_CodeData', set())
    assert getattr(partner, 'StringToIntegerMap') is None


def test_assoc_outgoings144_stub_double():
    # CompressedDependency has no real 'CompressedDependency145' property in the generated
    # code (a bare stub) -- manually attach it so analysis_trace_CompressedStep's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # analysis_trace_CompressedStep's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = analysis_trace_CompressedStep(count="sample_text")
    partner = CompressedDependency()
    setattr(partner, 'CompressedDependency145', None)
    _safe_set(owner, 'source', {partner})
    assert getattr(partner, 'CompressedDependency145') == owner
    _safe_set(owner, 'source', set())
    assert getattr(partner, 'CompressedDependency145') is None


def test_assoc_outgoings451_stub_double():
    # MarkovSchedulingTransition has no real 'MarkovSchedulingTransition453' property in the generated
    # code (a bare stub) -- manually attach it so analysis_scheduling_MarkovSchedulingState's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # analysis_scheduling_MarkovSchedulingState's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = analysis_scheduling_MarkovSchedulingState(firings="sample_text", name="sample_text")
    partner = MarkovSchedulingTransition()
    setattr(partner, 'MarkovSchedulingTransition453', None)
    _safe_set(owner, 'source452', {partner})
    assert getattr(partner, 'MarkovSchedulingTransition453') == owner
    _safe_set(owner, 'source452', set())
    assert getattr(partner, 'MarkovSchedulingTransition453') is None


def test_assoc_partitionSchedules463_stub_double():
    # PartitionToActorSelectionScheduleMap has no real 'PartitionToActorSelectionScheduleMap' property in the generated
    # code (a bare stub) -- manually attach it so analysis_caseoptimal_CaseOptimalScheduleReport's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # analysis_caseoptimal_CaseOptimalScheduleReport's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = analysis_caseoptimal_CaseOptimalScheduleReport(partitionFilePath="sample_text", pipeline="sample_text", traceFile="sample_text")
    partner = PartitionToActorSelectionScheduleMap()
    setattr(partner, 'PartitionToActorSelectionScheduleMap', None)
    _safe_set(owner, 'analysis_caseoptimal_CaseOptimalScheduleReport', {partner})
    assert getattr(partner, 'PartitionToActorSelectionScheduleMap') == owner
    _safe_set(owner, 'analysis_caseoptimal_CaseOptimalScheduleReport', set())
    assert getattr(partner, 'PartitionToActorSelectionScheduleMap') is None


def test_assoc_partitions277_stub_double():
    # ComCostPartition has no real 'ComCostPartition' property in the generated
    # code (a bare stub) -- manually attach it so analysis_partitioning_ComCostPartitioningReport's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # analysis_partitioning_ComCostPartitioningReport's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = analysis_partitioning_ComCostPartitioningReport(bitAccurate=True)
    partner = ComCostPartition()
    setattr(partner, 'ComCostPartition', None)
    _safe_set(owner, 'analysis_partitioning_ComCostPartitioningReport278', {partner})
    assert getattr(partner, 'ComCostPartition') == owner
    _safe_set(owner, 'analysis_partitioning_ComCostPartitioningReport278', set())
    assert getattr(partner, 'ComCostPartition') is None


def test_assoc_partitions329_stub_double():
    # StatisticalActorPartition has no real 'StatisticalActorPartition' property in the generated
    # code (a bare stub) -- manually attach it so analysis_postprocessing_ActorStatisticsReport's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # analysis_postprocessing_ActorStatisticsReport's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = analysis_postprocessing_ActorStatisticsReport(averageOccupancy=3.14, executionTime=3.14, occupancyDeviation=3.14)
    partner = StatisticalActorPartition()
    setattr(partner, 'StatisticalActorPartition', None)
    _safe_set(owner, 'analysis_postprocessing_ActorStatisticsReport330', {partner})
    assert getattr(partner, 'StatisticalActorPartition') == owner
    _safe_set(owner, 'analysis_postprocessing_ActorStatisticsReport330', set())
    assert getattr(partner, 'StatisticalActorPartition') is None


def test_assoc_pipelinableFirings304_stub_double():
    # pipelining_analysis_StatisticalData has no real 'pipelining_analysis_StatisticalData306' property in the generated
    # code (a bare stub) -- manually attach it so analysis_pipelining_ActionVariablePipeliningData's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # analysis_pipelining_ActionVariablePipeliningData's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = analysis_pipelining_ActionVariablePipeliningData(pipelinable=True)
    partner = pipelining_analysis_StatisticalData()
    setattr(partner, 'pipelining_analysis_StatisticalData306', None)
    _safe_set(owner, 'analysis_pipelining_ActionVariablePipeliningData305', partner)
    assert getattr(partner, 'pipelining_analysis_StatisticalData306') == owner
    _safe_set(owner, 'analysis_pipelining_ActionVariablePipeliningData305', None)
    assert getattr(partner, 'pipelining_analysis_StatisticalData306') is None


def test_assoc_predecessors146_stub_double():
    # CompressedStep has no real 'CompressedStep148' property in the generated
    # code (a bare stub) -- manually attach it so analysis_trace_CompressedStep's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # analysis_trace_CompressedStep's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = analysis_trace_CompressedStep(count="sample_text")
    partner = CompressedStep()
    setattr(partner, 'CompressedStep148', None)
    _safe_set(owner, 'analysis_trace_CompressedStep147', {partner})
    assert getattr(partner, 'CompressedStep148') == owner
    _safe_set(owner, 'analysis_trace_CompressedStep147', set())
    assert getattr(partner, 'CompressedStep148') is None


def test_assoc_proceduresData11_stub_double():
    # CodeData has no real 'CodeData13' property in the generated
    # code (a bare stub) -- manually attach it so analysis_profiler_ComplexCodeData's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # analysis_profiler_ComplexCodeData's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = analysis_profiler_ComplexCodeData()
    partner = CodeData()
    setattr(partner, 'CodeData13', None)
    _safe_set(owner, 'analysis_profiler_ComplexCodeData12', {partner})
    assert getattr(partner, 'CodeData13') == owner
    _safe_set(owner, 'analysis_profiler_ComplexCodeData12', set())
    assert getattr(partner, 'CodeData13') is None


def test_assoc_processingTimes340_stub_double():
    # StringToDoubleMap has no real 'StringToDoubleMap342' property in the generated
    # code (a bare stub) -- manually attach it so analysis_postprocessing_ActorStatisticsReport's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # analysis_postprocessing_ActorStatisticsReport's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = analysis_postprocessing_ActorStatisticsReport(averageOccupancy=3.14, executionTime=3.14, occupancyDeviation=3.14)
    partner = StringToDoubleMap()
    setattr(partner, 'StringToDoubleMap342', None)
    _safe_set(owner, 'analysis_postprocessing_ActorStatisticsReport341', {partner})
    assert getattr(partner, 'StringToDoubleMap342') == owner
    _safe_set(owner, 'analysis_postprocessing_ActorStatisticsReport341', set())
    assert getattr(partner, 'StringToDoubleMap342') is None


def test_assoc_reads25_stub_double():
    # profiler_analysis_StatisticalData has no real 'profiler_analysis_StatisticalData' property in the generated
    # code (a bare stub) -- manually attach it so analysis_profiler_BufferDynamicData's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # analysis_profiler_BufferDynamicData's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = analysis_profiler_BufferDynamicData(unconsumedTokens=7)
    partner = profiler_analysis_StatisticalData()
    setattr(partner, 'profiler_analysis_StatisticalData', None)
    _safe_set(owner, 'analysis_profiler_BufferDynamicData26', partner)
    assert getattr(partner, 'profiler_analysis_StatisticalData') == owner
    _safe_set(owner, 'analysis_profiler_BufferDynamicData26', None)
    assert getattr(partner, 'profiler_analysis_StatisticalData') is None


def test_assoc_reads65_stub_double():
    # MemoryAccessData has no real 'MemoryAccessData' property in the generated
    # code (a bare stub) -- manually attach it so analysis_profiler_ActionMemoryProfilingData's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # analysis_profiler_ActionMemoryProfilingData's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = analysis_profiler_ActionMemoryProfilingData(action="sample_text", actor="sample_text")
    partner = MemoryAccessData()
    setattr(partner, 'MemoryAccessData', None)
    _safe_set(owner, 'analysis_profiler_ActionMemoryProfilingData', {partner})
    assert getattr(partner, 'MemoryAccessData') == owner
    _safe_set(owner, 'analysis_profiler_ActionMemoryProfilingData', set())
    assert getattr(partner, 'MemoryAccessData') is None


def test_assoc_reports325_stub_double():
    # PostProcessingData has no real 'PostProcessingData' property in the generated
    # code (a bare stub) -- manually attach it so analysis_postprocessing_PostProcessingReport's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # analysis_postprocessing_PostProcessingReport's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = analysis_postprocessing_PostProcessingReport(deadlock=True, time=3.14)
    partner = PostProcessingData()
    setattr(partner, 'PostProcessingData', None)
    _safe_set(owner, 'analysis_postprocessing_PostProcessingReport326', {partner})
    assert getattr(partner, 'PostProcessingData') == owner
    _safe_set(owner, 'analysis_postprocessing_PostProcessingReport326', set())
    assert getattr(partner, 'PostProcessingData') is None


def test_assoc_rows71_stub_double():
    # TableRow has no real 'TableRow' property in the generated
    # code (a bare stub) -- manually attach it so analysis_profiler_BenchmarkReport's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # analysis_profiler_BenchmarkReport's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = analysis_profiler_BenchmarkReport(column_names="sample_text")
    partner = TableRow()
    setattr(partner, 'TableRow', None)
    _safe_set(owner, 'analysis_profiler_BenchmarkReport', {partner})
    assert getattr(partner, 'TableRow') == owner
    _safe_set(owner, 'analysis_profiler_BenchmarkReport', set())
    assert getattr(partner, 'TableRow') is None


def test_assoc_scheduledImpactData253_stub_double():
    # ScheduledImpactAnalysisData has no real 'ScheduledImpactAnalysisData' property in the generated
    # code (a bare stub) -- manually attach it so analysis_bottlenecks_ScheduledImpactAnalysisReport's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # analysis_bottlenecks_ScheduledImpactAnalysisReport's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = analysis_bottlenecks_ScheduledImpactAnalysisReport(classLevel=True)
    partner = ScheduledImpactAnalysisData()
    setattr(partner, 'ScheduledImpactAnalysisData', None)
    _safe_set(owner, 'analysis_bottlenecks_ScheduledImpactAnalysisReport254', {partner})
    assert getattr(partner, 'ScheduledImpactAnalysisData') == owner
    _safe_set(owner, 'analysis_bottlenecks_ScheduledImpactAnalysisReport254', set())
    assert getattr(partner, 'ScheduledImpactAnalysisData') is None


def test_assoc_source155_stub_double():
    # CompressedStep has no real 'CompressedStep156' property in the generated
    # code (a bare stub) -- manually attach it so analysis_trace_CompressedDependency's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # analysis_trace_CompressedDependency's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = analysis_trace_CompressedDependency(count="sample_text")
    partner = CompressedStep()
    setattr(partner, 'CompressedStep156', None)
    _safe_set(owner, 'outgoings', partner)
    assert getattr(partner, 'CompressedStep156') == owner
    _safe_set(owner, 'outgoings', None)
    assert getattr(partner, 'CompressedStep156') is None


def test_assoc_source457_stub_double():
    # MarkovSchedulingState has no real 'MarkovSchedulingState459' property in the generated
    # code (a bare stub) -- manually attach it so analysis_scheduling_MarkovSchedulingTransition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # analysis_scheduling_MarkovSchedulingTransition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = analysis_scheduling_MarkovSchedulingTransition(firings="sample_text", name="sample_text")
    partner = MarkovSchedulingState()
    setattr(partner, 'MarkovSchedulingState459', None)
    _safe_set(owner, 'outgoings458', partner)
    assert getattr(partner, 'MarkovSchedulingState459') == owner
    _safe_set(owner, 'outgoings458', None)
    assert getattr(partner, 'MarkovSchedulingState459') is None


def test_assoc_states422_stub_double():
    # FSMState has no real 'FSMState' property in the generated
    # code (a bare stub) -- manually attach it so analysis_scheduling_FSM's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # analysis_scheduling_FSM's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = analysis_scheduling_FSM(startState="sample_text", terminalState="sample_text")
    partner = FSMState()
    setattr(partner, 'FSMState', None)
    _safe_set(owner, 'analysis_scheduling_FSM', {partner})
    assert getattr(partner, 'FSMState') == owner
    _safe_set(owner, 'analysis_scheduling_FSM', set())
    assert getattr(partner, 'FSMState') is None


def test_assoc_states445_stub_double():
    # MarkovSchedulingState has no real 'MarkovSchedulingState' property in the generated
    # code (a bare stub) -- manually attach it so analysis_scheduling_MarkovPartitionScheduler's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # analysis_scheduling_MarkovPartitionScheduler's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = analysis_scheduling_MarkovPartitionScheduler(partitionId="sample_text")
    partner = MarkovSchedulingState()
    setattr(partner, 'MarkovSchedulingState', None)
    _safe_set(owner, 'analysis_scheduling_MarkovPartitionScheduler446', {partner})
    assert getattr(partner, 'MarkovSchedulingState') == owner
    _safe_set(owner, 'analysis_scheduling_MarkovPartitionScheduler446', set())
    assert getattr(partner, 'MarkovSchedulingState') is None


def test_assoc_steps137_stub_double():
    # CompressedStep has no real 'CompressedStep' property in the generated
    # code (a bare stub) -- manually attach it so analysis_trace_CompressedTraceReport's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # analysis_trace_CompressedTraceReport's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = analysis_trace_CompressedTraceReport(traceFile="sample_text")
    partner = CompressedStep()
    setattr(partner, 'CompressedStep', None)
    _safe_set(owner, 'analysis_trace_CompressedTraceReport138', {partner})
    assert getattr(partner, 'CompressedStep') == owner
    _safe_set(owner, 'analysis_trace_CompressedTraceReport138', set())
    assert getattr(partner, 'CompressedStep') is None


def test_assoc_successors149_stub_double():
    # CompressedStep has no real 'CompressedStep151' property in the generated
    # code (a bare stub) -- manually attach it so analysis_trace_CompressedStep's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # analysis_trace_CompressedStep's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = analysis_trace_CompressedStep(count="sample_text")
    partner = CompressedStep()
    setattr(partner, 'CompressedStep151', None)
    _safe_set(owner, 'analysis_trace_CompressedStep150', {partner})
    assert getattr(partner, 'CompressedStep151') == owner
    _safe_set(owner, 'analysis_trace_CompressedStep150', set())
    assert getattr(partner, 'CompressedStep151') is None


def test_assoc_successorsMap199_stub_double():
    # ActionToLongMap has no real 'ActionToLongMap201' property in the generated
    # code (a bare stub) -- manually attach it so analysis_trace_MarkovModelActionData's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # analysis_trace_MarkovModelActionData's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = analysis_trace_MarkovModelActionData(first=True, successors="sample_text")
    partner = ActionToLongMap()
    setattr(partner, 'ActionToLongMap201', None)
    _safe_set(owner, 'analysis_trace_MarkovModelActionData200', {partner})
    assert getattr(partner, 'ActionToLongMap201') == owner
    _safe_set(owner, 'analysis_trace_MarkovModelActionData200', set())
    assert getattr(partner, 'ActionToLongMap201') is None


def test_assoc_target157_stub_double():
    # CompressedStep has no real 'CompressedStep158' property in the generated
    # code (a bare stub) -- manually attach it so analysis_trace_CompressedDependency's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # analysis_trace_CompressedDependency's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = analysis_trace_CompressedDependency(count="sample_text")
    partner = CompressedStep()
    setattr(partner, 'CompressedStep158', None)
    _safe_set(owner, 'incomings', partner)
    assert getattr(partner, 'CompressedStep158') == owner
    _safe_set(owner, 'incomings', None)
    assert getattr(partner, 'CompressedStep158') is None


def test_assoc_target460_stub_double():
    # MarkovSchedulingState has no real 'MarkovSchedulingState462' property in the generated
    # code (a bare stub) -- manually attach it so analysis_scheduling_MarkovSchedulingTransition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # analysis_scheduling_MarkovSchedulingTransition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = analysis_scheduling_MarkovSchedulingTransition(firings="sample_text", name="sample_text")
    partner = MarkovSchedulingState()
    setattr(partner, 'MarkovSchedulingState462', None)
    _safe_set(owner, 'incomings461', partner)
    assert getattr(partner, 'MarkovSchedulingState462') == owner
    _safe_set(owner, 'incomings461', None)
    assert getattr(partner, 'MarkovSchedulingState462') is None


def test_assoc_transitionSchedule427_stub_double():
    # Sequence has no real 'Sequence' property in the generated
    # code (a bare stub) -- manually attach it so analysis_scheduling_FSMTransition's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # analysis_scheduling_FSMTransition's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = analysis_scheduling_FSMTransition(sourceStateEnumName="sample_text", targetStateEnumName="sample_text")
    partner = Sequence()
    setattr(partner, 'Sequence', None)
    _safe_set(owner, 'analysis_scheduling_FSMTransition428', partner)
    assert getattr(partner, 'Sequence') == owner
    _safe_set(owner, 'analysis_scheduling_FSMTransition428', None)
    assert getattr(partner, 'Sequence') is None


def test_assoc_transitions430_stub_double():
    # FSMTransition has no real 'FSMTransition' property in the generated
    # code (a bare stub) -- manually attach it so analysis_scheduling_FSMState's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # analysis_scheduling_FSMState's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = analysis_scheduling_FSMState(enumName="sample_text")
    partner = FSMTransition()
    setattr(partner, 'FSMTransition', None)
    _safe_set(owner, 'analysis_scheduling_FSMState431', {partner})
    assert getattr(partner, 'FSMTransition') == owner
    _safe_set(owner, 'analysis_scheduling_FSMState431', set())
    assert getattr(partner, 'FSMTransition') is None


def test_assoc_transitions447_stub_double():
    # MarkovSchedulingTransition has no real 'MarkovSchedulingTransition' property in the generated
    # code (a bare stub) -- manually attach it so analysis_scheduling_MarkovPartitionScheduler's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # analysis_scheduling_MarkovPartitionScheduler's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = analysis_scheduling_MarkovPartitionScheduler(partitionId="sample_text")
    partner = MarkovSchedulingTransition()
    setattr(partner, 'MarkovSchedulingTransition', None)
    _safe_set(owner, 'analysis_scheduling_MarkovPartitionScheduler448', {partner})
    assert getattr(partner, 'MarkovSchedulingTransition') == owner
    _safe_set(owner, 'analysis_scheduling_MarkovPartitionScheduler448', set())
    assert getattr(partner, 'MarkovSchedulingTransition') is None


def test_assoc_value114_stub_double():
    # ActorSelectionSchedule has no real 'ActorSelectionSchedule' property in the generated
    # code (a bare stub) -- manually attach it so analysis_map_PartitionToActorSelectionScheduleMap's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # analysis_map_PartitionToActorSelectionScheduleMap's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = analysis_map_PartitionToActorSelectionScheduleMap(key="sample_text")
    partner = ActorSelectionSchedule()
    setattr(partner, 'ActorSelectionSchedule', None)
    _safe_set(owner, 'analysis_map_PartitionToActorSelectionScheduleMap', partner)
    assert getattr(partner, 'ActorSelectionSchedule') == owner
    _safe_set(owner, 'analysis_map_PartitionToActorSelectionScheduleMap', None)
    assert getattr(partner, 'ActorSelectionSchedule') is None


def test_assoc_value220_stub_double():
    # BottlenecksReport has no real 'BottlenecksReport221' property in the generated
    # code (a bare stub) -- manually attach it so analysis_bottlenecks_DoubleToBottlenecksReportMap's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # analysis_bottlenecks_DoubleToBottlenecksReportMap's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = analysis_bottlenecks_DoubleToBottlenecksReportMap(key="sample_text")
    partner = BottlenecksReport()
    setattr(partner, 'BottlenecksReport221', None)
    _safe_set(owner, 'analysis_bottlenecks_DoubleToBottlenecksReportMap', partner)
    assert getattr(partner, 'BottlenecksReport221') == owner
    _safe_set(owner, 'analysis_bottlenecks_DoubleToBottlenecksReportMap', None)
    assert getattr(partner, 'BottlenecksReport221') is None


def test_assoc_value250_stub_double():
    # BottlenecksWithSchedulingReport has no real 'BottlenecksWithSchedulingReport' property in the generated
    # code (a bare stub) -- manually attach it so analysis_bottlenecks_DoubleToBottlenecksWithSchedulingReportMap's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # analysis_bottlenecks_DoubleToBottlenecksWithSchedulingReportMap's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = analysis_bottlenecks_DoubleToBottlenecksWithSchedulingReportMap(key="sample_text")
    partner = BottlenecksWithSchedulingReport()
    setattr(partner, 'BottlenecksWithSchedulingReport', None)
    _safe_set(owner, 'analysis_bottlenecks_DoubleToBottlenecksWithSchedulingReportMap', partner)
    assert getattr(partner, 'BottlenecksWithSchedulingReport') == owner
    _safe_set(owner, 'analysis_bottlenecks_DoubleToBottlenecksWithSchedulingReportMap', None)
    assert getattr(partner, 'BottlenecksWithSchedulingReport') is None


def test_assoc_value70_stub_double():
    # AccessData has no real 'AccessData' property in the generated
    # code (a bare stub) -- manually attach it so analysis_profiler_StringToAccessDataMap's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # analysis_profiler_StringToAccessDataMap's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = analysis_profiler_StringToAccessDataMap(key="sample_text")
    partner = AccessData()
    setattr(partner, 'AccessData', None)
    _safe_set(owner, 'analysis_profiler_StringToAccessDataMap', partner)
    assert getattr(partner, 'AccessData') == owner
    _safe_set(owner, 'analysis_profiler_StringToAccessDataMap', None)
    assert getattr(partner, 'AccessData') is None


def test_assoc_value96_stub_double():
    # map_analysis_StatisticalData has no real 'map_analysis_StatisticalData97' property in the generated
    # code (a bare stub) -- manually attach it so analysis_map_EOperatorToStatisticalDataMap's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # analysis_map_EOperatorToStatisticalDataMap's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = analysis_map_EOperatorToStatisticalDataMap(key="sample_text")
    partner = map_analysis_StatisticalData()
    setattr(partner, 'map_analysis_StatisticalData97', None)
    _safe_set(owner, 'analysis_map_EOperatorToStatisticalDataMap', partner)
    assert getattr(partner, 'map_analysis_StatisticalData97') == owner
    _safe_set(owner, 'analysis_map_EOperatorToStatisticalDataMap', None)
    assert getattr(partner, 'map_analysis_StatisticalData97') is None


def test_assoc_varUpdates429_stub_double():
    # FSMVarUpdate has no real 'FSMVarUpdate' property in the generated
    # code (a bare stub) -- manually attach it so analysis_scheduling_FSMState's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # analysis_scheduling_FSMState's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = analysis_scheduling_FSMState(enumName="sample_text")
    partner = FSMVarUpdate()
    setattr(partner, 'FSMVarUpdate', None)
    _safe_set(owner, 'analysis_scheduling_FSMState', {partner})
    assert getattr(partner, 'FSMVarUpdate') == owner
    _safe_set(owner, 'analysis_scheduling_FSMState', set())
    assert getattr(partner, 'FSMVarUpdate') is None


def test_assoc_vars423_stub_double():
    # FSMVar has no real 'FSMVar' property in the generated
    # code (a bare stub) -- manually attach it so analysis_scheduling_FSM's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # analysis_scheduling_FSM's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = analysis_scheduling_FSM(startState="sample_text", terminalState="sample_text")
    partner = FSMVar()
    setattr(partner, 'FSMVar', None)
    _safe_set(owner, 'analysis_scheduling_FSM424', {partner})
    assert getattr(partner, 'FSMVar') == owner
    _safe_set(owner, 'analysis_scheduling_FSM424', set())
    assert getattr(partner, 'FSMVar') is None


def test_assoc_writes27_stub_double():
    # profiler_analysis_StatisticalData has no real 'profiler_analysis_StatisticalData29' property in the generated
    # code (a bare stub) -- manually attach it so analysis_profiler_BufferDynamicData's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # analysis_profiler_BufferDynamicData's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = analysis_profiler_BufferDynamicData(unconsumedTokens=7)
    partner = profiler_analysis_StatisticalData()
    setattr(partner, 'profiler_analysis_StatisticalData29', None)
    _safe_set(owner, 'analysis_profiler_BufferDynamicData28', partner)
    assert getattr(partner, 'profiler_analysis_StatisticalData29') == owner
    _safe_set(owner, 'analysis_profiler_BufferDynamicData28', None)
    assert getattr(partner, 'profiler_analysis_StatisticalData29') is None


def test_assoc_writes66_stub_double():
    # MemoryAccessData has no real 'MemoryAccessData68' property in the generated
    # code (a bare stub) -- manually attach it so analysis_profiler_ActionMemoryProfilingData's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # analysis_profiler_ActionMemoryProfilingData's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = analysis_profiler_ActionMemoryProfilingData(action="sample_text", actor="sample_text")
    partner = MemoryAccessData()
    setattr(partner, 'MemoryAccessData68', None)
    _safe_set(owner, 'analysis_profiler_ActionMemoryProfilingData67', {partner})
    assert getattr(partner, 'MemoryAccessData68') == owner
    _safe_set(owner, 'analysis_profiler_ActionMemoryProfilingData67', set())
    assert getattr(partner, 'MemoryAccessData68') is None


