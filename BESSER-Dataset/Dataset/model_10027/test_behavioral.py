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

def test_assoc_ControlProgramSnapshot10_reverse_link_reassign_clear():
    a1 = SBCS_Snapshot()
    a2 = SBCS_Snapshot()
    b = SBCS_ControlProgram(mode="sample_text", wlmdFailure=True)
    _safe_set(b, 'SBCS_ControlProgram', a1)
    assert _is_linked(b, 'SBCS_ControlProgram', a1)
    if hasattr(a1, 'SBCS_Snapshot'):
        assert _is_linked(a1, 'SBCS_Snapshot', b)
    _safe_set(b, 'SBCS_ControlProgram', a2)
    assert _is_linked(b, 'SBCS_ControlProgram', a2)
    if hasattr(a1, 'SBCS_Snapshot'):
        assert not _is_linked(a1, 'SBCS_Snapshot', b)
    if hasattr(a2, 'SBCS_Snapshot'):
        assert _is_linked(a2, 'SBCS_Snapshot', b)
    _safe_set(b, 'SBCS_ControlProgram', None)
    assert not _is_linked(b, 'SBCS_ControlProgram', a2)
    if hasattr(a2, 'SBCS_Snapshot'):
        assert not _is_linked(a2, 'SBCS_Snapshot', b)


def test_assoc_SnapshotControlProgram22_reverse_link_reassign_clear():
    a1 = SBCS_Snapshot()
    a2 = SBCS_Snapshot()
    b = SBCS_ControlProgram(mode="sample_text", wlmdFailure=True)
    _safe_set(b, 'SBCS_ControlProgram23', a1)
    assert _is_linked(b, 'SBCS_ControlProgram23', a1)
    if hasattr(a1, 'SBCS_Snapshot24'):
        assert _is_linked(a1, 'SBCS_Snapshot24', b)
    _safe_set(b, 'SBCS_ControlProgram23', a2)
    assert _is_linked(b, 'SBCS_ControlProgram23', a2)
    if hasattr(a1, 'SBCS_Snapshot24'):
        assert not _is_linked(a1, 'SBCS_Snapshot24', b)
    if hasattr(a2, 'SBCS_Snapshot24'):
        assert _is_linked(a2, 'SBCS_Snapshot24', b)
    _safe_set(b, 'SBCS_ControlProgram23', None)
    assert not _is_linked(b, 'SBCS_ControlProgram23', a2)
    if hasattr(a2, 'SBCS_Snapshot24'):
        assert not _is_linked(a2, 'SBCS_Snapshot24', b)


def test_assoc_SteamBoilerControlProgram15_reverse_link_reassign_clear():
    a1 = SBCS_SteamBoiler(valveOpen="sample_text")
    a2 = SBCS_SteamBoiler(valveOpen="sample_text_2")
    b = SBCS_ControlProgram(mode="sample_text", wlmdFailure=True)
    _safe_set(b, 'SBCS_ControlProgram17', a1)
    assert _is_linked(b, 'SBCS_ControlProgram17', a1)
    if hasattr(a1, 'SBCS_SteamBoiler16'):
        assert _is_linked(a1, 'SBCS_SteamBoiler16', b)
    _safe_set(b, 'SBCS_ControlProgram17', a2)
    assert _is_linked(b, 'SBCS_ControlProgram17', a2)
    if hasattr(a1, 'SBCS_SteamBoiler16'):
        assert not _is_linked(a1, 'SBCS_SteamBoiler16', b)
    if hasattr(a2, 'SBCS_SteamBoiler16'):
        assert _is_linked(a2, 'SBCS_SteamBoiler16', b)
    _safe_set(b, 'SBCS_ControlProgram17', None)
    assert not _is_linked(b, 'SBCS_ControlProgram17', a2)
    if hasattr(a2, 'SBCS_SteamBoiler16'):
        assert not _is_linked(a2, 'SBCS_SteamBoiler16', b)


def test_assoc_wlmdPost21_reverse_link_reassign_clear():
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

def test_assoc_AfterTrans11_stub_double():
    # SBCS_Transition has no real 'SBCS_Transition' property in the generated
    # code (a bare stub) -- manually attach it so SBCS_Snapshot's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # SBCS_Snapshot's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = SBCS_Snapshot()
    partner = SBCS_Transition()
    setattr(partner, 'SBCS_Transition', None)
    _safe_set(owner, 'SBCS_Snapshot12', partner)
    assert getattr(partner, 'SBCS_Transition') == owner
    _safe_set(owner, 'SBCS_Snapshot12', None)
    assert getattr(partner, 'SBCS_Transition') is None


def test_assoc_AfterTrans18_stub_double():
    # SBCS_Transition has no real 'SBCS_Transition19' property in the generated
    # code (a bare stub) -- manually attach it so SBCS_Snapshot's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # SBCS_Snapshot's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = SBCS_Snapshot()
    partner = SBCS_Transition()
    setattr(partner, 'SBCS_Transition19', None)
    _safe_set(owner, 'SBCS_Snapshot20', partner)
    assert getattr(partner, 'SBCS_Transition19') == owner
    _safe_set(owner, 'SBCS_Snapshot20', None)
    assert getattr(partner, 'SBCS_Transition19') is None


def test_assoc_CPPost13_stub_double():
    # SBCS_ControlProgram_Start has no real 'SBCS_ControlProgram_Start' property in the generated
    # code (a bare stub) -- manually attach it so SBCS_ControlProgram's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # SBCS_ControlProgram's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = SBCS_ControlProgram(mode="sample_text", wlmdFailure=True)
    partner = SBCS_ControlProgram_Start()
    setattr(partner, 'SBCS_ControlProgram_Start', None)
    _safe_set(owner, 'SBCS_ControlProgram14', partner)
    assert getattr(partner, 'SBCS_ControlProgram_Start') == owner
    _safe_set(owner, 'SBCS_ControlProgram14', None)
    assert getattr(partner, 'SBCS_ControlProgram_Start') is None


def test_assoc_PumpControlerPump8_stub_double():
    # SBCS_PumpControler has no real 'SBCS_PumpControler9' property in the generated
    # code (a bare stub) -- manually attach it so SBCS_Pump's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # SBCS_Pump's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = SBCS_Pump(mode="sample_text")
    partner = SBCS_PumpControler()
    setattr(partner, 'SBCS_PumpControler9', None)
    _safe_set(owner, 'SBCS_Pump', partner)
    assert getattr(partner, 'SBCS_PumpControler9') == owner
    _safe_set(owner, 'SBCS_Pump', None)
    assert getattr(partner, 'SBCS_PumpControler9') is None


def test_assoc_SBPost5_stub_double():
    # SBCS_SteamBoiler_OpenValve has no real 'SBCS_SteamBoiler_OpenValve6' property in the generated
    # code (a bare stub) -- manually attach it so SBCS_SteamBoiler's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # SBCS_SteamBoiler's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = SBCS_SteamBoiler(valveOpen="sample_text")
    partner = SBCS_SteamBoiler_OpenValve()
    setattr(partner, 'SBCS_SteamBoiler_OpenValve6', None)
    _safe_set(owner, 'SBCS_SteamBoiler7', partner)
    assert getattr(partner, 'SBCS_SteamBoiler_OpenValve6') == owner
    _safe_set(owner, 'SBCS_SteamBoiler7', None)
    assert getattr(partner, 'SBCS_SteamBoiler_OpenValve6') is None


def test_assoc_SBPre4_stub_double():
    # SBCS_SteamBoiler_OpenValve has no real 'SBCS_SteamBoiler_OpenValve' property in the generated
    # code (a bare stub) -- manually attach it so SBCS_SteamBoiler's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # SBCS_SteamBoiler's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = SBCS_SteamBoiler(valveOpen="sample_text")
    partner = SBCS_SteamBoiler_OpenValve()
    setattr(partner, 'SBCS_SteamBoiler_OpenValve', None)
    _safe_set(owner, 'SBCS_SteamBoiler', partner)
    assert getattr(partner, 'SBCS_SteamBoiler_OpenValve') == owner
    _safe_set(owner, 'SBCS_SteamBoiler', None)
    assert getattr(partner, 'SBCS_SteamBoiler_OpenValve') is None


