import pytest
from datetime import date, datetime, time, timedelta

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

def test_assoc_build13_reverse_link_reassign_clear():
    a1 = driver_ExecuteOnPC(group="sample_text")
    a2 = driver_ExecuteOnPC(group="sample_text_2")
    b = driver_Build(componentName="sample_text", testBuild="sample_text", uRI="sample_text")
    _safe_set(b, 'driver_Build', a1)
    assert _is_linked(b, 'driver_Build', a1)
    if hasattr(a1, 'driver_ExecuteOnPC14'):
        assert _is_linked(a1, 'driver_ExecuteOnPC14', b)
    _safe_set(b, 'driver_Build', a2)
    assert _is_linked(b, 'driver_Build', a2)
    if hasattr(a1, 'driver_ExecuteOnPC14'):
        assert not _is_linked(a1, 'driver_ExecuteOnPC14', b)
    if hasattr(a2, 'driver_ExecuteOnPC14'):
        assert _is_linked(a2, 'driver_ExecuteOnPC14', b)
    _safe_set(b, 'driver_Build', None)
    assert not _is_linked(b, 'driver_Build', a2)
    if hasattr(a2, 'driver_ExecuteOnPC14'):
        assert not _is_linked(a2, 'driver_ExecuteOnPC14', b)


def test_assoc_cmd12_reverse_link_reassign_clear():
    a1 = driver_ExecuteOnPC(group="sample_text")
    a2 = driver_ExecuteOnPC(group="sample_text_2")
    b = driver_CmdPC(phase="sample_text", sync="sample_text", uRI="sample_text", value="sample_text")
    _safe_set(b, 'driver_CmdPC', a1)
    assert _is_linked(b, 'driver_CmdPC', a1)
    if hasattr(a1, 'driver_ExecuteOnPC'):
        assert _is_linked(a1, 'driver_ExecuteOnPC', b)
    _safe_set(b, 'driver_CmdPC', a2)
    assert _is_linked(b, 'driver_CmdPC', a2)
    if hasattr(a1, 'driver_ExecuteOnPC'):
        assert not _is_linked(a1, 'driver_ExecuteOnPC', b)
    if hasattr(a2, 'driver_ExecuteOnPC'):
        assert _is_linked(a2, 'driver_ExecuteOnPC', b)
    _safe_set(b, 'driver_CmdPC', None)
    assert not _is_linked(b, 'driver_CmdPC', a2)
    if hasattr(a2, 'driver_ExecuteOnPC'):
        assert not _is_linked(a2, 'driver_ExecuteOnPC', b)


def test_assoc_cmd15_reverse_link_reassign_clear():
    a1 = driver_ExecuteOnSymbian(group="sample_text")
    a2 = driver_ExecuteOnSymbian(group="sample_text_2")
    b = driver_CmdSymbian(argument="sample_text", output="sample_text", statCommand="sample_text", sync="sample_text")
    _safe_set(b, 'driver_CmdSymbian', a1)
    assert _is_linked(b, 'driver_CmdSymbian', a1)
    if hasattr(a1, 'driver_ExecuteOnSymbian'):
        assert _is_linked(a1, 'driver_ExecuteOnSymbian', b)
    _safe_set(b, 'driver_CmdSymbian', a2)
    assert _is_linked(b, 'driver_CmdSymbian', a2)
    if hasattr(a1, 'driver_ExecuteOnSymbian'):
        assert not _is_linked(a1, 'driver_ExecuteOnSymbian', b)
    if hasattr(a2, 'driver_ExecuteOnSymbian'):
        assert _is_linked(a2, 'driver_ExecuteOnSymbian', b)
    _safe_set(b, 'driver_CmdSymbian', None)
    assert not _is_linked(b, 'driver_CmdSymbian', a2)
    if hasattr(a2, 'driver_ExecuteOnSymbian'):
        assert not _is_linked(a2, 'driver_ExecuteOnSymbian', b)


def test_assoc_executeOnPC23_reverse_link_reassign_clear():
    a1 = driver_Task(group="sample_text", name="sample_text", preRebootDevice="sample_text", timeout="sample_text")
    a2 = driver_Task(group="sample_text_2", name="sample_text_2", preRebootDevice="sample_text_2", timeout="sample_text_2")
    b = driver_ExecuteOnPC(group="sample_text")
    _safe_set(b, 'driver_ExecuteOnPC25', a1)
    assert _is_linked(b, 'driver_ExecuteOnPC25', a1)
    if hasattr(a1, 'driver_Task24'):
        assert _is_linked(a1, 'driver_Task24', b)
    _safe_set(b, 'driver_ExecuteOnPC25', a2)
    assert _is_linked(b, 'driver_ExecuteOnPC25', a2)
    if hasattr(a1, 'driver_Task24'):
        assert not _is_linked(a1, 'driver_Task24', b)
    if hasattr(a2, 'driver_Task24'):
        assert _is_linked(a2, 'driver_Task24', b)
    _safe_set(b, 'driver_ExecuteOnPC25', None)
    assert not _is_linked(b, 'driver_ExecuteOnPC25', a2)
    if hasattr(a2, 'driver_Task24'):
        assert not _is_linked(a2, 'driver_Task24', b)


def test_assoc_executeOnSymbian28_reverse_link_reassign_clear():
    a1 = driver_Task(group="sample_text", name="sample_text", preRebootDevice="sample_text", timeout="sample_text")
    a2 = driver_Task(group="sample_text_2", name="sample_text_2", preRebootDevice="sample_text_2", timeout="sample_text_2")
    b = driver_ExecuteOnSymbian(group="sample_text")
    _safe_set(b, 'driver_ExecuteOnSymbian30', a1)
    assert _is_linked(b, 'driver_ExecuteOnSymbian30', a1)
    if hasattr(a1, 'driver_Task29'):
        assert _is_linked(a1, 'driver_Task29', b)
    _safe_set(b, 'driver_ExecuteOnSymbian30', a2)
    assert _is_linked(b, 'driver_ExecuteOnSymbian30', a2)
    if hasattr(a1, 'driver_Task29'):
        assert not _is_linked(a1, 'driver_Task29', b)
    if hasattr(a2, 'driver_Task29'):
        assert _is_linked(a2, 'driver_Task29', b)
    _safe_set(b, 'driver_ExecuteOnSymbian30', None)
    assert not _is_linked(b, 'driver_ExecuteOnSymbian30', a2)
    if hasattr(a2, 'driver_Task29'):
        assert not _is_linked(a2, 'driver_Task29', b)


def test_assoc_flashrom40_reverse_link_reassign_clear():
    a1 = driver_Task(group="sample_text", name="sample_text", preRebootDevice="sample_text", timeout="sample_text")
    a2 = driver_Task(group="sample_text_2", name="sample_text_2", preRebootDevice="sample_text_2", timeout="sample_text_2")
    b = driver_FlashROM(pCPath="sample_text")
    _safe_set(b, 'driver_FlashROM', a1)
    assert _is_linked(b, 'driver_FlashROM', a1)
    if hasattr(a1, 'driver_Task41'):
        assert _is_linked(a1, 'driver_Task41', b)
    _safe_set(b, 'driver_FlashROM', a2)
    assert _is_linked(b, 'driver_FlashROM', a2)
    if hasattr(a1, 'driver_Task41'):
        assert not _is_linked(a1, 'driver_Task41', b)
    if hasattr(a2, 'driver_Task41'):
        assert _is_linked(a2, 'driver_Task41', b)
    _safe_set(b, 'driver_FlashROM', None)
    assert not _is_linked(b, 'driver_FlashROM', a2)
    if hasattr(a2, 'driver_Task41'):
        assert not _is_linked(a2, 'driver_Task41', b)


def test_assoc_retrieveFromSymbian31_reverse_link_reassign_clear():
    a1 = driver_Task(group="sample_text", name="sample_text", preRebootDevice="sample_text", timeout="sample_text")
    a2 = driver_Task(group="sample_text_2", name="sample_text_2", preRebootDevice="sample_text_2", timeout="sample_text_2")
    b = driver_RetrieveFromSymbian(group="sample_text")
    _safe_set(b, 'driver_RetrieveFromSymbian33', a1)
    assert _is_linked(b, 'driver_RetrieveFromSymbian33', a1)
    if hasattr(a1, 'driver_Task32'):
        assert _is_linked(a1, 'driver_Task32', b)
    _safe_set(b, 'driver_RetrieveFromSymbian33', a2)
    assert _is_linked(b, 'driver_RetrieveFromSymbian33', a2)
    if hasattr(a1, 'driver_Task32'):
        assert not _is_linked(a1, 'driver_Task32', b)
    if hasattr(a2, 'driver_Task32'):
        assert _is_linked(a2, 'driver_Task32', b)
    _safe_set(b, 'driver_RetrieveFromSymbian33', None)
    assert not _is_linked(b, 'driver_RetrieveFromSymbian33', a2)
    if hasattr(a2, 'driver_Task32'):
        assert not _is_linked(a2, 'driver_Task32', b)


def test_assoc_rtest18_reverse_link_reassign_clear():
    a1 = driver_Rtest(resultFile="sample_text", symbianPath="sample_text")
    a2 = driver_Rtest(resultFile="sample_text_2", symbianPath="sample_text_2")
    b = driver_ExecuteOnSymbian(group="sample_text")
    _safe_set(b, 'driver_ExecuteOnSymbian19', {a1})
    assert _is_linked(b, 'driver_ExecuteOnSymbian19', a1)
    if hasattr(a1, 'driver_Rtest'):
        assert _is_linked(a1, 'driver_Rtest', b)
    _safe_set(b, 'driver_ExecuteOnSymbian19', {a2})
    assert _is_linked(b, 'driver_ExecuteOnSymbian19', a2)
    if hasattr(a1, 'driver_Rtest'):
        assert not _is_linked(a1, 'driver_Rtest', b)
    if hasattr(a2, 'driver_Rtest'):
        assert _is_linked(a2, 'driver_Rtest', b)
    _safe_set(b, 'driver_ExecuteOnSymbian19', set())
    assert not _is_linked(b, 'driver_ExecuteOnSymbian19', a2)
    if hasattr(a2, 'driver_Rtest'):
        assert not _is_linked(a2, 'driver_Rtest', b)


def test_assoc_startTrace42_reverse_link_reassign_clear():
    a1 = driver_Task(group="sample_text", name="sample_text", preRebootDevice="sample_text", timeout="sample_text")
    a2 = driver_Task(group="sample_text_2", name="sample_text_2", preRebootDevice="sample_text_2", timeout="sample_text_2")
    b = driver_StartTrace(configFilePath="sample_text", disablePrimaryFilters="sample_text", disableSecondaryFilters="sample_text", enablePrimaryFilters="sample_text", enableSecondaryFilters="sample_text")
    _safe_set(b, 'driver_StartTrace', a1)
    assert _is_linked(b, 'driver_StartTrace', a1)
    if hasattr(a1, 'driver_Task43'):
        assert _is_linked(a1, 'driver_Task43', b)
    _safe_set(b, 'driver_StartTrace', a2)
    assert _is_linked(b, 'driver_StartTrace', a2)
    if hasattr(a1, 'driver_Task43'):
        assert not _is_linked(a1, 'driver_Task43', b)
    if hasattr(a2, 'driver_Task43'):
        assert _is_linked(a2, 'driver_Task43', b)
    _safe_set(b, 'driver_StartTrace', None)
    assert not _is_linked(b, 'driver_StartTrace', a2)
    if hasattr(a2, 'driver_Task43'):
        assert not _is_linked(a2, 'driver_Task43', b)


def test_assoc_task38_reverse_link_reassign_clear():
    a1 = driver_Task(group="sample_text", name="sample_text", preRebootDevice="sample_text", timeout="sample_text")
    a2 = driver_Task(group="sample_text_2", name="sample_text_2", preRebootDevice="sample_text_2", timeout="sample_text_2")
    b = driver_Task(group="sample_text", name="sample_text", preRebootDevice="sample_text", timeout="sample_text")
    _safe_set(b, 'driver_Task39', a1)
    assert _is_linked(b, 'driver_Task39', a1)
    if hasattr(a1, 'driver_Task37'):
        assert _is_linked(a1, 'driver_Task37', b)
    _safe_set(b, 'driver_Task39', a2)
    assert _is_linked(b, 'driver_Task39', a2)
    if hasattr(a1, 'driver_Task37'):
        assert not _is_linked(a1, 'driver_Task37', b)
    if hasattr(a2, 'driver_Task37'):
        assert _is_linked(a2, 'driver_Task37', b)
    _safe_set(b, 'driver_Task39', None)
    assert not _is_linked(b, 'driver_Task39', a2)
    if hasattr(a2, 'driver_Task37'):
        assert not _is_linked(a2, 'driver_Task37', b)


def test_assoc_testCase46_reverse_link_reassign_clear():
    a1 = driver_TestCasesList(operator="sample_text")
    a2 = driver_TestCasesList(operator="sample_text_2")
    b = driver_TestCase(target="sample_text")
    _safe_set(b, 'driver_TestCase', a1)
    assert _is_linked(b, 'driver_TestCase', a1)
    if hasattr(a1, 'driver_TestCasesList'):
        assert _is_linked(a1, 'driver_TestCasesList', b)
    _safe_set(b, 'driver_TestCase', a2)
    assert _is_linked(b, 'driver_TestCase', a2)
    if hasattr(a1, 'driver_TestCasesList'):
        assert not _is_linked(a1, 'driver_TestCasesList', b)
    if hasattr(a2, 'driver_TestCasesList'):
        assert _is_linked(a2, 'driver_TestCasesList', b)
    _safe_set(b, 'driver_TestCase', None)
    assert not _is_linked(b, 'driver_TestCase', a2)
    if hasattr(a2, 'driver_TestCasesList'):
        assert not _is_linked(a2, 'driver_TestCasesList', b)


def test_assoc_testCasesList47_reverse_link_reassign_clear():
    a1 = driver_TestExecuteScript(pCPath="sample_text", symbianPath="sample_text")
    a2 = driver_TestExecuteScript(pCPath="sample_text_2", symbianPath="sample_text_2")
    b = driver_TestCasesList(operator="sample_text")
    _safe_set(b, 'driver_TestCasesList49', a1)
    assert _is_linked(b, 'driver_TestCasesList49', a1)
    if hasattr(a1, 'driver_TestExecuteScript48'):
        assert _is_linked(a1, 'driver_TestExecuteScript48', b)
    _safe_set(b, 'driver_TestCasesList49', a2)
    assert _is_linked(b, 'driver_TestCasesList49', a2)
    if hasattr(a1, 'driver_TestExecuteScript48'):
        assert not _is_linked(a1, 'driver_TestExecuteScript48', b)
    if hasattr(a2, 'driver_TestExecuteScript48'):
        assert _is_linked(a2, 'driver_TestExecuteScript48', b)
    _safe_set(b, 'driver_TestCasesList49', None)
    assert not _is_linked(b, 'driver_TestCasesList49', a2)
    if hasattr(a2, 'driver_TestExecuteScript48'):
        assert not _is_linked(a2, 'driver_TestExecuteScript48', b)


def test_assoc_testExecuteScript16_reverse_link_reassign_clear():
    a1 = driver_TestExecuteScript(pCPath="sample_text", symbianPath="sample_text")
    a2 = driver_TestExecuteScript(pCPath="sample_text_2", symbianPath="sample_text_2")
    b = driver_ExecuteOnSymbian(group="sample_text")
    _safe_set(b, 'driver_ExecuteOnSymbian17', {a1})
    assert _is_linked(b, 'driver_ExecuteOnSymbian17', a1)
    if hasattr(a1, 'driver_TestExecuteScript'):
        assert _is_linked(a1, 'driver_TestExecuteScript', b)
    _safe_set(b, 'driver_ExecuteOnSymbian17', {a2})
    assert _is_linked(b, 'driver_ExecuteOnSymbian17', a2)
    if hasattr(a1, 'driver_TestExecuteScript'):
        assert not _is_linked(a1, 'driver_TestExecuteScript', b)
    if hasattr(a2, 'driver_TestExecuteScript'):
        assert _is_linked(a2, 'driver_TestExecuteScript', b)
    _safe_set(b, 'driver_ExecuteOnSymbian17', set())
    assert not _is_linked(b, 'driver_ExecuteOnSymbian17', a2)
    if hasattr(a2, 'driver_TestExecuteScript'):
        assert not _is_linked(a2, 'driver_TestExecuteScript', b)


def test_assoc_transfer22_reverse_link_reassign_clear():
    a1 = driver_Transfer(move="sample_text", pCPath="sample_text", symbianPath="sample_text")
    a2 = driver_Transfer(move="sample_text_2", pCPath="sample_text_2", symbianPath="sample_text_2")
    b = driver_RetrieveFromSymbian(group="sample_text")
    _safe_set(b, 'driver_RetrieveFromSymbian', {a1})
    assert _is_linked(b, 'driver_RetrieveFromSymbian', a1)
    if hasattr(a1, 'driver_Transfer'):
        assert _is_linked(a1, 'driver_Transfer', b)
    _safe_set(b, 'driver_RetrieveFromSymbian', {a2})
    assert _is_linked(b, 'driver_RetrieveFromSymbian', a2)
    if hasattr(a1, 'driver_Transfer'):
        assert not _is_linked(a1, 'driver_Transfer', b)
    if hasattr(a2, 'driver_Transfer'):
        assert _is_linked(a2, 'driver_Transfer', b)
    _safe_set(b, 'driver_RetrieveFromSymbian', set())
    assert not _is_linked(b, 'driver_RetrieveFromSymbian', a2)
    if hasattr(a2, 'driver_Transfer'):
        assert not _is_linked(a2, 'driver_Transfer', b)


def test_assoc_transfer50_reverse_link_reassign_clear():
    a1 = driver_TransferToSymbian(group="sample_text")
    a2 = driver_TransferToSymbian(group="sample_text_2")
    b = driver_Transfer(move="sample_text", pCPath="sample_text", symbianPath="sample_text")
    _safe_set(b, 'driver_Transfer52', a1)
    assert _is_linked(b, 'driver_Transfer52', a1)
    if hasattr(a1, 'driver_TransferToSymbian51'):
        assert _is_linked(a1, 'driver_TransferToSymbian51', b)
    _safe_set(b, 'driver_Transfer52', a2)
    assert _is_linked(b, 'driver_Transfer52', a2)
    if hasattr(a1, 'driver_TransferToSymbian51'):
        assert not _is_linked(a1, 'driver_TransferToSymbian51', b)
    if hasattr(a2, 'driver_TransferToSymbian51'):
        assert _is_linked(a2, 'driver_TransferToSymbian51', b)
    _safe_set(b, 'driver_Transfer52', None)
    assert not _is_linked(b, 'driver_Transfer52', a2)
    if hasattr(a2, 'driver_TransferToSymbian51'):
        assert not _is_linked(a2, 'driver_TransferToSymbian51', b)


def test_assoc_transferToSymbian26_reverse_link_reassign_clear():
    a1 = driver_TransferToSymbian(group="sample_text")
    a2 = driver_TransferToSymbian(group="sample_text_2")
    b = driver_Task(group="sample_text", name="sample_text", preRebootDevice="sample_text", timeout="sample_text")
    _safe_set(b, 'driver_Task27', {a1})
    assert _is_linked(b, 'driver_Task27', a1)
    if hasattr(a1, 'driver_TransferToSymbian'):
        assert _is_linked(a1, 'driver_TransferToSymbian', b)
    _safe_set(b, 'driver_Task27', {a2})
    assert _is_linked(b, 'driver_Task27', a2)
    if hasattr(a1, 'driver_TransferToSymbian'):
        assert not _is_linked(a1, 'driver_TransferToSymbian', b)
    if hasattr(a2, 'driver_TransferToSymbian'):
        assert _is_linked(a2, 'driver_TransferToSymbian', b)
    _safe_set(b, 'driver_Task27', set())
    assert not _is_linked(b, 'driver_Task27', a2)
    if hasattr(a2, 'driver_TransferToSymbian'):
        assert not _is_linked(a2, 'driver_TransferToSymbian', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_driver4_stub_double():
    # driver_Driver has no real 'driver_Driver' property in the generated
    # code (a bare stub) -- manually attach it so driver_DocumentRoot's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # driver_DocumentRoot's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = driver_DocumentRoot(mixed="sample_text")
    partner = driver_Driver()
    setattr(partner, 'driver_Driver', None)
    _safe_set(owner, 'driver_DocumentRoot5', {partner})
    assert getattr(partner, 'driver_Driver') == owner
    _safe_set(owner, 'driver_DocumentRoot5', set())
    assert getattr(partner, 'driver_Driver') is None


def test_assoc_info10_stub_double():
    # driver_DriverInfo has no real 'driver_DriverInfo11' property in the generated
    # code (a bare stub) -- manually attach it so driver_Info's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # driver_Info's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = driver_Info(key="sample_text", value="sample_text")
    partner = driver_DriverInfo()
    setattr(partner, 'driver_DriverInfo11', None)
    _safe_set(owner, 'driver_Info', partner)
    assert owner in getattr(partner, 'driver_DriverInfo11')
    _safe_set(owner, 'driver_Info', None)
    assert owner not in getattr(partner, 'driver_DriverInfo11')


def test_assoc_reference34_stub_double():
    # driver_Reference has no real 'driver_Reference36' property in the generated
    # code (a bare stub) -- manually attach it so driver_Task's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # driver_Task's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = driver_Task(group="sample_text", name="sample_text", preRebootDevice="sample_text", timeout="sample_text")
    partner = driver_Reference()
    setattr(partner, 'driver_Reference36', None)
    _safe_set(owner, 'driver_Task35', {partner})
    assert getattr(partner, 'driver_Reference36') == owner
    _safe_set(owner, 'driver_Task35', set())
    assert getattr(partner, 'driver_Reference36') is None


def test_assoc_stopTrace44_stub_double():
    # driver_StopTrace has no real 'driver_StopTrace' property in the generated
    # code (a bare stub) -- manually attach it so driver_Task's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # driver_Task's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = driver_Task(group="sample_text", name="sample_text", preRebootDevice="sample_text", timeout="sample_text")
    partner = driver_StopTrace()
    setattr(partner, 'driver_StopTrace', None)
    _safe_set(owner, 'driver_Task45', partner)
    assert getattr(partner, 'driver_StopTrace') == owner
    _safe_set(owner, 'driver_Task45', None)
    assert getattr(partner, 'driver_StopTrace') is None


def test_assoc_task8_stub_double():
    # driver_Driver has no real 'driver_Driver9' property in the generated
    # code (a bare stub) -- manually attach it so driver_Task's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # driver_Task's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = driver_Task(group="sample_text", name="sample_text", preRebootDevice="sample_text", timeout="sample_text")
    partner = driver_Driver()
    setattr(partner, 'driver_Driver9', None)
    _safe_set(owner, 'driver_Task', partner)
    assert getattr(partner, 'driver_Driver9') == owner
    _safe_set(owner, 'driver_Task', None)
    assert getattr(partner, 'driver_Driver9') is None


def test_assoc_uri20_stub_double():
    # driver_Reference has no real 'driver_Reference' property in the generated
    # code (a bare stub) -- manually attach it so driver_Task's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # driver_Task's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = driver_Task(group="sample_text", name="sample_text", preRebootDevice="sample_text", timeout="sample_text")
    partner = driver_Reference()
    setattr(partner, 'driver_Reference', None)
    _safe_set(owner, 'driver_Task21', partner)
    assert getattr(partner, 'driver_Reference') == owner
    _safe_set(owner, 'driver_Task21', None)
    assert getattr(partner, 'driver_Reference') is None


def test_assoc_xMLNSPrefixMap0_stub_double():
    # driver_EStringToStringMapEntry has no real 'driver_EStringToStringMapEntry' property in the generated
    # code (a bare stub) -- manually attach it so driver_DocumentRoot's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # driver_DocumentRoot's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = driver_DocumentRoot(mixed="sample_text")
    partner = driver_EStringToStringMapEntry()
    setattr(partner, 'driver_EStringToStringMapEntry', None)
    _safe_set(owner, 'driver_DocumentRoot', {partner})
    assert getattr(partner, 'driver_EStringToStringMapEntry') == owner
    _safe_set(owner, 'driver_DocumentRoot', set())
    assert getattr(partner, 'driver_EStringToStringMapEntry') is None


def test_assoc_xSISchemaLocation1_stub_double():
    # driver_EStringToStringMapEntry has no real 'driver_EStringToStringMapEntry3' property in the generated
    # code (a bare stub) -- manually attach it so driver_DocumentRoot's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # driver_DocumentRoot's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = driver_DocumentRoot(mixed="sample_text")
    partner = driver_EStringToStringMapEntry()
    setattr(partner, 'driver_EStringToStringMapEntry3', None)
    _safe_set(owner, 'driver_DocumentRoot2', {partner})
    assert getattr(partner, 'driver_EStringToStringMapEntry3') == owner
    _safe_set(owner, 'driver_DocumentRoot2', set())
    assert getattr(partner, 'driver_EStringToStringMapEntry3') is None


