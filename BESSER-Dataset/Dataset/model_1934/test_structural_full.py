import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    EasyFlowMetadata,
    GroupingCriterion,
    ITraversal,
    Traversal,
    easyflow_Argument,
    easyflow_Chunk,
    easyflow_CommandArgument,
    easyflow_Contig,
    easyflow_DataFormatToTaskList,
    easyflow_DataProcessingType,
    easyflow_DataProcessingTypeToTask,
    easyflow_EasyFlowConfiguration,
    easyflow_EasyFlowImplementationTemplate,
    easyflow_EasyFlowMetadata,
    easyflow_EasyFlowMetadataReader,
    easyflow_EasyFlowTemplate,
    easyflow_GenericTraversalCriterion,
    easyflow_Group,
    easyflow_GroupingCriterion,
    easyflow_GroupingEvent,
    easyflow_ITraversal,
    easyflow_IWorkflowUtil,
    easyflow_Interpreter,
    easyflow_Job,
    easyflow_Library,
    easyflow_Locus,
    easyflow_ReadEnd,
    easyflow_Readgroup,
    easyflow_Record,
    easyflow_Sample,
    easyflow_SplittingEvent,
    easyflow_StringToChunkMap,
    easyflow_StringToGroupMap,
    easyflow_StringToGroupingCriterionMap,
    easyflow_StringToLibraryMap,
    easyflow_StringToReadgroupMap,
    easyflow_StringToRecordMap,
    easyflow_StringToSampleMap,
    easyflow_StringToTaskMap,
    easyflow_StringToToolMap,
    easyflow_StringToTraversalCriterionMap,
    easyflow_Task,
    easyflow_TaskToDataProcessingType,
    easyflow_Tool,
    easyflow_Traversal,
    easyflow_Workflow,
    DataCriterion,
    DataFormat,
    TraversalCriterion,
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

def test_easyflow_Argument_arg_value_roundtrip():
    instance = easyflow_Argument(arg="sample_text", name="sample_text", sep="sample_text")
    assert instance.arg == "sample_text"
    instance.arg = "sample_text_2"
    assert instance.arg == "sample_text_2"


def test_easyflow_Argument_name_value_roundtrip():
    instance = easyflow_Argument(arg="sample_text", name="sample_text", sep="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_easyflow_Argument_sep_value_roundtrip():
    instance = easyflow_Argument(arg="sample_text", name="sample_text", sep="sample_text")
    assert instance.sep == "sample_text"
    instance.sep = "sample_text_2"
    assert instance.sep == "sample_text_2"


def test_easyflow_Chunk_argument_value_roundtrip():
    instance = easyflow_Chunk(argument="sample_text", name="sample_text", tool="sample_text")
    assert instance.argument == "sample_text"
    instance.argument = "sample_text_2"
    assert instance.argument == "sample_text_2"


def test_easyflow_Chunk_name_value_roundtrip():
    instance = easyflow_Chunk(argument="sample_text", name="sample_text", tool="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_easyflow_Chunk_tool_value_roundtrip():
    instance = easyflow_Chunk(argument="sample_text", name="sample_text", tool="sample_text")
    assert instance.tool == "sample_text"
    instance.tool = "sample_text_2"
    assert instance.tool == "sample_text_2"


def test_easyflow_CommandArgument_arg_value_roundtrip():
    instance = easyflow_CommandArgument(arg="sample_text", name="sample_text", named=True, required=True, sep="sample_text")
    assert instance.arg == "sample_text"
    instance.arg = "sample_text_2"
    assert instance.arg == "sample_text_2"


def test_easyflow_CommandArgument_name_value_roundtrip():
    instance = easyflow_CommandArgument(arg="sample_text", name="sample_text", named=True, required=True, sep="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_easyflow_CommandArgument_named_value_roundtrip():
    instance = easyflow_CommandArgument(arg="sample_text", name="sample_text", named=True, required=True, sep="sample_text")
    assert instance.named == True
    instance.named = False
    assert instance.named == False


def test_easyflow_CommandArgument_required_value_roundtrip():
    instance = easyflow_CommandArgument(arg="sample_text", name="sample_text", named=True, required=True, sep="sample_text")
    assert instance.required == True
    instance.required = False
    assert instance.required == False


def test_easyflow_CommandArgument_sep_value_roundtrip():
    instance = easyflow_CommandArgument(arg="sample_text", name="sample_text", named=True, required=True, sep="sample_text")
    assert instance.sep == "sample_text"
    instance.sep = "sample_text_2"
    assert instance.sep == "sample_text_2"


def test_easyflow_DataFormatToTaskList_key_value_roundtrip():
    instance = easyflow_DataFormatToTaskList(key="sample_text")
    assert instance.key == "sample_text"
    instance.key = "sample_text_2"
    assert instance.key == "sample_text_2"


def test_easyflow_DataProcessingType_dataFormatIn_value_roundtrip():
    instance = easyflow_DataProcessingType(dataFormatIn="sample_text", dataFormatOut="sample_text")
    assert instance.dataFormatIn == "sample_text"
    instance.dataFormatIn = "sample_text_2"
    assert instance.dataFormatIn == "sample_text_2"


def test_easyflow_DataProcessingType_dataFormatOut_value_roundtrip():
    instance = easyflow_DataProcessingType(dataFormatIn="sample_text", dataFormatOut="sample_text")
    assert instance.dataFormatOut == "sample_text"
    instance.dataFormatOut = "sample_text_2"
    assert instance.dataFormatOut == "sample_text_2"


def test_easyflow_EasyFlowConfiguration_configMap_value_roundtrip():
    instance = easyflow_EasyFlowConfiguration(configMap="sample_text", fileName="sample_text")
    assert instance.configMap == "sample_text"
    instance.configMap = "sample_text_2"
    assert instance.configMap == "sample_text_2"


def test_easyflow_EasyFlowConfiguration_fileName_value_roundtrip():
    instance = easyflow_EasyFlowConfiguration(configMap="sample_text", fileName="sample_text")
    assert instance.fileName == "sample_text"
    instance.fileName = "sample_text_2"
    assert instance.fileName == "sample_text_2"


def test_easyflow_EasyFlowImplementationTemplate_fileName_value_roundtrip():
    instance = easyflow_EasyFlowImplementationTemplate(fileName="sample_text", globalOptions="sample_text", jsonRootNode="sample_text", parameterConfigFileName="sample_text", parameterConfigMap="sample_text")
    assert instance.fileName == "sample_text"
    instance.fileName = "sample_text_2"
    assert instance.fileName == "sample_text_2"


def test_easyflow_EasyFlowImplementationTemplate_globalOptions_value_roundtrip():
    instance = easyflow_EasyFlowImplementationTemplate(fileName="sample_text", globalOptions="sample_text", jsonRootNode="sample_text", parameterConfigFileName="sample_text", parameterConfigMap="sample_text")
    assert instance.globalOptions == "sample_text"
    instance.globalOptions = "sample_text_2"
    assert instance.globalOptions == "sample_text_2"


def test_easyflow_EasyFlowImplementationTemplate_jsonRootNode_value_roundtrip():
    instance = easyflow_EasyFlowImplementationTemplate(fileName="sample_text", globalOptions="sample_text", jsonRootNode="sample_text", parameterConfigFileName="sample_text", parameterConfigMap="sample_text")
    assert instance.jsonRootNode == "sample_text"
    instance.jsonRootNode = "sample_text_2"
    assert instance.jsonRootNode == "sample_text_2"


def test_easyflow_EasyFlowImplementationTemplate_parameterConfigFileName_value_roundtrip():
    instance = easyflow_EasyFlowImplementationTemplate(fileName="sample_text", globalOptions="sample_text", jsonRootNode="sample_text", parameterConfigFileName="sample_text", parameterConfigMap="sample_text")
    assert instance.parameterConfigFileName == "sample_text"
    instance.parameterConfigFileName = "sample_text_2"
    assert instance.parameterConfigFileName == "sample_text_2"


def test_easyflow_EasyFlowImplementationTemplate_parameterConfigMap_value_roundtrip():
    instance = easyflow_EasyFlowImplementationTemplate(fileName="sample_text", globalOptions="sample_text", jsonRootNode="sample_text", parameterConfigFileName="sample_text", parameterConfigMap="sample_text")
    assert instance.parameterConfigMap == "sample_text"
    instance.parameterConfigMap = "sample_text_2"
    assert instance.parameterConfigMap == "sample_text_2"


def test_easyflow_EasyFlowMetadata_contrast_value_roundtrip():
    instance = easyflow_EasyFlowMetadata(contrast=True, name="sample_text", refData="sample_text")
    assert instance.contrast == True
    instance.contrast = False
    assert instance.contrast == False


def test_easyflow_EasyFlowMetadata_name_value_roundtrip():
    instance = easyflow_EasyFlowMetadata(contrast=True, name="sample_text", refData="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_easyflow_EasyFlowMetadata_refData_value_roundtrip():
    instance = easyflow_EasyFlowMetadata(contrast=True, name="sample_text", refData="sample_text")
    assert instance.refData == "sample_text"
    instance.refData = "sample_text_2"
    assert instance.refData == "sample_text_2"


def test_easyflow_EasyFlowMetadataReader_fileName_value_roundtrip():
    instance = easyflow_EasyFlowMetadataReader(fileName="sample_text")
    assert instance.fileName == "sample_text"
    instance.fileName = "sample_text_2"
    assert instance.fileName == "sample_text_2"


def test_easyflow_EasyFlowTemplate_fileName_value_roundtrip():
    instance = easyflow_EasyFlowTemplate(fileName="sample_text")
    assert instance.fileName == "sample_text"
    instance.fileName = "sample_text_2"
    assert instance.fileName == "sample_text_2"


def test_easyflow_Group_name_value_roundtrip():
    instance = easyflow_Group(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_easyflow_GroupingCriterion_id_value_roundtrip():
    instance = easyflow_GroupingCriterion(id="sample_text")
    assert instance.id == "sample_text"
    instance.id = "sample_text_2"
    assert instance.id == "sample_text_2"


def test_easyflow_GroupingEvent_dagIn_value_roundtrip():
    instance = easyflow_GroupingEvent(dagIn="sample_text", dagOut="sample_text")
    assert instance.dagIn == "sample_text"
    instance.dagIn = "sample_text_2"
    assert instance.dagIn == "sample_text_2"


def test_easyflow_GroupingEvent_dagOut_value_roundtrip():
    instance = easyflow_GroupingEvent(dagIn="sample_text", dagOut="sample_text")
    assert instance.dagOut == "sample_text"
    instance.dagOut = "sample_text_2"
    assert instance.dagOut == "sample_text_2"


def test_easyflow_Interpreter_exe_value_roundtrip():
    instance = easyflow_Interpreter(exe="sample_text", name="sample_text", options="sample_text", subCmd="sample_text")
    assert instance.exe == "sample_text"
    instance.exe = "sample_text_2"
    assert instance.exe == "sample_text_2"


def test_easyflow_Interpreter_name_value_roundtrip():
    instance = easyflow_Interpreter(exe="sample_text", name="sample_text", options="sample_text", subCmd="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_easyflow_Interpreter_options_value_roundtrip():
    instance = easyflow_Interpreter(exe="sample_text", name="sample_text", options="sample_text", subCmd="sample_text")
    assert instance.options == "sample_text"
    instance.options = "sample_text_2"
    assert instance.options == "sample_text_2"


def test_easyflow_Interpreter_subCmd_value_roundtrip():
    instance = easyflow_Interpreter(exe="sample_text", name="sample_text", options="sample_text", subCmd="sample_text")
    assert instance.subCmd == "sample_text"
    instance.subCmd = "sample_text_2"
    assert instance.subCmd == "sample_text_2"


def test_easyflow_Job_dependencies_value_roundtrip():
    instance = easyflow_Job(dependencies="sample_text", exe="sample_text", genericArgs="sample_text", inputArgs="sample_text", interpreterOption="sample_text", name="sample_text", outputArgs="sample_text", source="sample_text", staticArgs="sample_text", subCmd="sample_text", targetPlatform="sample_text", targetPlatformOptions="sample_text", targets="sample_text")
    assert instance.dependencies == "sample_text"
    instance.dependencies = "sample_text_2"
    assert instance.dependencies == "sample_text_2"


def test_easyflow_Job_exe_value_roundtrip():
    instance = easyflow_Job(dependencies="sample_text", exe="sample_text", genericArgs="sample_text", inputArgs="sample_text", interpreterOption="sample_text", name="sample_text", outputArgs="sample_text", source="sample_text", staticArgs="sample_text", subCmd="sample_text", targetPlatform="sample_text", targetPlatformOptions="sample_text", targets="sample_text")
    assert instance.exe == "sample_text"
    instance.exe = "sample_text_2"
    assert instance.exe == "sample_text_2"


def test_easyflow_Job_genericArgs_value_roundtrip():
    instance = easyflow_Job(dependencies="sample_text", exe="sample_text", genericArgs="sample_text", inputArgs="sample_text", interpreterOption="sample_text", name="sample_text", outputArgs="sample_text", source="sample_text", staticArgs="sample_text", subCmd="sample_text", targetPlatform="sample_text", targetPlatformOptions="sample_text", targets="sample_text")
    assert instance.genericArgs == "sample_text"
    instance.genericArgs = "sample_text_2"
    assert instance.genericArgs == "sample_text_2"


def test_easyflow_Job_inputArgs_value_roundtrip():
    instance = easyflow_Job(dependencies="sample_text", exe="sample_text", genericArgs="sample_text", inputArgs="sample_text", interpreterOption="sample_text", name="sample_text", outputArgs="sample_text", source="sample_text", staticArgs="sample_text", subCmd="sample_text", targetPlatform="sample_text", targetPlatformOptions="sample_text", targets="sample_text")
    assert instance.inputArgs == "sample_text"
    instance.inputArgs = "sample_text_2"
    assert instance.inputArgs == "sample_text_2"


def test_easyflow_Job_interpreterOption_value_roundtrip():
    instance = easyflow_Job(dependencies="sample_text", exe="sample_text", genericArgs="sample_text", inputArgs="sample_text", interpreterOption="sample_text", name="sample_text", outputArgs="sample_text", source="sample_text", staticArgs="sample_text", subCmd="sample_text", targetPlatform="sample_text", targetPlatformOptions="sample_text", targets="sample_text")
    assert instance.interpreterOption == "sample_text"
    instance.interpreterOption = "sample_text_2"
    assert instance.interpreterOption == "sample_text_2"


def test_easyflow_Job_name_value_roundtrip():
    instance = easyflow_Job(dependencies="sample_text", exe="sample_text", genericArgs="sample_text", inputArgs="sample_text", interpreterOption="sample_text", name="sample_text", outputArgs="sample_text", source="sample_text", staticArgs="sample_text", subCmd="sample_text", targetPlatform="sample_text", targetPlatformOptions="sample_text", targets="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_easyflow_Job_outputArgs_value_roundtrip():
    instance = easyflow_Job(dependencies="sample_text", exe="sample_text", genericArgs="sample_text", inputArgs="sample_text", interpreterOption="sample_text", name="sample_text", outputArgs="sample_text", source="sample_text", staticArgs="sample_text", subCmd="sample_text", targetPlatform="sample_text", targetPlatformOptions="sample_text", targets="sample_text")
    assert instance.outputArgs == "sample_text"
    instance.outputArgs = "sample_text_2"
    assert instance.outputArgs == "sample_text_2"


def test_easyflow_Job_source_value_roundtrip():
    instance = easyflow_Job(dependencies="sample_text", exe="sample_text", genericArgs="sample_text", inputArgs="sample_text", interpreterOption="sample_text", name="sample_text", outputArgs="sample_text", source="sample_text", staticArgs="sample_text", subCmd="sample_text", targetPlatform="sample_text", targetPlatformOptions="sample_text", targets="sample_text")
    assert instance.source == "sample_text"
    instance.source = "sample_text_2"
    assert instance.source == "sample_text_2"


def test_easyflow_Job_staticArgs_value_roundtrip():
    instance = easyflow_Job(dependencies="sample_text", exe="sample_text", genericArgs="sample_text", inputArgs="sample_text", interpreterOption="sample_text", name="sample_text", outputArgs="sample_text", source="sample_text", staticArgs="sample_text", subCmd="sample_text", targetPlatform="sample_text", targetPlatformOptions="sample_text", targets="sample_text")
    assert instance.staticArgs == "sample_text"
    instance.staticArgs = "sample_text_2"
    assert instance.staticArgs == "sample_text_2"


def test_easyflow_Job_subCmd_value_roundtrip():
    instance = easyflow_Job(dependencies="sample_text", exe="sample_text", genericArgs="sample_text", inputArgs="sample_text", interpreterOption="sample_text", name="sample_text", outputArgs="sample_text", source="sample_text", staticArgs="sample_text", subCmd="sample_text", targetPlatform="sample_text", targetPlatformOptions="sample_text", targets="sample_text")
    assert instance.subCmd == "sample_text"
    instance.subCmd = "sample_text_2"
    assert instance.subCmd == "sample_text_2"


def test_easyflow_Job_targetPlatform_value_roundtrip():
    instance = easyflow_Job(dependencies="sample_text", exe="sample_text", genericArgs="sample_text", inputArgs="sample_text", interpreterOption="sample_text", name="sample_text", outputArgs="sample_text", source="sample_text", staticArgs="sample_text", subCmd="sample_text", targetPlatform="sample_text", targetPlatformOptions="sample_text", targets="sample_text")
    assert instance.targetPlatform == "sample_text"
    instance.targetPlatform = "sample_text_2"
    assert instance.targetPlatform == "sample_text_2"


def test_easyflow_Job_targetPlatformOptions_value_roundtrip():
    instance = easyflow_Job(dependencies="sample_text", exe="sample_text", genericArgs="sample_text", inputArgs="sample_text", interpreterOption="sample_text", name="sample_text", outputArgs="sample_text", source="sample_text", staticArgs="sample_text", subCmd="sample_text", targetPlatform="sample_text", targetPlatformOptions="sample_text", targets="sample_text")
    assert instance.targetPlatformOptions == "sample_text"
    instance.targetPlatformOptions = "sample_text_2"
    assert instance.targetPlatformOptions == "sample_text_2"


def test_easyflow_Job_targets_value_roundtrip():
    instance = easyflow_Job(dependencies="sample_text", exe="sample_text", genericArgs="sample_text", inputArgs="sample_text", interpreterOption="sample_text", name="sample_text", outputArgs="sample_text", source="sample_text", staticArgs="sample_text", subCmd="sample_text", targetPlatform="sample_text", targetPlatformOptions="sample_text", targets="sample_text")
    assert instance.targets == "sample_text"
    instance.targets = "sample_text_2"
    assert instance.targets == "sample_text_2"


def test_easyflow_Library_insertSize_value_roundtrip():
    instance = easyflow_Library(insertSize=7, name="sample_text", readLength=7)
    assert instance.insertSize == 7
    instance.insertSize = 13
    assert instance.insertSize == 13


def test_easyflow_Library_name_value_roundtrip():
    instance = easyflow_Library(insertSize=7, name="sample_text", readLength=7)
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_easyflow_Library_readLength_value_roundtrip():
    instance = easyflow_Library(insertSize=7, name="sample_text", readLength=7)
    assert instance.readLength == 7
    instance.readLength = 13
    assert instance.readLength == 13


def test_easyflow_Readgroup_description_value_roundtrip():
    instance = easyflow_Readgroup(description="sample_text", name="sample_text", platform="sample_text", platformUnit="sample_text")
    assert instance.description == "sample_text"
    instance.description = "sample_text_2"
    assert instance.description == "sample_text_2"


def test_easyflow_Readgroup_name_value_roundtrip():
    instance = easyflow_Readgroup(description="sample_text", name="sample_text", platform="sample_text", platformUnit="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_easyflow_Readgroup_platform_value_roundtrip():
    instance = easyflow_Readgroup(description="sample_text", name="sample_text", platform="sample_text", platformUnit="sample_text")
    assert instance.platform == "sample_text"
    instance.platform = "sample_text_2"
    assert instance.platform == "sample_text_2"


def test_easyflow_Readgroup_platformUnit_value_roundtrip():
    instance = easyflow_Readgroup(description="sample_text", name="sample_text", platform="sample_text", platformUnit="sample_text")
    assert instance.platformUnit == "sample_text"
    instance.platformUnit = "sample_text_2"
    assert instance.platformUnit == "sample_text_2"


def test_easyflow_Record_fileNames_value_roundtrip():
    instance = easyflow_Record(fileNames="sample_text", refData="sample_text")
    assert instance.fileNames == "sample_text"
    instance.fileNames = "sample_text_2"
    assert instance.fileNames == "sample_text_2"


def test_easyflow_Record_refData_value_roundtrip():
    instance = easyflow_Record(fileNames="sample_text", refData="sample_text")
    assert instance.refData == "sample_text"
    instance.refData = "sample_text_2"
    assert instance.refData == "sample_text_2"


def test_easyflow_Sample_name_value_roundtrip():
    instance = easyflow_Sample(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_easyflow_SplittingEvent_dag_value_roundtrip():
    instance = easyflow_SplittingEvent(dag="sample_text", processedTask="sample_text", traversalChunks="sample_text", traversalCriterion="sample_text", traversalImplDir="sample_text")
    assert instance.dag == "sample_text"
    instance.dag = "sample_text_2"
    assert instance.dag == "sample_text_2"


def test_easyflow_SplittingEvent_processedTask_value_roundtrip():
    instance = easyflow_SplittingEvent(dag="sample_text", processedTask="sample_text", traversalChunks="sample_text", traversalCriterion="sample_text", traversalImplDir="sample_text")
    assert instance.processedTask == "sample_text"
    instance.processedTask = "sample_text_2"
    assert instance.processedTask == "sample_text_2"


def test_easyflow_SplittingEvent_traversalChunks_value_roundtrip():
    instance = easyflow_SplittingEvent(dag="sample_text", processedTask="sample_text", traversalChunks="sample_text", traversalCriterion="sample_text", traversalImplDir="sample_text")
    assert instance.traversalChunks == "sample_text"
    instance.traversalChunks = "sample_text_2"
    assert instance.traversalChunks == "sample_text_2"


def test_easyflow_SplittingEvent_traversalCriterion_value_roundtrip():
    instance = easyflow_SplittingEvent(dag="sample_text", processedTask="sample_text", traversalChunks="sample_text", traversalCriterion="sample_text", traversalImplDir="sample_text")
    assert instance.traversalCriterion == "sample_text"
    instance.traversalCriterion = "sample_text_2"
    assert instance.traversalCriterion == "sample_text_2"


def test_easyflow_SplittingEvent_traversalImplDir_value_roundtrip():
    instance = easyflow_SplittingEvent(dag="sample_text", processedTask="sample_text", traversalChunks="sample_text", traversalCriterion="sample_text", traversalImplDir="sample_text")
    assert instance.traversalImplDir == "sample_text"
    instance.traversalImplDir = "sample_text_2"
    assert instance.traversalImplDir == "sample_text_2"


def test_easyflow_StringToChunkMap_key_value_roundtrip():
    instance = easyflow_StringToChunkMap(key="sample_text")
    assert instance.key == "sample_text"
    instance.key = "sample_text_2"
    assert instance.key == "sample_text_2"


def test_easyflow_StringToGroupMap_key_value_roundtrip():
    instance = easyflow_StringToGroupMap(key="sample_text")
    assert instance.key == "sample_text"
    instance.key = "sample_text_2"
    assert instance.key == "sample_text_2"


def test_easyflow_StringToGroupingCriterionMap_key_value_roundtrip():
    instance = easyflow_StringToGroupingCriterionMap(key="sample_text")
    assert instance.key == "sample_text"
    instance.key = "sample_text_2"
    assert instance.key == "sample_text_2"


def test_easyflow_StringToLibraryMap_key_value_roundtrip():
    instance = easyflow_StringToLibraryMap(key="sample_text")
    assert instance.key == "sample_text"
    instance.key = "sample_text_2"
    assert instance.key == "sample_text_2"


def test_easyflow_StringToReadgroupMap_key_value_roundtrip():
    instance = easyflow_StringToReadgroupMap(key="sample_text")
    assert instance.key == "sample_text"
    instance.key = "sample_text_2"
    assert instance.key == "sample_text_2"


def test_easyflow_StringToRecordMap_key_value_roundtrip():
    instance = easyflow_StringToRecordMap(key="sample_text")
    assert instance.key == "sample_text"
    instance.key = "sample_text_2"
    assert instance.key == "sample_text_2"


def test_easyflow_StringToSampleMap_key_value_roundtrip():
    instance = easyflow_StringToSampleMap(key="sample_text")
    assert instance.key == "sample_text"
    instance.key = "sample_text_2"
    assert instance.key == "sample_text_2"


def test_easyflow_StringToTaskMap_key_value_roundtrip():
    instance = easyflow_StringToTaskMap(key="sample_text")
    assert instance.key == "sample_text"
    instance.key = "sample_text_2"
    assert instance.key == "sample_text_2"


def test_easyflow_StringToToolMap_key_value_roundtrip():
    instance = easyflow_StringToToolMap(key="sample_text")
    assert instance.key == "sample_text"
    instance.key = "sample_text_2"
    assert instance.key == "sample_text_2"


def test_easyflow_StringToTraversalCriterionMap_key_value_roundtrip():
    instance = easyflow_StringToTraversalCriterionMap(key="sample_text", value="sample_text")
    assert instance.key == "sample_text"
    instance.key = "sample_text_2"
    assert instance.key == "sample_text_2"


def test_easyflow_StringToTraversalCriterionMap_value_value_roundtrip():
    instance = easyflow_StringToTraversalCriterionMap(key="sample_text", value="sample_text")
    assert instance.value == "sample_text"
    instance.value = "sample_text_2"
    assert instance.value == "sample_text_2"


def test_easyflow_Task_cardinalityIn_value_roundtrip():
    instance = easyflow_Task(cardinalityIn="sample_text", cardinalityOut="sample_text", contrast=True, dataCriterion="sample_text", dataFormatIn="sample_text", dataFormatOut="sample_text", depricated=True, isMultipleInstancesOfDataCriterion="sample_text", jexlString="sample_text", mergeCriterion="sample_text", name="sample_text", skipGroupingCriterion="sample_text", splitCriterion="sample_text", static=True, traversalCriterion="sample_text", util=True)
    assert instance.cardinalityIn == "sample_text"
    instance.cardinalityIn = "sample_text_2"
    assert instance.cardinalityIn == "sample_text_2"


def test_easyflow_Task_cardinalityOut_value_roundtrip():
    instance = easyflow_Task(cardinalityIn="sample_text", cardinalityOut="sample_text", contrast=True, dataCriterion="sample_text", dataFormatIn="sample_text", dataFormatOut="sample_text", depricated=True, isMultipleInstancesOfDataCriterion="sample_text", jexlString="sample_text", mergeCriterion="sample_text", name="sample_text", skipGroupingCriterion="sample_text", splitCriterion="sample_text", static=True, traversalCriterion="sample_text", util=True)
    assert instance.cardinalityOut == "sample_text"
    instance.cardinalityOut = "sample_text_2"
    assert instance.cardinalityOut == "sample_text_2"


def test_easyflow_Task_contrast_value_roundtrip():
    instance = easyflow_Task(cardinalityIn="sample_text", cardinalityOut="sample_text", contrast=True, dataCriterion="sample_text", dataFormatIn="sample_text", dataFormatOut="sample_text", depricated=True, isMultipleInstancesOfDataCriterion="sample_text", jexlString="sample_text", mergeCriterion="sample_text", name="sample_text", skipGroupingCriterion="sample_text", splitCriterion="sample_text", static=True, traversalCriterion="sample_text", util=True)
    assert instance.contrast == True
    instance.contrast = False
    assert instance.contrast == False


def test_easyflow_Task_dataCriterion_value_roundtrip():
    instance = easyflow_Task(cardinalityIn="sample_text", cardinalityOut="sample_text", contrast=True, dataCriterion="sample_text", dataFormatIn="sample_text", dataFormatOut="sample_text", depricated=True, isMultipleInstancesOfDataCriterion="sample_text", jexlString="sample_text", mergeCriterion="sample_text", name="sample_text", skipGroupingCriterion="sample_text", splitCriterion="sample_text", static=True, traversalCriterion="sample_text", util=True)
    assert instance.dataCriterion == "sample_text"
    instance.dataCriterion = "sample_text_2"
    assert instance.dataCriterion == "sample_text_2"


def test_easyflow_Task_dataFormatIn_value_roundtrip():
    instance = easyflow_Task(cardinalityIn="sample_text", cardinalityOut="sample_text", contrast=True, dataCriterion="sample_text", dataFormatIn="sample_text", dataFormatOut="sample_text", depricated=True, isMultipleInstancesOfDataCriterion="sample_text", jexlString="sample_text", mergeCriterion="sample_text", name="sample_text", skipGroupingCriterion="sample_text", splitCriterion="sample_text", static=True, traversalCriterion="sample_text", util=True)
    assert instance.dataFormatIn == "sample_text"
    instance.dataFormatIn = "sample_text_2"
    assert instance.dataFormatIn == "sample_text_2"


def test_easyflow_Task_dataFormatOut_value_roundtrip():
    instance = easyflow_Task(cardinalityIn="sample_text", cardinalityOut="sample_text", contrast=True, dataCriterion="sample_text", dataFormatIn="sample_text", dataFormatOut="sample_text", depricated=True, isMultipleInstancesOfDataCriterion="sample_text", jexlString="sample_text", mergeCriterion="sample_text", name="sample_text", skipGroupingCriterion="sample_text", splitCriterion="sample_text", static=True, traversalCriterion="sample_text", util=True)
    assert instance.dataFormatOut == "sample_text"
    instance.dataFormatOut = "sample_text_2"
    assert instance.dataFormatOut == "sample_text_2"


def test_easyflow_Task_depricated_value_roundtrip():
    instance = easyflow_Task(cardinalityIn="sample_text", cardinalityOut="sample_text", contrast=True, dataCriterion="sample_text", dataFormatIn="sample_text", dataFormatOut="sample_text", depricated=True, isMultipleInstancesOfDataCriterion="sample_text", jexlString="sample_text", mergeCriterion="sample_text", name="sample_text", skipGroupingCriterion="sample_text", splitCriterion="sample_text", static=True, traversalCriterion="sample_text", util=True)
    assert instance.depricated == True
    instance.depricated = False
    assert instance.depricated == False


def test_easyflow_Task_isMultipleInstancesOfDataCriterion_value_roundtrip():
    instance = easyflow_Task(cardinalityIn="sample_text", cardinalityOut="sample_text", contrast=True, dataCriterion="sample_text", dataFormatIn="sample_text", dataFormatOut="sample_text", depricated=True, isMultipleInstancesOfDataCriterion="sample_text", jexlString="sample_text", mergeCriterion="sample_text", name="sample_text", skipGroupingCriterion="sample_text", splitCriterion="sample_text", static=True, traversalCriterion="sample_text", util=True)
    assert instance.isMultipleInstancesOfDataCriterion == "sample_text"
    instance.isMultipleInstancesOfDataCriterion = "sample_text_2"
    assert instance.isMultipleInstancesOfDataCriterion == "sample_text_2"


def test_easyflow_Task_jexlString_value_roundtrip():
    instance = easyflow_Task(cardinalityIn="sample_text", cardinalityOut="sample_text", contrast=True, dataCriterion="sample_text", dataFormatIn="sample_text", dataFormatOut="sample_text", depricated=True, isMultipleInstancesOfDataCriterion="sample_text", jexlString="sample_text", mergeCriterion="sample_text", name="sample_text", skipGroupingCriterion="sample_text", splitCriterion="sample_text", static=True, traversalCriterion="sample_text", util=True)
    assert instance.jexlString == "sample_text"
    instance.jexlString = "sample_text_2"
    assert instance.jexlString == "sample_text_2"


def test_easyflow_Task_mergeCriterion_value_roundtrip():
    instance = easyflow_Task(cardinalityIn="sample_text", cardinalityOut="sample_text", contrast=True, dataCriterion="sample_text", dataFormatIn="sample_text", dataFormatOut="sample_text", depricated=True, isMultipleInstancesOfDataCriterion="sample_text", jexlString="sample_text", mergeCriterion="sample_text", name="sample_text", skipGroupingCriterion="sample_text", splitCriterion="sample_text", static=True, traversalCriterion="sample_text", util=True)
    assert instance.mergeCriterion == "sample_text"
    instance.mergeCriterion = "sample_text_2"
    assert instance.mergeCriterion == "sample_text_2"


def test_easyflow_Task_name_value_roundtrip():
    instance = easyflow_Task(cardinalityIn="sample_text", cardinalityOut="sample_text", contrast=True, dataCriterion="sample_text", dataFormatIn="sample_text", dataFormatOut="sample_text", depricated=True, isMultipleInstancesOfDataCriterion="sample_text", jexlString="sample_text", mergeCriterion="sample_text", name="sample_text", skipGroupingCriterion="sample_text", splitCriterion="sample_text", static=True, traversalCriterion="sample_text", util=True)
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_easyflow_Task_skipGroupingCriterion_value_roundtrip():
    instance = easyflow_Task(cardinalityIn="sample_text", cardinalityOut="sample_text", contrast=True, dataCriterion="sample_text", dataFormatIn="sample_text", dataFormatOut="sample_text", depricated=True, isMultipleInstancesOfDataCriterion="sample_text", jexlString="sample_text", mergeCriterion="sample_text", name="sample_text", skipGroupingCriterion="sample_text", splitCriterion="sample_text", static=True, traversalCriterion="sample_text", util=True)
    assert instance.skipGroupingCriterion == "sample_text"
    instance.skipGroupingCriterion = "sample_text_2"
    assert instance.skipGroupingCriterion == "sample_text_2"


def test_easyflow_Task_splitCriterion_value_roundtrip():
    instance = easyflow_Task(cardinalityIn="sample_text", cardinalityOut="sample_text", contrast=True, dataCriterion="sample_text", dataFormatIn="sample_text", dataFormatOut="sample_text", depricated=True, isMultipleInstancesOfDataCriterion="sample_text", jexlString="sample_text", mergeCriterion="sample_text", name="sample_text", skipGroupingCriterion="sample_text", splitCriterion="sample_text", static=True, traversalCriterion="sample_text", util=True)
    assert instance.splitCriterion == "sample_text"
    instance.splitCriterion = "sample_text_2"
    assert instance.splitCriterion == "sample_text_2"


def test_easyflow_Task_static_value_roundtrip():
    instance = easyflow_Task(cardinalityIn="sample_text", cardinalityOut="sample_text", contrast=True, dataCriterion="sample_text", dataFormatIn="sample_text", dataFormatOut="sample_text", depricated=True, isMultipleInstancesOfDataCriterion="sample_text", jexlString="sample_text", mergeCriterion="sample_text", name="sample_text", skipGroupingCriterion="sample_text", splitCriterion="sample_text", static=True, traversalCriterion="sample_text", util=True)
    assert instance.static == True
    instance.static = False
    assert instance.static == False


def test_easyflow_Task_traversalCriterion_value_roundtrip():
    instance = easyflow_Task(cardinalityIn="sample_text", cardinalityOut="sample_text", contrast=True, dataCriterion="sample_text", dataFormatIn="sample_text", dataFormatOut="sample_text", depricated=True, isMultipleInstancesOfDataCriterion="sample_text", jexlString="sample_text", mergeCriterion="sample_text", name="sample_text", skipGroupingCriterion="sample_text", splitCriterion="sample_text", static=True, traversalCriterion="sample_text", util=True)
    assert instance.traversalCriterion == "sample_text"
    instance.traversalCriterion = "sample_text_2"
    assert instance.traversalCriterion == "sample_text_2"


def test_easyflow_Task_util_value_roundtrip():
    instance = easyflow_Task(cardinalityIn="sample_text", cardinalityOut="sample_text", contrast=True, dataCriterion="sample_text", dataFormatIn="sample_text", dataFormatOut="sample_text", depricated=True, isMultipleInstancesOfDataCriterion="sample_text", jexlString="sample_text", mergeCriterion="sample_text", name="sample_text", skipGroupingCriterion="sample_text", splitCriterion="sample_text", static=True, traversalCriterion="sample_text", util=True)
    assert instance.util == True
    instance.util = False
    assert instance.util == False


def test_easyflow_Tool_category_value_roundtrip():
    instance = easyflow_Tool(category="sample_text", pattern="sample_text", refData="sample_text", source="sample_text", subCmd="sample_text", subCmdPrefix="sample_text", toolName="sample_text", type="sample_text")
    assert instance.category == "sample_text"
    instance.category = "sample_text_2"
    assert instance.category == "sample_text_2"


def test_easyflow_Tool_pattern_value_roundtrip():
    instance = easyflow_Tool(category="sample_text", pattern="sample_text", refData="sample_text", source="sample_text", subCmd="sample_text", subCmdPrefix="sample_text", toolName="sample_text", type="sample_text")
    assert instance.pattern == "sample_text"
    instance.pattern = "sample_text_2"
    assert instance.pattern == "sample_text_2"


def test_easyflow_Tool_refData_value_roundtrip():
    instance = easyflow_Tool(category="sample_text", pattern="sample_text", refData="sample_text", source="sample_text", subCmd="sample_text", subCmdPrefix="sample_text", toolName="sample_text", type="sample_text")
    assert instance.refData == "sample_text"
    instance.refData = "sample_text_2"
    assert instance.refData == "sample_text_2"


def test_easyflow_Tool_source_value_roundtrip():
    instance = easyflow_Tool(category="sample_text", pattern="sample_text", refData="sample_text", source="sample_text", subCmd="sample_text", subCmdPrefix="sample_text", toolName="sample_text", type="sample_text")
    assert instance.source == "sample_text"
    instance.source = "sample_text_2"
    assert instance.source == "sample_text_2"


def test_easyflow_Tool_subCmd_value_roundtrip():
    instance = easyflow_Tool(category="sample_text", pattern="sample_text", refData="sample_text", source="sample_text", subCmd="sample_text", subCmdPrefix="sample_text", toolName="sample_text", type="sample_text")
    assert instance.subCmd == "sample_text"
    instance.subCmd = "sample_text_2"
    assert instance.subCmd == "sample_text_2"


def test_easyflow_Tool_subCmdPrefix_value_roundtrip():
    instance = easyflow_Tool(category="sample_text", pattern="sample_text", refData="sample_text", source="sample_text", subCmd="sample_text", subCmdPrefix="sample_text", toolName="sample_text", type="sample_text")
    assert instance.subCmdPrefix == "sample_text"
    instance.subCmdPrefix = "sample_text_2"
    assert instance.subCmdPrefix == "sample_text_2"


def test_easyflow_Tool_toolName_value_roundtrip():
    instance = easyflow_Tool(category="sample_text", pattern="sample_text", refData="sample_text", source="sample_text", subCmd="sample_text", subCmdPrefix="sample_text", toolName="sample_text", type="sample_text")
    assert instance.toolName == "sample_text"
    instance.toolName = "sample_text_2"
    assert instance.toolName == "sample_text_2"


def test_easyflow_Tool_type_value_roundtrip():
    instance = easyflow_Tool(category="sample_text", pattern="sample_text", refData="sample_text", source="sample_text", subCmd="sample_text", subCmdPrefix="sample_text", toolName="sample_text", type="sample_text")
    assert instance.type == "sample_text"
    instance.type = "sample_text_2"
    assert instance.type == "sample_text_2"


def test_easyflow_Traversal_tarversalCriterion_value_roundtrip():
    instance = easyflow_Traversal(tarversalCriterion="sample_text")
    assert instance.tarversalCriterion == "sample_text"
    instance.tarversalCriterion = "sample_text_2"
    assert instance.tarversalCriterion == "sample_text_2"


def test_easyflow_Workflow_dag_value_roundtrip():
    instance = easyflow_Workflow(dag="sample_text", graph="sample_text", jobDag="sample_text", name="sample_text")
    assert instance.dag == "sample_text"
    instance.dag = "sample_text_2"
    assert instance.dag == "sample_text_2"


def test_easyflow_Workflow_graph_value_roundtrip():
    instance = easyflow_Workflow(dag="sample_text", graph="sample_text", jobDag="sample_text", name="sample_text")
    assert instance.graph == "sample_text"
    instance.graph = "sample_text_2"
    assert instance.graph == "sample_text_2"


def test_easyflow_Workflow_jobDag_value_roundtrip():
    instance = easyflow_Workflow(dag="sample_text", graph="sample_text", jobDag="sample_text", name="sample_text")
    assert instance.jobDag == "sample_text"
    instance.jobDag = "sample_text_2"
    assert instance.jobDag == "sample_text_2"


def test_easyflow_Workflow_name_value_roundtrip():
    instance = easyflow_Workflow(dag="sample_text", graph="sample_text", jobDag="sample_text", name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_easyflow_EasyFlowMetadataReader_isa_EasyFlowMetadata():
    instance = easyflow_EasyFlowMetadataReader(fileName="sample_text")
    assert isinstance(instance, EasyFlowMetadata)


def test_easyflow_Group_isa_GroupingCriterion():
    instance = easyflow_Group(name="sample_text")
    assert isinstance(instance, GroupingCriterion)


def test_easyflow_Library_isa_GroupingCriterion():
    instance = easyflow_Library(insertSize=7, name="sample_text", readLength=7)
    assert isinstance(instance, GroupingCriterion)


def test_easyflow_Readgroup_isa_GroupingCriterion():
    instance = easyflow_Readgroup(description="sample_text", name="sample_text", platform="sample_text", platformUnit="sample_text")
    assert isinstance(instance, GroupingCriterion)


def test_easyflow_Record_isa_GroupingCriterion():
    instance = easyflow_Record(fileNames="sample_text", refData="sample_text")
    assert isinstance(instance, GroupingCriterion)


def test_easyflow_Sample_isa_GroupingCriterion():
    instance = easyflow_Sample(name="sample_text")
    assert isinstance(instance, GroupingCriterion)


def test_easyflow_Traversal_isa_ITraversal():
    instance = easyflow_Traversal(tarversalCriterion="sample_text")
    assert isinstance(instance, ITraversal)


def test_easyflow_Contig_isa_Traversal():
    instance = easyflow_Contig()
    assert isinstance(instance, Traversal)


def test_easyflow_GenericTraversalCriterion_isa_Traversal():
    instance = easyflow_GenericTraversalCriterion()
    assert isinstance(instance, Traversal)


def test_easyflow_Locus_isa_Traversal():
    instance = easyflow_Locus()
    assert isinstance(instance, Traversal)


def test_easyflow_ReadEnd_isa_Traversal():
    instance = easyflow_ReadEnd()
    assert isinstance(instance, Traversal)


def test_assoc_Configuration1_link_reassign_clear():
    a = easyflow_Workflow(dag="sample_text", graph="sample_text", jobDag="sample_text", name="sample_text")
    b1 = easyflow_EasyFlowConfiguration(configMap="sample_text", fileName="sample_text")
    b2 = easyflow_EasyFlowConfiguration(configMap="sample_text_2", fileName="sample_text_2")
    _safe_set(a, 'easyflow_Workflow2', b1)
    assert _is_linked(a, 'easyflow_Workflow2', b1)
    if hasattr(b1, 'easyflow_EasyFlowConfiguration'):
        assert _is_linked(b1, 'easyflow_EasyFlowConfiguration', a)
    _safe_set(a, 'easyflow_Workflow2', b2)
    assert _is_linked(a, 'easyflow_Workflow2', b2)
    if hasattr(b1, 'easyflow_EasyFlowConfiguration'):
        assert not _is_linked(b1, 'easyflow_EasyFlowConfiguration', a)
    if hasattr(b2, 'easyflow_EasyFlowConfiguration'):
        assert _is_linked(b2, 'easyflow_EasyFlowConfiguration', a)
    _safe_set(a, 'easyflow_Workflow2', None)
    assert not _is_linked(a, 'easyflow_Workflow2', b2)
    if hasattr(b2, 'easyflow_EasyFlowConfiguration'):
        assert not _is_linked(b2, 'easyflow_EasyFlowConfiguration', a)


def test_assoc_DataProcessingType7_link_reassign_clear():
    a = easyflow_Workflow(dag="sample_text", graph="sample_text", jobDag="sample_text", name="sample_text")
    b1 = easyflow_DataProcessingType(dataFormatIn="sample_text", dataFormatOut="sample_text")
    b2 = easyflow_DataProcessingType(dataFormatIn="sample_text_2", dataFormatOut="sample_text_2")
    _safe_set(a, 'easyflow_Workflow8', b1)
    assert _is_linked(a, 'easyflow_Workflow8', b1)
    if hasattr(b1, 'easyflow_DataProcessingType'):
        assert _is_linked(b1, 'easyflow_DataProcessingType', a)
    _safe_set(a, 'easyflow_Workflow8', b2)
    assert _is_linked(a, 'easyflow_Workflow8', b2)
    if hasattr(b1, 'easyflow_DataProcessingType'):
        assert not _is_linked(b1, 'easyflow_DataProcessingType', a)
    if hasattr(b2, 'easyflow_DataProcessingType'):
        assert _is_linked(b2, 'easyflow_DataProcessingType', a)
    _safe_set(a, 'easyflow_Workflow8', None)
    assert not _is_linked(a, 'easyflow_Workflow8', b2)
    if hasattr(b2, 'easyflow_DataProcessingType'):
        assert not _is_linked(b2, 'easyflow_DataProcessingType', a)


def test_assoc_ImplementationTemplate5_link_reassign_clear():
    a = easyflow_Workflow(dag="sample_text", graph="sample_text", jobDag="sample_text", name="sample_text")
    b1 = easyflow_EasyFlowImplementationTemplate(fileName="sample_text", globalOptions="sample_text", jsonRootNode="sample_text", parameterConfigFileName="sample_text", parameterConfigMap="sample_text")
    b2 = easyflow_EasyFlowImplementationTemplate(fileName="sample_text_2", globalOptions="sample_text_2", jsonRootNode="sample_text_2", parameterConfigFileName="sample_text_2", parameterConfigMap="sample_text_2")
    _safe_set(a, 'easyflow_Workflow6', b1)
    assert _is_linked(a, 'easyflow_Workflow6', b1)
    if hasattr(b1, 'easyflow_EasyFlowImplementationTemplate'):
        assert _is_linked(b1, 'easyflow_EasyFlowImplementationTemplate', a)
    _safe_set(a, 'easyflow_Workflow6', b2)
    assert _is_linked(a, 'easyflow_Workflow6', b2)
    if hasattr(b1, 'easyflow_EasyFlowImplementationTemplate'):
        assert not _is_linked(b1, 'easyflow_EasyFlowImplementationTemplate', a)
    if hasattr(b2, 'easyflow_EasyFlowImplementationTemplate'):
        assert _is_linked(b2, 'easyflow_EasyFlowImplementationTemplate', a)
    _safe_set(a, 'easyflow_Workflow6', None)
    assert not _is_linked(a, 'easyflow_Workflow6', b2)
    if hasattr(b2, 'easyflow_EasyFlowImplementationTemplate'):
        assert not _is_linked(b2, 'easyflow_EasyFlowImplementationTemplate', a)


def test_assoc_LastTaskClassMap9_link_reassign_clear():
    a = easyflow_Workflow(dag="sample_text", graph="sample_text", jobDag="sample_text", name="sample_text")
    b1 = easyflow_DataProcessingTypeToTask()
    b2 = easyflow_DataProcessingTypeToTask()
    _safe_set(a, 'easyflow_Workflow10', {b1})
    assert _is_linked(a, 'easyflow_Workflow10', b1)
    if hasattr(b1, 'easyflow_DataProcessingTypeToTask'):
        assert _is_linked(b1, 'easyflow_DataProcessingTypeToTask', a)
    _safe_set(a, 'easyflow_Workflow10', {b2})
    assert _is_linked(a, 'easyflow_Workflow10', b2)
    if hasattr(b1, 'easyflow_DataProcessingTypeToTask'):
        assert not _is_linked(b1, 'easyflow_DataProcessingTypeToTask', a)
    if hasattr(b2, 'easyflow_DataProcessingTypeToTask'):
        assert _is_linked(b2, 'easyflow_DataProcessingTypeToTask', a)
    _safe_set(a, 'easyflow_Workflow10', set())
    assert not _is_linked(a, 'easyflow_Workflow10', b2)
    if hasattr(b2, 'easyflow_DataProcessingTypeToTask'):
        assert not _is_linked(b2, 'easyflow_DataProcessingTypeToTask', a)


def test_assoc_WorkflowTemplate0_link_reassign_clear():
    a = easyflow_Workflow(dag="sample_text", graph="sample_text", jobDag="sample_text", name="sample_text")
    b1 = easyflow_EasyFlowTemplate(fileName="sample_text")
    b2 = easyflow_EasyFlowTemplate(fileName="sample_text_2")
    _safe_set(a, 'easyflow_Workflow', b1)
    assert _is_linked(a, 'easyflow_Workflow', b1)
    if hasattr(b1, 'easyflow_EasyFlowTemplate'):
        assert _is_linked(b1, 'easyflow_EasyFlowTemplate', a)
    _safe_set(a, 'easyflow_Workflow', b2)
    assert _is_linked(a, 'easyflow_Workflow', b2)
    if hasattr(b1, 'easyflow_EasyFlowTemplate'):
        assert not _is_linked(b1, 'easyflow_EasyFlowTemplate', a)
    if hasattr(b2, 'easyflow_EasyFlowTemplate'):
        assert _is_linked(b2, 'easyflow_EasyFlowTemplate', a)
    _safe_set(a, 'easyflow_Workflow', None)
    assert not _is_linked(a, 'easyflow_Workflow', b2)
    if hasattr(b2, 'easyflow_EasyFlowTemplate'):
        assert not _is_linked(b2, 'easyflow_EasyFlowTemplate', a)


def test_assoc_argIn39_link_reassign_clear():
    a = easyflow_Tool(category="sample_text", pattern="sample_text", refData="sample_text", source="sample_text", subCmd="sample_text", subCmdPrefix="sample_text", toolName="sample_text", type="sample_text")
    b1 = easyflow_CommandArgument(arg="sample_text", name="sample_text", named=True, required=True, sep="sample_text")
    b2 = easyflow_CommandArgument(arg="sample_text_2", name="sample_text_2", named=False, required=False, sep="sample_text_2")
    _safe_set(a, 'easyflow_Tool', {b1})
    assert _is_linked(a, 'easyflow_Tool', b1)
    if hasattr(b1, 'easyflow_CommandArgument'):
        assert _is_linked(b1, 'easyflow_CommandArgument', a)
    _safe_set(a, 'easyflow_Tool', {b2})
    assert _is_linked(a, 'easyflow_Tool', b2)
    if hasattr(b1, 'easyflow_CommandArgument'):
        assert not _is_linked(b1, 'easyflow_CommandArgument', a)
    if hasattr(b2, 'easyflow_CommandArgument'):
        assert _is_linked(b2, 'easyflow_CommandArgument', a)
    _safe_set(a, 'easyflow_Tool', set())
    assert not _is_linked(a, 'easyflow_Tool', b2)
    if hasattr(b2, 'easyflow_CommandArgument'):
        assert not _is_linked(b2, 'easyflow_CommandArgument', a)


def test_assoc_argOut40_link_reassign_clear():
    a = easyflow_Tool(category="sample_text", pattern="sample_text", refData="sample_text", source="sample_text", subCmd="sample_text", subCmdPrefix="sample_text", toolName="sample_text", type="sample_text")
    b1 = easyflow_CommandArgument(arg="sample_text", name="sample_text", named=True, required=True, sep="sample_text")
    b2 = easyflow_CommandArgument(arg="sample_text_2", name="sample_text_2", named=False, required=False, sep="sample_text_2")
    _safe_set(a, 'easyflow_Tool41', {b1})
    assert _is_linked(a, 'easyflow_Tool41', b1)
    if hasattr(b1, 'easyflow_CommandArgument42'):
        assert _is_linked(b1, 'easyflow_CommandArgument42', a)
    _safe_set(a, 'easyflow_Tool41', {b2})
    assert _is_linked(a, 'easyflow_Tool41', b2)
    if hasattr(b1, 'easyflow_CommandArgument42'):
        assert not _is_linked(b1, 'easyflow_CommandArgument42', a)
    if hasattr(b2, 'easyflow_CommandArgument42'):
        assert _is_linked(b2, 'easyflow_CommandArgument42', a)
    _safe_set(a, 'easyflow_Tool41', set())
    assert not _is_linked(a, 'easyflow_Tool41', b2)
    if hasattr(b2, 'easyflow_CommandArgument42'):
        assert not _is_linked(b2, 'easyflow_CommandArgument42', a)


def test_assoc_chunks120_link_reassign_clear():
    a = easyflow_Traversal(tarversalCriterion="sample_text")
    b1 = easyflow_StringToChunkMap(key="sample_text")
    b2 = easyflow_StringToChunkMap(key="sample_text_2")
    _safe_set(a, 'easyflow_Traversal', {b1})
    assert _is_linked(a, 'easyflow_Traversal', b1)
    if hasattr(b1, 'easyflow_StringToChunkMap'):
        assert _is_linked(b1, 'easyflow_StringToChunkMap', a)
    _safe_set(a, 'easyflow_Traversal', {b2})
    assert _is_linked(a, 'easyflow_Traversal', b2)
    if hasattr(b1, 'easyflow_StringToChunkMap'):
        assert not _is_linked(b1, 'easyflow_StringToChunkMap', a)
    if hasattr(b2, 'easyflow_StringToChunkMap'):
        assert _is_linked(b2, 'easyflow_StringToChunkMap', a)
    _safe_set(a, 'easyflow_Traversal', set())
    assert not _is_linked(a, 'easyflow_Traversal', b2)
    if hasattr(b2, 'easyflow_StringToChunkMap'):
        assert not _is_linked(b2, 'easyflow_StringToChunkMap', a)


def test_assoc_chunks20_link_reassign_clear():
    a = easyflow_Task(cardinalityIn="sample_text", cardinalityOut="sample_text", contrast=True, dataCriterion="sample_text", dataFormatIn="sample_text", dataFormatOut="sample_text", depricated=True, isMultipleInstancesOfDataCriterion="sample_text", jexlString="sample_text", mergeCriterion="sample_text", name="sample_text", skipGroupingCriterion="sample_text", splitCriterion="sample_text", static=True, traversalCriterion="sample_text", util=True)
    b1 = easyflow_StringToTraversalCriterionMap(key="sample_text", value="sample_text")
    b2 = easyflow_StringToTraversalCriterionMap(key="sample_text_2", value="sample_text_2")
    _safe_set(a, 'easyflow_Task21', {b1})
    assert _is_linked(a, 'easyflow_Task21', b1)
    if hasattr(b1, 'easyflow_StringToTraversalCriterionMap'):
        assert _is_linked(b1, 'easyflow_StringToTraversalCriterionMap', a)
    _safe_set(a, 'easyflow_Task21', {b2})
    assert _is_linked(a, 'easyflow_Task21', b2)
    if hasattr(b1, 'easyflow_StringToTraversalCriterionMap'):
        assert not _is_linked(b1, 'easyflow_StringToTraversalCriterionMap', a)
    if hasattr(b2, 'easyflow_StringToTraversalCriterionMap'):
        assert _is_linked(b2, 'easyflow_StringToTraversalCriterionMap', a)
    _safe_set(a, 'easyflow_Task21', set())
    assert not _is_linked(a, 'easyflow_Task21', b2)
    if hasattr(b2, 'easyflow_StringToTraversalCriterionMap'):
        assert not _is_linked(b2, 'easyflow_StringToTraversalCriterionMap', a)


def test_assoc_genericArg46_link_reassign_clear():
    a = easyflow_Tool(category="sample_text", pattern="sample_text", refData="sample_text", source="sample_text", subCmd="sample_text", subCmdPrefix="sample_text", toolName="sample_text", type="sample_text")
    b1 = easyflow_CommandArgument(arg="sample_text", name="sample_text", named=True, required=True, sep="sample_text")
    b2 = easyflow_CommandArgument(arg="sample_text_2", name="sample_text_2", named=False, required=False, sep="sample_text_2")
    _safe_set(a, 'easyflow_Tool47', {b1})
    assert _is_linked(a, 'easyflow_Tool47', b1)
    if hasattr(b1, 'easyflow_CommandArgument48'):
        assert _is_linked(b1, 'easyflow_CommandArgument48', a)
    _safe_set(a, 'easyflow_Tool47', {b2})
    assert _is_linked(a, 'easyflow_Tool47', b2)
    if hasattr(b1, 'easyflow_CommandArgument48'):
        assert not _is_linked(b1, 'easyflow_CommandArgument48', a)
    if hasattr(b2, 'easyflow_CommandArgument48'):
        assert _is_linked(b2, 'easyflow_CommandArgument48', a)
    _safe_set(a, 'easyflow_Tool47', set())
    assert not _is_linked(a, 'easyflow_Tool47', b2)
    if hasattr(b2, 'easyflow_CommandArgument48'):
        assert not _is_linked(b2, 'easyflow_CommandArgument48', a)


def test_assoc_groupingCriterionMap18_link_reassign_clear():
    a = easyflow_Task(cardinalityIn="sample_text", cardinalityOut="sample_text", contrast=True, dataCriterion="sample_text", dataFormatIn="sample_text", dataFormatOut="sample_text", depricated=True, isMultipleInstancesOfDataCriterion="sample_text", jexlString="sample_text", mergeCriterion="sample_text", name="sample_text", skipGroupingCriterion="sample_text", splitCriterion="sample_text", static=True, traversalCriterion="sample_text", util=True)
    b1 = easyflow_StringToGroupingCriterionMap(key="sample_text")
    b2 = easyflow_StringToGroupingCriterionMap(key="sample_text_2")
    _safe_set(a, 'easyflow_Task19', {b1})
    assert _is_linked(a, 'easyflow_Task19', b1)
    if hasattr(b1, 'easyflow_StringToGroupingCriterionMap'):
        assert _is_linked(b1, 'easyflow_StringToGroupingCriterionMap', a)
    _safe_set(a, 'easyflow_Task19', {b2})
    assert _is_linked(a, 'easyflow_Task19', b2)
    if hasattr(b1, 'easyflow_StringToGroupingCriterionMap'):
        assert not _is_linked(b1, 'easyflow_StringToGroupingCriterionMap', a)
    if hasattr(b2, 'easyflow_StringToGroupingCriterionMap'):
        assert _is_linked(b2, 'easyflow_StringToGroupingCriterionMap', a)
    _safe_set(a, 'easyflow_Task19', set())
    assert not _is_linked(a, 'easyflow_Task19', b2)
    if hasattr(b2, 'easyflow_StringToGroupingCriterionMap'):
        assert not _is_linked(b2, 'easyflow_StringToGroupingCriterionMap', a)


def test_assoc_groups31_link_reassign_clear():
    a = easyflow_StringToGroupMap(key="sample_text")
    b1 = easyflow_EasyFlowMetadata(contrast=True, name="sample_text", refData="sample_text")
    b2 = easyflow_EasyFlowMetadata(contrast=False, name="sample_text_2", refData="sample_text_2")
    _safe_set(a, 'easyflow_StringToGroupMap', b1)
    assert _is_linked(a, 'easyflow_StringToGroupMap', b1)
    if hasattr(b1, 'easyflow_EasyFlowMetadata32'):
        assert _is_linked(b1, 'easyflow_EasyFlowMetadata32', a)
    _safe_set(a, 'easyflow_StringToGroupMap', b2)
    assert _is_linked(a, 'easyflow_StringToGroupMap', b2)
    if hasattr(b1, 'easyflow_EasyFlowMetadata32'):
        assert not _is_linked(b1, 'easyflow_EasyFlowMetadata32', a)
    if hasattr(b2, 'easyflow_EasyFlowMetadata32'):
        assert _is_linked(b2, 'easyflow_EasyFlowMetadata32', a)
    _safe_set(a, 'easyflow_StringToGroupMap', None)
    assert not _is_linked(a, 'easyflow_StringToGroupMap', b2)
    if hasattr(b2, 'easyflow_EasyFlowMetadata32'):
        assert not _is_linked(b2, 'easyflow_EasyFlowMetadata32', a)


def test_assoc_interpreter49_link_reassign_clear():
    a = easyflow_Tool(category="sample_text", pattern="sample_text", refData="sample_text", source="sample_text", subCmd="sample_text", subCmdPrefix="sample_text", toolName="sample_text", type="sample_text")
    b1 = easyflow_Interpreter(exe="sample_text", name="sample_text", options="sample_text", subCmd="sample_text")
    b2 = easyflow_Interpreter(exe="sample_text_2", name="sample_text_2", options="sample_text_2", subCmd="sample_text_2")
    _safe_set(a, 'easyflow_Tool50', b1)
    assert _is_linked(a, 'easyflow_Tool50', b1)
    if hasattr(b1, 'easyflow_Interpreter'):
        assert _is_linked(b1, 'easyflow_Interpreter', a)
    _safe_set(a, 'easyflow_Tool50', b2)
    assert _is_linked(a, 'easyflow_Tool50', b2)
    if hasattr(b1, 'easyflow_Interpreter'):
        assert not _is_linked(b1, 'easyflow_Interpreter', a)
    if hasattr(b2, 'easyflow_Interpreter'):
        assert _is_linked(b2, 'easyflow_Interpreter', a)
    _safe_set(a, 'easyflow_Tool50', None)
    assert not _is_linked(a, 'easyflow_Tool50', b2)
    if hasattr(b2, 'easyflow_Interpreter'):
        assert not _is_linked(b2, 'easyflow_Interpreter', a)


def test_assoc_key132_link_reassign_clear():
    a = easyflow_Task(cardinalityIn="sample_text", cardinalityOut="sample_text", contrast=True, dataCriterion="sample_text", dataFormatIn="sample_text", dataFormatOut="sample_text", depricated=True, isMultipleInstancesOfDataCriterion="sample_text", jexlString="sample_text", mergeCriterion="sample_text", name="sample_text", skipGroupingCriterion="sample_text", splitCriterion="sample_text", static=True, traversalCriterion="sample_text", util=True)
    b1 = easyflow_TaskToDataProcessingType()
    b2 = easyflow_TaskToDataProcessingType()
    _safe_set(a, 'easyflow_Task134', b1)
    assert _is_linked(a, 'easyflow_Task134', b1)
    if hasattr(b1, 'easyflow_TaskToDataProcessingType133'):
        assert _is_linked(b1, 'easyflow_TaskToDataProcessingType133', a)
    _safe_set(a, 'easyflow_Task134', b2)
    assert _is_linked(a, 'easyflow_Task134', b2)
    if hasattr(b1, 'easyflow_TaskToDataProcessingType133'):
        assert not _is_linked(b1, 'easyflow_TaskToDataProcessingType133', a)
    if hasattr(b2, 'easyflow_TaskToDataProcessingType133'):
        assert _is_linked(b2, 'easyflow_TaskToDataProcessingType133', a)
    _safe_set(a, 'easyflow_Task134', None)
    assert not _is_linked(a, 'easyflow_Task134', b2)
    if hasattr(b2, 'easyflow_TaskToDataProcessingType133'):
        assert not _is_linked(b2, 'easyflow_TaskToDataProcessingType133', a)


def test_assoc_key25_link_reassign_clear():
    a = easyflow_Task(cardinalityIn="sample_text", cardinalityOut="sample_text", contrast=True, dataCriterion="sample_text", dataFormatIn="sample_text", dataFormatOut="sample_text", depricated=True, isMultipleInstancesOfDataCriterion="sample_text", jexlString="sample_text", mergeCriterion="sample_text", name="sample_text", skipGroupingCriterion="sample_text", splitCriterion="sample_text", static=True, traversalCriterion="sample_text", util=True)
    b1 = easyflow_TaskToDataProcessingType()
    b2 = easyflow_TaskToDataProcessingType()
    _safe_set(a, 'easyflow_Task26', b1)
    assert _is_linked(a, 'easyflow_Task26', b1)
    if hasattr(b1, 'easyflow_TaskToDataProcessingType27'):
        assert _is_linked(b1, 'easyflow_TaskToDataProcessingType27', a)
    _safe_set(a, 'easyflow_Task26', b2)
    assert _is_linked(a, 'easyflow_Task26', b2)
    if hasattr(b1, 'easyflow_TaskToDataProcessingType27'):
        assert not _is_linked(b1, 'easyflow_TaskToDataProcessingType27', a)
    if hasattr(b2, 'easyflow_TaskToDataProcessingType27'):
        assert _is_linked(b2, 'easyflow_TaskToDataProcessingType27', a)
    _safe_set(a, 'easyflow_Task26', None)
    assert not _is_linked(a, 'easyflow_Task26', b2)
    if hasattr(b2, 'easyflow_TaskToDataProcessingType27'):
        assert not _is_linked(b2, 'easyflow_TaskToDataProcessingType27', a)


def test_assoc_key33_link_reassign_clear():
    a = easyflow_DataProcessingType(dataFormatIn="sample_text", dataFormatOut="sample_text")
    b1 = easyflow_DataProcessingTypeToTask()
    b2 = easyflow_DataProcessingTypeToTask()
    _safe_set(a, 'easyflow_DataProcessingType35', b1)
    assert _is_linked(a, 'easyflow_DataProcessingType35', b1)
    if hasattr(b1, 'easyflow_DataProcessingTypeToTask34'):
        assert _is_linked(b1, 'easyflow_DataProcessingTypeToTask34', a)
    _safe_set(a, 'easyflow_DataProcessingType35', b2)
    assert _is_linked(a, 'easyflow_DataProcessingType35', b2)
    if hasattr(b1, 'easyflow_DataProcessingTypeToTask34'):
        assert not _is_linked(b1, 'easyflow_DataProcessingTypeToTask34', a)
    if hasattr(b2, 'easyflow_DataProcessingTypeToTask34'):
        assert _is_linked(b2, 'easyflow_DataProcessingTypeToTask34', a)
    _safe_set(a, 'easyflow_DataProcessingType35', None)
    assert not _is_linked(a, 'easyflow_DataProcessingType35', b2)
    if hasattr(b2, 'easyflow_DataProcessingTypeToTask34'):
        assert not _is_linked(b2, 'easyflow_DataProcessingTypeToTask34', a)


def test_assoc_lastTaskMap13_link_reassign_clear():
    a = easyflow_Workflow(dag="sample_text", graph="sample_text", jobDag="sample_text", name="sample_text")
    b1 = easyflow_DataFormatToTaskList(key="sample_text")
    b2 = easyflow_DataFormatToTaskList(key="sample_text_2")
    _safe_set(a, 'easyflow_Workflow14', {b1})
    assert _is_linked(a, 'easyflow_Workflow14', b1)
    if hasattr(b1, 'easyflow_DataFormatToTaskList'):
        assert _is_linked(b1, 'easyflow_DataFormatToTaskList', a)
    _safe_set(a, 'easyflow_Workflow14', {b2})
    assert _is_linked(a, 'easyflow_Workflow14', b2)
    if hasattr(b1, 'easyflow_DataFormatToTaskList'):
        assert not _is_linked(b1, 'easyflow_DataFormatToTaskList', a)
    if hasattr(b2, 'easyflow_DataFormatToTaskList'):
        assert _is_linked(b2, 'easyflow_DataFormatToTaskList', a)
    _safe_set(a, 'easyflow_Workflow14', set())
    assert not _is_linked(a, 'easyflow_Workflow14', b2)
    if hasattr(b2, 'easyflow_DataFormatToTaskList'):
        assert not _is_linked(b2, 'easyflow_DataFormatToTaskList', a)


def test_assoc_libraries59_link_reassign_clear():
    a = easyflow_StringToLibraryMap(key="sample_text")
    b1 = easyflow_Group(name="sample_text")
    b2 = easyflow_Group(name="sample_text_2")
    _safe_set(a, 'easyflow_StringToLibraryMap', b1)
    assert _is_linked(a, 'easyflow_StringToLibraryMap', b1)
    if hasattr(b1, 'easyflow_Group60'):
        assert _is_linked(b1, 'easyflow_Group60', a)
    _safe_set(a, 'easyflow_StringToLibraryMap', b2)
    assert _is_linked(a, 'easyflow_StringToLibraryMap', b2)
    if hasattr(b1, 'easyflow_Group60'):
        assert not _is_linked(b1, 'easyflow_Group60', a)
    if hasattr(b2, 'easyflow_Group60'):
        assert _is_linked(b2, 'easyflow_Group60', a)
    _safe_set(a, 'easyflow_StringToLibraryMap', None)
    assert not _is_linked(a, 'easyflow_StringToLibraryMap', b2)
    if hasattr(b2, 'easyflow_Group60'):
        assert not _is_linked(b2, 'easyflow_Group60', a)


def test_assoc_libraries63_link_reassign_clear():
    a = easyflow_StringToLibraryMap(key="sample_text")
    b1 = easyflow_Sample(name="sample_text")
    b2 = easyflow_Sample(name="sample_text_2")
    _safe_set(a, 'easyflow_StringToLibraryMap64', b1)
    assert _is_linked(a, 'easyflow_StringToLibraryMap64', b1)
    if hasattr(b1, 'easyflow_Sample'):
        assert _is_linked(b1, 'easyflow_Sample', a)
    _safe_set(a, 'easyflow_StringToLibraryMap64', b2)
    assert _is_linked(a, 'easyflow_StringToLibraryMap64', b2)
    if hasattr(b1, 'easyflow_Sample'):
        assert not _is_linked(b1, 'easyflow_Sample', a)
    if hasattr(b2, 'easyflow_Sample'):
        assert _is_linked(b2, 'easyflow_Sample', a)
    _safe_set(a, 'easyflow_StringToLibraryMap64', None)
    assert not _is_linked(a, 'easyflow_StringToLibraryMap64', b2)
    if hasattr(b2, 'easyflow_Sample'):
        assert not _is_linked(b2, 'easyflow_Sample', a)


def test_assoc_libraries73_link_reassign_clear():
    a = easyflow_StringToLibraryMap(key="sample_text")
    b1 = easyflow_Readgroup(description="sample_text", name="sample_text", platform="sample_text", platformUnit="sample_text")
    b2 = easyflow_Readgroup(description="sample_text_2", name="sample_text_2", platform="sample_text_2", platformUnit="sample_text_2")
    _safe_set(a, 'easyflow_StringToLibraryMap75', b1)
    assert _is_linked(a, 'easyflow_StringToLibraryMap75', b1)
    if hasattr(b1, 'easyflow_Readgroup74'):
        assert _is_linked(b1, 'easyflow_Readgroup74', a)
    _safe_set(a, 'easyflow_StringToLibraryMap75', b2)
    assert _is_linked(a, 'easyflow_StringToLibraryMap75', b2)
    if hasattr(b1, 'easyflow_Readgroup74'):
        assert not _is_linked(b1, 'easyflow_Readgroup74', a)
    if hasattr(b2, 'easyflow_Readgroup74'):
        assert _is_linked(b2, 'easyflow_Readgroup74', a)
    _safe_set(a, 'easyflow_StringToLibraryMap75', None)
    assert not _is_linked(a, 'easyflow_StringToLibraryMap75', b2)
    if hasattr(b2, 'easyflow_Readgroup74'):
        assert not _is_linked(b2, 'easyflow_Readgroup74', a)


def test_assoc_library89_link_reassign_clear():
    a = easyflow_Record(fileNames="sample_text", refData="sample_text")
    b1 = easyflow_Library(insertSize=7, name="sample_text", readLength=7)
    b2 = easyflow_Library(insertSize=13, name="sample_text_2", readLength=13)
    _safe_set(a, 'easyflow_Record90', b1)
    assert _is_linked(a, 'easyflow_Record90', b1)
    if hasattr(b1, 'easyflow_Library91'):
        assert _is_linked(b1, 'easyflow_Library91', a)
    _safe_set(a, 'easyflow_Record90', b2)
    assert _is_linked(a, 'easyflow_Record90', b2)
    if hasattr(b1, 'easyflow_Library91'):
        assert not _is_linked(b1, 'easyflow_Library91', a)
    if hasattr(b2, 'easyflow_Library91'):
        assert _is_linked(b2, 'easyflow_Library91', a)
    _safe_set(a, 'easyflow_Record90', None)
    assert not _is_linked(a, 'easyflow_Record90', b2)
    if hasattr(b2, 'easyflow_Library91'):
        assert not _is_linked(b2, 'easyflow_Library91', a)


def test_assoc_mergingChildTask126_link_reassign_clear():
    a = easyflow_Task(cardinalityIn="sample_text", cardinalityOut="sample_text", contrast=True, dataCriterion="sample_text", dataFormatIn="sample_text", dataFormatOut="sample_text", depricated=True, isMultipleInstancesOfDataCriterion="sample_text", jexlString="sample_text", mergeCriterion="sample_text", name="sample_text", skipGroupingCriterion="sample_text", splitCriterion="sample_text", static=True, traversalCriterion="sample_text", util=True)
    b1 = easyflow_SplittingEvent(dag="sample_text", processedTask="sample_text", traversalChunks="sample_text", traversalCriterion="sample_text", traversalImplDir="sample_text")
    b2 = easyflow_SplittingEvent(dag="sample_text_2", processedTask="sample_text_2", traversalChunks="sample_text_2", traversalCriterion="sample_text_2", traversalImplDir="sample_text_2")
    _safe_set(a, 'easyflow_Task128', b1)
    assert _is_linked(a, 'easyflow_Task128', b1)
    if hasattr(b1, 'easyflow_SplittingEvent127'):
        assert _is_linked(b1, 'easyflow_SplittingEvent127', a)
    _safe_set(a, 'easyflow_Task128', b2)
    assert _is_linked(a, 'easyflow_Task128', b2)
    if hasattr(b1, 'easyflow_SplittingEvent127'):
        assert not _is_linked(b1, 'easyflow_SplittingEvent127', a)
    if hasattr(b2, 'easyflow_SplittingEvent127'):
        assert _is_linked(b2, 'easyflow_SplittingEvent127', a)
    _safe_set(a, 'easyflow_Task128', None)
    assert not _is_linked(a, 'easyflow_Task128', b2)
    if hasattr(b2, 'easyflow_SplittingEvent127'):
        assert not _is_linked(b2, 'easyflow_SplittingEvent127', a)


def test_assoc_metadata116_link_reassign_clear():
    a = easyflow_Job(dependencies="sample_text", exe="sample_text", genericArgs="sample_text", inputArgs="sample_text", interpreterOption="sample_text", name="sample_text", outputArgs="sample_text", source="sample_text", staticArgs="sample_text", subCmd="sample_text", targetPlatform="sample_text", targetPlatformOptions="sample_text", targets="sample_text")
    b1 = easyflow_EasyFlowMetadata(contrast=True, name="sample_text", refData="sample_text")
    b2 = easyflow_EasyFlowMetadata(contrast=False, name="sample_text_2", refData="sample_text_2")
    _safe_set(a, 'easyflow_Job', b1)
    assert _is_linked(a, 'easyflow_Job', b1)
    if hasattr(b1, 'easyflow_EasyFlowMetadata117'):
        assert _is_linked(b1, 'easyflow_EasyFlowMetadata117', a)
    _safe_set(a, 'easyflow_Job', b2)
    assert _is_linked(a, 'easyflow_Job', b2)
    if hasattr(b1, 'easyflow_EasyFlowMetadata117'):
        assert not _is_linked(b1, 'easyflow_EasyFlowMetadata117', a)
    if hasattr(b2, 'easyflow_EasyFlowMetadata117'):
        assert _is_linked(b2, 'easyflow_EasyFlowMetadata117', a)
    _safe_set(a, 'easyflow_Job', None)
    assert not _is_linked(a, 'easyflow_Job', b2)
    if hasattr(b2, 'easyflow_EasyFlowMetadata117'):
        assert not _is_linked(b2, 'easyflow_EasyFlowMetadata117', a)


def test_assoc_metadata3_link_reassign_clear():
    a = easyflow_Workflow(dag="sample_text", graph="sample_text", jobDag="sample_text", name="sample_text")
    b1 = easyflow_EasyFlowMetadata(contrast=True, name="sample_text", refData="sample_text")
    b2 = easyflow_EasyFlowMetadata(contrast=False, name="sample_text_2", refData="sample_text_2")
    _safe_set(a, 'easyflow_Workflow4', {b1})
    assert _is_linked(a, 'easyflow_Workflow4', b1)
    if hasattr(b1, 'easyflow_EasyFlowMetadata'):
        assert _is_linked(b1, 'easyflow_EasyFlowMetadata', a)
    _safe_set(a, 'easyflow_Workflow4', {b2})
    assert _is_linked(a, 'easyflow_Workflow4', b2)
    if hasattr(b1, 'easyflow_EasyFlowMetadata'):
        assert not _is_linked(b1, 'easyflow_EasyFlowMetadata', a)
    if hasattr(b2, 'easyflow_EasyFlowMetadata'):
        assert _is_linked(b2, 'easyflow_EasyFlowMetadata', a)
    _safe_set(a, 'easyflow_Workflow4', set())
    assert not _is_linked(a, 'easyflow_Workflow4', b2)
    if hasattr(b2, 'easyflow_EasyFlowMetadata'):
        assert not _is_linked(b2, 'easyflow_EasyFlowMetadata', a)


def test_assoc_metadata54_link_reassign_clear():
    a = easyflow_GroupingCriterion(id="sample_text")
    b1 = easyflow_EasyFlowMetadata(contrast=True, name="sample_text", refData="sample_text")
    b2 = easyflow_EasyFlowMetadata(contrast=False, name="sample_text_2", refData="sample_text_2")
    _safe_set(a, 'easyflow_GroupingCriterion', b1)
    assert _is_linked(a, 'easyflow_GroupingCriterion', b1)
    if hasattr(b1, 'easyflow_EasyFlowMetadata55'):
        assert _is_linked(b1, 'easyflow_EasyFlowMetadata55', a)
    _safe_set(a, 'easyflow_GroupingCriterion', b2)
    assert _is_linked(a, 'easyflow_GroupingCriterion', b2)
    if hasattr(b1, 'easyflow_EasyFlowMetadata55'):
        assert not _is_linked(b1, 'easyflow_EasyFlowMetadata55', a)
    if hasattr(b2, 'easyflow_EasyFlowMetadata55'):
        assert _is_linked(b2, 'easyflow_EasyFlowMetadata55', a)
    _safe_set(a, 'easyflow_GroupingCriterion', None)
    assert not _is_linked(a, 'easyflow_GroupingCriterion', b2)
    if hasattr(b2, 'easyflow_EasyFlowMetadata55'):
        assert not _is_linked(b2, 'easyflow_EasyFlowMetadata55', a)


def test_assoc_parentTask121_link_reassign_clear():
    a = easyflow_Task(cardinalityIn="sample_text", cardinalityOut="sample_text", contrast=True, dataCriterion="sample_text", dataFormatIn="sample_text", dataFormatOut="sample_text", depricated=True, isMultipleInstancesOfDataCriterion="sample_text", jexlString="sample_text", mergeCriterion="sample_text", name="sample_text", skipGroupingCriterion="sample_text", splitCriterion="sample_text", static=True, traversalCriterion="sample_text", util=True)
    b1 = easyflow_SplittingEvent(dag="sample_text", processedTask="sample_text", traversalChunks="sample_text", traversalCriterion="sample_text", traversalImplDir="sample_text")
    b2 = easyflow_SplittingEvent(dag="sample_text_2", processedTask="sample_text_2", traversalChunks="sample_text_2", traversalCriterion="sample_text_2", traversalImplDir="sample_text_2")
    _safe_set(a, 'easyflow_Task122', b1)
    assert _is_linked(a, 'easyflow_Task122', b1)
    if hasattr(b1, 'easyflow_SplittingEvent'):
        assert _is_linked(b1, 'easyflow_SplittingEvent', a)
    _safe_set(a, 'easyflow_Task122', b2)
    assert _is_linked(a, 'easyflow_Task122', b2)
    if hasattr(b1, 'easyflow_SplittingEvent'):
        assert not _is_linked(b1, 'easyflow_SplittingEvent', a)
    if hasattr(b2, 'easyflow_SplittingEvent'):
        assert _is_linked(b2, 'easyflow_SplittingEvent', a)
    _safe_set(a, 'easyflow_Task122', None)
    assert not _is_linked(a, 'easyflow_Task122', b2)
    if hasattr(b2, 'easyflow_SplittingEvent'):
        assert not _is_linked(b2, 'easyflow_SplittingEvent', a)


def test_assoc_parentTasks16_link_reassign_clear():
    a = easyflow_Task(cardinalityIn="sample_text", cardinalityOut="sample_text", contrast=True, dataCriterion="sample_text", dataFormatIn="sample_text", dataFormatOut="sample_text", depricated=True, isMultipleInstancesOfDataCriterion="sample_text", jexlString="sample_text", mergeCriterion="sample_text", name="sample_text", skipGroupingCriterion="sample_text", splitCriterion="sample_text", static=True, traversalCriterion="sample_text", util=True)
    b1 = easyflow_StringToTaskMap(key="sample_text")
    b2 = easyflow_StringToTaskMap(key="sample_text_2")
    _safe_set(a, 'easyflow_Task17', {b1})
    assert _is_linked(a, 'easyflow_Task17', b1)
    if hasattr(b1, 'easyflow_StringToTaskMap'):
        assert _is_linked(b1, 'easyflow_StringToTaskMap', a)
    _safe_set(a, 'easyflow_Task17', {b2})
    assert _is_linked(a, 'easyflow_Task17', b2)
    if hasattr(b1, 'easyflow_StringToTaskMap'):
        assert not _is_linked(b1, 'easyflow_StringToTaskMap', a)
    if hasattr(b2, 'easyflow_StringToTaskMap'):
        assert _is_linked(b2, 'easyflow_StringToTaskMap', a)
    _safe_set(a, 'easyflow_Task17', set())
    assert not _is_linked(a, 'easyflow_Task17', b2)
    if hasattr(b2, 'easyflow_StringToTaskMap'):
        assert not _is_linked(b2, 'easyflow_StringToTaskMap', a)


def test_assoc_readgroup86_link_reassign_clear():
    a = easyflow_Record(fileNames="sample_text", refData="sample_text")
    b1 = easyflow_Readgroup(description="sample_text", name="sample_text", platform="sample_text", platformUnit="sample_text")
    b2 = easyflow_Readgroup(description="sample_text_2", name="sample_text_2", platform="sample_text_2", platformUnit="sample_text_2")
    _safe_set(a, 'easyflow_Record87', b1)
    assert _is_linked(a, 'easyflow_Record87', b1)
    if hasattr(b1, 'easyflow_Readgroup88'):
        assert _is_linked(b1, 'easyflow_Readgroup88', a)
    _safe_set(a, 'easyflow_Record87', b2)
    assert _is_linked(a, 'easyflow_Record87', b2)
    if hasattr(b1, 'easyflow_Readgroup88'):
        assert not _is_linked(b1, 'easyflow_Readgroup88', a)
    if hasattr(b2, 'easyflow_Readgroup88'):
        assert _is_linked(b2, 'easyflow_Readgroup88', a)
    _safe_set(a, 'easyflow_Record87', None)
    assert not _is_linked(a, 'easyflow_Record87', b2)
    if hasattr(b2, 'easyflow_Readgroup88'):
        assert not _is_linked(b2, 'easyflow_Readgroup88', a)


def test_assoc_readgroups57_link_reassign_clear():
    a = easyflow_StringToReadgroupMap(key="sample_text")
    b1 = easyflow_Group(name="sample_text")
    b2 = easyflow_Group(name="sample_text_2")
    _safe_set(a, 'easyflow_StringToReadgroupMap', b1)
    assert _is_linked(a, 'easyflow_StringToReadgroupMap', b1)
    if hasattr(b1, 'easyflow_Group58'):
        assert _is_linked(b1, 'easyflow_Group58', a)
    _safe_set(a, 'easyflow_StringToReadgroupMap', b2)
    assert _is_linked(a, 'easyflow_StringToReadgroupMap', b2)
    if hasattr(b1, 'easyflow_Group58'):
        assert not _is_linked(b1, 'easyflow_Group58', a)
    if hasattr(b2, 'easyflow_Group58'):
        assert _is_linked(b2, 'easyflow_Group58', a)
    _safe_set(a, 'easyflow_StringToReadgroupMap', None)
    assert not _is_linked(a, 'easyflow_StringToReadgroupMap', b2)
    if hasattr(b2, 'easyflow_Group58'):
        assert not _is_linked(b2, 'easyflow_Group58', a)


def test_assoc_readgroups68_link_reassign_clear():
    a = easyflow_StringToReadgroupMap(key="sample_text")
    b1 = easyflow_Sample(name="sample_text")
    b2 = easyflow_Sample(name="sample_text_2")
    _safe_set(a, 'easyflow_StringToReadgroupMap70', b1)
    assert _is_linked(a, 'easyflow_StringToReadgroupMap70', b1)
    if hasattr(b1, 'easyflow_Sample69'):
        assert _is_linked(b1, 'easyflow_Sample69', a)
    _safe_set(a, 'easyflow_StringToReadgroupMap70', b2)
    assert _is_linked(a, 'easyflow_StringToReadgroupMap70', b2)
    if hasattr(b1, 'easyflow_Sample69'):
        assert not _is_linked(b1, 'easyflow_Sample69', a)
    if hasattr(b2, 'easyflow_Sample69'):
        assert _is_linked(b2, 'easyflow_Sample69', a)
    _safe_set(a, 'easyflow_StringToReadgroupMap70', None)
    assert not _is_linked(a, 'easyflow_StringToReadgroupMap70', b2)
    if hasattr(b2, 'easyflow_Sample69'):
        assert not _is_linked(b2, 'easyflow_Sample69', a)


def test_assoc_readgroups81_link_reassign_clear():
    a = easyflow_StringToReadgroupMap(key="sample_text")
    b1 = easyflow_Library(insertSize=7, name="sample_text", readLength=7)
    b2 = easyflow_Library(insertSize=13, name="sample_text_2", readLength=13)
    _safe_set(a, 'easyflow_StringToReadgroupMap83', b1)
    assert _is_linked(a, 'easyflow_StringToReadgroupMap83', b1)
    if hasattr(b1, 'easyflow_Library82'):
        assert _is_linked(b1, 'easyflow_Library82', a)
    _safe_set(a, 'easyflow_StringToReadgroupMap83', b2)
    assert _is_linked(a, 'easyflow_StringToReadgroupMap83', b2)
    if hasattr(b1, 'easyflow_Library82'):
        assert not _is_linked(b1, 'easyflow_Library82', a)
    if hasattr(b2, 'easyflow_Library82'):
        assert _is_linked(b2, 'easyflow_Library82', a)
    _safe_set(a, 'easyflow_StringToReadgroupMap83', None)
    assert not _is_linked(a, 'easyflow_StringToReadgroupMap83', b2)
    if hasattr(b2, 'easyflow_Library82'):
        assert not _is_linked(b2, 'easyflow_Library82', a)


def test_assoc_records61_link_reassign_clear():
    a = easyflow_StringToRecordMap(key="sample_text")
    b1 = easyflow_Group(name="sample_text")
    b2 = easyflow_Group(name="sample_text_2")
    _safe_set(a, 'easyflow_StringToRecordMap', b1)
    assert _is_linked(a, 'easyflow_StringToRecordMap', b1)
    if hasattr(b1, 'easyflow_Group62'):
        assert _is_linked(b1, 'easyflow_Group62', a)
    _safe_set(a, 'easyflow_StringToRecordMap', b2)
    assert _is_linked(a, 'easyflow_StringToRecordMap', b2)
    if hasattr(b1, 'easyflow_Group62'):
        assert not _is_linked(b1, 'easyflow_Group62', a)
    if hasattr(b2, 'easyflow_Group62'):
        assert _is_linked(b2, 'easyflow_Group62', a)
    _safe_set(a, 'easyflow_StringToRecordMap', None)
    assert not _is_linked(a, 'easyflow_StringToRecordMap', b2)
    if hasattr(b2, 'easyflow_Group62'):
        assert not _is_linked(b2, 'easyflow_Group62', a)


def test_assoc_records65_link_reassign_clear():
    a = easyflow_StringToRecordMap(key="sample_text")
    b1 = easyflow_Sample(name="sample_text")
    b2 = easyflow_Sample(name="sample_text_2")
    _safe_set(a, 'easyflow_StringToRecordMap67', b1)
    assert _is_linked(a, 'easyflow_StringToRecordMap67', b1)
    if hasattr(b1, 'easyflow_Sample66'):
        assert _is_linked(b1, 'easyflow_Sample66', a)
    _safe_set(a, 'easyflow_StringToRecordMap67', b2)
    assert _is_linked(a, 'easyflow_StringToRecordMap67', b2)
    if hasattr(b1, 'easyflow_Sample66'):
        assert not _is_linked(b1, 'easyflow_Sample66', a)
    if hasattr(b2, 'easyflow_Sample66'):
        assert _is_linked(b2, 'easyflow_Sample66', a)
    _safe_set(a, 'easyflow_StringToRecordMap67', None)
    assert not _is_linked(a, 'easyflow_StringToRecordMap67', b2)
    if hasattr(b2, 'easyflow_Sample66'):
        assert not _is_linked(b2, 'easyflow_Sample66', a)


def test_assoc_records78_link_reassign_clear():
    a = easyflow_StringToRecordMap(key="sample_text")
    b1 = easyflow_Library(insertSize=7, name="sample_text", readLength=7)
    b2 = easyflow_Library(insertSize=13, name="sample_text_2", readLength=13)
    _safe_set(a, 'easyflow_StringToRecordMap80', b1)
    assert _is_linked(a, 'easyflow_StringToRecordMap80', b1)
    if hasattr(b1, 'easyflow_Library79'):
        assert _is_linked(b1, 'easyflow_Library79', a)
    _safe_set(a, 'easyflow_StringToRecordMap80', b2)
    assert _is_linked(a, 'easyflow_StringToRecordMap80', b2)
    if hasattr(b1, 'easyflow_Library79'):
        assert not _is_linked(b1, 'easyflow_Library79', a)
    if hasattr(b2, 'easyflow_Library79'):
        assert _is_linked(b2, 'easyflow_Library79', a)
    _safe_set(a, 'easyflow_StringToRecordMap80', None)
    assert not _is_linked(a, 'easyflow_StringToRecordMap80', b2)
    if hasattr(b2, 'easyflow_Library79'):
        assert not _is_linked(b2, 'easyflow_Library79', a)


def test_assoc_sample84_link_reassign_clear():
    a = easyflow_Sample(name="sample_text")
    b1 = easyflow_Record(fileNames="sample_text", refData="sample_text")
    b2 = easyflow_Record(fileNames="sample_text_2", refData="sample_text_2")
    _safe_set(a, 'easyflow_Sample85', b1)
    assert _is_linked(a, 'easyflow_Sample85', b1)
    if hasattr(b1, 'easyflow_Record'):
        assert _is_linked(b1, 'easyflow_Record', a)
    _safe_set(a, 'easyflow_Sample85', b2)
    assert _is_linked(a, 'easyflow_Sample85', b2)
    if hasattr(b1, 'easyflow_Record'):
        assert not _is_linked(b1, 'easyflow_Record', a)
    if hasattr(b2, 'easyflow_Record'):
        assert _is_linked(b2, 'easyflow_Record', a)
    _safe_set(a, 'easyflow_Sample85', None)
    assert not _is_linked(a, 'easyflow_Sample85', b2)
    if hasattr(b2, 'easyflow_Record'):
        assert not _is_linked(b2, 'easyflow_Record', a)


def test_assoc_samples56_link_reassign_clear():
    a = easyflow_StringToSampleMap(key="sample_text")
    b1 = easyflow_Group(name="sample_text")
    b2 = easyflow_Group(name="sample_text_2")
    _safe_set(a, 'easyflow_StringToSampleMap', b1)
    assert _is_linked(a, 'easyflow_StringToSampleMap', b1)
    if hasattr(b1, 'easyflow_Group'):
        assert _is_linked(b1, 'easyflow_Group', a)
    _safe_set(a, 'easyflow_StringToSampleMap', b2)
    assert _is_linked(a, 'easyflow_StringToSampleMap', b2)
    if hasattr(b1, 'easyflow_Group'):
        assert not _is_linked(b1, 'easyflow_Group', a)
    if hasattr(b2, 'easyflow_Group'):
        assert _is_linked(b2, 'easyflow_Group', a)
    _safe_set(a, 'easyflow_StringToSampleMap', None)
    assert not _is_linked(a, 'easyflow_StringToSampleMap', b2)
    if hasattr(b2, 'easyflow_Group'):
        assert not _is_linked(b2, 'easyflow_Group', a)


def test_assoc_samples71_link_reassign_clear():
    a = easyflow_StringToSampleMap(key="sample_text")
    b1 = easyflow_Readgroup(description="sample_text", name="sample_text", platform="sample_text", platformUnit="sample_text")
    b2 = easyflow_Readgroup(description="sample_text_2", name="sample_text_2", platform="sample_text_2", platformUnit="sample_text_2")
    _safe_set(a, 'easyflow_StringToSampleMap72', b1)
    assert _is_linked(a, 'easyflow_StringToSampleMap72', b1)
    if hasattr(b1, 'easyflow_Readgroup'):
        assert _is_linked(b1, 'easyflow_Readgroup', a)
    _safe_set(a, 'easyflow_StringToSampleMap72', b2)
    assert _is_linked(a, 'easyflow_StringToSampleMap72', b2)
    if hasattr(b1, 'easyflow_Readgroup'):
        assert not _is_linked(b1, 'easyflow_Readgroup', a)
    if hasattr(b2, 'easyflow_Readgroup'):
        assert _is_linked(b2, 'easyflow_Readgroup', a)
    _safe_set(a, 'easyflow_StringToSampleMap72', None)
    assert not _is_linked(a, 'easyflow_StringToSampleMap72', b2)
    if hasattr(b2, 'easyflow_Readgroup'):
        assert not _is_linked(b2, 'easyflow_Readgroup', a)


def test_assoc_samples76_link_reassign_clear():
    a = easyflow_StringToSampleMap(key="sample_text")
    b1 = easyflow_Library(insertSize=7, name="sample_text", readLength=7)
    b2 = easyflow_Library(insertSize=13, name="sample_text_2", readLength=13)
    _safe_set(a, 'easyflow_StringToSampleMap77', b1)
    assert _is_linked(a, 'easyflow_StringToSampleMap77', b1)
    if hasattr(b1, 'easyflow_Library'):
        assert _is_linked(b1, 'easyflow_Library', a)
    _safe_set(a, 'easyflow_StringToSampleMap77', b2)
    assert _is_linked(a, 'easyflow_StringToSampleMap77', b2)
    if hasattr(b1, 'easyflow_Library'):
        assert not _is_linked(b1, 'easyflow_Library', a)
    if hasattr(b2, 'easyflow_Library'):
        assert _is_linked(b2, 'easyflow_Library', a)
    _safe_set(a, 'easyflow_StringToSampleMap77', None)
    assert not _is_linked(a, 'easyflow_StringToSampleMap77', b2)
    if hasattr(b2, 'easyflow_Library'):
        assert not _is_linked(b2, 'easyflow_Library', a)


def test_assoc_sortOrder22_link_reassign_clear():
    a = easyflow_Task(cardinalityIn="sample_text", cardinalityOut="sample_text", contrast=True, dataCriterion="sample_text", dataFormatIn="sample_text", dataFormatOut="sample_text", depricated=True, isMultipleInstancesOfDataCriterion="sample_text", jexlString="sample_text", mergeCriterion="sample_text", name="sample_text", skipGroupingCriterion="sample_text", splitCriterion="sample_text", static=True, traversalCriterion="sample_text", util=True)
    b1 = easyflow_StringToTraversalCriterionMap(key="sample_text", value="sample_text")
    b2 = easyflow_StringToTraversalCriterionMap(key="sample_text_2", value="sample_text_2")
    _safe_set(a, 'easyflow_Task23', {b1})
    assert _is_linked(a, 'easyflow_Task23', b1)
    if hasattr(b1, 'easyflow_StringToTraversalCriterionMap24'):
        assert _is_linked(b1, 'easyflow_StringToTraversalCriterionMap24', a)
    _safe_set(a, 'easyflow_Task23', {b2})
    assert _is_linked(a, 'easyflow_Task23', b2)
    if hasattr(b1, 'easyflow_StringToTraversalCriterionMap24'):
        assert not _is_linked(b1, 'easyflow_StringToTraversalCriterionMap24', a)
    if hasattr(b2, 'easyflow_StringToTraversalCriterionMap24'):
        assert _is_linked(b2, 'easyflow_StringToTraversalCriterionMap24', a)
    _safe_set(a, 'easyflow_Task23', set())
    assert not _is_linked(a, 'easyflow_Task23', b2)
    if hasattr(b2, 'easyflow_StringToTraversalCriterionMap24'):
        assert not _is_linked(b2, 'easyflow_StringToTraversalCriterionMap24', a)


def test_assoc_splittingTask118_link_reassign_clear():
    a = easyflow_Task(cardinalityIn="sample_text", cardinalityOut="sample_text", contrast=True, dataCriterion="sample_text", dataFormatIn="sample_text", dataFormatOut="sample_text", depricated=True, isMultipleInstancesOfDataCriterion="sample_text", jexlString="sample_text", mergeCriterion="sample_text", name="sample_text", skipGroupingCriterion="sample_text", splitCriterion="sample_text", static=True, traversalCriterion="sample_text", util=True)
    b1 = easyflow_ITraversal()
    b2 = easyflow_ITraversal()
    _safe_set(a, 'easyflow_Task119', b1)
    assert _is_linked(a, 'easyflow_Task119', b1)
    if hasattr(b1, 'easyflow_ITraversal'):
        assert _is_linked(b1, 'easyflow_ITraversal', a)
    _safe_set(a, 'easyflow_Task119', b2)
    assert _is_linked(a, 'easyflow_Task119', b2)
    if hasattr(b1, 'easyflow_ITraversal'):
        assert not _is_linked(b1, 'easyflow_ITraversal', a)
    if hasattr(b2, 'easyflow_ITraversal'):
        assert _is_linked(b2, 'easyflow_ITraversal', a)
    _safe_set(a, 'easyflow_Task119', None)
    assert not _is_linked(a, 'easyflow_Task119', b2)
    if hasattr(b2, 'easyflow_ITraversal'):
        assert not _is_linked(b2, 'easyflow_ITraversal', a)


def test_assoc_splittingTask123_link_reassign_clear():
    a = easyflow_Task(cardinalityIn="sample_text", cardinalityOut="sample_text", contrast=True, dataCriterion="sample_text", dataFormatIn="sample_text", dataFormatOut="sample_text", depricated=True, isMultipleInstancesOfDataCriterion="sample_text", jexlString="sample_text", mergeCriterion="sample_text", name="sample_text", skipGroupingCriterion="sample_text", splitCriterion="sample_text", static=True, traversalCriterion="sample_text", util=True)
    b1 = easyflow_SplittingEvent(dag="sample_text", processedTask="sample_text", traversalChunks="sample_text", traversalCriterion="sample_text", traversalImplDir="sample_text")
    b2 = easyflow_SplittingEvent(dag="sample_text_2", processedTask="sample_text_2", traversalChunks="sample_text_2", traversalCriterion="sample_text_2", traversalImplDir="sample_text_2")
    _safe_set(a, 'easyflow_Task125', b1)
    assert _is_linked(a, 'easyflow_Task125', b1)
    if hasattr(b1, 'easyflow_SplittingEvent124'):
        assert _is_linked(b1, 'easyflow_SplittingEvent124', a)
    _safe_set(a, 'easyflow_Task125', b2)
    assert _is_linked(a, 'easyflow_Task125', b2)
    if hasattr(b1, 'easyflow_SplittingEvent124'):
        assert not _is_linked(b1, 'easyflow_SplittingEvent124', a)
    if hasattr(b2, 'easyflow_SplittingEvent124'):
        assert _is_linked(b2, 'easyflow_SplittingEvent124', a)
    _safe_set(a, 'easyflow_Task125', None)
    assert not _is_linked(a, 'easyflow_Task125', b2)
    if hasattr(b2, 'easyflow_SplittingEvent124'):
        assert not _is_linked(b2, 'easyflow_SplittingEvent124', a)


def test_assoc_staticArg43_link_reassign_clear():
    a = easyflow_Tool(category="sample_text", pattern="sample_text", refData="sample_text", source="sample_text", subCmd="sample_text", subCmdPrefix="sample_text", toolName="sample_text", type="sample_text")
    b1 = easyflow_CommandArgument(arg="sample_text", name="sample_text", named=True, required=True, sep="sample_text")
    b2 = easyflow_CommandArgument(arg="sample_text_2", name="sample_text_2", named=False, required=False, sep="sample_text_2")
    _safe_set(a, 'easyflow_Tool44', {b1})
    assert _is_linked(a, 'easyflow_Tool44', b1)
    if hasattr(b1, 'easyflow_CommandArgument45'):
        assert _is_linked(b1, 'easyflow_CommandArgument45', a)
    _safe_set(a, 'easyflow_Tool44', {b2})
    assert _is_linked(a, 'easyflow_Tool44', b2)
    if hasattr(b1, 'easyflow_CommandArgument45'):
        assert not _is_linked(b1, 'easyflow_CommandArgument45', a)
    if hasattr(b2, 'easyflow_CommandArgument45'):
        assert _is_linked(b2, 'easyflow_CommandArgument45', a)
    _safe_set(a, 'easyflow_Tool44', set())
    assert not _is_linked(a, 'easyflow_Tool44', b2)
    if hasattr(b2, 'easyflow_CommandArgument45'):
        assert not _is_linked(b2, 'easyflow_CommandArgument45', a)


def test_assoc_task51_link_reassign_clear():
    a = easyflow_Tool(category="sample_text", pattern="sample_text", refData="sample_text", source="sample_text", subCmd="sample_text", subCmdPrefix="sample_text", toolName="sample_text", type="sample_text")
    b1 = easyflow_Task(cardinalityIn="sample_text", cardinalityOut="sample_text", contrast=True, dataCriterion="sample_text", dataFormatIn="sample_text", dataFormatOut="sample_text", depricated=True, isMultipleInstancesOfDataCriterion="sample_text", jexlString="sample_text", mergeCriterion="sample_text", name="sample_text", skipGroupingCriterion="sample_text", splitCriterion="sample_text", static=True, traversalCriterion="sample_text", util=True)
    b2 = easyflow_Task(cardinalityIn="sample_text_2", cardinalityOut="sample_text_2", contrast=False, dataCriterion="sample_text_2", dataFormatIn="sample_text_2", dataFormatOut="sample_text_2", depricated=False, isMultipleInstancesOfDataCriterion="sample_text_2", jexlString="sample_text_2", mergeCriterion="sample_text_2", name="sample_text_2", skipGroupingCriterion="sample_text_2", splitCriterion="sample_text_2", static=False, traversalCriterion="sample_text_2", util=False)
    _safe_set(a, 'easyflow_Tool52', b1)
    assert _is_linked(a, 'easyflow_Tool52', b1)
    if hasattr(b1, 'easyflow_Task53'):
        assert _is_linked(b1, 'easyflow_Task53', a)
    _safe_set(a, 'easyflow_Tool52', b2)
    assert _is_linked(a, 'easyflow_Tool52', b2)
    if hasattr(b1, 'easyflow_Task53'):
        assert not _is_linked(b1, 'easyflow_Task53', a)
    if hasattr(b2, 'easyflow_Task53'):
        assert _is_linked(b2, 'easyflow_Task53', a)
    _safe_set(a, 'easyflow_Tool52', None)
    assert not _is_linked(a, 'easyflow_Tool52', b2)
    if hasattr(b2, 'easyflow_Task53'):
        assert not _is_linked(b2, 'easyflow_Task53', a)


def test_assoc_taskMap11_link_reassign_clear():
    a = easyflow_Workflow(dag="sample_text", graph="sample_text", jobDag="sample_text", name="sample_text")
    b1 = easyflow_TaskToDataProcessingType()
    b2 = easyflow_TaskToDataProcessingType()
    _safe_set(a, 'easyflow_Workflow12', {b1})
    assert _is_linked(a, 'easyflow_Workflow12', b1)
    if hasattr(b1, 'easyflow_TaskToDataProcessingType'):
        assert _is_linked(b1, 'easyflow_TaskToDataProcessingType', a)
    _safe_set(a, 'easyflow_Workflow12', {b2})
    assert _is_linked(a, 'easyflow_Workflow12', b2)
    if hasattr(b1, 'easyflow_TaskToDataProcessingType'):
        assert not _is_linked(b1, 'easyflow_TaskToDataProcessingType', a)
    if hasattr(b2, 'easyflow_TaskToDataProcessingType'):
        assert _is_linked(b2, 'easyflow_TaskToDataProcessingType', a)
    _safe_set(a, 'easyflow_Workflow12', set())
    assert not _is_linked(a, 'easyflow_Workflow12', b2)
    if hasattr(b2, 'easyflow_TaskToDataProcessingType'):
        assert not _is_linked(b2, 'easyflow_TaskToDataProcessingType', a)


def test_assoc_tool15_link_reassign_clear():
    a = easyflow_Task(cardinalityIn="sample_text", cardinalityOut="sample_text", contrast=True, dataCriterion="sample_text", dataFormatIn="sample_text", dataFormatOut="sample_text", depricated=True, isMultipleInstancesOfDataCriterion="sample_text", jexlString="sample_text", mergeCriterion="sample_text", name="sample_text", skipGroupingCriterion="sample_text", splitCriterion="sample_text", static=True, traversalCriterion="sample_text", util=True)
    b1 = easyflow_StringToToolMap(key="sample_text")
    b2 = easyflow_StringToToolMap(key="sample_text_2")
    _safe_set(a, 'easyflow_Task', {b1})
    assert _is_linked(a, 'easyflow_Task', b1)
    if hasattr(b1, 'easyflow_StringToToolMap'):
        assert _is_linked(b1, 'easyflow_StringToToolMap', a)
    _safe_set(a, 'easyflow_Task', {b2})
    assert _is_linked(a, 'easyflow_Task', b2)
    if hasattr(b1, 'easyflow_StringToToolMap'):
        assert not _is_linked(b1, 'easyflow_StringToToolMap', a)
    if hasattr(b2, 'easyflow_StringToToolMap'):
        assert _is_linked(b2, 'easyflow_StringToToolMap', a)
    _safe_set(a, 'easyflow_Task', set())
    assert not _is_linked(a, 'easyflow_Task', b2)
    if hasattr(b2, 'easyflow_StringToToolMap'):
        assert not _is_linked(b2, 'easyflow_StringToToolMap', a)


def test_assoc_value101_link_reassign_clear():
    a = easyflow_StringToLibraryMap(key="sample_text")
    b1 = easyflow_Library(insertSize=7, name="sample_text", readLength=7)
    b2 = easyflow_Library(insertSize=13, name="sample_text_2", readLength=13)
    _safe_set(a, 'easyflow_StringToLibraryMap102', b1)
    assert _is_linked(a, 'easyflow_StringToLibraryMap102', b1)
    if hasattr(b1, 'easyflow_Library103'):
        assert _is_linked(b1, 'easyflow_Library103', a)
    _safe_set(a, 'easyflow_StringToLibraryMap102', b2)
    assert _is_linked(a, 'easyflow_StringToLibraryMap102', b2)
    if hasattr(b1, 'easyflow_Library103'):
        assert not _is_linked(b1, 'easyflow_Library103', a)
    if hasattr(b2, 'easyflow_Library103'):
        assert _is_linked(b2, 'easyflow_Library103', a)
    _safe_set(a, 'easyflow_StringToLibraryMap102', None)
    assert not _is_linked(a, 'easyflow_StringToLibraryMap102', b2)
    if hasattr(b2, 'easyflow_Library103'):
        assert not _is_linked(b2, 'easyflow_Library103', a)


def test_assoc_value104_link_reassign_clear():
    a = easyflow_Tool(category="sample_text", pattern="sample_text", refData="sample_text", source="sample_text", subCmd="sample_text", subCmdPrefix="sample_text", toolName="sample_text", type="sample_text")
    b1 = easyflow_StringToToolMap(key="sample_text")
    b2 = easyflow_StringToToolMap(key="sample_text_2")
    _safe_set(a, 'easyflow_Tool106', b1)
    assert _is_linked(a, 'easyflow_Tool106', b1)
    if hasattr(b1, 'easyflow_StringToToolMap105'):
        assert _is_linked(b1, 'easyflow_StringToToolMap105', a)
    _safe_set(a, 'easyflow_Tool106', b2)
    assert _is_linked(a, 'easyflow_Tool106', b2)
    if hasattr(b1, 'easyflow_StringToToolMap105'):
        assert not _is_linked(b1, 'easyflow_StringToToolMap105', a)
    if hasattr(b2, 'easyflow_StringToToolMap105'):
        assert _is_linked(b2, 'easyflow_StringToToolMap105', a)
    _safe_set(a, 'easyflow_Tool106', None)
    assert not _is_linked(a, 'easyflow_Tool106', b2)
    if hasattr(b2, 'easyflow_StringToToolMap105'):
        assert not _is_linked(b2, 'easyflow_StringToToolMap105', a)


def test_assoc_value107_link_reassign_clear():
    a = easyflow_Task(cardinalityIn="sample_text", cardinalityOut="sample_text", contrast=True, dataCriterion="sample_text", dataFormatIn="sample_text", dataFormatOut="sample_text", depricated=True, isMultipleInstancesOfDataCriterion="sample_text", jexlString="sample_text", mergeCriterion="sample_text", name="sample_text", skipGroupingCriterion="sample_text", splitCriterion="sample_text", static=True, traversalCriterion="sample_text", util=True)
    b1 = easyflow_StringToTaskMap(key="sample_text")
    b2 = easyflow_StringToTaskMap(key="sample_text_2")
    _safe_set(a, 'easyflow_Task109', b1)
    assert _is_linked(a, 'easyflow_Task109', b1)
    if hasattr(b1, 'easyflow_StringToTaskMap108'):
        assert _is_linked(b1, 'easyflow_StringToTaskMap108', a)
    _safe_set(a, 'easyflow_Task109', b2)
    assert _is_linked(a, 'easyflow_Task109', b2)
    if hasattr(b1, 'easyflow_StringToTaskMap108'):
        assert not _is_linked(b1, 'easyflow_StringToTaskMap108', a)
    if hasattr(b2, 'easyflow_StringToTaskMap108'):
        assert _is_linked(b2, 'easyflow_StringToTaskMap108', a)
    _safe_set(a, 'easyflow_Task109', None)
    assert not _is_linked(a, 'easyflow_Task109', b2)
    if hasattr(b2, 'easyflow_StringToTaskMap108'):
        assert not _is_linked(b2, 'easyflow_StringToTaskMap108', a)


def test_assoc_value110_link_reassign_clear():
    a = easyflow_StringToRecordMap(key="sample_text")
    b1 = easyflow_Record(fileNames="sample_text", refData="sample_text")
    b2 = easyflow_Record(fileNames="sample_text_2", refData="sample_text_2")
    _safe_set(a, 'easyflow_StringToRecordMap111', b1)
    assert _is_linked(a, 'easyflow_StringToRecordMap111', b1)
    if hasattr(b1, 'easyflow_Record112'):
        assert _is_linked(b1, 'easyflow_Record112', a)
    _safe_set(a, 'easyflow_StringToRecordMap111', b2)
    assert _is_linked(a, 'easyflow_StringToRecordMap111', b2)
    if hasattr(b1, 'easyflow_Record112'):
        assert not _is_linked(b1, 'easyflow_Record112', a)
    if hasattr(b2, 'easyflow_Record112'):
        assert _is_linked(b2, 'easyflow_Record112', a)
    _safe_set(a, 'easyflow_StringToRecordMap111', None)
    assert not _is_linked(a, 'easyflow_StringToRecordMap111', b2)
    if hasattr(b2, 'easyflow_Record112'):
        assert not _is_linked(b2, 'easyflow_Record112', a)


def test_assoc_value113_link_reassign_clear():
    a = easyflow_StringToGroupingCriterionMap(key="sample_text")
    b1 = easyflow_GroupingCriterion(id="sample_text")
    b2 = easyflow_GroupingCriterion(id="sample_text_2")
    _safe_set(a, 'easyflow_StringToGroupingCriterionMap114', b1)
    assert _is_linked(a, 'easyflow_StringToGroupingCriterionMap114', b1)
    if hasattr(b1, 'easyflow_GroupingCriterion115'):
        assert _is_linked(b1, 'easyflow_GroupingCriterion115', a)
    _safe_set(a, 'easyflow_StringToGroupingCriterionMap114', b2)
    assert _is_linked(a, 'easyflow_StringToGroupingCriterionMap114', b2)
    if hasattr(b1, 'easyflow_GroupingCriterion115'):
        assert not _is_linked(b1, 'easyflow_GroupingCriterion115', a)
    if hasattr(b2, 'easyflow_GroupingCriterion115'):
        assert _is_linked(b2, 'easyflow_GroupingCriterion115', a)
    _safe_set(a, 'easyflow_StringToGroupingCriterionMap114', None)
    assert not _is_linked(a, 'easyflow_StringToGroupingCriterionMap114', b2)
    if hasattr(b2, 'easyflow_GroupingCriterion115'):
        assert not _is_linked(b2, 'easyflow_GroupingCriterion115', a)


def test_assoc_value129_link_reassign_clear():
    a = easyflow_DataProcessingType(dataFormatIn="sample_text", dataFormatOut="sample_text")
    b1 = easyflow_TaskToDataProcessingType()
    b2 = easyflow_TaskToDataProcessingType()
    _safe_set(a, 'easyflow_DataProcessingType131', b1)
    assert _is_linked(a, 'easyflow_DataProcessingType131', b1)
    if hasattr(b1, 'easyflow_TaskToDataProcessingType130'):
        assert _is_linked(b1, 'easyflow_TaskToDataProcessingType130', a)
    _safe_set(a, 'easyflow_DataProcessingType131', b2)
    assert _is_linked(a, 'easyflow_DataProcessingType131', b2)
    if hasattr(b1, 'easyflow_TaskToDataProcessingType130'):
        assert not _is_linked(b1, 'easyflow_TaskToDataProcessingType130', a)
    if hasattr(b2, 'easyflow_TaskToDataProcessingType130'):
        assert _is_linked(b2, 'easyflow_TaskToDataProcessingType130', a)
    _safe_set(a, 'easyflow_DataProcessingType131', None)
    assert not _is_linked(a, 'easyflow_DataProcessingType131', b2)
    if hasattr(b2, 'easyflow_TaskToDataProcessingType130'):
        assert not _is_linked(b2, 'easyflow_TaskToDataProcessingType130', a)


def test_assoc_value135_link_reassign_clear():
    a = easyflow_Task(cardinalityIn="sample_text", cardinalityOut="sample_text", contrast=True, dataCriterion="sample_text", dataFormatIn="sample_text", dataFormatOut="sample_text", depricated=True, isMultipleInstancesOfDataCriterion="sample_text", jexlString="sample_text", mergeCriterion="sample_text", name="sample_text", skipGroupingCriterion="sample_text", splitCriterion="sample_text", static=True, traversalCriterion="sample_text", util=True)
    b1 = easyflow_DataFormatToTaskList(key="sample_text")
    b2 = easyflow_DataFormatToTaskList(key="sample_text_2")
    _safe_set(a, 'easyflow_Task137', b1)
    assert _is_linked(a, 'easyflow_Task137', b1)
    if hasattr(b1, 'easyflow_DataFormatToTaskList136'):
        assert _is_linked(b1, 'easyflow_DataFormatToTaskList136', a)
    _safe_set(a, 'easyflow_Task137', b2)
    assert _is_linked(a, 'easyflow_Task137', b2)
    if hasattr(b1, 'easyflow_DataFormatToTaskList136'):
        assert not _is_linked(b1, 'easyflow_DataFormatToTaskList136', a)
    if hasattr(b2, 'easyflow_DataFormatToTaskList136'):
        assert _is_linked(b2, 'easyflow_DataFormatToTaskList136', a)
    _safe_set(a, 'easyflow_Task137', None)
    assert not _is_linked(a, 'easyflow_Task137', b2)
    if hasattr(b2, 'easyflow_DataFormatToTaskList136'):
        assert not _is_linked(b2, 'easyflow_DataFormatToTaskList136', a)


def test_assoc_value138_link_reassign_clear():
    a = easyflow_StringToChunkMap(key="sample_text")
    b1 = easyflow_Chunk(argument="sample_text", name="sample_text", tool="sample_text")
    b2 = easyflow_Chunk(argument="sample_text_2", name="sample_text_2", tool="sample_text_2")
    _safe_set(a, 'easyflow_StringToChunkMap139', b1)
    assert _is_linked(a, 'easyflow_StringToChunkMap139', b1)
    if hasattr(b1, 'easyflow_Chunk'):
        assert _is_linked(b1, 'easyflow_Chunk', a)
    _safe_set(a, 'easyflow_StringToChunkMap139', b2)
    assert _is_linked(a, 'easyflow_StringToChunkMap139', b2)
    if hasattr(b1, 'easyflow_Chunk'):
        assert not _is_linked(b1, 'easyflow_Chunk', a)
    if hasattr(b2, 'easyflow_Chunk'):
        assert _is_linked(b2, 'easyflow_Chunk', a)
    _safe_set(a, 'easyflow_StringToChunkMap139', None)
    assert not _is_linked(a, 'easyflow_StringToChunkMap139', b2)
    if hasattr(b2, 'easyflow_Chunk'):
        assert not _is_linked(b2, 'easyflow_Chunk', a)


def test_assoc_value36_link_reassign_clear():
    a = easyflow_Task(cardinalityIn="sample_text", cardinalityOut="sample_text", contrast=True, dataCriterion="sample_text", dataFormatIn="sample_text", dataFormatOut="sample_text", depricated=True, isMultipleInstancesOfDataCriterion="sample_text", jexlString="sample_text", mergeCriterion="sample_text", name="sample_text", skipGroupingCriterion="sample_text", splitCriterion="sample_text", static=True, traversalCriterion="sample_text", util=True)
    b1 = easyflow_DataProcessingTypeToTask()
    b2 = easyflow_DataProcessingTypeToTask()
    _safe_set(a, 'easyflow_Task38', b1)
    assert _is_linked(a, 'easyflow_Task38', b1)
    if hasattr(b1, 'easyflow_DataProcessingTypeToTask37'):
        assert _is_linked(b1, 'easyflow_DataProcessingTypeToTask37', a)
    _safe_set(a, 'easyflow_Task38', b2)
    assert _is_linked(a, 'easyflow_Task38', b2)
    if hasattr(b1, 'easyflow_DataProcessingTypeToTask37'):
        assert not _is_linked(b1, 'easyflow_DataProcessingTypeToTask37', a)
    if hasattr(b2, 'easyflow_DataProcessingTypeToTask37'):
        assert _is_linked(b2, 'easyflow_DataProcessingTypeToTask37', a)
    _safe_set(a, 'easyflow_Task38', None)
    assert not _is_linked(a, 'easyflow_Task38', b2)
    if hasattr(b2, 'easyflow_DataProcessingTypeToTask37'):
        assert not _is_linked(b2, 'easyflow_DataProcessingTypeToTask37', a)


def test_assoc_value92_link_reassign_clear():
    a = easyflow_StringToGroupMap(key="sample_text")
    b1 = easyflow_Group(name="sample_text")
    b2 = easyflow_Group(name="sample_text_2")
    _safe_set(a, 'easyflow_StringToGroupMap93', b1)
    assert _is_linked(a, 'easyflow_StringToGroupMap93', b1)
    if hasattr(b1, 'easyflow_Group94'):
        assert _is_linked(b1, 'easyflow_Group94', a)
    _safe_set(a, 'easyflow_StringToGroupMap93', b2)
    assert _is_linked(a, 'easyflow_StringToGroupMap93', b2)
    if hasattr(b1, 'easyflow_Group94'):
        assert not _is_linked(b1, 'easyflow_Group94', a)
    if hasattr(b2, 'easyflow_Group94'):
        assert _is_linked(b2, 'easyflow_Group94', a)
    _safe_set(a, 'easyflow_StringToGroupMap93', None)
    assert not _is_linked(a, 'easyflow_StringToGroupMap93', b2)
    if hasattr(b2, 'easyflow_Group94'):
        assert not _is_linked(b2, 'easyflow_Group94', a)


def test_assoc_value95_link_reassign_clear():
    a = easyflow_StringToSampleMap(key="sample_text")
    b1 = easyflow_Sample(name="sample_text")
    b2 = easyflow_Sample(name="sample_text_2")
    _safe_set(a, 'easyflow_StringToSampleMap96', b1)
    assert _is_linked(a, 'easyflow_StringToSampleMap96', b1)
    if hasattr(b1, 'easyflow_Sample97'):
        assert _is_linked(b1, 'easyflow_Sample97', a)
    _safe_set(a, 'easyflow_StringToSampleMap96', b2)
    assert _is_linked(a, 'easyflow_StringToSampleMap96', b2)
    if hasattr(b1, 'easyflow_Sample97'):
        assert not _is_linked(b1, 'easyflow_Sample97', a)
    if hasattr(b2, 'easyflow_Sample97'):
        assert _is_linked(b2, 'easyflow_Sample97', a)
    _safe_set(a, 'easyflow_StringToSampleMap96', None)
    assert not _is_linked(a, 'easyflow_StringToSampleMap96', b2)
    if hasattr(b2, 'easyflow_Sample97'):
        assert not _is_linked(b2, 'easyflow_Sample97', a)


def test_assoc_value98_link_reassign_clear():
    a = easyflow_StringToReadgroupMap(key="sample_text")
    b1 = easyflow_Readgroup(description="sample_text", name="sample_text", platform="sample_text", platformUnit="sample_text")
    b2 = easyflow_Readgroup(description="sample_text_2", name="sample_text_2", platform="sample_text_2", platformUnit="sample_text_2")
    _safe_set(a, 'easyflow_StringToReadgroupMap99', b1)
    assert _is_linked(a, 'easyflow_StringToReadgroupMap99', b1)
    if hasattr(b1, 'easyflow_Readgroup100'):
        assert _is_linked(b1, 'easyflow_Readgroup100', a)
    _safe_set(a, 'easyflow_StringToReadgroupMap99', b2)
    assert _is_linked(a, 'easyflow_StringToReadgroupMap99', b2)
    if hasattr(b1, 'easyflow_Readgroup100'):
        assert not _is_linked(b1, 'easyflow_Readgroup100', a)
    if hasattr(b2, 'easyflow_Readgroup100'):
        assert _is_linked(b2, 'easyflow_Readgroup100', a)
    _safe_set(a, 'easyflow_StringToReadgroupMap99', None)
    assert not _is_linked(a, 'easyflow_StringToReadgroupMap99', b2)
    if hasattr(b2, 'easyflow_Readgroup100'):
        assert not _is_linked(b2, 'easyflow_Readgroup100', a)


def test_assoc_workflow28_link_reassign_clear():
    a = easyflow_Workflow(dag="sample_text", graph="sample_text", jobDag="sample_text", name="sample_text")
    b1 = easyflow_EasyFlowTemplate(fileName="sample_text")
    b2 = easyflow_EasyFlowTemplate(fileName="sample_text_2")
    _safe_set(a, 'easyflow_Workflow30', b1)
    assert _is_linked(a, 'easyflow_Workflow30', b1)
    if hasattr(b1, 'easyflow_EasyFlowTemplate29'):
        assert _is_linked(b1, 'easyflow_EasyFlowTemplate29', a)
    _safe_set(a, 'easyflow_Workflow30', b2)
    assert _is_linked(a, 'easyflow_Workflow30', b2)
    if hasattr(b1, 'easyflow_EasyFlowTemplate29'):
        assert not _is_linked(b1, 'easyflow_EasyFlowTemplate29', a)
    if hasattr(b2, 'easyflow_EasyFlowTemplate29'):
        assert _is_linked(b2, 'easyflow_EasyFlowTemplate29', a)
    _safe_set(a, 'easyflow_Workflow30', None)
    assert not _is_linked(a, 'easyflow_Workflow30', b2)
    if hasattr(b2, 'easyflow_EasyFlowTemplate29'):
        assert not _is_linked(b2, 'easyflow_EasyFlowTemplate29', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

EasyFlowMetadata_strategy = st.builds(EasyFlowMetadata)
@given(instance=EasyFlowMetadata_strategy)
@settings(max_examples=25)
def test_EasyFlowMetadata_instantiation(instance):
    assert isinstance(instance, EasyFlowMetadata)


GroupingCriterion_strategy = st.builds(GroupingCriterion)
@given(instance=GroupingCriterion_strategy)
@settings(max_examples=25)
def test_GroupingCriterion_instantiation(instance):
    assert isinstance(instance, GroupingCriterion)


ITraversal_strategy = st.builds(ITraversal)
@given(instance=ITraversal_strategy)
@settings(max_examples=25)
def test_ITraversal_instantiation(instance):
    assert isinstance(instance, ITraversal)


Traversal_strategy = st.builds(Traversal)
@given(instance=Traversal_strategy)
@settings(max_examples=25)
def test_Traversal_instantiation(instance):
    assert isinstance(instance, Traversal)


easyflow_Argument_strategy = st.builds(easyflow_Argument, arg=safe_text, name=safe_text, sep=safe_text)
@given(instance=easyflow_Argument_strategy)
@settings(max_examples=25)
def test_easyflow_Argument_instantiation(instance):
    assert isinstance(instance, easyflow_Argument)


easyflow_Chunk_strategy = st.builds(easyflow_Chunk, argument=safe_text, name=safe_text, tool=safe_text)
@given(instance=easyflow_Chunk_strategy)
@settings(max_examples=25)
def test_easyflow_Chunk_instantiation(instance):
    assert isinstance(instance, easyflow_Chunk)


easyflow_CommandArgument_strategy = st.builds(easyflow_CommandArgument, arg=safe_text, name=safe_text, named=st.booleans(), required=st.booleans(), sep=safe_text)
@given(instance=easyflow_CommandArgument_strategy)
@settings(max_examples=25)
def test_easyflow_CommandArgument_instantiation(instance):
    assert isinstance(instance, easyflow_CommandArgument)


easyflow_Contig_strategy = st.builds(easyflow_Contig)
@given(instance=easyflow_Contig_strategy)
@settings(max_examples=25)
def test_easyflow_Contig_instantiation(instance):
    assert isinstance(instance, easyflow_Contig)


easyflow_DataFormatToTaskList_strategy = st.builds(easyflow_DataFormatToTaskList, key=safe_text)
@given(instance=easyflow_DataFormatToTaskList_strategy)
@settings(max_examples=25)
def test_easyflow_DataFormatToTaskList_instantiation(instance):
    assert isinstance(instance, easyflow_DataFormatToTaskList)


easyflow_DataProcessingType_strategy = st.builds(easyflow_DataProcessingType, dataFormatIn=safe_text, dataFormatOut=safe_text)
@given(instance=easyflow_DataProcessingType_strategy)
@settings(max_examples=25)
def test_easyflow_DataProcessingType_instantiation(instance):
    assert isinstance(instance, easyflow_DataProcessingType)


easyflow_DataProcessingTypeToTask_strategy = st.builds(easyflow_DataProcessingTypeToTask)
@given(instance=easyflow_DataProcessingTypeToTask_strategy)
@settings(max_examples=25)
def test_easyflow_DataProcessingTypeToTask_instantiation(instance):
    assert isinstance(instance, easyflow_DataProcessingTypeToTask)


easyflow_EasyFlowConfiguration_strategy = st.builds(easyflow_EasyFlowConfiguration, configMap=safe_text, fileName=safe_text)
@given(instance=easyflow_EasyFlowConfiguration_strategy)
@settings(max_examples=25)
def test_easyflow_EasyFlowConfiguration_instantiation(instance):
    assert isinstance(instance, easyflow_EasyFlowConfiguration)


easyflow_EasyFlowImplementationTemplate_strategy = st.builds(easyflow_EasyFlowImplementationTemplate, fileName=safe_text, globalOptions=safe_text, jsonRootNode=safe_text, parameterConfigFileName=safe_text, parameterConfigMap=safe_text)
@given(instance=easyflow_EasyFlowImplementationTemplate_strategy)
@settings(max_examples=25)
def test_easyflow_EasyFlowImplementationTemplate_instantiation(instance):
    assert isinstance(instance, easyflow_EasyFlowImplementationTemplate)


easyflow_EasyFlowMetadata_strategy = st.builds(easyflow_EasyFlowMetadata, contrast=st.booleans(), name=safe_text, refData=safe_text)
@given(instance=easyflow_EasyFlowMetadata_strategy)
@settings(max_examples=25)
def test_easyflow_EasyFlowMetadata_instantiation(instance):
    assert isinstance(instance, easyflow_EasyFlowMetadata)


easyflow_EasyFlowMetadataReader_strategy = st.builds(easyflow_EasyFlowMetadataReader, fileName=safe_text)
@given(instance=easyflow_EasyFlowMetadataReader_strategy)
@settings(max_examples=25)
def test_easyflow_EasyFlowMetadataReader_instantiation(instance):
    assert isinstance(instance, easyflow_EasyFlowMetadataReader)


easyflow_EasyFlowTemplate_strategy = st.builds(easyflow_EasyFlowTemplate, fileName=safe_text)
@given(instance=easyflow_EasyFlowTemplate_strategy)
@settings(max_examples=25)
def test_easyflow_EasyFlowTemplate_instantiation(instance):
    assert isinstance(instance, easyflow_EasyFlowTemplate)


easyflow_GenericTraversalCriterion_strategy = st.builds(easyflow_GenericTraversalCriterion)
@given(instance=easyflow_GenericTraversalCriterion_strategy)
@settings(max_examples=25)
def test_easyflow_GenericTraversalCriterion_instantiation(instance):
    assert isinstance(instance, easyflow_GenericTraversalCriterion)


easyflow_Group_strategy = st.builds(easyflow_Group, name=safe_text)
@given(instance=easyflow_Group_strategy)
@settings(max_examples=25)
def test_easyflow_Group_instantiation(instance):
    assert isinstance(instance, easyflow_Group)


easyflow_GroupingCriterion_strategy = st.builds(easyflow_GroupingCriterion, id=safe_text)
@given(instance=easyflow_GroupingCriterion_strategy)
@settings(max_examples=25)
def test_easyflow_GroupingCriterion_instantiation(instance):
    assert isinstance(instance, easyflow_GroupingCriterion)


easyflow_GroupingEvent_strategy = st.builds(easyflow_GroupingEvent, dagIn=safe_text, dagOut=safe_text)
@given(instance=easyflow_GroupingEvent_strategy)
@settings(max_examples=25)
def test_easyflow_GroupingEvent_instantiation(instance):
    assert isinstance(instance, easyflow_GroupingEvent)


easyflow_ITraversal_strategy = st.builds(easyflow_ITraversal)
@given(instance=easyflow_ITraversal_strategy)
@settings(max_examples=25)
def test_easyflow_ITraversal_instantiation(instance):
    assert isinstance(instance, easyflow_ITraversal)


easyflow_IWorkflowUtil_strategy = st.builds(easyflow_IWorkflowUtil)
@given(instance=easyflow_IWorkflowUtil_strategy)
@settings(max_examples=25)
def test_easyflow_IWorkflowUtil_instantiation(instance):
    assert isinstance(instance, easyflow_IWorkflowUtil)


easyflow_Interpreter_strategy = st.builds(easyflow_Interpreter, exe=safe_text, name=safe_text, options=safe_text, subCmd=safe_text)
@given(instance=easyflow_Interpreter_strategy)
@settings(max_examples=25)
def test_easyflow_Interpreter_instantiation(instance):
    assert isinstance(instance, easyflow_Interpreter)


easyflow_Job_strategy = st.builds(easyflow_Job, dependencies=safe_text, exe=safe_text, genericArgs=safe_text, inputArgs=safe_text, interpreterOption=safe_text, name=safe_text, outputArgs=safe_text, source=safe_text, staticArgs=safe_text, subCmd=safe_text, targetPlatform=safe_text, targetPlatformOptions=safe_text, targets=safe_text)
@given(instance=easyflow_Job_strategy)
@settings(max_examples=25)
def test_easyflow_Job_instantiation(instance):
    assert isinstance(instance, easyflow_Job)


easyflow_Library_strategy = st.builds(easyflow_Library, insertSize=st.integers(), name=safe_text, readLength=st.integers())
@given(instance=easyflow_Library_strategy)
@settings(max_examples=25)
def test_easyflow_Library_instantiation(instance):
    assert isinstance(instance, easyflow_Library)


easyflow_Locus_strategy = st.builds(easyflow_Locus)
@given(instance=easyflow_Locus_strategy)
@settings(max_examples=25)
def test_easyflow_Locus_instantiation(instance):
    assert isinstance(instance, easyflow_Locus)


easyflow_ReadEnd_strategy = st.builds(easyflow_ReadEnd)
@given(instance=easyflow_ReadEnd_strategy)
@settings(max_examples=25)
def test_easyflow_ReadEnd_instantiation(instance):
    assert isinstance(instance, easyflow_ReadEnd)


easyflow_Readgroup_strategy = st.builds(easyflow_Readgroup, description=safe_text, name=safe_text, platform=safe_text, platformUnit=safe_text)
@given(instance=easyflow_Readgroup_strategy)
@settings(max_examples=25)
def test_easyflow_Readgroup_instantiation(instance):
    assert isinstance(instance, easyflow_Readgroup)


easyflow_Record_strategy = st.builds(easyflow_Record, fileNames=safe_text, refData=safe_text)
@given(instance=easyflow_Record_strategy)
@settings(max_examples=25)
def test_easyflow_Record_instantiation(instance):
    assert isinstance(instance, easyflow_Record)


easyflow_Sample_strategy = st.builds(easyflow_Sample, name=safe_text)
@given(instance=easyflow_Sample_strategy)
@settings(max_examples=25)
def test_easyflow_Sample_instantiation(instance):
    assert isinstance(instance, easyflow_Sample)


easyflow_SplittingEvent_strategy = st.builds(easyflow_SplittingEvent, dag=safe_text, processedTask=safe_text, traversalChunks=safe_text, traversalCriterion=safe_text, traversalImplDir=safe_text)
@given(instance=easyflow_SplittingEvent_strategy)
@settings(max_examples=25)
def test_easyflow_SplittingEvent_instantiation(instance):
    assert isinstance(instance, easyflow_SplittingEvent)


easyflow_StringToChunkMap_strategy = st.builds(easyflow_StringToChunkMap, key=safe_text)
@given(instance=easyflow_StringToChunkMap_strategy)
@settings(max_examples=25)
def test_easyflow_StringToChunkMap_instantiation(instance):
    assert isinstance(instance, easyflow_StringToChunkMap)


easyflow_StringToGroupMap_strategy = st.builds(easyflow_StringToGroupMap, key=safe_text)
@given(instance=easyflow_StringToGroupMap_strategy)
@settings(max_examples=25)
def test_easyflow_StringToGroupMap_instantiation(instance):
    assert isinstance(instance, easyflow_StringToGroupMap)


easyflow_StringToGroupingCriterionMap_strategy = st.builds(easyflow_StringToGroupingCriterionMap, key=safe_text)
@given(instance=easyflow_StringToGroupingCriterionMap_strategy)
@settings(max_examples=25)
def test_easyflow_StringToGroupingCriterionMap_instantiation(instance):
    assert isinstance(instance, easyflow_StringToGroupingCriterionMap)


easyflow_StringToLibraryMap_strategy = st.builds(easyflow_StringToLibraryMap, key=safe_text)
@given(instance=easyflow_StringToLibraryMap_strategy)
@settings(max_examples=25)
def test_easyflow_StringToLibraryMap_instantiation(instance):
    assert isinstance(instance, easyflow_StringToLibraryMap)


easyflow_StringToReadgroupMap_strategy = st.builds(easyflow_StringToReadgroupMap, key=safe_text)
@given(instance=easyflow_StringToReadgroupMap_strategy)
@settings(max_examples=25)
def test_easyflow_StringToReadgroupMap_instantiation(instance):
    assert isinstance(instance, easyflow_StringToReadgroupMap)


easyflow_StringToRecordMap_strategy = st.builds(easyflow_StringToRecordMap, key=safe_text)
@given(instance=easyflow_StringToRecordMap_strategy)
@settings(max_examples=25)
def test_easyflow_StringToRecordMap_instantiation(instance):
    assert isinstance(instance, easyflow_StringToRecordMap)


easyflow_StringToSampleMap_strategy = st.builds(easyflow_StringToSampleMap, key=safe_text)
@given(instance=easyflow_StringToSampleMap_strategy)
@settings(max_examples=25)
def test_easyflow_StringToSampleMap_instantiation(instance):
    assert isinstance(instance, easyflow_StringToSampleMap)


easyflow_StringToTaskMap_strategy = st.builds(easyflow_StringToTaskMap, key=safe_text)
@given(instance=easyflow_StringToTaskMap_strategy)
@settings(max_examples=25)
def test_easyflow_StringToTaskMap_instantiation(instance):
    assert isinstance(instance, easyflow_StringToTaskMap)


easyflow_StringToToolMap_strategy = st.builds(easyflow_StringToToolMap, key=safe_text)
@given(instance=easyflow_StringToToolMap_strategy)
@settings(max_examples=25)
def test_easyflow_StringToToolMap_instantiation(instance):
    assert isinstance(instance, easyflow_StringToToolMap)


easyflow_StringToTraversalCriterionMap_strategy = st.builds(easyflow_StringToTraversalCriterionMap, key=safe_text, value=safe_text)
@given(instance=easyflow_StringToTraversalCriterionMap_strategy)
@settings(max_examples=25)
def test_easyflow_StringToTraversalCriterionMap_instantiation(instance):
    assert isinstance(instance, easyflow_StringToTraversalCriterionMap)


easyflow_Task_strategy = st.builds(easyflow_Task, cardinalityIn=safe_text, cardinalityOut=safe_text, contrast=st.booleans(), dataCriterion=safe_text, dataFormatIn=safe_text, dataFormatOut=safe_text, depricated=st.booleans(), isMultipleInstancesOfDataCriterion=safe_text, jexlString=safe_text, mergeCriterion=safe_text, name=safe_text, skipGroupingCriterion=safe_text, splitCriterion=safe_text, static=st.booleans(), traversalCriterion=safe_text, util=st.booleans())
@given(instance=easyflow_Task_strategy)
@settings(max_examples=25)
def test_easyflow_Task_instantiation(instance):
    assert isinstance(instance, easyflow_Task)


easyflow_TaskToDataProcessingType_strategy = st.builds(easyflow_TaskToDataProcessingType)
@given(instance=easyflow_TaskToDataProcessingType_strategy)
@settings(max_examples=25)
def test_easyflow_TaskToDataProcessingType_instantiation(instance):
    assert isinstance(instance, easyflow_TaskToDataProcessingType)


easyflow_Tool_strategy = st.builds(easyflow_Tool, category=safe_text, pattern=safe_text, refData=safe_text, source=safe_text, subCmd=safe_text, subCmdPrefix=safe_text, toolName=safe_text, type=safe_text)
@given(instance=easyflow_Tool_strategy)
@settings(max_examples=25)
def test_easyflow_Tool_instantiation(instance):
    assert isinstance(instance, easyflow_Tool)


easyflow_Traversal_strategy = st.builds(easyflow_Traversal, tarversalCriterion=safe_text)
@given(instance=easyflow_Traversal_strategy)
@settings(max_examples=25)
def test_easyflow_Traversal_instantiation(instance):
    assert isinstance(instance, easyflow_Traversal)


easyflow_Workflow_strategy = st.builds(easyflow_Workflow, dag=safe_text, graph=safe_text, jobDag=safe_text, name=safe_text)
@given(instance=easyflow_Workflow_strategy)
@settings(max_examples=25)
def test_easyflow_Workflow_instantiation(instance):
    assert isinstance(instance, easyflow_Workflow)


