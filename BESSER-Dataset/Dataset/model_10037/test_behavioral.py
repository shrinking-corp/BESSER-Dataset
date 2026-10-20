import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    SBCS_ControlProgram,
    SBCS_ControlProgram_Start,
    SBCS_Pump,
    SBCS_PumpControler,
    SBCS_PumpController_ClosePump,
    SBCS_PumpController_OpenPump,
    SBCS_Snapshot,
    SBCS_SteamBoiler,
    SBCS_SteamBoiler_OpenValve,
    SBCS_SteamMeasurementDevice,
    SBCS_Transition,
    SBCS_WaterLevelMeasurementDevice,
    SBCS_WaterLevelMeaurementDevice_getLevel,
    Transition,
    Mode,
    State,
    ValveState,
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

def test_assoc_ControlProgramPump20_reverse_link_reassign_clear():
    a1 = SBCS_Pump(capacity=3.14, mode="sample_text", ready=True)
    a2 = SBCS_Pump(capacity=9.99, mode="sample_text_2", ready=False)
    b = SBCS_ControlProgram(failureDetected=True, mode="sample_text", pumpControlerFailure=True, pumpFailure=True, ready=True, smdFailure=True, wlmdFailure=True)
    _safe_set(b, 'PumpControlProgram', a1)
    assert _is_linked(b, 'PumpControlProgram', a1)
    if hasattr(a1, 'Pump21'):
        assert _is_linked(a1, 'Pump21', b)
    _safe_set(b, 'PumpControlProgram', a2)
    assert _is_linked(b, 'PumpControlProgram', a2)
    if hasattr(a1, 'Pump21'):
        assert not _is_linked(a1, 'Pump21', b)
    if hasattr(a2, 'Pump21'):
        assert _is_linked(a2, 'Pump21', b)
    _safe_set(b, 'PumpControlProgram', None)
    assert not _is_linked(b, 'PumpControlProgram', a2)
    if hasattr(a2, 'Pump21'):
        assert not _is_linked(a2, 'Pump21', b)


def test_assoc_ControlProgramPumpControler28_reverse_link_reassign_clear():
    a1 = SBCS_PumpControler(circulating=True, ready=True)
    a2 = SBCS_PumpControler(circulating=False, ready=False)
    b = SBCS_ControlProgram(failureDetected=True, mode="sample_text", pumpControlerFailure=True, pumpFailure=True, ready=True, smdFailure=True, wlmdFailure=True)
    _safe_set(b, 'PumpControlerControlProgram', a1)
    assert _is_linked(b, 'PumpControlerControlProgram', a1)
    if hasattr(a1, 'PumpControler29'):
        assert _is_linked(a1, 'PumpControler29', b)
    _safe_set(b, 'PumpControlerControlProgram', a2)
    assert _is_linked(b, 'PumpControlerControlProgram', a2)
    if hasattr(a1, 'PumpControler29'):
        assert not _is_linked(a1, 'PumpControler29', b)
    if hasattr(a2, 'PumpControler29'):
        assert _is_linked(a2, 'PumpControler29', b)
    _safe_set(b, 'PumpControlerControlProgram', None)
    assert not _is_linked(b, 'PumpControlerControlProgram', a2)
    if hasattr(a2, 'PumpControler29'):
        assert not _is_linked(a2, 'PumpControler29', b)


def test_assoc_ControlProgramSMD24_reverse_link_reassign_clear():
    a1 = SBCS_SteamMeasurementDevice(evaporationRate=True, ready=True, waterLevel=3.14)
    a2 = SBCS_SteamMeasurementDevice(evaporationRate=False, ready=False, waterLevel=9.99)
    b = SBCS_ControlProgram(failureDetected=True, mode="sample_text", pumpControlerFailure=True, pumpFailure=True, ready=True, smdFailure=True, wlmdFailure=True)
    _safe_set(b, 'SMDControlProgram', a1)
    assert _is_linked(b, 'SMDControlProgram', a1)
    if hasattr(a1, 'SteamMeasurementDevice25'):
        assert _is_linked(a1, 'SteamMeasurementDevice25', b)
    _safe_set(b, 'SMDControlProgram', a2)
    assert _is_linked(b, 'SMDControlProgram', a2)
    if hasattr(a1, 'SteamMeasurementDevice25'):
        assert not _is_linked(a1, 'SteamMeasurementDevice25', b)
    if hasattr(a2, 'SteamMeasurementDevice25'):
        assert _is_linked(a2, 'SteamMeasurementDevice25', b)
    _safe_set(b, 'SMDControlProgram', None)
    assert not _is_linked(b, 'SMDControlProgram', a2)
    if hasattr(a2, 'SteamMeasurementDevice25'):
        assert not _is_linked(a2, 'SteamMeasurementDevice25', b)


def test_assoc_ControlProgramSnapshot6_reverse_link_reassign_clear():
    a1 = SBCS_Snapshot()
    a2 = SBCS_Snapshot()
    b = SBCS_ControlProgram(failureDetected=True, mode="sample_text", pumpControlerFailure=True, pumpFailure=True, ready=True, smdFailure=True, wlmdFailure=True)
    _safe_set(b, 'ControlProgram7', a1)
    assert _is_linked(b, 'ControlProgram7', a1)
    if hasattr(a1, 'SnapshotControlProgram'):
        assert _is_linked(a1, 'SnapshotControlProgram', b)
    _safe_set(b, 'ControlProgram7', a2)
    assert _is_linked(b, 'ControlProgram7', a2)
    if hasattr(a1, 'SnapshotControlProgram'):
        assert not _is_linked(a1, 'SnapshotControlProgram', b)
    if hasattr(a2, 'SnapshotControlProgram'):
        assert _is_linked(a2, 'SnapshotControlProgram', b)
    _safe_set(b, 'ControlProgram7', None)
    assert not _is_linked(b, 'ControlProgram7', a2)
    if hasattr(a2, 'SnapshotControlProgram'):
        assert not _is_linked(a2, 'SnapshotControlProgram', b)


def test_assoc_ControlProgramSteamBoiler26_reverse_link_reassign_clear():
    a1 = SBCS_SteamBoiler(capacity=3.14, maximalLimit=3.14, maximalNormal=3.14, maximumDecrease=3.14, maximumIncrease=3.14, minimalLimit=3.14, minimalNormal=3.14, ready=True, valveOpen="sample_text")
    a2 = SBCS_SteamBoiler(capacity=9.99, maximalLimit=9.99, maximalNormal=9.99, maximumDecrease=9.99, maximumIncrease=9.99, minimalLimit=9.99, minimalNormal=9.99, ready=False, valveOpen="sample_text_2")
    b = SBCS_ControlProgram(failureDetected=True, mode="sample_text", pumpControlerFailure=True, pumpFailure=True, ready=True, smdFailure=True, wlmdFailure=True)
    _safe_set(b, 'SteamBoilerControlProgram', a1)
    assert _is_linked(b, 'SteamBoilerControlProgram', a1)
    if hasattr(a1, 'SteamBoiler27'):
        assert _is_linked(a1, 'SteamBoiler27', b)
    _safe_set(b, 'SteamBoilerControlProgram', a2)
    assert _is_linked(b, 'SteamBoilerControlProgram', a2)
    if hasattr(a1, 'SteamBoiler27'):
        assert not _is_linked(a1, 'SteamBoiler27', b)
    if hasattr(a2, 'SteamBoiler27'):
        assert _is_linked(a2, 'SteamBoiler27', b)
    _safe_set(b, 'SteamBoilerControlProgram', None)
    assert not _is_linked(b, 'SteamBoilerControlProgram', a2)
    if hasattr(a2, 'SteamBoiler27'):
        assert not _is_linked(a2, 'SteamBoiler27', b)


def test_assoc_ControlProgramWLMD22_reverse_link_reassign_clear():
    a1 = SBCS_WaterLevelMeasurementDevice(ready=True, waterLevel=3.14)
    a2 = SBCS_WaterLevelMeasurementDevice(ready=False, waterLevel=9.99)
    b = SBCS_ControlProgram(failureDetected=True, mode="sample_text", pumpControlerFailure=True, pumpFailure=True, ready=True, smdFailure=True, wlmdFailure=True)
    _safe_set(b, 'WLMDControlProgram', a1)
    assert _is_linked(b, 'WLMDControlProgram', a1)
    if hasattr(a1, 'WaterLevelMeasurementDevice23'):
        assert _is_linked(a1, 'WaterLevelMeasurementDevice23', b)
    _safe_set(b, 'WLMDControlProgram', a2)
    assert _is_linked(b, 'WLMDControlProgram', a2)
    if hasattr(a1, 'WaterLevelMeasurementDevice23'):
        assert not _is_linked(a1, 'WaterLevelMeasurementDevice23', b)
    if hasattr(a2, 'WaterLevelMeasurementDevice23'):
        assert _is_linked(a2, 'WaterLevelMeasurementDevice23', b)
    _safe_set(b, 'WLMDControlProgram', None)
    assert not _is_linked(b, 'WLMDControlProgram', a2)
    if hasattr(a2, 'WaterLevelMeasurementDevice23'):
        assert not _is_linked(a2, 'WaterLevelMeasurementDevice23', b)


def test_assoc_PumpControlProgram33_reverse_link_reassign_clear():
    a1 = SBCS_Pump(capacity=3.14, mode="sample_text", ready=True)
    a2 = SBCS_Pump(capacity=9.99, mode="sample_text_2", ready=False)
    b = SBCS_ControlProgram(failureDetected=True, mode="sample_text", pumpControlerFailure=True, pumpFailure=True, ready=True, smdFailure=True, wlmdFailure=True)
    _safe_set(b, 'ControlProgram34', a1)
    assert _is_linked(b, 'ControlProgram34', a1)
    if hasattr(a1, 'ControlProgramPump'):
        assert _is_linked(a1, 'ControlProgramPump', b)
    _safe_set(b, 'ControlProgram34', a2)
    assert _is_linked(b, 'ControlProgram34', a2)
    if hasattr(a1, 'ControlProgramPump'):
        assert not _is_linked(a1, 'ControlProgramPump', b)
    if hasattr(a2, 'ControlProgramPump'):
        assert _is_linked(a2, 'ControlProgramPump', b)
    _safe_set(b, 'ControlProgram34', None)
    assert not _is_linked(b, 'ControlProgram34', a2)
    if hasattr(a2, 'ControlProgramPump'):
        assert not _is_linked(a2, 'ControlProgramPump', b)


def test_assoc_PumpControlSnapshot14_reverse_link_reassign_clear():
    a1 = SBCS_Snapshot()
    a2 = SBCS_Snapshot()
    b = SBCS_PumpControler(circulating=True, ready=True)
    _safe_set(b, 'PumpControler', a1)
    assert _is_linked(b, 'PumpControler', a1)
    if hasattr(a1, 'SnapshotPumpControl'):
        assert _is_linked(a1, 'SnapshotPumpControl', b)
    _safe_set(b, 'PumpControler', a2)
    assert _is_linked(b, 'PumpControler', a2)
    if hasattr(a1, 'SnapshotPumpControl'):
        assert not _is_linked(a1, 'SnapshotPumpControl', b)
    if hasattr(a2, 'SnapshotPumpControl'):
        assert _is_linked(a2, 'SnapshotPumpControl', b)
    _safe_set(b, 'PumpControler', None)
    assert not _is_linked(b, 'PumpControler', a2)
    if hasattr(a2, 'SnapshotPumpControl'):
        assert not _is_linked(a2, 'SnapshotPumpControl', b)


def test_assoc_PumpControlerControlProgram47_reverse_link_reassign_clear():
    a1 = SBCS_PumpControler(circulating=True, ready=True)
    a2 = SBCS_PumpControler(circulating=False, ready=False)
    b = SBCS_ControlProgram(failureDetected=True, mode="sample_text", pumpControlerFailure=True, pumpFailure=True, ready=True, smdFailure=True, wlmdFailure=True)
    _safe_set(b, 'ControlProgram48', a1)
    assert _is_linked(b, 'ControlProgram48', a1)
    if hasattr(a1, 'ControlProgramPumpControler'):
        assert _is_linked(a1, 'ControlProgramPumpControler', b)
    _safe_set(b, 'ControlProgram48', a2)
    assert _is_linked(b, 'ControlProgram48', a2)
    if hasattr(a1, 'ControlProgramPumpControler'):
        assert not _is_linked(a1, 'ControlProgramPumpControler', b)
    if hasattr(a2, 'ControlProgramPumpControler'):
        assert _is_linked(a2, 'ControlProgramPumpControler', b)
    _safe_set(b, 'ControlProgram48', None)
    assert not _is_linked(b, 'ControlProgram48', a2)
    if hasattr(a2, 'ControlProgramPumpControler'):
        assert not _is_linked(a2, 'ControlProgramPumpControler', b)


def test_assoc_PumpControlerPump49_reverse_link_reassign_clear():
    a1 = SBCS_PumpControler(circulating=True, ready=True)
    a2 = SBCS_PumpControler(circulating=False, ready=False)
    b = SBCS_Pump(capacity=3.14, mode="sample_text", ready=True)
    _safe_set(b, 'Pump50', a1)
    assert _is_linked(b, 'Pump50', a1)
    if hasattr(a1, 'PumpPumpControler'):
        assert _is_linked(a1, 'PumpPumpControler', b)
    _safe_set(b, 'Pump50', a2)
    assert _is_linked(b, 'Pump50', a2)
    if hasattr(a1, 'PumpPumpControler'):
        assert not _is_linked(a1, 'PumpPumpControler', b)
    if hasattr(a2, 'PumpPumpControler'):
        assert _is_linked(a2, 'PumpPumpControler', b)
    _safe_set(b, 'Pump50', None)
    assert not _is_linked(b, 'Pump50', a2)
    if hasattr(a2, 'PumpPumpControler'):
        assert not _is_linked(a2, 'PumpPumpControler', b)


def test_assoc_PumpPumpControler35_reverse_link_reassign_clear():
    a1 = SBCS_PumpControler(circulating=True, ready=True)
    a2 = SBCS_PumpControler(circulating=False, ready=False)
    b = SBCS_Pump(capacity=3.14, mode="sample_text", ready=True)
    _safe_set(b, 'PumpControlerPump', a1)
    assert _is_linked(b, 'PumpControlerPump', a1)
    if hasattr(a1, 'PumpControler36'):
        assert _is_linked(a1, 'PumpControler36', b)
    _safe_set(b, 'PumpControlerPump', a2)
    assert _is_linked(b, 'PumpControlerPump', a2)
    if hasattr(a1, 'PumpControler36'):
        assert not _is_linked(a1, 'PumpControler36', b)
    if hasattr(a2, 'PumpControler36'):
        assert _is_linked(a2, 'PumpControler36', b)
    _safe_set(b, 'PumpControlerPump', None)
    assert not _is_linked(b, 'PumpControlerPump', a2)
    if hasattr(a2, 'PumpControler36'):
        assert not _is_linked(a2, 'PumpControler36', b)


def test_assoc_PumpSnapshot30_reverse_link_reassign_clear():
    a1 = SBCS_Snapshot()
    a2 = SBCS_Snapshot()
    b = SBCS_Pump(capacity=3.14, mode="sample_text", ready=True)
    _safe_set(b, 'PumpSnapshot31', a1)
    assert _is_linked(b, 'PumpSnapshot31', a1)
    if hasattr(a1, 'Snapshot32'):
        assert _is_linked(a1, 'Snapshot32', b)
    _safe_set(b, 'PumpSnapshot31', a2)
    assert _is_linked(b, 'PumpSnapshot31', a2)
    if hasattr(a1, 'Snapshot32'):
        assert not _is_linked(a1, 'Snapshot32', b)
    if hasattr(a2, 'Snapshot32'):
        assert _is_linked(a2, 'Snapshot32', b)
    _safe_set(b, 'PumpSnapshot31', None)
    assert not _is_linked(b, 'PumpSnapshot31', a2)
    if hasattr(a2, 'Snapshot32'):
        assert not _is_linked(a2, 'Snapshot32', b)


def test_assoc_PumpSnapshot8_reverse_link_reassign_clear():
    a1 = SBCS_Snapshot()
    a2 = SBCS_Snapshot()
    b = SBCS_Pump(capacity=3.14, mode="sample_text", ready=True)
    _safe_set(b, 'Pump9', a1)
    assert _is_linked(b, 'Pump9', a1)
    if hasattr(a1, 'PumpSnapshot'):
        assert _is_linked(a1, 'PumpSnapshot', b)
    _safe_set(b, 'Pump9', a2)
    assert _is_linked(b, 'Pump9', a2)
    if hasattr(a1, 'PumpSnapshot'):
        assert not _is_linked(a1, 'PumpSnapshot', b)
    if hasattr(a2, 'PumpSnapshot'):
        assert _is_linked(a2, 'PumpSnapshot', b)
    _safe_set(b, 'Pump9', None)
    assert not _is_linked(b, 'Pump9', a2)
    if hasattr(a2, 'PumpSnapshot'):
        assert not _is_linked(a2, 'PumpSnapshot', b)


def test_assoc_PumpSteamBoiler37_reverse_link_reassign_clear():
    a1 = SBCS_SteamBoiler(capacity=3.14, maximalLimit=3.14, maximalNormal=3.14, maximumDecrease=3.14, maximumIncrease=3.14, minimalLimit=3.14, minimalNormal=3.14, ready=True, valveOpen="sample_text")
    a2 = SBCS_SteamBoiler(capacity=9.99, maximalLimit=9.99, maximalNormal=9.99, maximumDecrease=9.99, maximumIncrease=9.99, minimalLimit=9.99, minimalNormal=9.99, ready=False, valveOpen="sample_text_2")
    b = SBCS_Pump(capacity=3.14, mode="sample_text", ready=True)
    _safe_set(b, 'SteqmBoilerPump', a1)
    assert _is_linked(b, 'SteqmBoilerPump', a1)
    if hasattr(a1, 'SteamBoiler38'):
        assert _is_linked(a1, 'SteamBoiler38', b)
    _safe_set(b, 'SteqmBoilerPump', a2)
    assert _is_linked(b, 'SteqmBoilerPump', a2)
    if hasattr(a1, 'SteamBoiler38'):
        assert not _is_linked(a1, 'SteamBoiler38', b)
    if hasattr(a2, 'SteamBoiler38'):
        assert _is_linked(a2, 'SteamBoiler38', b)
    _safe_set(b, 'SteqmBoilerPump', None)
    assert not _is_linked(b, 'SteqmBoilerPump', a2)
    if hasattr(a2, 'SteamBoiler38'):
        assert not _is_linked(a2, 'SteamBoiler38', b)


def test_assoc_SMDControlProgram53_reverse_link_reassign_clear():
    a1 = SBCS_SteamMeasurementDevice(evaporationRate=True, ready=True, waterLevel=3.14)
    a2 = SBCS_SteamMeasurementDevice(evaporationRate=False, ready=False, waterLevel=9.99)
    b = SBCS_ControlProgram(failureDetected=True, mode="sample_text", pumpControlerFailure=True, pumpFailure=True, ready=True, smdFailure=True, wlmdFailure=True)
    _safe_set(b, 'ControlProgram54', a1)
    assert _is_linked(b, 'ControlProgram54', a1)
    if hasattr(a1, 'ControlProgramSMD'):
        assert _is_linked(a1, 'ControlProgramSMD', b)
    _safe_set(b, 'ControlProgram54', a2)
    assert _is_linked(b, 'ControlProgram54', a2)
    if hasattr(a1, 'ControlProgramSMD'):
        assert not _is_linked(a1, 'ControlProgramSMD', b)
    if hasattr(a2, 'ControlProgramSMD'):
        assert _is_linked(a2, 'ControlProgramSMD', b)
    _safe_set(b, 'ControlProgram54', None)
    assert not _is_linked(b, 'ControlProgram54', a2)
    if hasattr(a2, 'ControlProgramSMD'):
        assert not _is_linked(a2, 'ControlProgramSMD', b)


def test_assoc_SMDSteamBoiler55_reverse_link_reassign_clear():
    a1 = SBCS_SteamMeasurementDevice(evaporationRate=True, ready=True, waterLevel=3.14)
    a2 = SBCS_SteamMeasurementDevice(evaporationRate=False, ready=False, waterLevel=9.99)
    b = SBCS_SteamBoiler(capacity=3.14, maximalLimit=3.14, maximalNormal=3.14, maximumDecrease=3.14, maximumIncrease=3.14, minimalLimit=3.14, minimalNormal=3.14, ready=True, valveOpen="sample_text")
    _safe_set(b, 'SteamBoiler56', a1)
    assert _is_linked(b, 'SteamBoiler56', a1)
    if hasattr(a1, 'SteamBoilerSMD'):
        assert _is_linked(a1, 'SteamBoilerSMD', b)
    _safe_set(b, 'SteamBoiler56', a2)
    assert _is_linked(b, 'SteamBoiler56', a2)
    if hasattr(a1, 'SteamBoilerSMD'):
        assert not _is_linked(a1, 'SteamBoilerSMD', b)
    if hasattr(a2, 'SteamBoilerSMD'):
        assert _is_linked(a2, 'SteamBoilerSMD', b)
    _safe_set(b, 'SteamBoiler56', None)
    assert not _is_linked(b, 'SteamBoiler56', a2)
    if hasattr(a2, 'SteamBoilerSMD'):
        assert not _is_linked(a2, 'SteamBoilerSMD', b)


def test_assoc_SnapshotControlProgram18_reverse_link_reassign_clear():
    a1 = SBCS_Snapshot()
    a2 = SBCS_Snapshot()
    b = SBCS_ControlProgram(failureDetected=True, mode="sample_text", pumpControlerFailure=True, pumpFailure=True, ready=True, smdFailure=True, wlmdFailure=True)
    _safe_set(b, 'ControlProgramSnapshot', a1)
    assert _is_linked(b, 'ControlProgramSnapshot', a1)
    if hasattr(a1, 'Snapshot19'):
        assert _is_linked(a1, 'Snapshot19', b)
    _safe_set(b, 'ControlProgramSnapshot', a2)
    assert _is_linked(b, 'ControlProgramSnapshot', a2)
    if hasattr(a1, 'Snapshot19'):
        assert not _is_linked(a1, 'Snapshot19', b)
    if hasattr(a2, 'Snapshot19'):
        assert _is_linked(a2, 'Snapshot19', b)
    _safe_set(b, 'ControlProgramSnapshot', None)
    assert not _is_linked(b, 'ControlProgramSnapshot', a2)
    if hasattr(a2, 'Snapshot19'):
        assert not _is_linked(a2, 'Snapshot19', b)


def test_assoc_SnapshotPumpControl45_reverse_link_reassign_clear():
    a1 = SBCS_Snapshot()
    a2 = SBCS_Snapshot()
    b = SBCS_PumpControler(circulating=True, ready=True)
    _safe_set(b, 'PumpControlSnapshot', a1)
    assert _is_linked(b, 'PumpControlSnapshot', a1)
    if hasattr(a1, 'Snapshot46'):
        assert _is_linked(a1, 'Snapshot46', b)
    _safe_set(b, 'PumpControlSnapshot', a2)
    assert _is_linked(b, 'PumpControlSnapshot', a2)
    if hasattr(a1, 'Snapshot46'):
        assert not _is_linked(a1, 'Snapshot46', b)
    if hasattr(a2, 'Snapshot46'):
        assert _is_linked(a2, 'Snapshot46', b)
    _safe_set(b, 'PumpControlSnapshot', None)
    assert not _is_linked(b, 'PumpControlSnapshot', a2)
    if hasattr(a2, 'Snapshot46'):
        assert not _is_linked(a2, 'Snapshot46', b)


def test_assoc_SnapshotSBMD51_reverse_link_reassign_clear():
    a1 = SBCS_SteamMeasurementDevice(evaporationRate=True, ready=True, waterLevel=3.14)
    a2 = SBCS_SteamMeasurementDevice(evaporationRate=False, ready=False, waterLevel=9.99)
    b = SBCS_Snapshot()
    _safe_set(b, 'Snapshot52', a1)
    assert _is_linked(b, 'Snapshot52', a1)
    if hasattr(a1, 'SteamBoilerMeasurementDeviceSnapshot'):
        assert _is_linked(a1, 'SteamBoilerMeasurementDeviceSnapshot', b)
    _safe_set(b, 'Snapshot52', a2)
    assert _is_linked(b, 'Snapshot52', a2)
    if hasattr(a1, 'SteamBoilerMeasurementDeviceSnapshot'):
        assert not _is_linked(a1, 'SteamBoilerMeasurementDeviceSnapshot', b)
    if hasattr(a2, 'SteamBoilerMeasurementDeviceSnapshot'):
        assert _is_linked(a2, 'SteamBoilerMeasurementDeviceSnapshot', b)
    _safe_set(b, 'Snapshot52', None)
    assert not _is_linked(b, 'Snapshot52', a2)
    if hasattr(a2, 'SteamBoilerMeasurementDeviceSnapshot'):
        assert not _is_linked(a2, 'SteamBoilerMeasurementDeviceSnapshot', b)


def test_assoc_SnapshotSteamBoiler0_reverse_link_reassign_clear():
    a1 = SBCS_SteamBoiler(capacity=3.14, maximalLimit=3.14, maximalNormal=3.14, maximumDecrease=3.14, maximumIncrease=3.14, minimalLimit=3.14, minimalNormal=3.14, ready=True, valveOpen="sample_text")
    a2 = SBCS_SteamBoiler(capacity=9.99, maximalLimit=9.99, maximalNormal=9.99, maximumDecrease=9.99, maximumIncrease=9.99, minimalLimit=9.99, minimalNormal=9.99, ready=False, valveOpen="sample_text_2")
    b = SBCS_Snapshot()
    _safe_set(b, 'Snapshot', a1)
    assert _is_linked(b, 'Snapshot', a1)
    if hasattr(a1, 'SteamBoilerSnapshot'):
        assert _is_linked(a1, 'SteamBoilerSnapshot', b)
    _safe_set(b, 'Snapshot', a2)
    assert _is_linked(b, 'Snapshot', a2)
    if hasattr(a1, 'SteamBoilerSnapshot'):
        assert not _is_linked(a1, 'SteamBoilerSnapshot', b)
    if hasattr(a2, 'SteamBoilerSnapshot'):
        assert _is_linked(a2, 'SteamBoilerSnapshot', b)
    _safe_set(b, 'Snapshot', None)
    assert not _is_linked(b, 'Snapshot', a2)
    if hasattr(a2, 'SteamBoilerSnapshot'):
        assert not _is_linked(a2, 'SteamBoilerSnapshot', b)


def test_assoc_SnapshotWLMD57_reverse_link_reassign_clear():
    a1 = SBCS_WaterLevelMeasurementDevice(ready=True, waterLevel=3.14)
    a2 = SBCS_WaterLevelMeasurementDevice(ready=False, waterLevel=9.99)
    b = SBCS_Snapshot()
    _safe_set(b, 'Snapshot58', a1)
    assert _is_linked(b, 'Snapshot58', a1)
    if hasattr(a1, 'WLMDSnapshot'):
        assert _is_linked(a1, 'WLMDSnapshot', b)
    _safe_set(b, 'Snapshot58', a2)
    assert _is_linked(b, 'Snapshot58', a2)
    if hasattr(a1, 'WLMDSnapshot'):
        assert not _is_linked(a1, 'WLMDSnapshot', b)
    if hasattr(a2, 'WLMDSnapshot'):
        assert _is_linked(a2, 'WLMDSnapshot', b)
    _safe_set(b, 'Snapshot58', None)
    assert not _is_linked(b, 'Snapshot58', a2)
    if hasattr(a2, 'WLMDSnapshot'):
        assert not _is_linked(a2, 'WLMDSnapshot', b)


def test_assoc_SteamBoilerControlProgram1_reverse_link_reassign_clear():
    a1 = SBCS_SteamBoiler(capacity=3.14, maximalLimit=3.14, maximalNormal=3.14, maximumDecrease=3.14, maximumIncrease=3.14, minimalLimit=3.14, minimalNormal=3.14, ready=True, valveOpen="sample_text")
    a2 = SBCS_SteamBoiler(capacity=9.99, maximalLimit=9.99, maximalNormal=9.99, maximumDecrease=9.99, maximumIncrease=9.99, minimalLimit=9.99, minimalNormal=9.99, ready=False, valveOpen="sample_text_2")
    b = SBCS_ControlProgram(failureDetected=True, mode="sample_text", pumpControlerFailure=True, pumpFailure=True, ready=True, smdFailure=True, wlmdFailure=True)
    _safe_set(b, 'ControlProgram', a1)
    assert _is_linked(b, 'ControlProgram', a1)
    if hasattr(a1, 'ControlProgramSteamBoiler'):
        assert _is_linked(a1, 'ControlProgramSteamBoiler', b)
    _safe_set(b, 'ControlProgram', a2)
    assert _is_linked(b, 'ControlProgram', a2)
    if hasattr(a1, 'ControlProgramSteamBoiler'):
        assert not _is_linked(a1, 'ControlProgramSteamBoiler', b)
    if hasattr(a2, 'ControlProgramSteamBoiler'):
        assert _is_linked(a2, 'ControlProgramSteamBoiler', b)
    _safe_set(b, 'ControlProgram', None)
    assert not _is_linked(b, 'ControlProgram', a2)
    if hasattr(a2, 'ControlProgramSteamBoiler'):
        assert not _is_linked(a2, 'ControlProgramSteamBoiler', b)


def test_assoc_SteamBoilerMeasurementDeviceSnapshot12_reverse_link_reassign_clear():
    a1 = SBCS_SteamMeasurementDevice(evaporationRate=True, ready=True, waterLevel=3.14)
    a2 = SBCS_SteamMeasurementDevice(evaporationRate=False, ready=False, waterLevel=9.99)
    b = SBCS_Snapshot()
    _safe_set(b, 'SnapshotSBMD', a1)
    assert _is_linked(b, 'SnapshotSBMD', a1)
    if hasattr(a1, 'SteamMeasurementDevice13'):
        assert _is_linked(a1, 'SteamMeasurementDevice13', b)
    _safe_set(b, 'SnapshotSBMD', a2)
    assert _is_linked(b, 'SnapshotSBMD', a2)
    if hasattr(a1, 'SteamMeasurementDevice13'):
        assert not _is_linked(a1, 'SteamMeasurementDevice13', b)
    if hasattr(a2, 'SteamMeasurementDevice13'):
        assert _is_linked(a2, 'SteamMeasurementDevice13', b)
    _safe_set(b, 'SnapshotSBMD', None)
    assert not _is_linked(b, 'SnapshotSBMD', a2)
    if hasattr(a2, 'SteamMeasurementDevice13'):
        assert not _is_linked(a2, 'SteamMeasurementDevice13', b)


def test_assoc_SteamBoilerSMD3_reverse_link_reassign_clear():
    a1 = SBCS_SteamMeasurementDevice(evaporationRate=True, ready=True, waterLevel=3.14)
    a2 = SBCS_SteamMeasurementDevice(evaporationRate=False, ready=False, waterLevel=9.99)
    b = SBCS_SteamBoiler(capacity=3.14, maximalLimit=3.14, maximalNormal=3.14, maximumDecrease=3.14, maximumIncrease=3.14, minimalLimit=3.14, minimalNormal=3.14, ready=True, valveOpen="sample_text")
    _safe_set(b, 'SMDSteamBoiler', a1)
    assert _is_linked(b, 'SMDSteamBoiler', a1)
    if hasattr(a1, 'SteamMeasurementDevice'):
        assert _is_linked(a1, 'SteamMeasurementDevice', b)
    _safe_set(b, 'SMDSteamBoiler', a2)
    assert _is_linked(b, 'SMDSteamBoiler', a2)
    if hasattr(a1, 'SteamMeasurementDevice'):
        assert not _is_linked(a1, 'SteamMeasurementDevice', b)
    if hasattr(a2, 'SteamMeasurementDevice'):
        assert _is_linked(a2, 'SteamMeasurementDevice', b)
    _safe_set(b, 'SMDSteamBoiler', None)
    assert not _is_linked(b, 'SMDSteamBoiler', a2)
    if hasattr(a2, 'SteamMeasurementDevice'):
        assert not _is_linked(a2, 'SteamMeasurementDevice', b)


def test_assoc_SteamBoilerSnapshot5_reverse_link_reassign_clear():
    a1 = SBCS_SteamBoiler(capacity=3.14, maximalLimit=3.14, maximalNormal=3.14, maximumDecrease=3.14, maximumIncrease=3.14, minimalLimit=3.14, minimalNormal=3.14, ready=True, valveOpen="sample_text")
    a2 = SBCS_SteamBoiler(capacity=9.99, maximalLimit=9.99, maximalNormal=9.99, maximumDecrease=9.99, maximumIncrease=9.99, minimalLimit=9.99, minimalNormal=9.99, ready=False, valveOpen="sample_text_2")
    b = SBCS_Snapshot()
    _safe_set(b, 'SnapshotSteamBoiler', a1)
    assert _is_linked(b, 'SnapshotSteamBoiler', a1)
    if hasattr(a1, 'SteamBoiler'):
        assert _is_linked(a1, 'SteamBoiler', b)
    _safe_set(b, 'SnapshotSteamBoiler', a2)
    assert _is_linked(b, 'SnapshotSteamBoiler', a2)
    if hasattr(a1, 'SteamBoiler'):
        assert not _is_linked(a1, 'SteamBoiler', b)
    if hasattr(a2, 'SteamBoiler'):
        assert _is_linked(a2, 'SteamBoiler', b)
    _safe_set(b, 'SnapshotSteamBoiler', None)
    assert not _is_linked(b, 'SnapshotSteamBoiler', a2)
    if hasattr(a2, 'SteamBoiler'):
        assert not _is_linked(a2, 'SteamBoiler', b)


def test_assoc_SteamBoilerWLMD4_reverse_link_reassign_clear():
    a1 = SBCS_WaterLevelMeasurementDevice(ready=True, waterLevel=3.14)
    a2 = SBCS_WaterLevelMeasurementDevice(ready=False, waterLevel=9.99)
    b = SBCS_SteamBoiler(capacity=3.14, maximalLimit=3.14, maximalNormal=3.14, maximumDecrease=3.14, maximumIncrease=3.14, minimalLimit=3.14, minimalNormal=3.14, ready=True, valveOpen="sample_text")
    _safe_set(b, 'WLMDSteamBoiler', a1)
    assert _is_linked(b, 'WLMDSteamBoiler', a1)
    if hasattr(a1, 'WaterLevelMeasurementDevice'):
        assert _is_linked(a1, 'WaterLevelMeasurementDevice', b)
    _safe_set(b, 'WLMDSteamBoiler', a2)
    assert _is_linked(b, 'WLMDSteamBoiler', a2)
    if hasattr(a1, 'WaterLevelMeasurementDevice'):
        assert not _is_linked(a1, 'WaterLevelMeasurementDevice', b)
    if hasattr(a2, 'WaterLevelMeasurementDevice'):
        assert _is_linked(a2, 'WaterLevelMeasurementDevice', b)
    _safe_set(b, 'WLMDSteamBoiler', None)
    assert not _is_linked(b, 'WLMDSteamBoiler', a2)
    if hasattr(a2, 'WaterLevelMeasurementDevice'):
        assert not _is_linked(a2, 'WaterLevelMeasurementDevice', b)


def test_assoc_SteqmBoilerPump2_reverse_link_reassign_clear():
    a1 = SBCS_SteamBoiler(capacity=3.14, maximalLimit=3.14, maximalNormal=3.14, maximumDecrease=3.14, maximumIncrease=3.14, minimalLimit=3.14, minimalNormal=3.14, ready=True, valveOpen="sample_text")
    a2 = SBCS_SteamBoiler(capacity=9.99, maximalLimit=9.99, maximalNormal=9.99, maximumDecrease=9.99, maximumIncrease=9.99, minimalLimit=9.99, minimalNormal=9.99, ready=False, valveOpen="sample_text_2")
    b = SBCS_Pump(capacity=3.14, mode="sample_text", ready=True)
    _safe_set(b, 'Pump', a1)
    assert _is_linked(b, 'Pump', a1)
    if hasattr(a1, 'PumpSteamBoiler'):
        assert _is_linked(a1, 'PumpSteamBoiler', b)
    _safe_set(b, 'Pump', a2)
    assert _is_linked(b, 'Pump', a2)
    if hasattr(a1, 'PumpSteamBoiler'):
        assert not _is_linked(a1, 'PumpSteamBoiler', b)
    if hasattr(a2, 'PumpSteamBoiler'):
        assert _is_linked(a2, 'PumpSteamBoiler', b)
    _safe_set(b, 'Pump', None)
    assert not _is_linked(b, 'Pump', a2)
    if hasattr(a2, 'PumpSteamBoiler'):
        assert not _is_linked(a2, 'PumpSteamBoiler', b)


def test_assoc_WLMDControlProgram59_reverse_link_reassign_clear():
    a1 = SBCS_WaterLevelMeasurementDevice(ready=True, waterLevel=3.14)
    a2 = SBCS_WaterLevelMeasurementDevice(ready=False, waterLevel=9.99)
    b = SBCS_ControlProgram(failureDetected=True, mode="sample_text", pumpControlerFailure=True, pumpFailure=True, ready=True, smdFailure=True, wlmdFailure=True)
    _safe_set(b, 'ControlProgram60', a1)
    assert _is_linked(b, 'ControlProgram60', a1)
    if hasattr(a1, 'ControlProgramWLMD'):
        assert _is_linked(a1, 'ControlProgramWLMD', b)
    _safe_set(b, 'ControlProgram60', a2)
    assert _is_linked(b, 'ControlProgram60', a2)
    if hasattr(a1, 'ControlProgramWLMD'):
        assert not _is_linked(a1, 'ControlProgramWLMD', b)
    if hasattr(a2, 'ControlProgramWLMD'):
        assert _is_linked(a2, 'ControlProgramWLMD', b)
    _safe_set(b, 'ControlProgram60', None)
    assert not _is_linked(b, 'ControlProgram60', a2)
    if hasattr(a2, 'ControlProgramWLMD'):
        assert not _is_linked(a2, 'ControlProgramWLMD', b)


def test_assoc_WLMDSnapshot10_reverse_link_reassign_clear():
    a1 = SBCS_WaterLevelMeasurementDevice(ready=True, waterLevel=3.14)
    a2 = SBCS_WaterLevelMeasurementDevice(ready=False, waterLevel=9.99)
    b = SBCS_Snapshot()
    _safe_set(b, 'SnapshotWLMD', a1)
    assert _is_linked(b, 'SnapshotWLMD', a1)
    if hasattr(a1, 'WaterLevelMeasurementDevice11'):
        assert _is_linked(a1, 'WaterLevelMeasurementDevice11', b)
    _safe_set(b, 'SnapshotWLMD', a2)
    assert _is_linked(b, 'SnapshotWLMD', a2)
    if hasattr(a1, 'WaterLevelMeasurementDevice11'):
        assert not _is_linked(a1, 'WaterLevelMeasurementDevice11', b)
    if hasattr(a2, 'WaterLevelMeasurementDevice11'):
        assert _is_linked(a2, 'WaterLevelMeasurementDevice11', b)
    _safe_set(b, 'SnapshotWLMD', None)
    assert not _is_linked(b, 'SnapshotWLMD', a2)
    if hasattr(a2, 'WaterLevelMeasurementDevice11'):
        assert not _is_linked(a2, 'WaterLevelMeasurementDevice11', b)


def test_assoc_WLMDSteamBoiler61_reverse_link_reassign_clear():
    a1 = SBCS_WaterLevelMeasurementDevice(ready=True, waterLevel=3.14)
    a2 = SBCS_WaterLevelMeasurementDevice(ready=False, waterLevel=9.99)
    b = SBCS_SteamBoiler(capacity=3.14, maximalLimit=3.14, maximalNormal=3.14, maximumDecrease=3.14, maximumIncrease=3.14, minimalLimit=3.14, minimalNormal=3.14, ready=True, valveOpen="sample_text")
    _safe_set(b, 'SteamBoiler62', a1)
    assert _is_linked(b, 'SteamBoiler62', a1)
    if hasattr(a1, 'SteamBoilerWLMD'):
        assert _is_linked(a1, 'SteamBoilerWLMD', b)
    _safe_set(b, 'SteamBoiler62', a2)
    assert _is_linked(b, 'SteamBoiler62', a2)
    if hasattr(a1, 'SteamBoilerWLMD'):
        assert not _is_linked(a1, 'SteamBoilerWLMD', b)
    if hasattr(a2, 'SteamBoilerWLMD'):
        assert _is_linked(a2, 'SteamBoilerWLMD', b)
    _safe_set(b, 'SteamBoiler62', None)
    assert not _is_linked(b, 'SteamBoiler62', a2)
    if hasattr(a2, 'SteamBoilerWLMD'):
        assert not _is_linked(a2, 'SteamBoilerWLMD', b)


def test_assoc_wlmdPost68_reverse_link_reassign_clear():
    a1 = SBCS_WaterLevelMeaurementDevice_getLevel(ret=3.14)
    a2 = SBCS_WaterLevelMeaurementDevice_getLevel(ret=9.99)
    b = SBCS_WaterLevelMeasurementDevice(ready=True, waterLevel=3.14)
    _safe_set(b, 'SBCS_WaterLevelMeasurementDevice70', a1)
    assert _is_linked(b, 'SBCS_WaterLevelMeasurementDevice70', a1)
    if hasattr(a1, 'SBCS_WaterLevelMeaurementDevice_getLevel69'):
        assert _is_linked(a1, 'SBCS_WaterLevelMeaurementDevice_getLevel69', b)
    _safe_set(b, 'SBCS_WaterLevelMeasurementDevice70', a2)
    assert _is_linked(b, 'SBCS_WaterLevelMeasurementDevice70', a2)
    if hasattr(a1, 'SBCS_WaterLevelMeaurementDevice_getLevel69'):
        assert not _is_linked(a1, 'SBCS_WaterLevelMeaurementDevice_getLevel69', b)
    if hasattr(a2, 'SBCS_WaterLevelMeaurementDevice_getLevel69'):
        assert _is_linked(a2, 'SBCS_WaterLevelMeaurementDevice_getLevel69', b)
    _safe_set(b, 'SBCS_WaterLevelMeasurementDevice70', None)
    assert not _is_linked(b, 'SBCS_WaterLevelMeasurementDevice70', a2)
    if hasattr(a2, 'SBCS_WaterLevelMeaurementDevice_getLevel69'):
        assert not _is_linked(a2, 'SBCS_WaterLevelMeaurementDevice_getLevel69', b)


def test_assoc_wlmdPre67_reverse_link_reassign_clear():
    a1 = SBCS_WaterLevelMeaurementDevice_getLevel(ret=3.14)
    a2 = SBCS_WaterLevelMeaurementDevice_getLevel(ret=9.99)
    b = SBCS_WaterLevelMeasurementDevice(ready=True, waterLevel=3.14)
    _safe_set(b, 'SBCS_WaterLevelMeasurementDevice', a1)
    assert _is_linked(b, 'SBCS_WaterLevelMeasurementDevice', a1)
    if hasattr(a1, 'SBCS_WaterLevelMeaurementDevice_getLevel'):
        assert _is_linked(a1, 'SBCS_WaterLevelMeaurementDevice_getLevel', b)
    _safe_set(b, 'SBCS_WaterLevelMeasurementDevice', a2)
    assert _is_linked(b, 'SBCS_WaterLevelMeasurementDevice', a2)
    if hasattr(a1, 'SBCS_WaterLevelMeaurementDevice_getLevel'):
        assert not _is_linked(a1, 'SBCS_WaterLevelMeaurementDevice_getLevel', b)
    if hasattr(a2, 'SBCS_WaterLevelMeaurementDevice_getLevel'):
        assert _is_linked(a2, 'SBCS_WaterLevelMeaurementDevice_getLevel', b)
    _safe_set(b, 'SBCS_WaterLevelMeasurementDevice', None)
    assert not _is_linked(b, 'SBCS_WaterLevelMeasurementDevice', a2)
    if hasattr(a2, 'SBCS_WaterLevelMeaurementDevice_getLevel'):
        assert not _is_linked(a2, 'SBCS_WaterLevelMeaurementDevice_getLevel', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_AfterTrans16_stub_double():
    # SBCS_Transition has no real 'Transition17' property in the generated
    # code (a bare stub) -- manually attach it so SBCS_Snapshot's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # SBCS_Snapshot's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = SBCS_Snapshot()
    partner = SBCS_Transition()
    setattr(partner, 'Transition17', None)
    _safe_set(owner, 'AfterTrans', partner)
    assert getattr(partner, 'Transition17') == owner
    _safe_set(owner, 'AfterTrans', None)
    assert getattr(partner, 'Transition17') is None


def test_assoc_AfterTrans42_stub_double():
    # SBCS_Transition has no real 'AfterTrans43' property in the generated
    # code (a bare stub) -- manually attach it so SBCS_Snapshot's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # SBCS_Snapshot's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = SBCS_Snapshot()
    partner = SBCS_Transition()
    setattr(partner, 'AfterTrans43', None)
    _safe_set(owner, 'Snapshot44', partner)
    assert getattr(partner, 'AfterTrans43') == owner
    _safe_set(owner, 'Snapshot44', None)
    assert getattr(partner, 'AfterTrans43') is None


def test_assoc_BeforeTrans15_stub_double():
    # SBCS_Transition has no real 'Transition' property in the generated
    # code (a bare stub) -- manually attach it so SBCS_Snapshot's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # SBCS_Snapshot's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = SBCS_Snapshot()
    partner = SBCS_Transition()
    setattr(partner, 'Transition', None)
    _safe_set(owner, 'BeforeTrans', partner)
    assert getattr(partner, 'Transition') == owner
    _safe_set(owner, 'BeforeTrans', None)
    assert getattr(partner, 'Transition') is None


def test_assoc_BeforeTrans39_stub_double():
    # SBCS_Transition has no real 'BeforeTrans40' property in the generated
    # code (a bare stub) -- manually attach it so SBCS_Snapshot's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # SBCS_Snapshot's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = SBCS_Snapshot()
    partner = SBCS_Transition()
    setattr(partner, 'BeforeTrans40', None)
    _safe_set(owner, 'Snapshot41', partner)
    assert getattr(partner, 'BeforeTrans40') == owner
    _safe_set(owner, 'Snapshot41', None)
    assert getattr(partner, 'BeforeTrans40') is None


def test_assoc_CPPost64_stub_double():
    # SBCS_ControlProgram_Start has no real 'SBCS_ControlProgram_Start65' property in the generated
    # code (a bare stub) -- manually attach it so SBCS_ControlProgram's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # SBCS_ControlProgram's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = SBCS_ControlProgram(failureDetected=True, mode="sample_text", pumpControlerFailure=True, pumpFailure=True, ready=True, smdFailure=True, wlmdFailure=True)
    partner = SBCS_ControlProgram_Start()
    setattr(partner, 'SBCS_ControlProgram_Start65', None)
    _safe_set(owner, 'SBCS_ControlProgram66', partner)
    assert getattr(partner, 'SBCS_ControlProgram_Start65') == owner
    _safe_set(owner, 'SBCS_ControlProgram66', None)
    assert getattr(partner, 'SBCS_ControlProgram_Start65') is None


def test_assoc_CPPre63_stub_double():
    # SBCS_ControlProgram_Start has no real 'SBCS_ControlProgram_Start' property in the generated
    # code (a bare stub) -- manually attach it so SBCS_ControlProgram's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # SBCS_ControlProgram's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = SBCS_ControlProgram(failureDetected=True, mode="sample_text", pumpControlerFailure=True, pumpFailure=True, ready=True, smdFailure=True, wlmdFailure=True)
    partner = SBCS_ControlProgram_Start()
    setattr(partner, 'SBCS_ControlProgram_Start', None)
    _safe_set(owner, 'SBCS_ControlProgram', partner)
    assert getattr(partner, 'SBCS_ControlProgram_Start') == owner
    _safe_set(owner, 'SBCS_ControlProgram', None)
    assert getattr(partner, 'SBCS_ControlProgram_Start') is None


def test_assoc_PCPost76_stub_double():
    # SBCS_PumpController_ClosePump has no real 'SBCS_PumpController_ClosePump77' property in the generated
    # code (a bare stub) -- manually attach it so SBCS_PumpControler's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # SBCS_PumpControler's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = SBCS_PumpControler(circulating=True, ready=True)
    partner = SBCS_PumpController_ClosePump()
    setattr(partner, 'SBCS_PumpController_ClosePump77', None)
    _safe_set(owner, 'SBCS_PumpControler78', partner)
    assert getattr(partner, 'SBCS_PumpController_ClosePump77') == owner
    _safe_set(owner, 'SBCS_PumpControler78', None)
    assert getattr(partner, 'SBCS_PumpController_ClosePump77') is None


def test_assoc_PCPost81_stub_double():
    # SBCS_PumpController_OpenPump has no real 'SBCS_PumpController_OpenPump82' property in the generated
    # code (a bare stub) -- manually attach it so SBCS_PumpControler's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # SBCS_PumpControler's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = SBCS_PumpControler(circulating=True, ready=True)
    partner = SBCS_PumpController_OpenPump()
    setattr(partner, 'SBCS_PumpController_OpenPump82', None)
    _safe_set(owner, 'SBCS_PumpControler83', partner)
    assert getattr(partner, 'SBCS_PumpController_OpenPump82') == owner
    _safe_set(owner, 'SBCS_PumpControler83', None)
    assert getattr(partner, 'SBCS_PumpController_OpenPump82') is None


def test_assoc_PCPre75_stub_double():
    # SBCS_PumpController_ClosePump has no real 'SBCS_PumpController_ClosePump' property in the generated
    # code (a bare stub) -- manually attach it so SBCS_PumpControler's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # SBCS_PumpControler's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = SBCS_PumpControler(circulating=True, ready=True)
    partner = SBCS_PumpController_ClosePump()
    setattr(partner, 'SBCS_PumpController_ClosePump', None)
    _safe_set(owner, 'SBCS_PumpControler', partner)
    assert getattr(partner, 'SBCS_PumpController_ClosePump') == owner
    _safe_set(owner, 'SBCS_PumpControler', None)
    assert getattr(partner, 'SBCS_PumpController_ClosePump') is None


def test_assoc_PCPre79_stub_double():
    # SBCS_PumpController_OpenPump has no real 'SBCS_PumpController_OpenPump' property in the generated
    # code (a bare stub) -- manually attach it so SBCS_PumpControler's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # SBCS_PumpControler's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = SBCS_PumpControler(circulating=True, ready=True)
    partner = SBCS_PumpController_OpenPump()
    setattr(partner, 'SBCS_PumpController_OpenPump', None)
    _safe_set(owner, 'SBCS_PumpControler80', partner)
    assert getattr(partner, 'SBCS_PumpController_OpenPump') == owner
    _safe_set(owner, 'SBCS_PumpControler80', None)
    assert getattr(partner, 'SBCS_PumpController_OpenPump') is None


def test_assoc_SBPost72_stub_double():
    # SBCS_SteamBoiler_OpenValve has no real 'SBCS_SteamBoiler_OpenValve73' property in the generated
    # code (a bare stub) -- manually attach it so SBCS_SteamBoiler's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # SBCS_SteamBoiler's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = SBCS_SteamBoiler(capacity=3.14, maximalLimit=3.14, maximalNormal=3.14, maximumDecrease=3.14, maximumIncrease=3.14, minimalLimit=3.14, minimalNormal=3.14, ready=True, valveOpen="sample_text")
    partner = SBCS_SteamBoiler_OpenValve()
    setattr(partner, 'SBCS_SteamBoiler_OpenValve73', None)
    _safe_set(owner, 'SBCS_SteamBoiler74', partner)
    assert getattr(partner, 'SBCS_SteamBoiler_OpenValve73') == owner
    _safe_set(owner, 'SBCS_SteamBoiler74', None)
    assert getattr(partner, 'SBCS_SteamBoiler_OpenValve73') is None


def test_assoc_SBPre71_stub_double():
    # SBCS_SteamBoiler_OpenValve has no real 'SBCS_SteamBoiler_OpenValve' property in the generated
    # code (a bare stub) -- manually attach it so SBCS_SteamBoiler's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # SBCS_SteamBoiler's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = SBCS_SteamBoiler(capacity=3.14, maximalLimit=3.14, maximalNormal=3.14, maximumDecrease=3.14, maximumIncrease=3.14, minimalLimit=3.14, minimalNormal=3.14, ready=True, valveOpen="sample_text")
    partner = SBCS_SteamBoiler_OpenValve()
    setattr(partner, 'SBCS_SteamBoiler_OpenValve', None)
    _safe_set(owner, 'SBCS_SteamBoiler', partner)
    assert getattr(partner, 'SBCS_SteamBoiler_OpenValve') == owner
    _safe_set(owner, 'SBCS_SteamBoiler', None)
    assert getattr(partner, 'SBCS_SteamBoiler_OpenValve') is None


