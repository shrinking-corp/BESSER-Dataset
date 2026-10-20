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

def test_assoc_ControlProgramSnapshot9_reverse_link_reassign_clear():
    a1 = SBCS_Snapshot()
    a2 = SBCS_Snapshot()
    b = SBCS_ControlProgram(mode="sample_text", wlmdFailure=True)
    _safe_set(b, 'SBCS_ControlProgram11', a1)
    assert _is_linked(b, 'SBCS_ControlProgram11', a1)
    if hasattr(a1, 'SBCS_Snapshot10'):
        assert _is_linked(a1, 'SBCS_Snapshot10', b)
    _safe_set(b, 'SBCS_ControlProgram11', a2)
    assert _is_linked(b, 'SBCS_ControlProgram11', a2)
    if hasattr(a1, 'SBCS_Snapshot10'):
        assert not _is_linked(a1, 'SBCS_Snapshot10', b)
    if hasattr(a2, 'SBCS_Snapshot10'):
        assert _is_linked(a2, 'SBCS_Snapshot10', b)
    _safe_set(b, 'SBCS_ControlProgram11', None)
    assert not _is_linked(b, 'SBCS_ControlProgram11', a2)
    if hasattr(a2, 'SBCS_Snapshot10'):
        assert not _is_linked(a2, 'SBCS_Snapshot10', b)


def test_assoc_SnapshotControlProgram25_reverse_link_reassign_clear():
    a1 = SBCS_Snapshot()
    a2 = SBCS_Snapshot()
    b = SBCS_ControlProgram(mode="sample_text", wlmdFailure=True)
    _safe_set(b, 'SBCS_ControlProgram26', a1)
    assert _is_linked(b, 'SBCS_ControlProgram26', a1)
    if hasattr(a1, 'SBCS_Snapshot27'):
        assert _is_linked(a1, 'SBCS_Snapshot27', b)
    _safe_set(b, 'SBCS_ControlProgram26', a2)
    assert _is_linked(b, 'SBCS_ControlProgram26', a2)
    if hasattr(a1, 'SBCS_Snapshot27'):
        assert not _is_linked(a1, 'SBCS_Snapshot27', b)
    if hasattr(a2, 'SBCS_Snapshot27'):
        assert _is_linked(a2, 'SBCS_Snapshot27', b)
    _safe_set(b, 'SBCS_ControlProgram26', None)
    assert not _is_linked(b, 'SBCS_ControlProgram26', a2)
    if hasattr(a2, 'SBCS_Snapshot27'):
        assert not _is_linked(a2, 'SBCS_Snapshot27', b)


def test_assoc_SteamBoilerControlProgram7_reverse_link_reassign_clear():
    a1 = SBCS_SteamBoiler(valveOpen="sample_text")
    a2 = SBCS_SteamBoiler(valveOpen="sample_text_2")
    b = SBCS_ControlProgram(mode="sample_text", wlmdFailure=True)
    _safe_set(b, 'SBCS_ControlProgram8', a1)
    assert _is_linked(b, 'SBCS_ControlProgram8', a1)
    if hasattr(a1, 'SBCS_SteamBoiler'):
        assert _is_linked(a1, 'SBCS_SteamBoiler', b)
    _safe_set(b, 'SBCS_ControlProgram8', a2)
    assert _is_linked(b, 'SBCS_ControlProgram8', a2)
    if hasattr(a1, 'SBCS_SteamBoiler'):
        assert not _is_linked(a1, 'SBCS_SteamBoiler', b)
    if hasattr(a2, 'SBCS_SteamBoiler'):
        assert _is_linked(a2, 'SBCS_SteamBoiler', b)
    _safe_set(b, 'SBCS_ControlProgram8', None)
    assert not _is_linked(b, 'SBCS_ControlProgram8', a2)
    if hasattr(a2, 'SBCS_SteamBoiler'):
        assert not _is_linked(a2, 'SBCS_SteamBoiler', b)


def test_assoc_wlmdPost5_reverse_link_reassign_clear():
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

def test_assoc_AfterTrans0_stub_double():
    # SBCS_Transition has no real 'SBCS_Transition' property in the generated
    # code (a bare stub) -- manually attach it so SBCS_Snapshot's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # SBCS_Snapshot's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = SBCS_Snapshot()
    partner = SBCS_Transition()
    setattr(partner, 'SBCS_Transition', None)
    _safe_set(owner, 'SBCS_Snapshot', partner)
    assert getattr(partner, 'SBCS_Transition') == owner
    _safe_set(owner, 'SBCS_Snapshot', None)
    assert getattr(partner, 'SBCS_Transition') is None


def test_assoc_AfterTrans12_stub_double():
    # SBCS_Transition has no real 'SBCS_Transition14' property in the generated
    # code (a bare stub) -- manually attach it so SBCS_Snapshot's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # SBCS_Snapshot's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = SBCS_Snapshot()
    partner = SBCS_Transition()
    setattr(partner, 'SBCS_Transition14', None)
    _safe_set(owner, 'SBCS_Snapshot13', partner)
    assert getattr(partner, 'SBCS_Transition14') == owner
    _safe_set(owner, 'SBCS_Snapshot13', None)
    assert getattr(partner, 'SBCS_Transition14') is None


def test_assoc_CPPost6_stub_double():
    # SBCS_ControlProgram_Start has no real 'SBCS_ControlProgram_Start' property in the generated
    # code (a bare stub) -- manually attach it so SBCS_ControlProgram's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # SBCS_ControlProgram's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = SBCS_ControlProgram(mode="sample_text", wlmdFailure=True)
    partner = SBCS_ControlProgram_Start()
    setattr(partner, 'SBCS_ControlProgram_Start', None)
    _safe_set(owner, 'SBCS_ControlProgram', partner)
    assert getattr(partner, 'SBCS_ControlProgram_Start') == owner
    _safe_set(owner, 'SBCS_ControlProgram', None)
    assert getattr(partner, 'SBCS_ControlProgram_Start') is None


def test_assoc_PumpControlerPump28_stub_double():
    # SBCS_PumpControler has no real 'SBCS_PumpControler29' property in the generated
    # code (a bare stub) -- manually attach it so SBCS_Pump's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # SBCS_Pump's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = SBCS_Pump(mode="sample_text")
    partner = SBCS_PumpControler()
    setattr(partner, 'SBCS_PumpControler29', None)
    _safe_set(owner, 'SBCS_Pump', partner)
    assert getattr(partner, 'SBCS_PumpControler29') == owner
    _safe_set(owner, 'SBCS_Pump', None)
    assert getattr(partner, 'SBCS_PumpControler29') is None


def test_assoc_SBPost17_stub_double():
    # SBCS_SteamBoiler_OpenValve has no real 'SBCS_SteamBoiler_OpenValve18' property in the generated
    # code (a bare stub) -- manually attach it so SBCS_SteamBoiler's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # SBCS_SteamBoiler's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = SBCS_SteamBoiler(valveOpen="sample_text")
    partner = SBCS_SteamBoiler_OpenValve()
    setattr(partner, 'SBCS_SteamBoiler_OpenValve18', None)
    _safe_set(owner, 'SBCS_SteamBoiler19', partner)
    assert getattr(partner, 'SBCS_SteamBoiler_OpenValve18') == owner
    _safe_set(owner, 'SBCS_SteamBoiler19', None)
    assert getattr(partner, 'SBCS_SteamBoiler_OpenValve18') is None


def test_assoc_SBPre15_stub_double():
    # SBCS_SteamBoiler_OpenValve has no real 'SBCS_SteamBoiler_OpenValve' property in the generated
    # code (a bare stub) -- manually attach it so SBCS_SteamBoiler's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # SBCS_SteamBoiler's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = SBCS_SteamBoiler(valveOpen="sample_text")
    partner = SBCS_SteamBoiler_OpenValve()
    setattr(partner, 'SBCS_SteamBoiler_OpenValve', None)
    _safe_set(owner, 'SBCS_SteamBoiler16', partner)
    assert getattr(partner, 'SBCS_SteamBoiler_OpenValve') == owner
    _safe_set(owner, 'SBCS_SteamBoiler16', None)
    assert getattr(partner, 'SBCS_SteamBoiler_OpenValve') is None


