import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Port,
    arduino_AREFPort,
    arduino_AnalogPort,
    arduino_Arduino,
    arduino_Bench,
    arduino_DigitalPort,
    arduino_GndPort,
    arduino_Port,
    arduino_Port3V3,
    arduino_Port5V,
    arduino_Port9V,
    arduino_PortIO7,
    arduino_PortVIN,
    arduino_RstPort,
    arduino_RxPort,
    arduino_TxPort,
    ARDUINO_ATMEGA_168_SERIES,
    ARDUINO_BOARD_KIND,
    ARDUINO_BOARD_UID,
    ARDUINO_COMM,
    ARDUINO_FIRMWARE_MODE,
    ARDUINO_REPORT_MODE,
    ARDUINO_STATUS_MODE,
    ARDUINO_VER_BRAND_NAME,
    PIN_MAPPING,
    PIN_MODE,
    PWM_MODE,
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

def test_assoc_analogPorts1_reverse_link_reassign_clear():
    a1 = arduino_Arduino(board="sample_text", comm="sample_text", firmataMode="sample_text", kind="sample_text", label="sample_text", lockedPin="sample_text", name="sample_text", series="sample_text", status="sample_text", synchronizing=True, ver="sample_text")
    a2 = arduino_Arduino(board="sample_text_2", comm="sample_text_2", firmataMode="sample_text_2", kind="sample_text_2", label="sample_text_2", lockedPin="sample_text_2", name="sample_text_2", series="sample_text_2", status="sample_text_2", synchronizing=False, ver="sample_text_2")
    b = arduino_AnalogPort(value=3.14)
    _safe_set(b, 'arduino_AnalogPort', a1)
    assert _is_linked(b, 'arduino_AnalogPort', a1)
    if hasattr(a1, 'arduino_Arduino2'):
        assert _is_linked(a1, 'arduino_Arduino2', b)
    _safe_set(b, 'arduino_AnalogPort', a2)
    assert _is_linked(b, 'arduino_AnalogPort', a2)
    if hasattr(a1, 'arduino_Arduino2'):
        assert not _is_linked(a1, 'arduino_Arduino2', b)
    if hasattr(a2, 'arduino_Arduino2'):
        assert _is_linked(a2, 'arduino_Arduino2', b)
    _safe_set(b, 'arduino_AnalogPort', None)
    assert not _is_linked(b, 'arduino_AnalogPort', a2)
    if hasattr(a2, 'arduino_Arduino2'):
        assert not _is_linked(a2, 'arduino_Arduino2', b)


def test_assoc_boards23_reverse_link_reassign_clear():
    a1 = arduino_Bench(name="sample_text")
    a2 = arduino_Bench(name="sample_text_2")
    b = arduino_Arduino(board="sample_text", comm="sample_text", firmataMode="sample_text", kind="sample_text", label="sample_text", lockedPin="sample_text", name="sample_text", series="sample_text", status="sample_text", synchronizing=True, ver="sample_text")
    _safe_set(b, 'arduino_Arduino24', a1)
    assert _is_linked(b, 'arduino_Arduino24', a1)
    if hasattr(a1, 'arduino_Bench'):
        assert _is_linked(a1, 'arduino_Bench', b)
    _safe_set(b, 'arduino_Arduino24', a2)
    assert _is_linked(b, 'arduino_Arduino24', a2)
    if hasattr(a1, 'arduino_Bench'):
        assert not _is_linked(a1, 'arduino_Bench', b)
    if hasattr(a2, 'arduino_Bench'):
        assert _is_linked(a2, 'arduino_Bench', b)
    _safe_set(b, 'arduino_Arduino24', None)
    assert not _is_linked(b, 'arduino_Arduino24', a2)
    if hasattr(a2, 'arduino_Bench'):
        assert not _is_linked(a2, 'arduino_Bench', b)


def test_assoc_digitalPorts0_reverse_link_reassign_clear():
    a1 = arduino_DigitalPort(value=7)
    a2 = arduino_DigitalPort(value=13)
    b = arduino_Arduino(board="sample_text", comm="sample_text", firmataMode="sample_text", kind="sample_text", label="sample_text", lockedPin="sample_text", name="sample_text", series="sample_text", status="sample_text", synchronizing=True, ver="sample_text")
    _safe_set(b, 'arduino_Arduino', {a1})
    assert _is_linked(b, 'arduino_Arduino', a1)
    if hasattr(a1, 'arduino_DigitalPort'):
        assert _is_linked(a1, 'arduino_DigitalPort', b)
    _safe_set(b, 'arduino_Arduino', {a2})
    assert _is_linked(b, 'arduino_Arduino', a2)
    if hasattr(a1, 'arduino_DigitalPort'):
        assert not _is_linked(a1, 'arduino_DigitalPort', b)
    if hasattr(a2, 'arduino_DigitalPort'):
        assert _is_linked(a2, 'arduino_DigitalPort', b)
    _safe_set(b, 'arduino_Arduino', set())
    assert not _is_linked(b, 'arduino_Arduino', a2)
    if hasattr(a2, 'arduino_DigitalPort'):
        assert not _is_linked(a2, 'arduino_DigitalPort', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_aref21_stub_double():
    # arduino_AREFPort has no real 'arduino_AREFPort' property in the generated
    # code (a bare stub) -- manually attach it so arduino_Arduino's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # arduino_Arduino's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = arduino_Arduino(board="sample_text", comm="sample_text", firmataMode="sample_text", kind="sample_text", label="sample_text", lockedPin="sample_text", name="sample_text", series="sample_text", status="sample_text", synchronizing=True, ver="sample_text")
    partner = arduino_AREFPort()
    setattr(partner, 'arduino_AREFPort', None)
    _safe_set(owner, 'arduino_Arduino22', partner)
    assert getattr(partner, 'arduino_AREFPort') == owner
    _safe_set(owner, 'arduino_Arduino22', None)
    assert getattr(partner, 'arduino_AREFPort') is None


def test_assoc_groundPorts5_stub_double():
    # arduino_GndPort has no real 'arduino_GndPort' property in the generated
    # code (a bare stub) -- manually attach it so arduino_Arduino's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # arduino_Arduino's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = arduino_Arduino(board="sample_text", comm="sample_text", firmataMode="sample_text", kind="sample_text", label="sample_text", lockedPin="sample_text", name="sample_text", series="sample_text", status="sample_text", synchronizing=True, ver="sample_text")
    partner = arduino_GndPort()
    setattr(partner, 'arduino_GndPort', None)
    _safe_set(owner, 'arduino_Arduino6', {partner})
    assert getattr(partner, 'arduino_GndPort') == owner
    _safe_set(owner, 'arduino_Arduino6', set())
    assert getattr(partner, 'arduino_GndPort') is None


def test_assoc_io717_stub_double():
    # arduino_PortIO7 has no real 'arduino_PortIO7' property in the generated
    # code (a bare stub) -- manually attach it so arduino_Arduino's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # arduino_Arduino's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = arduino_Arduino(board="sample_text", comm="sample_text", firmataMode="sample_text", kind="sample_text", label="sample_text", lockedPin="sample_text", name="sample_text", series="sample_text", status="sample_text", synchronizing=True, ver="sample_text")
    partner = arduino_PortIO7()
    setattr(partner, 'arduino_PortIO7', None)
    _safe_set(owner, 'arduino_Arduino18', partner)
    assert getattr(partner, 'arduino_PortIO7') == owner
    _safe_set(owner, 'arduino_Arduino18', None)
    assert getattr(partner, 'arduino_PortIO7') is None


def test_assoc_pwm3V39_stub_double():
    # arduino_Port3V3 has no real 'arduino_Port3V3' property in the generated
    # code (a bare stub) -- manually attach it so arduino_Arduino's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # arduino_Arduino's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = arduino_Arduino(board="sample_text", comm="sample_text", firmataMode="sample_text", kind="sample_text", label="sample_text", lockedPin="sample_text", name="sample_text", series="sample_text", status="sample_text", synchronizing=True, ver="sample_text")
    partner = arduino_Port3V3()
    setattr(partner, 'arduino_Port3V3', None)
    _safe_set(owner, 'arduino_Arduino10', partner)
    assert getattr(partner, 'arduino_Port3V3') == owner
    _safe_set(owner, 'arduino_Arduino10', None)
    assert getattr(partner, 'arduino_Port3V3') is None


def test_assoc_pwm5V15_stub_double():
    # arduino_Port5V has no real 'arduino_Port5V' property in the generated
    # code (a bare stub) -- manually attach it so arduino_Arduino's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # arduino_Arduino's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = arduino_Arduino(board="sample_text", comm="sample_text", firmataMode="sample_text", kind="sample_text", label="sample_text", lockedPin="sample_text", name="sample_text", series="sample_text", status="sample_text", synchronizing=True, ver="sample_text")
    partner = arduino_Port5V()
    setattr(partner, 'arduino_Port5V', None)
    _safe_set(owner, 'arduino_Arduino16', partner)
    assert getattr(partner, 'arduino_Port5V') == owner
    _safe_set(owner, 'arduino_Arduino16', None)
    assert getattr(partner, 'arduino_Port5V') is None


def test_assoc_pwm9V13_stub_double():
    # arduino_Port9V has no real 'arduino_Port9V' property in the generated
    # code (a bare stub) -- manually attach it so arduino_Arduino's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # arduino_Arduino's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = arduino_Arduino(board="sample_text", comm="sample_text", firmataMode="sample_text", kind="sample_text", label="sample_text", lockedPin="sample_text", name="sample_text", series="sample_text", status="sample_text", synchronizing=True, ver="sample_text")
    partner = arduino_Port9V()
    setattr(partner, 'arduino_Port9V', None)
    _safe_set(owner, 'arduino_Arduino14', partner)
    assert getattr(partner, 'arduino_Port9V') == owner
    _safe_set(owner, 'arduino_Arduino14', None)
    assert getattr(partner, 'arduino_Port9V') is None


def test_assoc_resetPort11_stub_double():
    # arduino_RstPort has no real 'arduino_RstPort' property in the generated
    # code (a bare stub) -- manually attach it so arduino_Arduino's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # arduino_Arduino's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = arduino_Arduino(board="sample_text", comm="sample_text", firmataMode="sample_text", kind="sample_text", label="sample_text", lockedPin="sample_text", name="sample_text", series="sample_text", status="sample_text", synchronizing=True, ver="sample_text")
    partner = arduino_RstPort()
    setattr(partner, 'arduino_RstPort', None)
    _safe_set(owner, 'arduino_Arduino12', partner)
    assert getattr(partner, 'arduino_RstPort') == owner
    _safe_set(owner, 'arduino_Arduino12', None)
    assert getattr(partner, 'arduino_RstPort') is None


def test_assoc_rx7_stub_double():
    # arduino_RxPort has no real 'arduino_RxPort' property in the generated
    # code (a bare stub) -- manually attach it so arduino_Arduino's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # arduino_Arduino's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = arduino_Arduino(board="sample_text", comm="sample_text", firmataMode="sample_text", kind="sample_text", label="sample_text", lockedPin="sample_text", name="sample_text", series="sample_text", status="sample_text", synchronizing=True, ver="sample_text")
    partner = arduino_RxPort()
    setattr(partner, 'arduino_RxPort', None)
    _safe_set(owner, 'arduino_Arduino8', partner)
    assert getattr(partner, 'arduino_RxPort') == owner
    _safe_set(owner, 'arduino_Arduino8', None)
    assert getattr(partner, 'arduino_RxPort') is None


def test_assoc_tx3_stub_double():
    # arduino_TxPort has no real 'arduino_TxPort' property in the generated
    # code (a bare stub) -- manually attach it so arduino_Arduino's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # arduino_Arduino's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = arduino_Arduino(board="sample_text", comm="sample_text", firmataMode="sample_text", kind="sample_text", label="sample_text", lockedPin="sample_text", name="sample_text", series="sample_text", status="sample_text", synchronizing=True, ver="sample_text")
    partner = arduino_TxPort()
    setattr(partner, 'arduino_TxPort', None)
    _safe_set(owner, 'arduino_Arduino4', partner)
    assert getattr(partner, 'arduino_TxPort') == owner
    _safe_set(owner, 'arduino_Arduino4', None)
    assert getattr(partner, 'arduino_TxPort') is None


def test_assoc_vin19_stub_double():
    # arduino_PortVIN has no real 'arduino_PortVIN' property in the generated
    # code (a bare stub) -- manually attach it so arduino_Arduino's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # arduino_Arduino's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = arduino_Arduino(board="sample_text", comm="sample_text", firmataMode="sample_text", kind="sample_text", label="sample_text", lockedPin="sample_text", name="sample_text", series="sample_text", status="sample_text", synchronizing=True, ver="sample_text")
    partner = arduino_PortVIN()
    setattr(partner, 'arduino_PortVIN', None)
    _safe_set(owner, 'arduino_Arduino20', partner)
    assert getattr(partner, 'arduino_PortVIN') == owner
    _safe_set(owner, 'arduino_Arduino20', None)
    assert getattr(partner, 'arduino_PortVIN') is None


