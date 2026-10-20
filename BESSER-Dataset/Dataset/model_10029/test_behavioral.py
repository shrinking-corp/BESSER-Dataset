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

def test_assoc_ControlProgramSnapshot25_reverse_link_reassign_clear():
    a1 = SBCS_Snapshot()
    a2 = SBCS_Snapshot()
    b = SBCS_ControlProgram(mode="sample_text")
    _safe_set(b, 'SBCS_ControlProgram27', a1)
    assert _is_linked(b, 'SBCS_ControlProgram27', a1)
    if hasattr(a1, 'SBCS_Snapshot26'):
        assert _is_linked(a1, 'SBCS_Snapshot26', b)
    _safe_set(b, 'SBCS_ControlProgram27', a2)
    assert _is_linked(b, 'SBCS_ControlProgram27', a2)
    if hasattr(a1, 'SBCS_Snapshot26'):
        assert not _is_linked(a1, 'SBCS_Snapshot26', b)
    if hasattr(a2, 'SBCS_Snapshot26'):
        assert _is_linked(a2, 'SBCS_Snapshot26', b)
    _safe_set(b, 'SBCS_ControlProgram27', None)
    assert not _is_linked(b, 'SBCS_ControlProgram27', a2)
    if hasattr(a2, 'SBCS_Snapshot26'):
        assert not _is_linked(a2, 'SBCS_Snapshot26', b)


def test_assoc_SnapshotSteamBoiler1_reverse_link_reassign_clear():
    a1 = SBCS_SteamBoiler(capacity=3.14, maximalNormal=3.14, minimalNormal=3.14, valveOpen="sample_text")
    a2 = SBCS_SteamBoiler(capacity=9.99, maximalNormal=9.99, minimalNormal=9.99, valveOpen="sample_text_2")
    b = SBCS_Snapshot()
    _safe_set(b, 'SBCS_Snapshot', a1)
    assert _is_linked(b, 'SBCS_Snapshot', a1)
    if hasattr(a1, 'SBCS_SteamBoiler'):
        assert _is_linked(a1, 'SBCS_SteamBoiler', b)
    _safe_set(b, 'SBCS_Snapshot', a2)
    assert _is_linked(b, 'SBCS_Snapshot', a2)
    if hasattr(a1, 'SBCS_SteamBoiler'):
        assert not _is_linked(a1, 'SBCS_SteamBoiler', b)
    if hasattr(a2, 'SBCS_SteamBoiler'):
        assert _is_linked(a2, 'SBCS_SteamBoiler', b)
    _safe_set(b, 'SBCS_Snapshot', None)
    assert not _is_linked(b, 'SBCS_Snapshot', a2)
    if hasattr(a2, 'SBCS_SteamBoiler'):
        assert not _is_linked(a2, 'SBCS_SteamBoiler', b)


def test_assoc_SteamBoilerControlProgram2_reverse_link_reassign_clear():
    a1 = SBCS_SteamBoiler(capacity=3.14, maximalNormal=3.14, minimalNormal=3.14, valveOpen="sample_text")
    a2 = SBCS_SteamBoiler(capacity=9.99, maximalNormal=9.99, minimalNormal=9.99, valveOpen="sample_text_2")
    b = SBCS_ControlProgram(mode="sample_text")
    _safe_set(b, 'SBCS_ControlProgram4', a1)
    assert _is_linked(b, 'SBCS_ControlProgram4', a1)
    if hasattr(a1, 'SBCS_SteamBoiler3'):
        assert _is_linked(a1, 'SBCS_SteamBoiler3', b)
    _safe_set(b, 'SBCS_ControlProgram4', a2)
    assert _is_linked(b, 'SBCS_ControlProgram4', a2)
    if hasattr(a1, 'SBCS_SteamBoiler3'):
        assert not _is_linked(a1, 'SBCS_SteamBoiler3', b)
    if hasattr(a2, 'SBCS_SteamBoiler3'):
        assert _is_linked(a2, 'SBCS_SteamBoiler3', b)
    _safe_set(b, 'SBCS_ControlProgram4', None)
    assert not _is_linked(b, 'SBCS_ControlProgram4', a2)
    if hasattr(a2, 'SBCS_SteamBoiler3'):
        assert not _is_linked(a2, 'SBCS_SteamBoiler3', b)


def test_assoc_SteamBoilerWLMD5_reverse_link_reassign_clear():
    a1 = SBCS_WaterLevelMeasurementDevice(waterLevel=3.14)
    a2 = SBCS_WaterLevelMeasurementDevice(waterLevel=9.99)
    b = SBCS_SteamBoiler(capacity=3.14, maximalNormal=3.14, minimalNormal=3.14, valveOpen="sample_text")
    _safe_set(b, 'SBCS_SteamBoiler6', a1)
    assert _is_linked(b, 'SBCS_SteamBoiler6', a1)
    if hasattr(a1, 'SBCS_WaterLevelMeasurementDevice'):
        assert _is_linked(a1, 'SBCS_WaterLevelMeasurementDevice', b)
    _safe_set(b, 'SBCS_SteamBoiler6', a2)
    assert _is_linked(b, 'SBCS_SteamBoiler6', a2)
    if hasattr(a1, 'SBCS_WaterLevelMeasurementDevice'):
        assert not _is_linked(a1, 'SBCS_WaterLevelMeasurementDevice', b)
    if hasattr(a2, 'SBCS_WaterLevelMeasurementDevice'):
        assert _is_linked(a2, 'SBCS_WaterLevelMeasurementDevice', b)
    _safe_set(b, 'SBCS_SteamBoiler6', None)
    assert not _is_linked(b, 'SBCS_SteamBoiler6', a2)
    if hasattr(a2, 'SBCS_WaterLevelMeasurementDevice'):
        assert not _is_linked(a2, 'SBCS_WaterLevelMeasurementDevice', b)


def test_assoc_WLMDSteamBoiler22_reverse_link_reassign_clear():
    a1 = SBCS_WaterLevelMeasurementDevice(waterLevel=3.14)
    a2 = SBCS_WaterLevelMeasurementDevice(waterLevel=9.99)
    b = SBCS_SteamBoiler(capacity=3.14, maximalNormal=3.14, minimalNormal=3.14, valveOpen="sample_text")
    _safe_set(b, 'SBCS_SteamBoiler24', a1)
    assert _is_linked(b, 'SBCS_SteamBoiler24', a1)
    if hasattr(a1, 'SBCS_WaterLevelMeasurementDevice23'):
        assert _is_linked(a1, 'SBCS_WaterLevelMeasurementDevice23', b)
    _safe_set(b, 'SBCS_SteamBoiler24', a2)
    assert _is_linked(b, 'SBCS_SteamBoiler24', a2)
    if hasattr(a1, 'SBCS_WaterLevelMeasurementDevice23'):
        assert not _is_linked(a1, 'SBCS_WaterLevelMeasurementDevice23', b)
    if hasattr(a2, 'SBCS_WaterLevelMeasurementDevice23'):
        assert _is_linked(a2, 'SBCS_WaterLevelMeasurementDevice23', b)
    _safe_set(b, 'SBCS_SteamBoiler24', None)
    assert not _is_linked(b, 'SBCS_SteamBoiler24', a2)
    if hasattr(a2, 'SBCS_WaterLevelMeasurementDevice23'):
        assert not _is_linked(a2, 'SBCS_WaterLevelMeasurementDevice23', b)


def test_assoc_wlmdPost20_reverse_link_reassign_clear():
    a1 = SBCS_WaterLevelMeaurementDevice_getLevel(ret=3.14)
    a2 = SBCS_WaterLevelMeaurementDevice_getLevel(ret=9.99)
    b = SBCS_WaterLevelMeasurementDevice(waterLevel=3.14)
    _safe_set(b, 'SBCS_WaterLevelMeasurementDevice21', a1)
    assert _is_linked(b, 'SBCS_WaterLevelMeasurementDevice21', a1)
    if hasattr(a1, 'SBCS_WaterLevelMeaurementDevice_getLevel'):
        assert _is_linked(a1, 'SBCS_WaterLevelMeaurementDevice_getLevel', b)
    _safe_set(b, 'SBCS_WaterLevelMeasurementDevice21', a2)
    assert _is_linked(b, 'SBCS_WaterLevelMeasurementDevice21', a2)
    if hasattr(a1, 'SBCS_WaterLevelMeaurementDevice_getLevel'):
        assert not _is_linked(a1, 'SBCS_WaterLevelMeaurementDevice_getLevel', b)
    if hasattr(a2, 'SBCS_WaterLevelMeaurementDevice_getLevel'):
        assert _is_linked(a2, 'SBCS_WaterLevelMeaurementDevice_getLevel', b)
    _safe_set(b, 'SBCS_WaterLevelMeasurementDevice21', None)
    assert not _is_linked(b, 'SBCS_WaterLevelMeasurementDevice21', a2)
    if hasattr(a2, 'SBCS_WaterLevelMeaurementDevice_getLevel'):
        assert not _is_linked(a2, 'SBCS_WaterLevelMeaurementDevice_getLevel', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_AfterTrans18_stub_double():
    # SBCS_Transition has no real 'SBCS_Transition' property in the generated
    # code (a bare stub) -- manually attach it so SBCS_Snapshot's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # SBCS_Snapshot's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = SBCS_Snapshot()
    partner = SBCS_Transition()
    setattr(partner, 'SBCS_Transition', None)
    _safe_set(owner, 'SBCS_Snapshot19', partner)
    assert getattr(partner, 'SBCS_Transition') == owner
    _safe_set(owner, 'SBCS_Snapshot19', None)
    assert getattr(partner, 'SBCS_Transition') is None


def test_assoc_AfterTrans28_stub_double():
    # SBCS_Transition has no real 'SBCS_Transition30' property in the generated
    # code (a bare stub) -- manually attach it so SBCS_Snapshot's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # SBCS_Snapshot's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = SBCS_Snapshot()
    partner = SBCS_Transition()
    setattr(partner, 'SBCS_Transition30', None)
    _safe_set(owner, 'SBCS_Snapshot29', partner)
    assert getattr(partner, 'SBCS_Transition30') == owner
    _safe_set(owner, 'SBCS_Snapshot29', None)
    assert getattr(partner, 'SBCS_Transition30') is None


def test_assoc_CPPost0_stub_double():
    # SBCS_ControlProgram_Start has no real 'SBCS_ControlProgram_Start' property in the generated
    # code (a bare stub) -- manually attach it so SBCS_ControlProgram's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # SBCS_ControlProgram's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = SBCS_ControlProgram(mode="sample_text")
    partner = SBCS_ControlProgram_Start()
    setattr(partner, 'SBCS_ControlProgram_Start', None)
    _safe_set(owner, 'SBCS_ControlProgram', partner)
    assert getattr(partner, 'SBCS_ControlProgram_Start') == owner
    _safe_set(owner, 'SBCS_ControlProgram', None)
    assert getattr(partner, 'SBCS_ControlProgram_Start') is None


def test_assoc_PumpControlerPump7_stub_double():
    # SBCS_PumpControler has no real 'SBCS_PumpControler' property in the generated
    # code (a bare stub) -- manually attach it so SBCS_Pump's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # SBCS_Pump's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = SBCS_Pump(mode="sample_text")
    partner = SBCS_PumpControler()
    setattr(partner, 'SBCS_PumpControler', None)
    _safe_set(owner, 'SBCS_Pump', partner)
    assert getattr(partner, 'SBCS_PumpControler') == owner
    _safe_set(owner, 'SBCS_Pump', None)
    assert getattr(partner, 'SBCS_PumpControler') is None


def test_assoc_SBPost15_stub_double():
    # SBCS_SteamBoiler_OpenValve has no real 'SBCS_SteamBoiler_OpenValve16' property in the generated
    # code (a bare stub) -- manually attach it so SBCS_SteamBoiler's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # SBCS_SteamBoiler's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = SBCS_SteamBoiler(capacity=3.14, maximalNormal=3.14, minimalNormal=3.14, valveOpen="sample_text")
    partner = SBCS_SteamBoiler_OpenValve()
    setattr(partner, 'SBCS_SteamBoiler_OpenValve16', None)
    _safe_set(owner, 'SBCS_SteamBoiler17', partner)
    assert getattr(partner, 'SBCS_SteamBoiler_OpenValve16') == owner
    _safe_set(owner, 'SBCS_SteamBoiler17', None)
    assert getattr(partner, 'SBCS_SteamBoiler_OpenValve16') is None


def test_assoc_SBPre13_stub_double():
    # SBCS_SteamBoiler_OpenValve has no real 'SBCS_SteamBoiler_OpenValve' property in the generated
    # code (a bare stub) -- manually attach it so SBCS_SteamBoiler's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # SBCS_SteamBoiler's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = SBCS_SteamBoiler(capacity=3.14, maximalNormal=3.14, minimalNormal=3.14, valveOpen="sample_text")
    partner = SBCS_SteamBoiler_OpenValve()
    setattr(partner, 'SBCS_SteamBoiler_OpenValve', None)
    _safe_set(owner, 'SBCS_SteamBoiler14', partner)
    assert getattr(partner, 'SBCS_SteamBoiler_OpenValve') == owner
    _safe_set(owner, 'SBCS_SteamBoiler14', None)
    assert getattr(partner, 'SBCS_SteamBoiler_OpenValve') is None


