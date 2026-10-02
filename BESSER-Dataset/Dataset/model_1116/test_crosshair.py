from enum import Enum
from python_code import FSMCombinator
import pytest

def test_Enum__generate_next_value_():
    with pytest.raises(TypeError, match="'SymbolicBoundedInt'\\ object\\ is\\ not\\ reversible"):
        Enum._generate_next_value_(FSMCombinator.OR, '', 0, 2)

def test_Enum__generate_next_value__2():
    with pytest.raises(AttributeError, match="'LazyIntSymbolicStr'\\ object\\ has\\ no\\ attribute\\ 'sort'"):
        Enum._generate_next_value_(FSMCombinator.OR, 0, 0, '\x00')

def test_Enum__generate_next_value__3():
    assert Enum._generate_next_value_(FSMCombinator.OR, 0, 0, 0) == 0

def test_Enum___new__():
    with pytest.raises(TypeError, match='issubclass\\(\\)\\ arg\\ 2\\ must\\ be\\ a\\ class,\\ a\\ tuple\\ of\\ classes,\\ or\\ a\\ union'):
        Enum.__new__(FSMCombinator.OR, 0)

def test_Enum___new___2():
    assert Enum.__new__(FSMCombinator.OR, 'OR') == FSMCombinator.OR

from enum import Enum
from python_code import FSMComparator
import pytest

def test_Enum__generate_next_value_():
    with pytest.raises(TypeError, match="'SymbolicBoundedInt'\\ object\\ is\\ not\\ reversible"):
        Enum._generate_next_value_(FSMComparator.EQ, 0, 0, 2)

def test_Enum__generate_next_value__2():
    with pytest.raises(AttributeError, match="'LazyIntSymbolicStr'\\ object\\ has\\ no\\ attribute\\ 'sort'"):
        Enum._generate_next_value_(FSMComparator.NEQ, 0, 0, '\x00')

def test_Enum__generate_next_value__3():
    assert Enum._generate_next_value_(FSMComparator.EQ, '', 0, 0) == ''

def test_Enum___new__():
    with pytest.raises(TypeError, match='issubclass\\(\\)\\ arg\\ 2\\ must\\ be\\ a\\ class,\\ a\\ tuple\\ of\\ classes,\\ or\\ a\\ union'):
        Enum.__new__(FSMComparator.EQ, 0)

def test_Enum___new___2():
    assert Enum.__new__(FSMComparator.EQ, 'EQ') == FSMComparator.EQ

from enum import Enum
from python_code import FSMOp
import pytest

def test_Enum__generate_next_value_():
    with pytest.raises(TypeError, match="'SymbolicBoundedInt'\\ object\\ is\\ not\\ reversible"):
        Enum._generate_next_value_(FSMOp.SET, 0, 0, 2)

def test_Enum__generate_next_value__2():
    with pytest.raises(AttributeError, match="'LazyIntSymbolicStr'\\ object\\ has\\ no\\ attribute\\ 'sort'"):
        Enum._generate_next_value_(FSMOp.SET, 0, 0, '\x00')

def test_Enum__generate_next_value__3():
    assert Enum._generate_next_value_(FSMOp.ADD, 0, 0, 0) == 0

def test_Enum___new__():
    with pytest.raises(TypeError, match='issubclass\\(\\)\\ arg\\ 2\\ must\\ be\\ a\\ class,\\ a\\ tuple\\ of\\ classes,\\ or\\ a\\ union'):
        Enum.__new__(FSMOp.SET, 0)

def test_Enum___new___2():
    assert Enum.__new__(FSMOp.SET, 'SET') == FSMOp.SET

from enum import Enum
from python_code import Optimizer
import pytest

def test_Enum__generate_next_value_():
    with pytest.raises(TypeError, match="'SymbolicBoundedInt'\\ object\\ is\\ not\\ reversible"):
        Enum._generate_next_value_(Optimizer.RLE, '', 0, 2)

def test_Enum__generate_next_value__2():
    with pytest.raises(AttributeError, match="'LazyIntSymbolicStr'\\ object\\ has\\ no\\ attribute\\ 'sort'"):
        Enum._generate_next_value_(Optimizer.RLE, '', 0, '\x00')

def test_Enum__generate_next_value__3():
    assert Enum._generate_next_value_(Optimizer.RLE, 0, 0, 0) == 0

def test_Enum___new__():
    with pytest.raises(TypeError, match='issubclass\\(\\)\\ arg\\ 2\\ must\\ be\\ a\\ class,\\ a\\ tuple\\ of\\ classes,\\ or\\ a\\ union'):
        Enum.__new__(Optimizer.RLE, 0)

def test_Enum___new___2():
    assert Enum.__new__(Optimizer.RLE, 'RLE') == Optimizer.RLE

from python_code import analysis_AnalysisReport

def test_analysis_AnalysisReport___init__():
    assert analysis_AnalysisReport.__init__(analysis_AnalysisReport('', datetime.date(1, 1, 1)), '', datetime.date(1, 1, 2)) == None

from python_code import analysis_bottlenecks_ActionBottlenecksData
from python_code import bottlenecks_analysis_Action

def test_analysis_bottlenecks_ActionBottlenecksData___init__():
    assert analysis_bottlenecks_ActionBottlenecksData.__init__(analysis_bottlenecks_ActionBottlenecksData(0.0, 0.0, 0.0, 0.0, 0.0, 0.0, '', '', analysis_bottlenecks_ActionBottlenecksData=bottlenecks_analysis_Action()), 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, '', '', analysis_bottlenecks_ActionBottlenecksData=bottlenecks_analysis_Action()) == None

from python_code import analysis_bottlenecks_ActionBottlenecksWithSchedulingData
from python_code import bottlenecks_analysis_Action

def test_analysis_bottlenecks_ActionBottlenecksWithSchedulingData___init__():
    assert analysis_bottlenecks_ActionBottlenecksWithSchedulingData.__init__(analysis_bottlenecks_ActionBottlenecksWithSchedulingData(0.0, 0.0, '', '', analysis_bottlenecks_ActionBottlenecksWithSchedulingData=bottlenecks_analysis_Action(), analysis_bottlenecks_ActionBottlenecksWithSchedulingData231=set(), analysis_bottlenecks_ActionBottlenecksWithSchedulingData233=set(), analysis_bottlenecks_ActionBottlenecksWithSchedulingData235=set()), 0.0, 0.0, '', '', analysis_bottlenecks_ActionBottlenecksWithSchedulingData=bottlenecks_analysis_Action(), analysis_bottlenecks_ActionBottlenecksWithSchedulingData231=set(), analysis_bottlenecks_ActionBottlenecksWithSchedulingData233=set(), analysis_bottlenecks_ActionBottlenecksWithSchedulingData235=set()) == None

from python_code import analysis_bottlenecks_BottlenecksReport
from python_code import bottlenecks_analysis_Network

def test_analysis_bottlenecks_BottlenecksReport___init__():
    assert analysis_bottlenecks_BottlenecksReport.__init__(analysis_bottlenecks_BottlenecksReport(0.0, 0.0, 0.0, 0.0, '\x00', '', analysis_bottlenecks_BottlenecksReport=bottlenecks_analysis_Network(), analysis_bottlenecks_BottlenecksReport204=set()), 0.0, 0.0, 0.0, 0.0, '', '', analysis_bottlenecks_BottlenecksReport=bottlenecks_analysis_Network(), analysis_bottlenecks_BottlenecksReport204=set()) == None

from python_code import analysis_bottlenecks_BottlenecksWithSchedulingReport
from python_code import bottlenecks_analysis_Network

def test_analysis_bottlenecks_BottlenecksWithSchedulingReport___init__():
    assert analysis_bottlenecks_BottlenecksWithSchedulingReport.__init__(analysis_bottlenecks_BottlenecksWithSchedulingReport('', 0.0, 0.0, '', 0.0, float("nan"), analysis_bottlenecks_BottlenecksWithSchedulingReport=bottlenecks_analysis_Network(), analysis_bottlenecks_BottlenecksWithSchedulingReport225=set(), analysis_bottlenecks_BottlenecksWithSchedulingReport227=set()), '', 0.0, 0.0, '', 0.0, 0.0, analysis_bottlenecks_BottlenecksWithSchedulingReport=bottlenecks_analysis_Network(), analysis_bottlenecks_BottlenecksWithSchedulingReport225=set(), analysis_bottlenecks_BottlenecksWithSchedulingReport227=set()) == None

from python_code import BottlenecksReport
from python_code import analysis_bottlenecks_DoubleToBottlenecksReportMap

def test_analysis_bottlenecks_DoubleToBottlenecksReportMap___init__():
    assert analysis_bottlenecks_DoubleToBottlenecksReportMap.__init__(analysis_bottlenecks_DoubleToBottlenecksReportMap('', analysis_bottlenecks_DoubleToBottlenecksReportMap=BottlenecksReport()), '', analysis_bottlenecks_DoubleToBottlenecksReportMap=BottlenecksReport()) == None

from python_code import BottlenecksWithSchedulingReport
from python_code import analysis_bottlenecks_DoubleToBottlenecksWithSchedulingReportMap

def test_analysis_bottlenecks_DoubleToBottlenecksWithSchedulingReportMap___init__():
    assert analysis_bottlenecks_DoubleToBottlenecksWithSchedulingReportMap.__init__(analysis_bottlenecks_DoubleToBottlenecksWithSchedulingReportMap('', analysis_bottlenecks_DoubleToBottlenecksWithSchedulingReportMap=BottlenecksWithSchedulingReport()), '', analysis_bottlenecks_DoubleToBottlenecksWithSchedulingReportMap=BottlenecksWithSchedulingReport()) == None

from python_code import BottlenecksReport
from python_code import analysis_bottlenecks_ImpactAnalysisReport
from python_code import bottlenecks_analysis_Network

def test_analysis_bottlenecks_ImpactAnalysisReport___init__():
    assert analysis_bottlenecks_ImpactAnalysisReport.__init__(analysis_bottlenecks_ImpactAnalysisReport(False, analysis_bottlenecks_ImpactAnalysisReport=bottlenecks_analysis_Network(), analysis_bottlenecks_ImpactAnalysisReport209=set(), analysis_bottlenecks_ImpactAnalysisReport211=BottlenecksReport()), False, analysis_bottlenecks_ImpactAnalysisReport=bottlenecks_analysis_Network(), analysis_bottlenecks_ImpactAnalysisReport209=set(), analysis_bottlenecks_ImpactAnalysisReport211=BottlenecksReport()) == None

from python_code import BottlenecksWithSchedulingReport
from python_code import analysis_bottlenecks_ScheduledImpactAnalysisReport
from python_code import bottlenecks_analysis_Network

def test_analysis_bottlenecks_ScheduledImpactAnalysisReport___init__():
    assert analysis_bottlenecks_ScheduledImpactAnalysisReport.__init__(analysis_bottlenecks_ScheduledImpactAnalysisReport(False, analysis_bottlenecks_ScheduledImpactAnalysisReport=bottlenecks_analysis_Network(), analysis_bottlenecks_ScheduledImpactAnalysisReport256=BottlenecksWithSchedulingReport(), analysis_bottlenecks_ScheduledImpactAnalysisReport254=set()), False, analysis_bottlenecks_ScheduledImpactAnalysisReport=bottlenecks_analysis_Network(), analysis_bottlenecks_ScheduledImpactAnalysisReport256=BottlenecksWithSchedulingReport(), analysis_bottlenecks_ScheduledImpactAnalysisReport254=set()) == None

from python_code import analysis_buffers_BoundedBufferData
from python_code import buffers_analysis_Buffer

def test_analysis_buffers_BoundedBufferData___init__():
    assert analysis_buffers_BoundedBufferData.__init__(analysis_buffers_BoundedBufferData(0, 0, analysis_buffers_BoundedBufferData=buffers_analysis_Buffer()), 0, 0, analysis_buffers_BoundedBufferData=buffers_analysis_Buffer()) == None

from python_code import analysis_buffers_BoundedBuffersReport
from python_code import buffers_analysis_Network

def test_analysis_buffers_BoundedBuffersReport___init__():
    assert analysis_buffers_BoundedBuffersReport.__init__(analysis_buffers_BoundedBuffersReport(False, False, 0, 0, analysis_buffers_BoundedBuffersReport=buffers_analysis_Network(), analysis_buffers_BoundedBuffersReport260=set()), False, False, 0, 0, analysis_buffers_BoundedBuffersReport=buffers_analysis_Network(), analysis_buffers_BoundedBuffersReport260=set()) == None

from python_code import BottlenecksWithSchedulingReport
from python_code import BoundedBuffersReport
from python_code import analysis_buffers_OptimalBuffersReport
from python_code import buffers_analysis_Network

def test_analysis_buffers_OptimalBuffersReport___init__():
    assert analysis_buffers_OptimalBuffersReport.__init__(analysis_buffers_OptimalBuffersReport(False, False, analysis_buffers_OptimalBuffersReport=buffers_analysis_Network(), analysis_buffers_OptimalBuffersReport265=set(), analysis_buffers_OptimalBuffersReport267=BoundedBuffersReport(), analysis_buffers_OptimalBuffersReport269=BottlenecksWithSchedulingReport()), False, False, analysis_buffers_OptimalBuffersReport=buffers_analysis_Network(), analysis_buffers_OptimalBuffersReport265=set(), analysis_buffers_OptimalBuffersReport267=BoundedBuffersReport(), analysis_buffers_OptimalBuffersReport269=BottlenecksWithSchedulingReport()) == None

from python_code import analysis_caseoptimal_CaseOptimalScheduleReport

def test_analysis_caseoptimal_CaseOptimalScheduleReport___init__():
    assert analysis_caseoptimal_CaseOptimalScheduleReport.__init__(analysis_caseoptimal_CaseOptimalScheduleReport('', '', '', analysis_caseoptimal_CaseOptimalScheduleReport=set()), '', '', '', analysis_caseoptimal_CaseOptimalScheduleReport=set()) == None

from python_code import analysis_map_ActionToDoubleMap
from python_code import map_analysis_Action

def test_analysis_map_ActionToDoubleMap___init__():
    assert analysis_map_ActionToDoubleMap.__init__(analysis_map_ActionToDoubleMap('', analysis_map_ActionToDoubleMap=map_analysis_Action()), '', analysis_map_ActionToDoubleMap=map_analysis_Action()) == None

from python_code import analysis_map_ActionToLongMap
from python_code import map_analysis_Action

def test_analysis_map_ActionToLongMap___init__():
    assert analysis_map_ActionToLongMap.__init__(analysis_map_ActionToLongMap('', analysis_map_ActionToLongMap=map_analysis_Action()), '', analysis_map_ActionToLongMap=map_analysis_Action()) == None

from python_code import analysis_map_ActorToLongMap
from python_code import map_analysis_Actor

def test_analysis_map_ActorToLongMap___init__():
    assert analysis_map_ActorToLongMap.__init__(analysis_map_ActorToLongMap('', analysis_map_ActorToLongMap=map_analysis_Actor()), '', analysis_map_ActorToLongMap=map_analysis_Actor()) == None

from python_code import analysis_map_BufferToDoubleMap
from python_code import map_analysis_Buffer

def test_analysis_map_BufferToDoubleMap___init__():
    assert analysis_map_BufferToDoubleMap.__init__(analysis_map_BufferToDoubleMap('', analysis_map_BufferToDoubleMap=map_analysis_Buffer()), '', analysis_map_BufferToDoubleMap=map_analysis_Buffer()) == None

from python_code import analysis_map_BufferToIntegerMap
from python_code import map_analysis_Buffer

def test_analysis_map_BufferToIntegerMap___init__():
    assert analysis_map_BufferToIntegerMap.__init__(analysis_map_BufferToIntegerMap('', analysis_map_BufferToIntegerMap=map_analysis_Buffer()), '', analysis_map_BufferToIntegerMap=map_analysis_Buffer()) == None

from python_code import analysis_map_BufferToLongMap
from python_code import map_analysis_Buffer

def test_analysis_map_BufferToLongMap___init__():
    assert analysis_map_BufferToLongMap.__init__(analysis_map_BufferToLongMap('', analysis_map_BufferToLongMap=map_analysis_Buffer()), '', analysis_map_BufferToLongMap=map_analysis_Buffer()) == None

from python_code import analysis_map_DoubleToDoubleMap

def test_analysis_map_DoubleToDoubleMap___init__():
    assert analysis_map_DoubleToDoubleMap.__init__(analysis_map_DoubleToDoubleMap('', '\x00'), '\x00\x00', '') == None

from python_code import analysis_map_EOperatorToStatisticalDataMap
from python_code import map_analysis_StatisticalData

def test_analysis_map_EOperatorToStatisticalDataMap___init__():
    assert analysis_map_EOperatorToStatisticalDataMap.__init__(analysis_map_EOperatorToStatisticalDataMap('', analysis_map_EOperatorToStatisticalDataMap=map_analysis_StatisticalData()), '', analysis_map_EOperatorToStatisticalDataMap=map_analysis_StatisticalData()) == None

from python_code import analysis_map_GuardToLongMap
from python_code import map_analysis_Guard

def test_analysis_map_GuardToLongMap___init__():
    assert analysis_map_GuardToLongMap.__init__(analysis_map_GuardToLongMap('', analysis_map_GuardToLongMap=map_analysis_Guard()), '', analysis_map_GuardToLongMap=map_analysis_Guard()) == None

from python_code import ActorSelectionSchedule
from python_code import analysis_map_PartitionToActorSelectionScheduleMap

def test_analysis_map_PartitionToActorSelectionScheduleMap___init__():
    assert analysis_map_PartitionToActorSelectionScheduleMap.__init__(analysis_map_PartitionToActorSelectionScheduleMap('', analysis_map_PartitionToActorSelectionScheduleMap=ActorSelectionSchedule()), '', analysis_map_PartitionToActorSelectionScheduleMap=ActorSelectionSchedule()) == None

from python_code import analysis_map_PortToLongMap
from python_code import map_analysis_Port

def test_analysis_map_PortToLongMap___init__():
    assert analysis_map_PortToLongMap.__init__(analysis_map_PortToLongMap('', analysis_map_PortToLongMap=map_analysis_Port()), '', analysis_map_PortToLongMap=map_analysis_Port()) == None

from python_code import analysis_map_StringToDoubleMap

def test_analysis_map_StringToDoubleMap___init__():
    assert analysis_map_StringToDoubleMap.__init__(analysis_map_StringToDoubleMap('', '\x00'), '\x00\x00', '') == None

from python_code import analysis_map_StringToIntegerMap

def test_analysis_map_StringToIntegerMap___init__():
    assert analysis_map_StringToIntegerMap.__init__(analysis_map_StringToIntegerMap('', '\x00'), '\x00\x00', '') == None

from python_code import analysis_map_StringToLongMap

def test_analysis_map_StringToLongMap___init__():
    assert analysis_map_StringToLongMap.__init__(analysis_map_StringToLongMap('', '\x00'), '\x00\x00', '') == None

from python_code import analysis_map_StringToStringMap

def test_analysis_map_StringToStringMap___init__():
    assert analysis_map_StringToStringMap.__init__(analysis_map_StringToStringMap('', '\x00'), '\x00\x00', '') == None

from python_code import analysis_map_VariableToLongMap
from python_code import map_analysis_Variable

def test_analysis_map_VariableToLongMap___init__():
    assert analysis_map_VariableToLongMap.__init__(analysis_map_VariableToLongMap('', analysis_map_VariableToLongMap=map_analysis_Variable()), '', analysis_map_VariableToLongMap=map_analysis_Variable()) == None

from python_code import analysis_partitioning_BalancedPipelinePartition

def test_analysis_partitioning_BalancedPipelinePartition___init__():
    assert analysis_partitioning_BalancedPipelinePartition.__init__(analysis_partitioning_BalancedPipelinePartition(0.0, 0.0, 0.0, analysis_partitioning_BalancedPipelinePartition=set()), 0.0, 0.0, 0.0, analysis_partitioning_BalancedPipelinePartition=set()) == None

from python_code import analysis_partitioning_ComCostPartition

def test_analysis_partitioning_ComCostPartition___init__():
    assert analysis_partitioning_ComCostPartition.__init__(analysis_partitioning_ComCostPartition('', '', analysis_partitioning_ComCostPartition281=set(), analysis_partitioning_ComCostPartition284=set(), analysis_partitioning_ComCostPartition=set()), '', '', analysis_partitioning_ComCostPartition281=set(), analysis_partitioning_ComCostPartition284=set(), analysis_partitioning_ComCostPartition=set()) == None

from python_code import analysis_partitioning_ComCostPartitioningReport
from python_code import partitioning_analysis_Network

def test_analysis_partitioning_ComCostPartitioningReport___init__():
    assert analysis_partitioning_ComCostPartitioningReport.__init__(analysis_partitioning_ComCostPartitioningReport(False, analysis_partitioning_ComCostPartitioningReport=partitioning_analysis_Network(), analysis_partitioning_ComCostPartitioningReport278=set()), False, analysis_partitioning_ComCostPartitioningReport=partitioning_analysis_Network(), analysis_partitioning_ComCostPartitioningReport278=set()) == None

from python_code import analysis_partitioning_WorkloadBalancePartition

def test_analysis_partitioning_WorkloadBalancePartition___init__():
    assert analysis_partitioning_WorkloadBalancePartition.__init__(analysis_partitioning_WorkloadBalancePartition(0.0, analysis_partitioning_WorkloadBalancePartition=set()), 0.0, analysis_partitioning_WorkloadBalancePartition=set()) == None

from python_code import analysis_pipelining_ActionVariablePipeliningData
from python_code import pipelining_analysis_Action
from python_code import pipelining_analysis_StatisticalData

def test_analysis_pipelining_ActionVariablePipeliningData___init__():
    assert analysis_pipelining_ActionVariablePipeliningData.__init__(analysis_pipelining_ActionVariablePipeliningData(True, analysis_pipelining_ActionVariablePipeliningData=pipelining_analysis_Action(), analysis_pipelining_ActionVariablePipeliningData303=pipelining_analysis_StatisticalData(), analysis_pipelining_ActionVariablePipeliningData305=pipelining_analysis_StatisticalData()), False, analysis_pipelining_ActionVariablePipeliningData=pipelining_analysis_Action(), analysis_pipelining_ActionVariablePipeliningData303=pipelining_analysis_StatisticalData(), analysis_pipelining_ActionVariablePipeliningData305=pipelining_analysis_StatisticalData()) == None

from python_code import BottlenecksReport
from python_code import analysis_pipelining_ImpactAnalysisData
from python_code import pipelining_analysis_ActorClass

def test_analysis_pipelining_ImpactAnalysisData___init__():
    assert analysis_pipelining_ImpactAnalysisData.__init__(analysis_pipelining_ImpactAnalysisData(0.0, analysis_pipelining_ImpactAnalysisData=BottlenecksReport(), analysis_pipelining_ImpactAnalysisData320=set(), analysis_pipelining_ImpactAnalysisData323=pipelining_analysis_ActorClass()), 0.0, analysis_pipelining_ImpactAnalysisData=BottlenecksReport(), analysis_pipelining_ImpactAnalysisData320=set(), analysis_pipelining_ImpactAnalysisData323=pipelining_analysis_ActorClass()) == None

from python_code import analysis_postprocessing_ActorStatisticsReport
from python_code import analysis_postprocessing_PostProcessingReport
from python_code import postprocessing_analysis_Network

def test_analysis_postprocessing_ActorStatisticsReport___init__():
    assert analysis_postprocessing_ActorStatisticsReport.__init__(analysis_postprocessing_ActorStatisticsReport(0.0, 0.0, 0.0, analysis_postprocessing_ActorStatisticsReport=postprocessing_analysis_Network(), analysis_postprocessing_ActorStatisticsReport330=set(), analysis_postprocessing_ActorStatisticsReport332=set(), analysis_postprocessing_ActorStatisticsReport335=set(), analysis_postprocessing_ActorStatisticsReport338=set(), analysis_postprocessing_ActorStatisticsReport341=set(), PostProcessingData=analysis_postprocessing_PostProcessingReport(0.0, False, analysis_postprocessing_PostProcessingReport=postprocessing_analysis_Network(), analysis_postprocessing_PostProcessingReport326=set())), 0.0, 0.0, float("inf"), analysis_postprocessing_ActorStatisticsReport=postprocessing_analysis_Network(), analysis_postprocessing_ActorStatisticsReport330=set(), analysis_postprocessing_ActorStatisticsReport332={<python_code.StringToDoubleMap object at 0x000001EDA6AA15D0>}, analysis_postprocessing_ActorStatisticsReport335=set(), analysis_postprocessing_ActorStatisticsReport338=set(), analysis_postprocessing_ActorStatisticsReport341=set(), PostProcessingData=analysis_postprocessing_PostProcessingReport(0.0, False, analysis_postprocessing_PostProcessingReport=postprocessing_analysis_Network(), analysis_postprocessing_PostProcessingReport326=set())) == None

from python_code import analysis_postprocessing_PostProcessingReport
from python_code import postprocessing_analysis_Network

def test_analysis_postprocessing_PostProcessingReport___init__():
    assert analysis_postprocessing_PostProcessingReport.__init__(analysis_postprocessing_PostProcessingReport(0.0, False, analysis_postprocessing_PostProcessingReport=postprocessing_analysis_Network(), analysis_postprocessing_PostProcessingReport326=set()), 0.0, False, analysis_postprocessing_PostProcessingReport=postprocessing_analysis_Network(), analysis_postprocessing_PostProcessingReport326=set()) == None

from python_code import analysis_postprocessing_StatisticalActorPartition

def test_analysis_postprocessing_StatisticalActorPartition___init__():
    assert analysis_postprocessing_StatisticalActorPartition.__init__(analysis_postprocessing_StatisticalActorPartition('\x00', 0.0, ''), '', 0.0, '') == None

from python_code import analysis_profiler_AccessData

def test_analysis_profiler_AccessData___init__():
    assert analysis_profiler_AccessData.__init__(analysis_profiler_AccessData(0.0, 0.0, 0.0, 0.0, 0.0), 0.0, 0.0, 0.0, 0.0, 0.0) == None

from python_code import analysis_profiler_BenchmarkReport

def test_analysis_profiler_BenchmarkReport___init__():
    assert analysis_profiler_BenchmarkReport.__init__(analysis_profiler_BenchmarkReport('', analysis_profiler_BenchmarkReport=set()), '', analysis_profiler_BenchmarkReport=set()) == None

from python_code import analysis_profiler_ActionMemoryProfilingData
from python_code import analysis_profiler_BufferAccessData

def test_analysis_profiler_BufferAccessData___init__():
    assert analysis_profiler_BufferAccessData.__init__(analysis_profiler_BufferAccessData('', '', '\x01', '', MemoryAccessData68=analysis_profiler_ActionMemoryProfilingData('', '', analysis_profiler_ActionMemoryProfilingData=set(), analysis_profiler_ActionMemoryProfilingData67=set()), MemoryAccessData=analysis_profiler_ActionMemoryProfilingData('', '', analysis_profiler_ActionMemoryProfilingData=set(), analysis_profiler_ActionMemoryProfilingData67=set())), '', '', '', '', MemoryAccessData68=analysis_profiler_ActionMemoryProfilingData('', '', analysis_profiler_ActionMemoryProfilingData=set(), analysis_profiler_ActionMemoryProfilingData67=set()), MemoryAccessData=analysis_profiler_ActionMemoryProfilingData('\x00', '', analysis_profiler_ActionMemoryProfilingData=set(), analysis_profiler_ActionMemoryProfilingData67=set())) == None

from python_code import analysis_profiler_BufferDynamicData
from python_code import profiler_analysis_Buffer
from python_code import profiler_analysis_StatisticalData

def test_analysis_profiler_BufferDynamicData___init__():
    assert analysis_profiler_BufferDynamicData.__init__(analysis_profiler_BufferDynamicData(0, analysis_profiler_BufferDynamicData41=set(), analysis_profiler_BufferDynamicData44=set(), analysis_profiler_BufferDynamicData=profiler_analysis_Buffer(), analysis_profiler_BufferDynamicData26=profiler_analysis_StatisticalData(), analysis_profiler_BufferDynamicData28=profiler_analysis_StatisticalData(), analysis_profiler_BufferDynamicData31=profiler_analysis_StatisticalData(), analysis_profiler_BufferDynamicData34=set(), analysis_profiler_BufferDynamicData36=set(), analysis_profiler_BufferDynamicData39=set()), 0, analysis_profiler_BufferDynamicData41=set(), analysis_profiler_BufferDynamicData44=set(), analysis_profiler_BufferDynamicData=profiler_analysis_Buffer(), analysis_profiler_BufferDynamicData26=profiler_analysis_StatisticalData(), analysis_profiler_BufferDynamicData28=profiler_analysis_StatisticalData(), analysis_profiler_BufferDynamicData31=profiler_analysis_StatisticalData(), analysis_profiler_BufferDynamicData34=set(), analysis_profiler_BufferDynamicData36=set(), analysis_profiler_BufferDynamicData39=set()) == None

from python_code import analysis_profiler_CodeData

def test_analysis_profiler_CodeData___init__():
    assert analysis_profiler_CodeData.__init__(analysis_profiler_CodeData('', '', analysis_profiler_CodeData=set(), analysis_profiler_CodeData8=set()), '', '', analysis_profiler_CodeData=set(), analysis_profiler_CodeData8=set()) == None

from python_code import ComplexCodeData
from python_code import analysis_profiler_CodeProfilingReport
from python_code import profiler_analysis_Network

def test_analysis_profiler_CodeProfilingReport___init__():
    assert analysis_profiler_CodeProfilingReport.__init__(analysis_profiler_CodeProfilingReport(analysis_profiler_CodeProfilingReport=profiler_analysis_Network(), analysis_profiler_CodeProfilingReport2=set(), analysis_profiler_CodeProfilingReport4=ComplexCodeData()), analysis_profiler_CodeProfilingReport=profiler_analysis_Network(), analysis_profiler_CodeProfilingReport2=set(), analysis_profiler_CodeProfilingReport4=ComplexCodeData()) == None

def test_analysis_profiler_CodeProfilingReport_getActorClassData():
    assert analysis_profiler_CodeProfilingReport.getActorClassData(analysis_profiler_CodeProfilingReport(analysis_profiler_CodeProfilingReport=profiler_analysis_Network(), analysis_profiler_CodeProfilingReport2=set(), analysis_profiler_CodeProfilingReport4=ComplexCodeData()), 0) == None

from python_code import analysis_profiler_ActionMemoryProfilingData
from python_code import analysis_profiler_LocalVariableAccessData

def test_analysis_profiler_LocalVariableAccessData___init__():
    assert analysis_profiler_LocalVariableAccessData.__init__(analysis_profiler_LocalVariableAccessData('', MemoryAccessData68=analysis_profiler_ActionMemoryProfilingData('', '', analysis_profiler_ActionMemoryProfilingData=set(), analysis_profiler_ActionMemoryProfilingData67=set()), MemoryAccessData=analysis_profiler_ActionMemoryProfilingData('\x00', '', analysis_profiler_ActionMemoryProfilingData=set(), analysis_profiler_ActionMemoryProfilingData67=set())), '', MemoryAccessData68=analysis_profiler_ActionMemoryProfilingData('', '', analysis_profiler_ActionMemoryProfilingData=set(), analysis_profiler_ActionMemoryProfilingData67=set()), MemoryAccessData=analysis_profiler_ActionMemoryProfilingData('', '', analysis_profiler_ActionMemoryProfilingData=set(), analysis_profiler_ActionMemoryProfilingData67=set())) == None

from python_code import analysis_profiler_MemoryProfilingReport

def test_analysis_profiler_MemoryProfilingReport___init__():
    assert analysis_profiler_MemoryProfilingReport.__init__(analysis_profiler_MemoryProfilingReport('', analysis_profiler_MemoryProfilingReport=set()), '', analysis_profiler_MemoryProfilingReport=set()) == None

def test_analysis_profiler_MemoryProfilingReport_getActionData():
    assert analysis_profiler_MemoryProfilingReport.getActionData(analysis_profiler_MemoryProfilingReport('', analysis_profiler_MemoryProfilingReport=set()), '\x00', '') == None

from python_code import analysis_profiler_ActionMemoryProfilingData
from python_code import analysis_profiler_SharedVariableAccessData

def test_analysis_profiler_SharedVariableAccessData___init__():
    assert analysis_profiler_SharedVariableAccessData.__init__(analysis_profiler_SharedVariableAccessData('', MemoryAccessData68=analysis_profiler_ActionMemoryProfilingData('', '', analysis_profiler_ActionMemoryProfilingData=set(), analysis_profiler_ActionMemoryProfilingData67=set()), MemoryAccessData=analysis_profiler_ActionMemoryProfilingData('\x00', '', analysis_profiler_ActionMemoryProfilingData=set(), analysis_profiler_ActionMemoryProfilingData67=set())), '', MemoryAccessData68=analysis_profiler_ActionMemoryProfilingData('', '', analysis_profiler_ActionMemoryProfilingData=set(), analysis_profiler_ActionMemoryProfilingData67=set()), MemoryAccessData=analysis_profiler_ActionMemoryProfilingData('', '', analysis_profiler_ActionMemoryProfilingData=set(), analysis_profiler_ActionMemoryProfilingData67=set())) == None
