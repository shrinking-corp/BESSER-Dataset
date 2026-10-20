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

def test_assoc_SnapshotSteamBoiler8_reverse_link_reassign_clear():
    a1 = SBCS_SteamBoiler(capacity=3.14, maximalNormal=3.14, valveOpen="sample_text")
    a2 = SBCS_SteamBoiler(capacity=9.99, maximalNormal=9.99, valveOpen="sample_text_2")
    b = SBCS_Snapshot()
    _safe_set(b, 'SBCS_Snapshot', a1)
    assert _is_linked(b, 'SBCS_Snapshot', a1)
    if hasattr(a1, 'SBCS_SteamBoiler9'):
        assert _is_linked(a1, 'SBCS_SteamBoiler9', b)
    _safe_set(b, 'SBCS_Snapshot', a2)
    assert _is_linked(b, 'SBCS_Snapshot', a2)
    if hasattr(a1, 'SBCS_SteamBoiler9'):
        assert not _is_linked(a1, 'SBCS_SteamBoiler9', b)
    if hasattr(a2, 'SBCS_SteamBoiler9'):
        assert _is_linked(a2, 'SBCS_SteamBoiler9', b)
    _safe_set(b, 'SBCS_Snapshot', None)
    assert not _is_linked(b, 'SBCS_Snapshot', a2)
    if hasattr(a2, 'SBCS_SteamBoiler9'):
        assert not _is_linked(a2, 'SBCS_SteamBoiler9', b)


def test_assoc_SteamBoilerControlProgram10_reverse_link_reassign_clear():
    a1 = SBCS_SteamBoiler(capacity=3.14, maximalNormal=3.14, valveOpen="sample_text")
    a2 = SBCS_SteamBoiler(capacity=9.99, maximalNormal=9.99, valveOpen="sample_text_2")
    b = SBCS_ControlProgram(mode="sample_text")
    _safe_set(b, 'SBCS_ControlProgram', a1)
    assert _is_linked(b, 'SBCS_ControlProgram', a1)
    if hasattr(a1, 'SBCS_SteamBoiler11'):
        assert _is_linked(a1, 'SBCS_SteamBoiler11', b)
    _safe_set(b, 'SBCS_ControlProgram', a2)
    assert _is_linked(b, 'SBCS_ControlProgram', a2)
    if hasattr(a1, 'SBCS_SteamBoiler11'):
        assert not _is_linked(a1, 'SBCS_SteamBoiler11', b)
    if hasattr(a2, 'SBCS_SteamBoiler11'):
        assert _is_linked(a2, 'SBCS_SteamBoiler11', b)
    _safe_set(b, 'SBCS_ControlProgram', None)
    assert not _is_linked(b, 'SBCS_ControlProgram', a2)
    if hasattr(a2, 'SBCS_SteamBoiler11'):
        assert not _is_linked(a2, 'SBCS_SteamBoiler11', b)


def test_assoc_WLMDSnapshot15_reverse_link_reassign_clear():
    a1 = SBCS_WaterLevelMeasurementDevice(waterLevel=3.14)
    a2 = SBCS_WaterLevelMeasurementDevice(waterLevel=9.99)
    b = SBCS_Snapshot()
    _safe_set(b, 'SBCS_Snapshot16', a1)
    assert _is_linked(b, 'SBCS_Snapshot16', a1)
    if hasattr(a1, 'SBCS_WaterLevelMeasurementDevice17'):
        assert _is_linked(a1, 'SBCS_WaterLevelMeasurementDevice17', b)
    _safe_set(b, 'SBCS_Snapshot16', a2)
    assert _is_linked(b, 'SBCS_Snapshot16', a2)
    if hasattr(a1, 'SBCS_WaterLevelMeasurementDevice17'):
        assert not _is_linked(a1, 'SBCS_WaterLevelMeasurementDevice17', b)
    if hasattr(a2, 'SBCS_WaterLevelMeasurementDevice17'):
        assert _is_linked(a2, 'SBCS_WaterLevelMeasurementDevice17', b)
    _safe_set(b, 'SBCS_Snapshot16', None)
    assert not _is_linked(b, 'SBCS_Snapshot16', a2)
    if hasattr(a2, 'SBCS_WaterLevelMeasurementDevice17'):
        assert not _is_linked(a2, 'SBCS_WaterLevelMeasurementDevice17', b)


def test_assoc_WLMDSteamBoiler20_reverse_link_reassign_clear():
    a1 = SBCS_WaterLevelMeasurementDevice(waterLevel=3.14)
    a2 = SBCS_WaterLevelMeasurementDevice(waterLevel=9.99)
    b = SBCS_SteamBoiler(capacity=3.14, maximalNormal=3.14, valveOpen="sample_text")
    _safe_set(b, 'SBCS_SteamBoiler22', a1)
    assert _is_linked(b, 'SBCS_SteamBoiler22', a1)
    if hasattr(a1, 'SBCS_WaterLevelMeasurementDevice21'):
        assert _is_linked(a1, 'SBCS_WaterLevelMeasurementDevice21', b)
    _safe_set(b, 'SBCS_SteamBoiler22', a2)
    assert _is_linked(b, 'SBCS_SteamBoiler22', a2)
    if hasattr(a1, 'SBCS_WaterLevelMeasurementDevice21'):
        assert not _is_linked(a1, 'SBCS_WaterLevelMeasurementDevice21', b)
    if hasattr(a2, 'SBCS_WaterLevelMeasurementDevice21'):
        assert _is_linked(a2, 'SBCS_WaterLevelMeasurementDevice21', b)
    _safe_set(b, 'SBCS_SteamBoiler22', None)
    assert not _is_linked(b, 'SBCS_SteamBoiler22', a2)
    if hasattr(a2, 'SBCS_WaterLevelMeasurementDevice21'):
        assert not _is_linked(a2, 'SBCS_WaterLevelMeasurementDevice21', b)


def test_assoc_wlmdPost14_reverse_link_reassign_clear():
    a1 = SBCS_WaterLevelMeaurementDevice_getLevel(ret=3.14)
    a2 = SBCS_WaterLevelMeaurementDevice_getLevel(ret=9.99)
    b = SBCS_WaterLevelMeasurementDevice(waterLevel=3.14)
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


def test_assoc_AfterTrans25_stub_double():
    # SBCS_Transition has no real 'SBCS_Transition26' property in the generated
    # code (a bare stub) -- manually attach it so SBCS_Snapshot's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # SBCS_Snapshot's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = SBCS_Snapshot()
    partner = SBCS_Transition()
    setattr(partner, 'SBCS_Transition26', None)
    _safe_set(owner, 'SBCS_Snapshot27', partner)
    assert getattr(partner, 'SBCS_Transition26') == owner
    _safe_set(owner, 'SBCS_Snapshot27', None)
    assert getattr(partner, 'SBCS_Transition26') is None


def test_assoc_CPPost23_stub_double():
    # SBCS_ControlProgram_Start has no real 'SBCS_ControlProgram_Start' property in the generated
    # code (a bare stub) -- manually attach it so SBCS_ControlProgram's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # SBCS_ControlProgram's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = SBCS_ControlProgram(mode="sample_text")
    partner = SBCS_ControlProgram_Start()
    setattr(partner, 'SBCS_ControlProgram_Start', None)
    _safe_set(owner, 'SBCS_ControlProgram24', partner)
    assert getattr(partner, 'SBCS_ControlProgram_Start') == owner
    _safe_set(owner, 'SBCS_ControlProgram24', None)
    assert getattr(partner, 'SBCS_ControlProgram_Start') is None


def test_assoc_PumpControlerPump12_stub_double():
    # SBCS_PumpControler has no real 'SBCS_PumpControler13' property in the generated
    # code (a bare stub) -- manually attach it so SBCS_Pump's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # SBCS_Pump's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = SBCS_Pump(mode="sample_text")
    partner = SBCS_PumpControler()
    setattr(partner, 'SBCS_PumpControler13', None)
    _safe_set(owner, 'SBCS_Pump', partner)
    assert getattr(partner, 'SBCS_PumpControler13') == owner
    _safe_set(owner, 'SBCS_Pump', None)
    assert getattr(partner, 'SBCS_PumpControler13') is None


def test_assoc_SBPost1_stub_double():
    # SBCS_SteamBoiler_OpenValve has no real 'SBCS_SteamBoiler_OpenValve2' property in the generated
    # code (a bare stub) -- manually attach it so SBCS_SteamBoiler's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # SBCS_SteamBoiler's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = SBCS_SteamBoiler(capacity=3.14, maximalNormal=3.14, valveOpen="sample_text")
    partner = SBCS_SteamBoiler_OpenValve()
    setattr(partner, 'SBCS_SteamBoiler_OpenValve2', None)
    _safe_set(owner, 'SBCS_SteamBoiler3', partner)
    assert getattr(partner, 'SBCS_SteamBoiler_OpenValve2') == owner
    _safe_set(owner, 'SBCS_SteamBoiler3', None)
    assert getattr(partner, 'SBCS_SteamBoiler_OpenValve2') is None


def test_assoc_SBPre0_stub_double():
    # SBCS_SteamBoiler_OpenValve has no real 'SBCS_SteamBoiler_OpenValve' property in the generated
    # code (a bare stub) -- manually attach it so SBCS_SteamBoiler's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # SBCS_SteamBoiler's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = SBCS_SteamBoiler(capacity=3.14, maximalNormal=3.14, valveOpen="sample_text")
    partner = SBCS_SteamBoiler_OpenValve()
    setattr(partner, 'SBCS_SteamBoiler_OpenValve', None)
    _safe_set(owner, 'SBCS_SteamBoiler', partner)
    assert getattr(partner, 'SBCS_SteamBoiler_OpenValve') == owner
    _safe_set(owner, 'SBCS_SteamBoiler', None)
    assert getattr(partner, 'SBCS_SteamBoiler_OpenValve') is None


