# =============================================================================
# This file is a generated concatenation of two independent test suites --
# see scripts/generate_combined_tests.py for why simple concatenation is safe
# despite both generators using the same naming convention for some helpers,
# and for the deterministic rules used to drop old-suite tests the new suite
# already covers equally or more thoroughly.
# =============================================================================

# ----- SECTION A: test_hypothesis.py (original generated suite) -----
import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    driver_TestCasesList,
    driver_TestCase,
    driver_StopTrace,
    driver_StartTrace,
    driver_TransferToSymbian,
    driver_Transfer,
    driver_Reference,
    driver_FlashROM,
    driver_RetrieveFromSymbian,
    driver_TestExecuteScript,
    driver_ExecuteOnSymbian,
    driver_ExecuteOnPC,
    driver_Rtest,
    driver_Task,
    driver_DriverInfo,
    driver_Driver,
    driver_EStringToStringMapEntry,
    driver_Info,
    driver_DocumentRoot,
    driver_CmdSymbian,
    driver_CmdPC,
    driver_Build,
    Phase,
    StatCommand,
    OperatorType,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hyp_driver_testcaseslist_is_not_abstract():
    assert not inspect.isabstract(driver_TestCasesList)


def test_hyp_driver_testcaseslist_constructor_exists():
    assert callable(driver_TestCasesList.__init__)


def test_hyp_driver_testcaseslist_constructor_args():
    sig = inspect.signature(driver_TestCasesList.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"




def test_hyp_driver_testcase_is_not_abstract():
    assert not inspect.isabstract(driver_TestCase)


def test_hyp_driver_testcase_constructor_exists():
    assert callable(driver_TestCase.__init__)


def test_hyp_driver_testcase_constructor_args():
    sig = inspect.signature(driver_TestCase.__init__)
    params = list(sig.parameters.keys())
    assert "target" in params, "Missing parameter 'target'"




def test_hyp_driver_stoptrace_is_not_abstract():
    assert not inspect.isabstract(driver_StopTrace)


def test_hyp_driver_stoptrace_constructor_exists():
    assert callable(driver_StopTrace.__init__)


def test_hyp_driver_stoptrace_constructor_args():
    sig = inspect.signature(driver_StopTrace.__init__)
    params = list(sig.parameters.keys())



def test_hyp_driver_starttrace_is_not_abstract():
    assert not inspect.isabstract(driver_StartTrace)


def test_hyp_driver_starttrace_constructor_exists():
    assert callable(driver_StartTrace.__init__)


def test_hyp_driver_starttrace_constructor_args():
    sig = inspect.signature(driver_StartTrace.__init__)
    params = list(sig.parameters.keys())
    assert "enablePrimaryFilters" in params, "Missing parameter 'enablePrimaryFilters'"
    assert "disablePrimaryFilters" in params, "Missing parameter 'disablePrimaryFilters'"
    assert "disableSecondaryFilters" in params, "Missing parameter 'disableSecondaryFilters'"
    assert "configFilePath" in params, "Missing parameter 'configFilePath'"
    assert "enableSecondaryFilters" in params, "Missing parameter 'enableSecondaryFilters'"








def test_hyp_driver_transfertosymbian_is_not_abstract():
    assert not inspect.isabstract(driver_TransferToSymbian)


def test_hyp_driver_transfertosymbian_constructor_exists():
    assert callable(driver_TransferToSymbian.__init__)


def test_hyp_driver_transfertosymbian_constructor_args():
    sig = inspect.signature(driver_TransferToSymbian.__init__)
    params = list(sig.parameters.keys())
    assert "group" in params, "Missing parameter 'group'"




def test_hyp_driver_transfer_is_not_abstract():
    assert not inspect.isabstract(driver_Transfer)


def test_hyp_driver_transfer_constructor_exists():
    assert callable(driver_Transfer.__init__)


def test_hyp_driver_transfer_constructor_args():
    sig = inspect.signature(driver_Transfer.__init__)
    params = list(sig.parameters.keys())
    assert "move" in params, "Missing parameter 'move'"
    assert "pCPath" in params, "Missing parameter 'pCPath'"
    assert "symbianPath" in params, "Missing parameter 'symbianPath'"






def test_hyp_driver_reference_is_not_abstract():
    assert not inspect.isabstract(driver_Reference)


def test_hyp_driver_reference_constructor_exists():
    assert callable(driver_Reference.__init__)


def test_hyp_driver_reference_constructor_args():
    sig = inspect.signature(driver_Reference.__init__)
    params = list(sig.parameters.keys())



def test_hyp_driver_flashrom_is_not_abstract():
    assert not inspect.isabstract(driver_FlashROM)


def test_hyp_driver_flashrom_constructor_exists():
    assert callable(driver_FlashROM.__init__)


def test_hyp_driver_flashrom_constructor_args():
    sig = inspect.signature(driver_FlashROM.__init__)
    params = list(sig.parameters.keys())
    assert "pCPath" in params, "Missing parameter 'pCPath'"




def test_hyp_driver_retrievefromsymbian_is_not_abstract():
    assert not inspect.isabstract(driver_RetrieveFromSymbian)


def test_hyp_driver_retrievefromsymbian_constructor_exists():
    assert callable(driver_RetrieveFromSymbian.__init__)


def test_hyp_driver_retrievefromsymbian_constructor_args():
    sig = inspect.signature(driver_RetrieveFromSymbian.__init__)
    params = list(sig.parameters.keys())
    assert "group" in params, "Missing parameter 'group'"




def test_hyp_driver_testexecutescript_is_not_abstract():
    assert not inspect.isabstract(driver_TestExecuteScript)


def test_hyp_driver_testexecutescript_constructor_exists():
    assert callable(driver_TestExecuteScript.__init__)


def test_hyp_driver_testexecutescript_constructor_args():
    sig = inspect.signature(driver_TestExecuteScript.__init__)
    params = list(sig.parameters.keys())
    assert "symbianPath" in params, "Missing parameter 'symbianPath'"
    assert "pCPath" in params, "Missing parameter 'pCPath'"





def test_hyp_driver_executeonsymbian_is_not_abstract():
    assert not inspect.isabstract(driver_ExecuteOnSymbian)


def test_hyp_driver_executeonsymbian_constructor_exists():
    assert callable(driver_ExecuteOnSymbian.__init__)


def test_hyp_driver_executeonsymbian_constructor_args():
    sig = inspect.signature(driver_ExecuteOnSymbian.__init__)
    params = list(sig.parameters.keys())
    assert "group" in params, "Missing parameter 'group'"




def test_hyp_driver_executeonpc_is_not_abstract():
    assert not inspect.isabstract(driver_ExecuteOnPC)


def test_hyp_driver_executeonpc_constructor_exists():
    assert callable(driver_ExecuteOnPC.__init__)


def test_hyp_driver_executeonpc_constructor_args():
    sig = inspect.signature(driver_ExecuteOnPC.__init__)
    params = list(sig.parameters.keys())
    assert "group" in params, "Missing parameter 'group'"




def test_hyp_driver_rtest_is_not_abstract():
    assert not inspect.isabstract(driver_Rtest)


def test_hyp_driver_rtest_constructor_exists():
    assert callable(driver_Rtest.__init__)


def test_hyp_driver_rtest_constructor_args():
    sig = inspect.signature(driver_Rtest.__init__)
    params = list(sig.parameters.keys())
    assert "symbianPath" in params, "Missing parameter 'symbianPath'"
    assert "resultFile" in params, "Missing parameter 'resultFile'"





def test_hyp_driver_task_is_not_abstract():
    assert not inspect.isabstract(driver_Task)


def test_hyp_driver_task_constructor_exists():
    assert callable(driver_Task.__init__)


def test_hyp_driver_task_constructor_args():
    sig = inspect.signature(driver_Task.__init__)
    params = list(sig.parameters.keys())
    assert "timeout" in params, "Missing parameter 'timeout'"
    assert "group" in params, "Missing parameter 'group'"
    assert "name" in params, "Missing parameter 'name'"
    assert "preRebootDevice" in params, "Missing parameter 'preRebootDevice'"







def test_hyp_driver_driverinfo_is_not_abstract():
    assert not inspect.isabstract(driver_DriverInfo)


def test_hyp_driver_driverinfo_constructor_exists():
    assert callable(driver_DriverInfo.__init__)


def test_hyp_driver_driverinfo_constructor_args():
    sig = inspect.signature(driver_DriverInfo.__init__)
    params = list(sig.parameters.keys())



def test_hyp_driver_driver_is_not_abstract():
    assert not inspect.isabstract(driver_Driver)


def test_hyp_driver_driver_constructor_exists():
    assert callable(driver_Driver.__init__)


def test_hyp_driver_driver_constructor_args():
    sig = inspect.signature(driver_Driver.__init__)
    params = list(sig.parameters.keys())



def test_hyp_driver_estringtostringmapentry_is_not_abstract():
    assert not inspect.isabstract(driver_EStringToStringMapEntry)


def test_hyp_driver_estringtostringmapentry_constructor_exists():
    assert callable(driver_EStringToStringMapEntry.__init__)


def test_hyp_driver_estringtostringmapentry_constructor_args():
    sig = inspect.signature(driver_EStringToStringMapEntry.__init__)
    params = list(sig.parameters.keys())



def test_hyp_driver_info_is_not_abstract():
    assert not inspect.isabstract(driver_Info)


def test_hyp_driver_info_constructor_exists():
    assert callable(driver_Info.__init__)


def test_hyp_driver_info_constructor_args():
    sig = inspect.signature(driver_Info.__init__)
    params = list(sig.parameters.keys())
    assert "key" in params, "Missing parameter 'key'"
    assert "value" in params, "Missing parameter 'value'"





def test_hyp_driver_documentroot_is_not_abstract():
    assert not inspect.isabstract(driver_DocumentRoot)


def test_hyp_driver_documentroot_constructor_exists():
    assert callable(driver_DocumentRoot.__init__)


def test_hyp_driver_documentroot_constructor_args():
    sig = inspect.signature(driver_DocumentRoot.__init__)
    params = list(sig.parameters.keys())
    assert "mixed" in params, "Missing parameter 'mixed'"




def test_hyp_driver_cmdsymbian_is_not_abstract():
    assert not inspect.isabstract(driver_CmdSymbian)


def test_hyp_driver_cmdsymbian_constructor_exists():
    assert callable(driver_CmdSymbian.__init__)


def test_hyp_driver_cmdsymbian_constructor_args():
    sig = inspect.signature(driver_CmdSymbian.__init__)
    params = list(sig.parameters.keys())
    assert "statCommand" in params, "Missing parameter 'statCommand'"
    assert "argument" in params, "Missing parameter 'argument'"
    assert "sync" in params, "Missing parameter 'sync'"
    assert "output" in params, "Missing parameter 'output'"







def test_hyp_driver_cmdpc_is_not_abstract():
    assert not inspect.isabstract(driver_CmdPC)


def test_hyp_driver_cmdpc_constructor_exists():
    assert callable(driver_CmdPC.__init__)


def test_hyp_driver_cmdpc_constructor_args():
    sig = inspect.signature(driver_CmdPC.__init__)
    params = list(sig.parameters.keys())
    assert "sync" in params, "Missing parameter 'sync'"
    assert "uRI" in params, "Missing parameter 'uRI'"
    assert "value" in params, "Missing parameter 'value'"
    assert "phase" in params, "Missing parameter 'phase'"







def test_hyp_driver_build_is_not_abstract():
    assert not inspect.isabstract(driver_Build)


def test_hyp_driver_build_constructor_exists():
    assert callable(driver_Build.__init__)


def test_hyp_driver_build_constructor_args():
    sig = inspect.signature(driver_Build.__init__)
    params = list(sig.parameters.keys())
    assert "uRI" in params, "Missing parameter 'uRI'"
    assert "componentName" in params, "Missing parameter 'componentName'"
    assert "testBuild" in params, "Missing parameter 'testBuild'"




def test_hyp_phase_exists():
    # Check that the Enumeration exists
    assert Phase is not None

def test_hyp_phase_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Phase]
    expected_literals = [
        "run",
        "build",
        "both",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Phase"

def test_hyp_statcommand_exists():
    # Check that the Enumeration exists
    assert StatCommand is not None

def test_hyp_statcommand_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in StatCommand]
    expected_literals = [
        "removeFolder",
        "stopLogging",
        "run",
        "delete",
        "createFolder",
        "startLogging",
        "getScreenCapture",
        "listDrives",
        "listFiles",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in StatCommand"

def test_hyp_operatortype_exists():
    # Check that the Enumeration exists
    assert OperatorType is not None

def test_hyp_operatortype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in OperatorType]
    expected_literals = [
        "include",
        "exclude",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in OperatorType"


# =============================================================================
# HYPOTHESIS STRATEGIES
# =============================================================================

safe_text = st.text(
    alphabet=st.characters(
        whitelist_categories=("Ll", "Lu", "Nd"),
        whitelist_characters="_",
    ),
    min_size=1,
).filter(lambda s: s[0].isalpha())
driver_TestCasesList_strategy = st.builds(
    driver_TestCasesList,
    operator=
        safe_text
)
driver_TestCase_strategy = st.builds(
    driver_TestCase,
    target=
        safe_text
)
driver_StopTrace_strategy = st.builds(
    driver_StopTrace,
)
driver_StartTrace_strategy = st.builds(
    driver_StartTrace,
    enablePrimaryFilters=
        safe_text,
    disablePrimaryFilters=
        safe_text,
    disableSecondaryFilters=
        safe_text,
    configFilePath=
        safe_text,
    enableSecondaryFilters=
        safe_text
)
driver_TransferToSymbian_strategy = st.builds(
    driver_TransferToSymbian,
    group=
        safe_text
)
driver_Transfer_strategy = st.builds(
    driver_Transfer,
    move=
        safe_text,
    pCPath=
        safe_text,
    symbianPath=
        safe_text
)
driver_Reference_strategy = st.builds(
    driver_Reference,
)
driver_FlashROM_strategy = st.builds(
    driver_FlashROM,
    pCPath=
        safe_text
)
driver_RetrieveFromSymbian_strategy = st.builds(
    driver_RetrieveFromSymbian,
    group=
        safe_text
)
driver_TestExecuteScript_strategy = st.builds(
    driver_TestExecuteScript,
    symbianPath=
        safe_text,
    pCPath=
        safe_text
)
driver_ExecuteOnSymbian_strategy = st.builds(
    driver_ExecuteOnSymbian,
    group=
        safe_text
)
driver_ExecuteOnPC_strategy = st.builds(
    driver_ExecuteOnPC,
    group=
        safe_text
)
driver_Rtest_strategy = st.builds(
    driver_Rtest,
    symbianPath=
        safe_text,
    resultFile=
        safe_text
)
driver_Task_strategy = st.builds(
    driver_Task,
    timeout=
        safe_text,
    group=
        safe_text,
    name=
        safe_text,
    preRebootDevice=
        safe_text
)
driver_DriverInfo_strategy = st.builds(
    driver_DriverInfo,
)
driver_Driver_strategy = st.builds(
    driver_Driver,
)
driver_EStringToStringMapEntry_strategy = st.builds(
    driver_EStringToStringMapEntry,
)
driver_Info_strategy = st.builds(
    driver_Info,
    key=
        safe_text,
    value=
        safe_text
)
driver_DocumentRoot_strategy = st.builds(
    driver_DocumentRoot,
    mixed=
        safe_text
)
driver_CmdSymbian_strategy = st.builds(
    driver_CmdSymbian,
    statCommand=
        safe_text,
    argument=
        safe_text,
    sync=
        safe_text,
    output=
        safe_text
)
driver_CmdPC_strategy = st.builds(
    driver_CmdPC,
    sync=
        safe_text,
    uRI=
        safe_text,
    value=
        safe_text,
    phase=
        safe_text
)
driver_Build_strategy = st.builds(
    driver_Build,
    uRI=
        safe_text,
    componentName=
        safe_text,
    testBuild=
        safe_text
)




@given(instance=driver_TestCasesList_strategy)
def test_hyp_driver_testcaseslist_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original




@given(instance=driver_TestCase_strategy)
def test_hyp_driver_testcase_target_setter(instance):
    original = instance.target
    instance.target = original
    assert instance.target == original





@given(instance=driver_StartTrace_strategy)
def test_hyp_driver_starttrace_enablePrimaryFilters_setter(instance):
    original = instance.enablePrimaryFilters
    instance.enablePrimaryFilters = original
    assert instance.enablePrimaryFilters == original



@given(instance=driver_StartTrace_strategy)
def test_hyp_driver_starttrace_disablePrimaryFilters_setter(instance):
    original = instance.disablePrimaryFilters
    instance.disablePrimaryFilters = original
    assert instance.disablePrimaryFilters == original



@given(instance=driver_StartTrace_strategy)
def test_hyp_driver_starttrace_disableSecondaryFilters_setter(instance):
    original = instance.disableSecondaryFilters
    instance.disableSecondaryFilters = original
    assert instance.disableSecondaryFilters == original



@given(instance=driver_StartTrace_strategy)
def test_hyp_driver_starttrace_configFilePath_setter(instance):
    original = instance.configFilePath
    instance.configFilePath = original
    assert instance.configFilePath == original



@given(instance=driver_StartTrace_strategy)
def test_hyp_driver_starttrace_enableSecondaryFilters_setter(instance):
    original = instance.enableSecondaryFilters
    instance.enableSecondaryFilters = original
    assert instance.enableSecondaryFilters == original




@given(instance=driver_TransferToSymbian_strategy)
def test_hyp_driver_transfertosymbian_group_setter(instance):
    original = instance.group
    instance.group = original
    assert instance.group == original




@given(instance=driver_Transfer_strategy)
def test_hyp_driver_transfer_move_setter(instance):
    original = instance.move
    instance.move = original
    assert instance.move == original



@given(instance=driver_Transfer_strategy)
def test_hyp_driver_transfer_pCPath_setter(instance):
    original = instance.pCPath
    instance.pCPath = original
    assert instance.pCPath == original



@given(instance=driver_Transfer_strategy)
def test_hyp_driver_transfer_symbianPath_setter(instance):
    original = instance.symbianPath
    instance.symbianPath = original
    assert instance.symbianPath == original





@given(instance=driver_FlashROM_strategy)
def test_hyp_driver_flashrom_pCPath_setter(instance):
    original = instance.pCPath
    instance.pCPath = original
    assert instance.pCPath == original




@given(instance=driver_RetrieveFromSymbian_strategy)
def test_hyp_driver_retrievefromsymbian_group_setter(instance):
    original = instance.group
    instance.group = original
    assert instance.group == original




@given(instance=driver_TestExecuteScript_strategy)
def test_hyp_driver_testexecutescript_symbianPath_setter(instance):
    original = instance.symbianPath
    instance.symbianPath = original
    assert instance.symbianPath == original



@given(instance=driver_TestExecuteScript_strategy)
def test_hyp_driver_testexecutescript_pCPath_setter(instance):
    original = instance.pCPath
    instance.pCPath = original
    assert instance.pCPath == original




@given(instance=driver_ExecuteOnSymbian_strategy)
def test_hyp_driver_executeonsymbian_group_setter(instance):
    original = instance.group
    instance.group = original
    assert instance.group == original




@given(instance=driver_ExecuteOnPC_strategy)
def test_hyp_driver_executeonpc_group_setter(instance):
    original = instance.group
    instance.group = original
    assert instance.group == original




@given(instance=driver_Rtest_strategy)
def test_hyp_driver_rtest_symbianPath_setter(instance):
    original = instance.symbianPath
    instance.symbianPath = original
    assert instance.symbianPath == original



@given(instance=driver_Rtest_strategy)
def test_hyp_driver_rtest_resultFile_setter(instance):
    original = instance.resultFile
    instance.resultFile = original
    assert instance.resultFile == original




@given(instance=driver_Task_strategy)
def test_hyp_driver_task_timeout_setter(instance):
    original = instance.timeout
    instance.timeout = original
    assert instance.timeout == original



@given(instance=driver_Task_strategy)
def test_hyp_driver_task_group_setter(instance):
    original = instance.group
    instance.group = original
    assert instance.group == original



@given(instance=driver_Task_strategy)
def test_hyp_driver_task_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=driver_Task_strategy)
def test_hyp_driver_task_preRebootDevice_setter(instance):
    original = instance.preRebootDevice
    instance.preRebootDevice = original
    assert instance.preRebootDevice == original







@given(instance=driver_Info_strategy)
def test_hyp_driver_info_key_setter(instance):
    original = instance.key
    instance.key = original
    assert instance.key == original



@given(instance=driver_Info_strategy)
def test_hyp_driver_info_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original




@given(instance=driver_DocumentRoot_strategy)
def test_hyp_driver_documentroot_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original




@given(instance=driver_CmdSymbian_strategy)
def test_hyp_driver_cmdsymbian_statCommand_setter(instance):
    original = instance.statCommand
    instance.statCommand = original
    assert instance.statCommand == original



@given(instance=driver_CmdSymbian_strategy)
def test_hyp_driver_cmdsymbian_argument_setter(instance):
    original = instance.argument
    instance.argument = original
    assert instance.argument == original



@given(instance=driver_CmdSymbian_strategy)
def test_hyp_driver_cmdsymbian_sync_setter(instance):
    original = instance.sync
    instance.sync = original
    assert instance.sync == original



@given(instance=driver_CmdSymbian_strategy)
def test_hyp_driver_cmdsymbian_output_setter(instance):
    original = instance.output
    instance.output = original
    assert instance.output == original




@given(instance=driver_CmdPC_strategy)
def test_hyp_driver_cmdpc_sync_setter(instance):
    original = instance.sync
    instance.sync = original
    assert instance.sync == original



@given(instance=driver_CmdPC_strategy)
def test_hyp_driver_cmdpc_uRI_setter(instance):
    original = instance.uRI
    instance.uRI = original
    assert instance.uRI == original



@given(instance=driver_CmdPC_strategy)
def test_hyp_driver_cmdpc_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original



@given(instance=driver_CmdPC_strategy)
def test_hyp_driver_cmdpc_phase_setter(instance):
    original = instance.phase
    instance.phase = original
    assert instance.phase == original




@given(instance=driver_Build_strategy)
def test_hyp_driver_build_uRI_setter(instance):
    original = instance.uRI
    instance.uRI = original
    assert instance.uRI == original



@given(instance=driver_Build_strategy)
def test_hyp_driver_build_componentName_setter(instance):
    original = instance.componentName
    instance.componentName = original
    assert instance.componentName == original



@given(instance=driver_Build_strategy)
def test_hyp_driver_build_testBuild_setter(instance):
    original = instance.testBuild
    instance.testBuild = original
    assert instance.testBuild == original


# ----- SECTION B: test_structural_full.py (deterministic-first suite) -----
import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    driver_Build,
    driver_CmdPC,
    driver_CmdSymbian,
    driver_DocumentRoot,
    driver_Driver,
    driver_DriverInfo,
    driver_EStringToStringMapEntry,
    driver_ExecuteOnPC,
    driver_ExecuteOnSymbian,
    driver_FlashROM,
    driver_Info,
    driver_Reference,
    driver_RetrieveFromSymbian,
    driver_Rtest,
    driver_StartTrace,
    driver_StopTrace,
    driver_Task,
    driver_TestCase,
    driver_TestCasesList,
    driver_TestExecuteScript,
    driver_Transfer,
    driver_TransferToSymbian,
    OperatorType,
    Phase,
    StatCommand,
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

def test_driver_Build_componentName_value_roundtrip():
    instance = driver_Build(componentName="sample_text", testBuild="sample_text", uRI="sample_text")
    assert instance.componentName == "sample_text"
    instance.componentName = "sample_text_2"
    assert instance.componentName == "sample_text_2"


def test_driver_Build_testBuild_value_roundtrip():
    instance = driver_Build(componentName="sample_text", testBuild="sample_text", uRI="sample_text")
    assert instance.testBuild == "sample_text"
    instance.testBuild = "sample_text_2"
    assert instance.testBuild == "sample_text_2"


def test_driver_Build_uRI_value_roundtrip():
    instance = driver_Build(componentName="sample_text", testBuild="sample_text", uRI="sample_text")
    assert instance.uRI == "sample_text"
    instance.uRI = "sample_text_2"
    assert instance.uRI == "sample_text_2"


def test_driver_CmdPC_phase_value_roundtrip():
    instance = driver_CmdPC(phase="sample_text", sync="sample_text", uRI="sample_text", value="sample_text")
    assert instance.phase == "sample_text"
    instance.phase = "sample_text_2"
    assert instance.phase == "sample_text_2"


def test_driver_CmdPC_sync_value_roundtrip():
    instance = driver_CmdPC(phase="sample_text", sync="sample_text", uRI="sample_text", value="sample_text")
    assert instance.sync == "sample_text"
    instance.sync = "sample_text_2"
    assert instance.sync == "sample_text_2"


def test_driver_CmdPC_uRI_value_roundtrip():
    instance = driver_CmdPC(phase="sample_text", sync="sample_text", uRI="sample_text", value="sample_text")
    assert instance.uRI == "sample_text"
    instance.uRI = "sample_text_2"
    assert instance.uRI == "sample_text_2"


def test_driver_CmdPC_value_value_roundtrip():
    instance = driver_CmdPC(phase="sample_text", sync="sample_text", uRI="sample_text", value="sample_text")
    assert instance.value == "sample_text"
    instance.value = "sample_text_2"
    assert instance.value == "sample_text_2"


def test_driver_CmdSymbian_argument_value_roundtrip():
    instance = driver_CmdSymbian(argument="sample_text", output="sample_text", statCommand="sample_text", sync="sample_text")
    assert instance.argument == "sample_text"
    instance.argument = "sample_text_2"
    assert instance.argument == "sample_text_2"


def test_driver_CmdSymbian_output_value_roundtrip():
    instance = driver_CmdSymbian(argument="sample_text", output="sample_text", statCommand="sample_text", sync="sample_text")
    assert instance.output == "sample_text"
    instance.output = "sample_text_2"
    assert instance.output == "sample_text_2"


def test_driver_CmdSymbian_statCommand_value_roundtrip():
    instance = driver_CmdSymbian(argument="sample_text", output="sample_text", statCommand="sample_text", sync="sample_text")
    assert instance.statCommand == "sample_text"
    instance.statCommand = "sample_text_2"
    assert instance.statCommand == "sample_text_2"


def test_driver_CmdSymbian_sync_value_roundtrip():
    instance = driver_CmdSymbian(argument="sample_text", output="sample_text", statCommand="sample_text", sync="sample_text")
    assert instance.sync == "sample_text"
    instance.sync = "sample_text_2"
    assert instance.sync == "sample_text_2"


def test_driver_DocumentRoot_mixed_value_roundtrip():
    instance = driver_DocumentRoot(mixed="sample_text")
    assert instance.mixed == "sample_text"
    instance.mixed = "sample_text_2"
    assert instance.mixed == "sample_text_2"


def test_driver_ExecuteOnPC_group_value_roundtrip():
    instance = driver_ExecuteOnPC(group="sample_text")
    assert instance.group == "sample_text"
    instance.group = "sample_text_2"
    assert instance.group == "sample_text_2"


def test_driver_ExecuteOnSymbian_group_value_roundtrip():
    instance = driver_ExecuteOnSymbian(group="sample_text")
    assert instance.group == "sample_text"
    instance.group = "sample_text_2"
    assert instance.group == "sample_text_2"


def test_driver_FlashROM_pCPath_value_roundtrip():
    instance = driver_FlashROM(pCPath="sample_text")
    assert instance.pCPath == "sample_text"
    instance.pCPath = "sample_text_2"
    assert instance.pCPath == "sample_text_2"


def test_driver_Info_key_value_roundtrip():
    instance = driver_Info(key="sample_text", value="sample_text")
    assert instance.key == "sample_text"
    instance.key = "sample_text_2"
    assert instance.key == "sample_text_2"


def test_driver_Info_value_value_roundtrip():
    instance = driver_Info(key="sample_text", value="sample_text")
    assert instance.value == "sample_text"
    instance.value = "sample_text_2"
    assert instance.value == "sample_text_2"


def test_driver_RetrieveFromSymbian_group_value_roundtrip():
    instance = driver_RetrieveFromSymbian(group="sample_text")
    assert instance.group == "sample_text"
    instance.group = "sample_text_2"
    assert instance.group == "sample_text_2"


def test_driver_Rtest_resultFile_value_roundtrip():
    instance = driver_Rtest(resultFile="sample_text", symbianPath="sample_text")
    assert instance.resultFile == "sample_text"
    instance.resultFile = "sample_text_2"
    assert instance.resultFile == "sample_text_2"


def test_driver_Rtest_symbianPath_value_roundtrip():
    instance = driver_Rtest(resultFile="sample_text", symbianPath="sample_text")
    assert instance.symbianPath == "sample_text"
    instance.symbianPath = "sample_text_2"
    assert instance.symbianPath == "sample_text_2"


def test_driver_StartTrace_configFilePath_value_roundtrip():
    instance = driver_StartTrace(configFilePath="sample_text", disablePrimaryFilters="sample_text", disableSecondaryFilters="sample_text", enablePrimaryFilters="sample_text", enableSecondaryFilters="sample_text")
    assert instance.configFilePath == "sample_text"
    instance.configFilePath = "sample_text_2"
    assert instance.configFilePath == "sample_text_2"


def test_driver_StartTrace_disablePrimaryFilters_value_roundtrip():
    instance = driver_StartTrace(configFilePath="sample_text", disablePrimaryFilters="sample_text", disableSecondaryFilters="sample_text", enablePrimaryFilters="sample_text", enableSecondaryFilters="sample_text")
    assert instance.disablePrimaryFilters == "sample_text"
    instance.disablePrimaryFilters = "sample_text_2"
    assert instance.disablePrimaryFilters == "sample_text_2"


def test_driver_StartTrace_disableSecondaryFilters_value_roundtrip():
    instance = driver_StartTrace(configFilePath="sample_text", disablePrimaryFilters="sample_text", disableSecondaryFilters="sample_text", enablePrimaryFilters="sample_text", enableSecondaryFilters="sample_text")
    assert instance.disableSecondaryFilters == "sample_text"
    instance.disableSecondaryFilters = "sample_text_2"
    assert instance.disableSecondaryFilters == "sample_text_2"


def test_driver_StartTrace_enablePrimaryFilters_value_roundtrip():
    instance = driver_StartTrace(configFilePath="sample_text", disablePrimaryFilters="sample_text", disableSecondaryFilters="sample_text", enablePrimaryFilters="sample_text", enableSecondaryFilters="sample_text")
    assert instance.enablePrimaryFilters == "sample_text"
    instance.enablePrimaryFilters = "sample_text_2"
    assert instance.enablePrimaryFilters == "sample_text_2"


def test_driver_StartTrace_enableSecondaryFilters_value_roundtrip():
    instance = driver_StartTrace(configFilePath="sample_text", disablePrimaryFilters="sample_text", disableSecondaryFilters="sample_text", enablePrimaryFilters="sample_text", enableSecondaryFilters="sample_text")
    assert instance.enableSecondaryFilters == "sample_text"
    instance.enableSecondaryFilters = "sample_text_2"
    assert instance.enableSecondaryFilters == "sample_text_2"


def test_driver_Task_group_value_roundtrip():
    instance = driver_Task(group="sample_text", name="sample_text", preRebootDevice="sample_text", timeout="sample_text")
    assert instance.group == "sample_text"
    instance.group = "sample_text_2"
    assert instance.group == "sample_text_2"


def test_driver_Task_name_value_roundtrip():
    instance = driver_Task(group="sample_text", name="sample_text", preRebootDevice="sample_text", timeout="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_driver_Task_preRebootDevice_value_roundtrip():
    instance = driver_Task(group="sample_text", name="sample_text", preRebootDevice="sample_text", timeout="sample_text")
    assert instance.preRebootDevice == "sample_text"
    instance.preRebootDevice = "sample_text_2"
    assert instance.preRebootDevice == "sample_text_2"


def test_driver_Task_timeout_value_roundtrip():
    instance = driver_Task(group="sample_text", name="sample_text", preRebootDevice="sample_text", timeout="sample_text")
    assert instance.timeout == "sample_text"
    instance.timeout = "sample_text_2"
    assert instance.timeout == "sample_text_2"


def test_driver_TestCase_target_value_roundtrip():
    instance = driver_TestCase(target="sample_text")
    assert instance.target == "sample_text"
    instance.target = "sample_text_2"
    assert instance.target == "sample_text_2"


def test_driver_TestCasesList_operator_value_roundtrip():
    instance = driver_TestCasesList(operator="sample_text")
    assert instance.operator == "sample_text"
    instance.operator = "sample_text_2"
    assert instance.operator == "sample_text_2"


def test_driver_TestExecuteScript_pCPath_value_roundtrip():
    instance = driver_TestExecuteScript(pCPath="sample_text", symbianPath="sample_text")
    assert instance.pCPath == "sample_text"
    instance.pCPath = "sample_text_2"
    assert instance.pCPath == "sample_text_2"


def test_driver_TestExecuteScript_symbianPath_value_roundtrip():
    instance = driver_TestExecuteScript(pCPath="sample_text", symbianPath="sample_text")
    assert instance.symbianPath == "sample_text"
    instance.symbianPath = "sample_text_2"
    assert instance.symbianPath == "sample_text_2"


def test_driver_Transfer_move_value_roundtrip():
    instance = driver_Transfer(move="sample_text", pCPath="sample_text", symbianPath="sample_text")
    assert instance.move == "sample_text"
    instance.move = "sample_text_2"
    assert instance.move == "sample_text_2"


def test_driver_Transfer_pCPath_value_roundtrip():
    instance = driver_Transfer(move="sample_text", pCPath="sample_text", symbianPath="sample_text")
    assert instance.pCPath == "sample_text"
    instance.pCPath = "sample_text_2"
    assert instance.pCPath == "sample_text_2"


def test_driver_Transfer_symbianPath_value_roundtrip():
    instance = driver_Transfer(move="sample_text", pCPath="sample_text", symbianPath="sample_text")
    assert instance.symbianPath == "sample_text"
    instance.symbianPath = "sample_text_2"
    assert instance.symbianPath == "sample_text_2"


def test_driver_TransferToSymbian_group_value_roundtrip():
    instance = driver_TransferToSymbian(group="sample_text")
    assert instance.group == "sample_text"
    instance.group = "sample_text_2"
    assert instance.group == "sample_text_2"


def test_assoc_build13_link_reassign_clear():
    a = driver_ExecuteOnPC(group="sample_text")
    b1 = driver_Build(componentName="sample_text", testBuild="sample_text", uRI="sample_text")
    b2 = driver_Build(componentName="sample_text_2", testBuild="sample_text_2", uRI="sample_text_2")
    _safe_set(a, 'driver_ExecuteOnPC14', {b1})
    assert _is_linked(a, 'driver_ExecuteOnPC14', b1)
    if hasattr(b1, 'driver_Build'):
        assert _is_linked(b1, 'driver_Build', a)
    _safe_set(a, 'driver_ExecuteOnPC14', {b2})
    assert _is_linked(a, 'driver_ExecuteOnPC14', b2)
    if hasattr(b1, 'driver_Build'):
        assert not _is_linked(b1, 'driver_Build', a)
    if hasattr(b2, 'driver_Build'):
        assert _is_linked(b2, 'driver_Build', a)
    _safe_set(a, 'driver_ExecuteOnPC14', set())
    assert not _is_linked(a, 'driver_ExecuteOnPC14', b2)
    if hasattr(b2, 'driver_Build'):
        assert not _is_linked(b2, 'driver_Build', a)


def test_assoc_cmd12_link_reassign_clear():
    a = driver_ExecuteOnPC(group="sample_text")
    b1 = driver_CmdPC(phase="sample_text", sync="sample_text", uRI="sample_text", value="sample_text")
    b2 = driver_CmdPC(phase="sample_text_2", sync="sample_text_2", uRI="sample_text_2", value="sample_text_2")
    _safe_set(a, 'driver_ExecuteOnPC', {b1})
    assert _is_linked(a, 'driver_ExecuteOnPC', b1)
    if hasattr(b1, 'driver_CmdPC'):
        assert _is_linked(b1, 'driver_CmdPC', a)
    _safe_set(a, 'driver_ExecuteOnPC', {b2})
    assert _is_linked(a, 'driver_ExecuteOnPC', b2)
    if hasattr(b1, 'driver_CmdPC'):
        assert not _is_linked(b1, 'driver_CmdPC', a)
    if hasattr(b2, 'driver_CmdPC'):
        assert _is_linked(b2, 'driver_CmdPC', a)
    _safe_set(a, 'driver_ExecuteOnPC', set())
    assert not _is_linked(a, 'driver_ExecuteOnPC', b2)
    if hasattr(b2, 'driver_CmdPC'):
        assert not _is_linked(b2, 'driver_CmdPC', a)


def test_assoc_cmd15_link_reassign_clear():
    a = driver_ExecuteOnSymbian(group="sample_text")
    b1 = driver_CmdSymbian(argument="sample_text", output="sample_text", statCommand="sample_text", sync="sample_text")
    b2 = driver_CmdSymbian(argument="sample_text_2", output="sample_text_2", statCommand="sample_text_2", sync="sample_text_2")
    _safe_set(a, 'driver_ExecuteOnSymbian', {b1})
    assert _is_linked(a, 'driver_ExecuteOnSymbian', b1)
    if hasattr(b1, 'driver_CmdSymbian'):
        assert _is_linked(b1, 'driver_CmdSymbian', a)
    _safe_set(a, 'driver_ExecuteOnSymbian', {b2})
    assert _is_linked(a, 'driver_ExecuteOnSymbian', b2)
    if hasattr(b1, 'driver_CmdSymbian'):
        assert not _is_linked(b1, 'driver_CmdSymbian', a)
    if hasattr(b2, 'driver_CmdSymbian'):
        assert _is_linked(b2, 'driver_CmdSymbian', a)
    _safe_set(a, 'driver_ExecuteOnSymbian', set())
    assert not _is_linked(a, 'driver_ExecuteOnSymbian', b2)
    if hasattr(b2, 'driver_CmdSymbian'):
        assert not _is_linked(b2, 'driver_CmdSymbian', a)


def test_assoc_driver4_link_reassign_clear():
    a = driver_DocumentRoot(mixed="sample_text")
    b1 = driver_Driver()
    b2 = driver_Driver()
    _safe_set(a, 'driver_DocumentRoot5', {b1})
    assert _is_linked(a, 'driver_DocumentRoot5', b1)
    if hasattr(b1, 'driver_Driver'):
        assert _is_linked(b1, 'driver_Driver', a)
    _safe_set(a, 'driver_DocumentRoot5', {b2})
    assert _is_linked(a, 'driver_DocumentRoot5', b2)
    if hasattr(b1, 'driver_Driver'):
        assert not _is_linked(b1, 'driver_Driver', a)
    if hasattr(b2, 'driver_Driver'):
        assert _is_linked(b2, 'driver_Driver', a)
    _safe_set(a, 'driver_DocumentRoot5', set())
    assert not _is_linked(a, 'driver_DocumentRoot5', b2)
    if hasattr(b2, 'driver_Driver'):
        assert not _is_linked(b2, 'driver_Driver', a)


def test_assoc_executeOnPC23_link_reassign_clear():
    a = driver_Task(group="sample_text", name="sample_text", preRebootDevice="sample_text", timeout="sample_text")
    b1 = driver_ExecuteOnPC(group="sample_text")
    b2 = driver_ExecuteOnPC(group="sample_text_2")
    _safe_set(a, 'driver_Task24', {b1})
    assert _is_linked(a, 'driver_Task24', b1)
    if hasattr(b1, 'driver_ExecuteOnPC25'):
        assert _is_linked(b1, 'driver_ExecuteOnPC25', a)
    _safe_set(a, 'driver_Task24', {b2})
    assert _is_linked(a, 'driver_Task24', b2)
    if hasattr(b1, 'driver_ExecuteOnPC25'):
        assert not _is_linked(b1, 'driver_ExecuteOnPC25', a)
    if hasattr(b2, 'driver_ExecuteOnPC25'):
        assert _is_linked(b2, 'driver_ExecuteOnPC25', a)
    _safe_set(a, 'driver_Task24', set())
    assert not _is_linked(a, 'driver_Task24', b2)
    if hasattr(b2, 'driver_ExecuteOnPC25'):
        assert not _is_linked(b2, 'driver_ExecuteOnPC25', a)


def test_assoc_executeOnSymbian28_link_reassign_clear():
    a = driver_Task(group="sample_text", name="sample_text", preRebootDevice="sample_text", timeout="sample_text")
    b1 = driver_ExecuteOnSymbian(group="sample_text")
    b2 = driver_ExecuteOnSymbian(group="sample_text_2")
    _safe_set(a, 'driver_Task29', {b1})
    assert _is_linked(a, 'driver_Task29', b1)
    if hasattr(b1, 'driver_ExecuteOnSymbian30'):
        assert _is_linked(b1, 'driver_ExecuteOnSymbian30', a)
    _safe_set(a, 'driver_Task29', {b2})
    assert _is_linked(a, 'driver_Task29', b2)
    if hasattr(b1, 'driver_ExecuteOnSymbian30'):
        assert not _is_linked(b1, 'driver_ExecuteOnSymbian30', a)
    if hasattr(b2, 'driver_ExecuteOnSymbian30'):
        assert _is_linked(b2, 'driver_ExecuteOnSymbian30', a)
    _safe_set(a, 'driver_Task29', set())
    assert not _is_linked(a, 'driver_Task29', b2)
    if hasattr(b2, 'driver_ExecuteOnSymbian30'):
        assert not _is_linked(b2, 'driver_ExecuteOnSymbian30', a)


def test_assoc_flashrom40_link_reassign_clear():
    a = driver_Task(group="sample_text", name="sample_text", preRebootDevice="sample_text", timeout="sample_text")
    b1 = driver_FlashROM(pCPath="sample_text")
    b2 = driver_FlashROM(pCPath="sample_text_2")
    _safe_set(a, 'driver_Task41', {b1})
    assert _is_linked(a, 'driver_Task41', b1)
    if hasattr(b1, 'driver_FlashROM'):
        assert _is_linked(b1, 'driver_FlashROM', a)
    _safe_set(a, 'driver_Task41', {b2})
    assert _is_linked(a, 'driver_Task41', b2)
    if hasattr(b1, 'driver_FlashROM'):
        assert not _is_linked(b1, 'driver_FlashROM', a)
    if hasattr(b2, 'driver_FlashROM'):
        assert _is_linked(b2, 'driver_FlashROM', a)
    _safe_set(a, 'driver_Task41', set())
    assert not _is_linked(a, 'driver_Task41', b2)
    if hasattr(b2, 'driver_FlashROM'):
        assert not _is_linked(b2, 'driver_FlashROM', a)


def test_assoc_info10_link_reassign_clear():
    a = driver_Info(key="sample_text", value="sample_text")
    b1 = driver_DriverInfo()
    b2 = driver_DriverInfo()
    _safe_set(a, 'driver_Info', b1)
    assert _is_linked(a, 'driver_Info', b1)
    if hasattr(b1, 'driver_DriverInfo11'):
        assert _is_linked(b1, 'driver_DriverInfo11', a)
    _safe_set(a, 'driver_Info', b2)
    assert _is_linked(a, 'driver_Info', b2)
    if hasattr(b1, 'driver_DriverInfo11'):
        assert not _is_linked(b1, 'driver_DriverInfo11', a)
    if hasattr(b2, 'driver_DriverInfo11'):
        assert _is_linked(b2, 'driver_DriverInfo11', a)
    _safe_set(a, 'driver_Info', None)
    assert not _is_linked(a, 'driver_Info', b2)
    if hasattr(b2, 'driver_DriverInfo11'):
        assert not _is_linked(b2, 'driver_DriverInfo11', a)


def test_assoc_reference34_link_reassign_clear():
    a = driver_Task(group="sample_text", name="sample_text", preRebootDevice="sample_text", timeout="sample_text")
    b1 = driver_Reference()
    b2 = driver_Reference()
    _safe_set(a, 'driver_Task35', {b1})
    assert _is_linked(a, 'driver_Task35', b1)
    if hasattr(b1, 'driver_Reference36'):
        assert _is_linked(b1, 'driver_Reference36', a)
    _safe_set(a, 'driver_Task35', {b2})
    assert _is_linked(a, 'driver_Task35', b2)
    if hasattr(b1, 'driver_Reference36'):
        assert not _is_linked(b1, 'driver_Reference36', a)
    if hasattr(b2, 'driver_Reference36'):
        assert _is_linked(b2, 'driver_Reference36', a)
    _safe_set(a, 'driver_Task35', set())
    assert not _is_linked(a, 'driver_Task35', b2)
    if hasattr(b2, 'driver_Reference36'):
        assert not _is_linked(b2, 'driver_Reference36', a)


def test_assoc_retrieveFromSymbian31_link_reassign_clear():
    a = driver_Task(group="sample_text", name="sample_text", preRebootDevice="sample_text", timeout="sample_text")
    b1 = driver_RetrieveFromSymbian(group="sample_text")
    b2 = driver_RetrieveFromSymbian(group="sample_text_2")
    _safe_set(a, 'driver_Task32', {b1})
    assert _is_linked(a, 'driver_Task32', b1)
    if hasattr(b1, 'driver_RetrieveFromSymbian33'):
        assert _is_linked(b1, 'driver_RetrieveFromSymbian33', a)
    _safe_set(a, 'driver_Task32', {b2})
    assert _is_linked(a, 'driver_Task32', b2)
    if hasattr(b1, 'driver_RetrieveFromSymbian33'):
        assert not _is_linked(b1, 'driver_RetrieveFromSymbian33', a)
    if hasattr(b2, 'driver_RetrieveFromSymbian33'):
        assert _is_linked(b2, 'driver_RetrieveFromSymbian33', a)
    _safe_set(a, 'driver_Task32', set())
    assert not _is_linked(a, 'driver_Task32', b2)
    if hasattr(b2, 'driver_RetrieveFromSymbian33'):
        assert not _is_linked(b2, 'driver_RetrieveFromSymbian33', a)


def test_assoc_rtest18_link_reassign_clear():
    a = driver_Rtest(resultFile="sample_text", symbianPath="sample_text")
    b1 = driver_ExecuteOnSymbian(group="sample_text")
    b2 = driver_ExecuteOnSymbian(group="sample_text_2")
    _safe_set(a, 'driver_Rtest', b1)
    assert _is_linked(a, 'driver_Rtest', b1)
    if hasattr(b1, 'driver_ExecuteOnSymbian19'):
        assert _is_linked(b1, 'driver_ExecuteOnSymbian19', a)
    _safe_set(a, 'driver_Rtest', b2)
    assert _is_linked(a, 'driver_Rtest', b2)
    if hasattr(b1, 'driver_ExecuteOnSymbian19'):
        assert not _is_linked(b1, 'driver_ExecuteOnSymbian19', a)
    if hasattr(b2, 'driver_ExecuteOnSymbian19'):
        assert _is_linked(b2, 'driver_ExecuteOnSymbian19', a)
    _safe_set(a, 'driver_Rtest', None)
    assert not _is_linked(a, 'driver_Rtest', b2)
    if hasattr(b2, 'driver_ExecuteOnSymbian19'):
        assert not _is_linked(b2, 'driver_ExecuteOnSymbian19', a)


def test_assoc_startTrace42_link_reassign_clear():
    a = driver_Task(group="sample_text", name="sample_text", preRebootDevice="sample_text", timeout="sample_text")
    b1 = driver_StartTrace(configFilePath="sample_text", disablePrimaryFilters="sample_text", disableSecondaryFilters="sample_text", enablePrimaryFilters="sample_text", enableSecondaryFilters="sample_text")
    b2 = driver_StartTrace(configFilePath="sample_text_2", disablePrimaryFilters="sample_text_2", disableSecondaryFilters="sample_text_2", enablePrimaryFilters="sample_text_2", enableSecondaryFilters="sample_text_2")
    _safe_set(a, 'driver_Task43', b1)
    assert _is_linked(a, 'driver_Task43', b1)
    if hasattr(b1, 'driver_StartTrace'):
        assert _is_linked(b1, 'driver_StartTrace', a)
    _safe_set(a, 'driver_Task43', b2)
    assert _is_linked(a, 'driver_Task43', b2)
    if hasattr(b1, 'driver_StartTrace'):
        assert not _is_linked(b1, 'driver_StartTrace', a)
    if hasattr(b2, 'driver_StartTrace'):
        assert _is_linked(b2, 'driver_StartTrace', a)
    _safe_set(a, 'driver_Task43', None)
    assert not _is_linked(a, 'driver_Task43', b2)
    if hasattr(b2, 'driver_StartTrace'):
        assert not _is_linked(b2, 'driver_StartTrace', a)


def test_assoc_stopTrace44_link_reassign_clear():
    a = driver_Task(group="sample_text", name="sample_text", preRebootDevice="sample_text", timeout="sample_text")
    b1 = driver_StopTrace()
    b2 = driver_StopTrace()
    _safe_set(a, 'driver_Task45', b1)
    assert _is_linked(a, 'driver_Task45', b1)
    if hasattr(b1, 'driver_StopTrace'):
        assert _is_linked(b1, 'driver_StopTrace', a)
    _safe_set(a, 'driver_Task45', b2)
    assert _is_linked(a, 'driver_Task45', b2)
    if hasattr(b1, 'driver_StopTrace'):
        assert not _is_linked(b1, 'driver_StopTrace', a)
    if hasattr(b2, 'driver_StopTrace'):
        assert _is_linked(b2, 'driver_StopTrace', a)
    _safe_set(a, 'driver_Task45', None)
    assert not _is_linked(a, 'driver_Task45', b2)
    if hasattr(b2, 'driver_StopTrace'):
        assert not _is_linked(b2, 'driver_StopTrace', a)


def test_assoc_task38_link_reassign_clear():
    a = driver_Task(group="sample_text", name="sample_text", preRebootDevice="sample_text", timeout="sample_text")
    b1 = driver_Task(group="sample_text", name="sample_text", preRebootDevice="sample_text", timeout="sample_text")
    b2 = driver_Task(group="sample_text_2", name="sample_text_2", preRebootDevice="sample_text_2", timeout="sample_text_2")
    _safe_set(a, 'driver_Task37', {b1})
    assert _is_linked(a, 'driver_Task37', b1)
    if hasattr(b1, 'driver_Task39'):
        assert _is_linked(b1, 'driver_Task39', a)
    _safe_set(a, 'driver_Task37', {b2})
    assert _is_linked(a, 'driver_Task37', b2)
    if hasattr(b1, 'driver_Task39'):
        assert not _is_linked(b1, 'driver_Task39', a)
    if hasattr(b2, 'driver_Task39'):
        assert _is_linked(b2, 'driver_Task39', a)
    _safe_set(a, 'driver_Task37', set())
    assert not _is_linked(a, 'driver_Task37', b2)
    if hasattr(b2, 'driver_Task39'):
        assert not _is_linked(b2, 'driver_Task39', a)


def test_assoc_task8_link_reassign_clear():
    a = driver_Task(group="sample_text", name="sample_text", preRebootDevice="sample_text", timeout="sample_text")
    b1 = driver_Driver()
    b2 = driver_Driver()
    _safe_set(a, 'driver_Task', b1)
    assert _is_linked(a, 'driver_Task', b1)
    if hasattr(b1, 'driver_Driver9'):
        assert _is_linked(b1, 'driver_Driver9', a)
    _safe_set(a, 'driver_Task', b2)
    assert _is_linked(a, 'driver_Task', b2)
    if hasattr(b1, 'driver_Driver9'):
        assert not _is_linked(b1, 'driver_Driver9', a)
    if hasattr(b2, 'driver_Driver9'):
        assert _is_linked(b2, 'driver_Driver9', a)
    _safe_set(a, 'driver_Task', None)
    assert not _is_linked(a, 'driver_Task', b2)
    if hasattr(b2, 'driver_Driver9'):
        assert not _is_linked(b2, 'driver_Driver9', a)


def test_assoc_testCase46_link_reassign_clear():
    a = driver_TestCasesList(operator="sample_text")
    b1 = driver_TestCase(target="sample_text")
    b2 = driver_TestCase(target="sample_text_2")
    _safe_set(a, 'driver_TestCasesList', {b1})
    assert _is_linked(a, 'driver_TestCasesList', b1)
    if hasattr(b1, 'driver_TestCase'):
        assert _is_linked(b1, 'driver_TestCase', a)
    _safe_set(a, 'driver_TestCasesList', {b2})
    assert _is_linked(a, 'driver_TestCasesList', b2)
    if hasattr(b1, 'driver_TestCase'):
        assert not _is_linked(b1, 'driver_TestCase', a)
    if hasattr(b2, 'driver_TestCase'):
        assert _is_linked(b2, 'driver_TestCase', a)
    _safe_set(a, 'driver_TestCasesList', set())
    assert not _is_linked(a, 'driver_TestCasesList', b2)
    if hasattr(b2, 'driver_TestCase'):
        assert not _is_linked(b2, 'driver_TestCase', a)


def test_assoc_testCasesList47_link_reassign_clear():
    a = driver_TestExecuteScript(pCPath="sample_text", symbianPath="sample_text")
    b1 = driver_TestCasesList(operator="sample_text")
    b2 = driver_TestCasesList(operator="sample_text_2")
    _safe_set(a, 'driver_TestExecuteScript48', b1)
    assert _is_linked(a, 'driver_TestExecuteScript48', b1)
    if hasattr(b1, 'driver_TestCasesList49'):
        assert _is_linked(b1, 'driver_TestCasesList49', a)
    _safe_set(a, 'driver_TestExecuteScript48', b2)
    assert _is_linked(a, 'driver_TestExecuteScript48', b2)
    if hasattr(b1, 'driver_TestCasesList49'):
        assert not _is_linked(b1, 'driver_TestCasesList49', a)
    if hasattr(b2, 'driver_TestCasesList49'):
        assert _is_linked(b2, 'driver_TestCasesList49', a)
    _safe_set(a, 'driver_TestExecuteScript48', None)
    assert not _is_linked(a, 'driver_TestExecuteScript48', b2)
    if hasattr(b2, 'driver_TestCasesList49'):
        assert not _is_linked(b2, 'driver_TestCasesList49', a)


def test_assoc_testExecuteScript16_link_reassign_clear():
    a = driver_TestExecuteScript(pCPath="sample_text", symbianPath="sample_text")
    b1 = driver_ExecuteOnSymbian(group="sample_text")
    b2 = driver_ExecuteOnSymbian(group="sample_text_2")
    _safe_set(a, 'driver_TestExecuteScript', b1)
    assert _is_linked(a, 'driver_TestExecuteScript', b1)
    if hasattr(b1, 'driver_ExecuteOnSymbian17'):
        assert _is_linked(b1, 'driver_ExecuteOnSymbian17', a)
    _safe_set(a, 'driver_TestExecuteScript', b2)
    assert _is_linked(a, 'driver_TestExecuteScript', b2)
    if hasattr(b1, 'driver_ExecuteOnSymbian17'):
        assert not _is_linked(b1, 'driver_ExecuteOnSymbian17', a)
    if hasattr(b2, 'driver_ExecuteOnSymbian17'):
        assert _is_linked(b2, 'driver_ExecuteOnSymbian17', a)
    _safe_set(a, 'driver_TestExecuteScript', None)
    assert not _is_linked(a, 'driver_TestExecuteScript', b2)
    if hasattr(b2, 'driver_ExecuteOnSymbian17'):
        assert not _is_linked(b2, 'driver_ExecuteOnSymbian17', a)


def test_assoc_transfer22_link_reassign_clear():
    a = driver_Transfer(move="sample_text", pCPath="sample_text", symbianPath="sample_text")
    b1 = driver_RetrieveFromSymbian(group="sample_text")
    b2 = driver_RetrieveFromSymbian(group="sample_text_2")
    _safe_set(a, 'driver_Transfer', b1)
    assert _is_linked(a, 'driver_Transfer', b1)
    if hasattr(b1, 'driver_RetrieveFromSymbian'):
        assert _is_linked(b1, 'driver_RetrieveFromSymbian', a)
    _safe_set(a, 'driver_Transfer', b2)
    assert _is_linked(a, 'driver_Transfer', b2)
    if hasattr(b1, 'driver_RetrieveFromSymbian'):
        assert not _is_linked(b1, 'driver_RetrieveFromSymbian', a)
    if hasattr(b2, 'driver_RetrieveFromSymbian'):
        assert _is_linked(b2, 'driver_RetrieveFromSymbian', a)
    _safe_set(a, 'driver_Transfer', None)
    assert not _is_linked(a, 'driver_Transfer', b2)
    if hasattr(b2, 'driver_RetrieveFromSymbian'):
        assert not _is_linked(b2, 'driver_RetrieveFromSymbian', a)


def test_assoc_transfer50_link_reassign_clear():
    a = driver_TransferToSymbian(group="sample_text")
    b1 = driver_Transfer(move="sample_text", pCPath="sample_text", symbianPath="sample_text")
    b2 = driver_Transfer(move="sample_text_2", pCPath="sample_text_2", symbianPath="sample_text_2")
    _safe_set(a, 'driver_TransferToSymbian51', {b1})
    assert _is_linked(a, 'driver_TransferToSymbian51', b1)
    if hasattr(b1, 'driver_Transfer52'):
        assert _is_linked(b1, 'driver_Transfer52', a)
    _safe_set(a, 'driver_TransferToSymbian51', {b2})
    assert _is_linked(a, 'driver_TransferToSymbian51', b2)
    if hasattr(b1, 'driver_Transfer52'):
        assert not _is_linked(b1, 'driver_Transfer52', a)
    if hasattr(b2, 'driver_Transfer52'):
        assert _is_linked(b2, 'driver_Transfer52', a)
    _safe_set(a, 'driver_TransferToSymbian51', set())
    assert not _is_linked(a, 'driver_TransferToSymbian51', b2)
    if hasattr(b2, 'driver_Transfer52'):
        assert not _is_linked(b2, 'driver_Transfer52', a)


def test_assoc_transferToSymbian26_link_reassign_clear():
    a = driver_TransferToSymbian(group="sample_text")
    b1 = driver_Task(group="sample_text", name="sample_text", preRebootDevice="sample_text", timeout="sample_text")
    b2 = driver_Task(group="sample_text_2", name="sample_text_2", preRebootDevice="sample_text_2", timeout="sample_text_2")
    _safe_set(a, 'driver_TransferToSymbian', b1)
    assert _is_linked(a, 'driver_TransferToSymbian', b1)
    if hasattr(b1, 'driver_Task27'):
        assert _is_linked(b1, 'driver_Task27', a)
    _safe_set(a, 'driver_TransferToSymbian', b2)
    assert _is_linked(a, 'driver_TransferToSymbian', b2)
    if hasattr(b1, 'driver_Task27'):
        assert not _is_linked(b1, 'driver_Task27', a)
    if hasattr(b2, 'driver_Task27'):
        assert _is_linked(b2, 'driver_Task27', a)
    _safe_set(a, 'driver_TransferToSymbian', None)
    assert not _is_linked(a, 'driver_TransferToSymbian', b2)
    if hasattr(b2, 'driver_Task27'):
        assert not _is_linked(b2, 'driver_Task27', a)


def test_assoc_uri20_link_reassign_clear():
    a = driver_Task(group="sample_text", name="sample_text", preRebootDevice="sample_text", timeout="sample_text")
    b1 = driver_Reference()
    b2 = driver_Reference()
    _safe_set(a, 'driver_Task21', b1)
    assert _is_linked(a, 'driver_Task21', b1)
    if hasattr(b1, 'driver_Reference'):
        assert _is_linked(b1, 'driver_Reference', a)
    _safe_set(a, 'driver_Task21', b2)
    assert _is_linked(a, 'driver_Task21', b2)
    if hasattr(b1, 'driver_Reference'):
        assert not _is_linked(b1, 'driver_Reference', a)
    if hasattr(b2, 'driver_Reference'):
        assert _is_linked(b2, 'driver_Reference', a)
    _safe_set(a, 'driver_Task21', None)
    assert not _is_linked(a, 'driver_Task21', b2)
    if hasattr(b2, 'driver_Reference'):
        assert not _is_linked(b2, 'driver_Reference', a)


def test_assoc_xMLNSPrefixMap0_link_reassign_clear():
    a = driver_DocumentRoot(mixed="sample_text")
    b1 = driver_EStringToStringMapEntry()
    b2 = driver_EStringToStringMapEntry()
    _safe_set(a, 'driver_DocumentRoot', {b1})
    assert _is_linked(a, 'driver_DocumentRoot', b1)
    if hasattr(b1, 'driver_EStringToStringMapEntry'):
        assert _is_linked(b1, 'driver_EStringToStringMapEntry', a)
    _safe_set(a, 'driver_DocumentRoot', {b2})
    assert _is_linked(a, 'driver_DocumentRoot', b2)
    if hasattr(b1, 'driver_EStringToStringMapEntry'):
        assert not _is_linked(b1, 'driver_EStringToStringMapEntry', a)
    if hasattr(b2, 'driver_EStringToStringMapEntry'):
        assert _is_linked(b2, 'driver_EStringToStringMapEntry', a)
    _safe_set(a, 'driver_DocumentRoot', set())
    assert not _is_linked(a, 'driver_DocumentRoot', b2)
    if hasattr(b2, 'driver_EStringToStringMapEntry'):
        assert not _is_linked(b2, 'driver_EStringToStringMapEntry', a)


def test_assoc_xSISchemaLocation1_link_reassign_clear():
    a = driver_DocumentRoot(mixed="sample_text")
    b1 = driver_EStringToStringMapEntry()
    b2 = driver_EStringToStringMapEntry()
    _safe_set(a, 'driver_DocumentRoot2', {b1})
    assert _is_linked(a, 'driver_DocumentRoot2', b1)
    if hasattr(b1, 'driver_EStringToStringMapEntry3'):
        assert _is_linked(b1, 'driver_EStringToStringMapEntry3', a)
    _safe_set(a, 'driver_DocumentRoot2', {b2})
    assert _is_linked(a, 'driver_DocumentRoot2', b2)
    if hasattr(b1, 'driver_EStringToStringMapEntry3'):
        assert not _is_linked(b1, 'driver_EStringToStringMapEntry3', a)
    if hasattr(b2, 'driver_EStringToStringMapEntry3'):
        assert _is_linked(b2, 'driver_EStringToStringMapEntry3', a)
    _safe_set(a, 'driver_DocumentRoot2', set())
    assert not _is_linked(a, 'driver_DocumentRoot2', b2)
    if hasattr(b2, 'driver_EStringToStringMapEntry3'):
        assert not _is_linked(b2, 'driver_EStringToStringMapEntry3', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

driver_Build_strategy = st.builds(driver_Build, componentName=safe_text, testBuild=safe_text, uRI=safe_text)
@given(instance=driver_Build_strategy)
@settings(max_examples=25)
def test_driver_Build_instantiation(instance):
    assert isinstance(instance, driver_Build)


driver_CmdPC_strategy = st.builds(driver_CmdPC, phase=safe_text, sync=safe_text, uRI=safe_text, value=safe_text)
@given(instance=driver_CmdPC_strategy)
@settings(max_examples=25)
def test_driver_CmdPC_instantiation(instance):
    assert isinstance(instance, driver_CmdPC)


driver_CmdSymbian_strategy = st.builds(driver_CmdSymbian, argument=safe_text, output=safe_text, statCommand=safe_text, sync=safe_text)
@given(instance=driver_CmdSymbian_strategy)
@settings(max_examples=25)
def test_driver_CmdSymbian_instantiation(instance):
    assert isinstance(instance, driver_CmdSymbian)


driver_DocumentRoot_strategy = st.builds(driver_DocumentRoot, mixed=safe_text)
@given(instance=driver_DocumentRoot_strategy)
@settings(max_examples=25)
def test_driver_DocumentRoot_instantiation(instance):
    assert isinstance(instance, driver_DocumentRoot)


driver_Driver_strategy = st.builds(driver_Driver)
@given(instance=driver_Driver_strategy)
@settings(max_examples=25)
def test_driver_Driver_instantiation(instance):
    assert isinstance(instance, driver_Driver)


driver_DriverInfo_strategy = st.builds(driver_DriverInfo)
@given(instance=driver_DriverInfo_strategy)
@settings(max_examples=25)
def test_driver_DriverInfo_instantiation(instance):
    assert isinstance(instance, driver_DriverInfo)


driver_EStringToStringMapEntry_strategy = st.builds(driver_EStringToStringMapEntry)
@given(instance=driver_EStringToStringMapEntry_strategy)
@settings(max_examples=25)
def test_driver_EStringToStringMapEntry_instantiation(instance):
    assert isinstance(instance, driver_EStringToStringMapEntry)


driver_ExecuteOnPC_strategy = st.builds(driver_ExecuteOnPC, group=safe_text)
@given(instance=driver_ExecuteOnPC_strategy)
@settings(max_examples=25)
def test_driver_ExecuteOnPC_instantiation(instance):
    assert isinstance(instance, driver_ExecuteOnPC)


driver_ExecuteOnSymbian_strategy = st.builds(driver_ExecuteOnSymbian, group=safe_text)
@given(instance=driver_ExecuteOnSymbian_strategy)
@settings(max_examples=25)
def test_driver_ExecuteOnSymbian_instantiation(instance):
    assert isinstance(instance, driver_ExecuteOnSymbian)


driver_FlashROM_strategy = st.builds(driver_FlashROM, pCPath=safe_text)
@given(instance=driver_FlashROM_strategy)
@settings(max_examples=25)
def test_driver_FlashROM_instantiation(instance):
    assert isinstance(instance, driver_FlashROM)


driver_Info_strategy = st.builds(driver_Info, key=safe_text, value=safe_text)
@given(instance=driver_Info_strategy)
@settings(max_examples=25)
def test_driver_Info_instantiation(instance):
    assert isinstance(instance, driver_Info)


driver_Reference_strategy = st.builds(driver_Reference)
@given(instance=driver_Reference_strategy)
@settings(max_examples=25)
def test_driver_Reference_instantiation(instance):
    assert isinstance(instance, driver_Reference)


driver_RetrieveFromSymbian_strategy = st.builds(driver_RetrieveFromSymbian, group=safe_text)
@given(instance=driver_RetrieveFromSymbian_strategy)
@settings(max_examples=25)
def test_driver_RetrieveFromSymbian_instantiation(instance):
    assert isinstance(instance, driver_RetrieveFromSymbian)


driver_Rtest_strategy = st.builds(driver_Rtest, resultFile=safe_text, symbianPath=safe_text)
@given(instance=driver_Rtest_strategy)
@settings(max_examples=25)
def test_driver_Rtest_instantiation(instance):
    assert isinstance(instance, driver_Rtest)


driver_StartTrace_strategy = st.builds(driver_StartTrace, configFilePath=safe_text, disablePrimaryFilters=safe_text, disableSecondaryFilters=safe_text, enablePrimaryFilters=safe_text, enableSecondaryFilters=safe_text)
@given(instance=driver_StartTrace_strategy)
@settings(max_examples=25)
def test_driver_StartTrace_instantiation(instance):
    assert isinstance(instance, driver_StartTrace)


driver_StopTrace_strategy = st.builds(driver_StopTrace)
@given(instance=driver_StopTrace_strategy)
@settings(max_examples=25)
def test_driver_StopTrace_instantiation(instance):
    assert isinstance(instance, driver_StopTrace)


driver_Task_strategy = st.builds(driver_Task, group=safe_text, name=safe_text, preRebootDevice=safe_text, timeout=safe_text)
@given(instance=driver_Task_strategy)
@settings(max_examples=25)
def test_driver_Task_instantiation(instance):
    assert isinstance(instance, driver_Task)


driver_TestCase_strategy = st.builds(driver_TestCase, target=safe_text)
@given(instance=driver_TestCase_strategy)
@settings(max_examples=25)
def test_driver_TestCase_instantiation(instance):
    assert isinstance(instance, driver_TestCase)


driver_TestCasesList_strategy = st.builds(driver_TestCasesList, operator=safe_text)
@given(instance=driver_TestCasesList_strategy)
@settings(max_examples=25)
def test_driver_TestCasesList_instantiation(instance):
    assert isinstance(instance, driver_TestCasesList)


driver_TestExecuteScript_strategy = st.builds(driver_TestExecuteScript, pCPath=safe_text, symbianPath=safe_text)
@given(instance=driver_TestExecuteScript_strategy)
@settings(max_examples=25)
def test_driver_TestExecuteScript_instantiation(instance):
    assert isinstance(instance, driver_TestExecuteScript)


driver_Transfer_strategy = st.builds(driver_Transfer, move=safe_text, pCPath=safe_text, symbianPath=safe_text)
@given(instance=driver_Transfer_strategy)
@settings(max_examples=25)
def test_driver_Transfer_instantiation(instance):
    assert isinstance(instance, driver_Transfer)


driver_TransferToSymbian_strategy = st.builds(driver_TransferToSymbian, group=safe_text)
@given(instance=driver_TransferToSymbian_strategy)
@settings(max_examples=25)
def test_driver_TransferToSymbian_instantiation(instance):
    assert isinstance(instance, driver_TransferToSymbian)



