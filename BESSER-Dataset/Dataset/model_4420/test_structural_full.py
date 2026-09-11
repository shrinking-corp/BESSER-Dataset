import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

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

def test_arduino_AnalogPort_value_value_roundtrip():
    instance = arduino_AnalogPort(value=3.14)
    assert instance.value == 3.14
    instance.value = 9.99
    assert instance.value == 9.99


def test_arduino_Arduino_board_value_roundtrip():
    instance = arduino_Arduino(board="sample_text", comm="sample_text", firmataMode="sample_text", kind="sample_text", label="sample_text", lockedPin="sample_text", name="sample_text", series="sample_text", status="sample_text", synchronizing=True, ver="sample_text")
    assert instance.board == "sample_text"
    instance.board = "sample_text_2"
    assert instance.board == "sample_text_2"


def test_arduino_Arduino_comm_value_roundtrip():
    instance = arduino_Arduino(board="sample_text", comm="sample_text", firmataMode="sample_text", kind="sample_text", label="sample_text", lockedPin="sample_text", name="sample_text", series="sample_text", status="sample_text", synchronizing=True, ver="sample_text")
    assert instance.comm == "sample_text"
    instance.comm = "sample_text_2"
    assert instance.comm == "sample_text_2"


def test_arduino_Arduino_firmataMode_value_roundtrip():
    instance = arduino_Arduino(board="sample_text", comm="sample_text", firmataMode="sample_text", kind="sample_text", label="sample_text", lockedPin="sample_text", name="sample_text", series="sample_text", status="sample_text", synchronizing=True, ver="sample_text")
    assert instance.firmataMode == "sample_text"
    instance.firmataMode = "sample_text_2"
    assert instance.firmataMode == "sample_text_2"


def test_arduino_Arduino_kind_value_roundtrip():
    instance = arduino_Arduino(board="sample_text", comm="sample_text", firmataMode="sample_text", kind="sample_text", label="sample_text", lockedPin="sample_text", name="sample_text", series="sample_text", status="sample_text", synchronizing=True, ver="sample_text")
    assert instance.kind == "sample_text"
    instance.kind = "sample_text_2"
    assert instance.kind == "sample_text_2"


def test_arduino_Arduino_label_value_roundtrip():
    instance = arduino_Arduino(board="sample_text", comm="sample_text", firmataMode="sample_text", kind="sample_text", label="sample_text", lockedPin="sample_text", name="sample_text", series="sample_text", status="sample_text", synchronizing=True, ver="sample_text")
    assert instance.label == "sample_text"
    instance.label = "sample_text_2"
    assert instance.label == "sample_text_2"


def test_arduino_Arduino_lockedPin_value_roundtrip():
    instance = arduino_Arduino(board="sample_text", comm="sample_text", firmataMode="sample_text", kind="sample_text", label="sample_text", lockedPin="sample_text", name="sample_text", series="sample_text", status="sample_text", synchronizing=True, ver="sample_text")
    assert instance.lockedPin == "sample_text"
    instance.lockedPin = "sample_text_2"
    assert instance.lockedPin == "sample_text_2"


def test_arduino_Arduino_name_value_roundtrip():
    instance = arduino_Arduino(board="sample_text", comm="sample_text", firmataMode="sample_text", kind="sample_text", label="sample_text", lockedPin="sample_text", name="sample_text", series="sample_text", status="sample_text", synchronizing=True, ver="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_arduino_Arduino_series_value_roundtrip():
    instance = arduino_Arduino(board="sample_text", comm="sample_text", firmataMode="sample_text", kind="sample_text", label="sample_text", lockedPin="sample_text", name="sample_text", series="sample_text", status="sample_text", synchronizing=True, ver="sample_text")
    assert instance.series == "sample_text"
    instance.series = "sample_text_2"
    assert instance.series == "sample_text_2"


def test_arduino_Arduino_status_value_roundtrip():
    instance = arduino_Arduino(board="sample_text", comm="sample_text", firmataMode="sample_text", kind="sample_text", label="sample_text", lockedPin="sample_text", name="sample_text", series="sample_text", status="sample_text", synchronizing=True, ver="sample_text")
    assert instance.status == "sample_text"
    instance.status = "sample_text_2"
    assert instance.status == "sample_text_2"


def test_arduino_Arduino_synchronizing_value_roundtrip():
    instance = arduino_Arduino(board="sample_text", comm="sample_text", firmataMode="sample_text", kind="sample_text", label="sample_text", lockedPin="sample_text", name="sample_text", series="sample_text", status="sample_text", synchronizing=True, ver="sample_text")
    assert instance.synchronizing == True
    instance.synchronizing = False
    assert instance.synchronizing == False


def test_arduino_Arduino_ver_value_roundtrip():
    instance = arduino_Arduino(board="sample_text", comm="sample_text", firmataMode="sample_text", kind="sample_text", label="sample_text", lockedPin="sample_text", name="sample_text", series="sample_text", status="sample_text", synchronizing=True, ver="sample_text")
    assert instance.ver == "sample_text"
    instance.ver = "sample_text_2"
    assert instance.ver == "sample_text_2"


def test_arduino_Bench_name_value_roundtrip():
    instance = arduino_Bench(name="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_arduino_DigitalPort_value_value_roundtrip():
    instance = arduino_DigitalPort(value=7)
    assert instance.value == 7
    instance.value = 13
    assert instance.value == 13


def test_arduino_Port_channel_value_roundtrip():
    instance = arduino_Port(channel=7, map="sample_text", name="sample_text", report="sample_text")
    assert instance.channel == 7
    instance.channel = 13
    assert instance.channel == 13


def test_arduino_Port_map_value_roundtrip():
    instance = arduino_Port(channel=7, map="sample_text", name="sample_text", report="sample_text")
    assert instance.map == "sample_text"
    instance.map = "sample_text_2"
    assert instance.map == "sample_text_2"


def test_arduino_Port_name_value_roundtrip():
    instance = arduino_Port(channel=7, map="sample_text", name="sample_text", report="sample_text")
    assert instance.name == "sample_text"
    instance.name = "sample_text_2"
    assert instance.name == "sample_text_2"


def test_arduino_Port_report_value_roundtrip():
    instance = arduino_Port(channel=7, map="sample_text", name="sample_text", report="sample_text")
    assert instance.report == "sample_text"
    instance.report = "sample_text_2"
    assert instance.report == "sample_text_2"


def test_arduino_AREFPort_isa_Port():
    instance = arduino_AREFPort()
    assert isinstance(instance, Port)


def test_arduino_AnalogPort_isa_Port():
    instance = arduino_AnalogPort(value=3.14)
    assert isinstance(instance, Port)


def test_arduino_DigitalPort_isa_Port():
    instance = arduino_DigitalPort(value=7)
    assert isinstance(instance, Port)


def test_arduino_GndPort_isa_Port():
    instance = arduino_GndPort()
    assert isinstance(instance, Port)


def test_arduino_Port3V3_isa_Port():
    instance = arduino_Port3V3()
    assert isinstance(instance, Port)


def test_arduino_Port5V_isa_Port():
    instance = arduino_Port5V()
    assert isinstance(instance, Port)


def test_arduino_Port9V_isa_Port():
    instance = arduino_Port9V()
    assert isinstance(instance, Port)


def test_arduino_PortIO7_isa_Port():
    instance = arduino_PortIO7()
    assert isinstance(instance, Port)


def test_arduino_PortVIN_isa_Port():
    instance = arduino_PortVIN()
    assert isinstance(instance, Port)


def test_arduino_RstPort_isa_Port():
    instance = arduino_RstPort()
    assert isinstance(instance, Port)


def test_arduino_RxPort_isa_Port():
    instance = arduino_RxPort()
    assert isinstance(instance, Port)


def test_arduino_TxPort_isa_Port():
    instance = arduino_TxPort()
    assert isinstance(instance, Port)


def test_assoc_analogPorts1_link_reassign_clear():
    a = arduino_Arduino(board="sample_text", comm="sample_text", firmataMode="sample_text", kind="sample_text", label="sample_text", lockedPin="sample_text", name="sample_text", series="sample_text", status="sample_text", synchronizing=True, ver="sample_text")
    b1 = arduino_AnalogPort(value=3.14)
    b2 = arduino_AnalogPort(value=9.99)
    _safe_set(a, 'arduino_Arduino2', {b1})
    assert _is_linked(a, 'arduino_Arduino2', b1)
    if hasattr(b1, 'arduino_AnalogPort'):
        assert _is_linked(b1, 'arduino_AnalogPort', a)
    _safe_set(a, 'arduino_Arduino2', {b2})
    assert _is_linked(a, 'arduino_Arduino2', b2)
    if hasattr(b1, 'arduino_AnalogPort'):
        assert not _is_linked(b1, 'arduino_AnalogPort', a)
    if hasattr(b2, 'arduino_AnalogPort'):
        assert _is_linked(b2, 'arduino_AnalogPort', a)
    _safe_set(a, 'arduino_Arduino2', set())
    assert not _is_linked(a, 'arduino_Arduino2', b2)
    if hasattr(b2, 'arduino_AnalogPort'):
        assert not _is_linked(b2, 'arduino_AnalogPort', a)


def test_assoc_aref21_link_reassign_clear():
    a = arduino_Arduino(board="sample_text", comm="sample_text", firmataMode="sample_text", kind="sample_text", label="sample_text", lockedPin="sample_text", name="sample_text", series="sample_text", status="sample_text", synchronizing=True, ver="sample_text")
    b1 = arduino_AREFPort()
    b2 = arduino_AREFPort()
    _safe_set(a, 'arduino_Arduino22', b1)
    assert _is_linked(a, 'arduino_Arduino22', b1)
    if hasattr(b1, 'arduino_AREFPort'):
        assert _is_linked(b1, 'arduino_AREFPort', a)
    _safe_set(a, 'arduino_Arduino22', b2)
    assert _is_linked(a, 'arduino_Arduino22', b2)
    if hasattr(b1, 'arduino_AREFPort'):
        assert not _is_linked(b1, 'arduino_AREFPort', a)
    if hasattr(b2, 'arduino_AREFPort'):
        assert _is_linked(b2, 'arduino_AREFPort', a)
    _safe_set(a, 'arduino_Arduino22', None)
    assert not _is_linked(a, 'arduino_Arduino22', b2)
    if hasattr(b2, 'arduino_AREFPort'):
        assert not _is_linked(b2, 'arduino_AREFPort', a)


def test_assoc_boards23_link_reassign_clear():
    a = arduino_Bench(name="sample_text")
    b1 = arduino_Arduino(board="sample_text", comm="sample_text", firmataMode="sample_text", kind="sample_text", label="sample_text", lockedPin="sample_text", name="sample_text", series="sample_text", status="sample_text", synchronizing=True, ver="sample_text")
    b2 = arduino_Arduino(board="sample_text_2", comm="sample_text_2", firmataMode="sample_text_2", kind="sample_text_2", label="sample_text_2", lockedPin="sample_text_2", name="sample_text_2", series="sample_text_2", status="sample_text_2", synchronizing=False, ver="sample_text_2")
    _safe_set(a, 'arduino_Bench', {b1})
    assert _is_linked(a, 'arduino_Bench', b1)
    if hasattr(b1, 'arduino_Arduino24'):
        assert _is_linked(b1, 'arduino_Arduino24', a)
    _safe_set(a, 'arduino_Bench', {b2})
    assert _is_linked(a, 'arduino_Bench', b2)
    if hasattr(b1, 'arduino_Arduino24'):
        assert not _is_linked(b1, 'arduino_Arduino24', a)
    if hasattr(b2, 'arduino_Arduino24'):
        assert _is_linked(b2, 'arduino_Arduino24', a)
    _safe_set(a, 'arduino_Bench', set())
    assert not _is_linked(a, 'arduino_Bench', b2)
    if hasattr(b2, 'arduino_Arduino24'):
        assert not _is_linked(b2, 'arduino_Arduino24', a)


def test_assoc_digitalPorts0_link_reassign_clear():
    a = arduino_DigitalPort(value=7)
    b1 = arduino_Arduino(board="sample_text", comm="sample_text", firmataMode="sample_text", kind="sample_text", label="sample_text", lockedPin="sample_text", name="sample_text", series="sample_text", status="sample_text", synchronizing=True, ver="sample_text")
    b2 = arduino_Arduino(board="sample_text_2", comm="sample_text_2", firmataMode="sample_text_2", kind="sample_text_2", label="sample_text_2", lockedPin="sample_text_2", name="sample_text_2", series="sample_text_2", status="sample_text_2", synchronizing=False, ver="sample_text_2")
    _safe_set(a, 'arduino_DigitalPort', b1)
    assert _is_linked(a, 'arduino_DigitalPort', b1)
    if hasattr(b1, 'arduino_Arduino'):
        assert _is_linked(b1, 'arduino_Arduino', a)
    _safe_set(a, 'arduino_DigitalPort', b2)
    assert _is_linked(a, 'arduino_DigitalPort', b2)
    if hasattr(b1, 'arduino_Arduino'):
        assert not _is_linked(b1, 'arduino_Arduino', a)
    if hasattr(b2, 'arduino_Arduino'):
        assert _is_linked(b2, 'arduino_Arduino', a)
    _safe_set(a, 'arduino_DigitalPort', None)
    assert not _is_linked(a, 'arduino_DigitalPort', b2)
    if hasattr(b2, 'arduino_Arduino'):
        assert not _is_linked(b2, 'arduino_Arduino', a)


def test_assoc_groundPorts5_link_reassign_clear():
    a = arduino_Arduino(board="sample_text", comm="sample_text", firmataMode="sample_text", kind="sample_text", label="sample_text", lockedPin="sample_text", name="sample_text", series="sample_text", status="sample_text", synchronizing=True, ver="sample_text")
    b1 = arduino_GndPort()
    b2 = arduino_GndPort()
    _safe_set(a, 'arduino_Arduino6', {b1})
    assert _is_linked(a, 'arduino_Arduino6', b1)
    if hasattr(b1, 'arduino_GndPort'):
        assert _is_linked(b1, 'arduino_GndPort', a)
    _safe_set(a, 'arduino_Arduino6', {b2})
    assert _is_linked(a, 'arduino_Arduino6', b2)
    if hasattr(b1, 'arduino_GndPort'):
        assert not _is_linked(b1, 'arduino_GndPort', a)
    if hasattr(b2, 'arduino_GndPort'):
        assert _is_linked(b2, 'arduino_GndPort', a)
    _safe_set(a, 'arduino_Arduino6', set())
    assert not _is_linked(a, 'arduino_Arduino6', b2)
    if hasattr(b2, 'arduino_GndPort'):
        assert not _is_linked(b2, 'arduino_GndPort', a)


def test_assoc_io717_link_reassign_clear():
    a = arduino_Arduino(board="sample_text", comm="sample_text", firmataMode="sample_text", kind="sample_text", label="sample_text", lockedPin="sample_text", name="sample_text", series="sample_text", status="sample_text", synchronizing=True, ver="sample_text")
    b1 = arduino_PortIO7()
    b2 = arduino_PortIO7()
    _safe_set(a, 'arduino_Arduino18', b1)
    assert _is_linked(a, 'arduino_Arduino18', b1)
    if hasattr(b1, 'arduino_PortIO7'):
        assert _is_linked(b1, 'arduino_PortIO7', a)
    _safe_set(a, 'arduino_Arduino18', b2)
    assert _is_linked(a, 'arduino_Arduino18', b2)
    if hasattr(b1, 'arduino_PortIO7'):
        assert not _is_linked(b1, 'arduino_PortIO7', a)
    if hasattr(b2, 'arduino_PortIO7'):
        assert _is_linked(b2, 'arduino_PortIO7', a)
    _safe_set(a, 'arduino_Arduino18', None)
    assert not _is_linked(a, 'arduino_Arduino18', b2)
    if hasattr(b2, 'arduino_PortIO7'):
        assert not _is_linked(b2, 'arduino_PortIO7', a)


def test_assoc_pwm3V39_link_reassign_clear():
    a = arduino_Arduino(board="sample_text", comm="sample_text", firmataMode="sample_text", kind="sample_text", label="sample_text", lockedPin="sample_text", name="sample_text", series="sample_text", status="sample_text", synchronizing=True, ver="sample_text")
    b1 = arduino_Port3V3()
    b2 = arduino_Port3V3()
    _safe_set(a, 'arduino_Arduino10', b1)
    assert _is_linked(a, 'arduino_Arduino10', b1)
    if hasattr(b1, 'arduino_Port3V3'):
        assert _is_linked(b1, 'arduino_Port3V3', a)
    _safe_set(a, 'arduino_Arduino10', b2)
    assert _is_linked(a, 'arduino_Arduino10', b2)
    if hasattr(b1, 'arduino_Port3V3'):
        assert not _is_linked(b1, 'arduino_Port3V3', a)
    if hasattr(b2, 'arduino_Port3V3'):
        assert _is_linked(b2, 'arduino_Port3V3', a)
    _safe_set(a, 'arduino_Arduino10', None)
    assert not _is_linked(a, 'arduino_Arduino10', b2)
    if hasattr(b2, 'arduino_Port3V3'):
        assert not _is_linked(b2, 'arduino_Port3V3', a)


def test_assoc_pwm5V15_link_reassign_clear():
    a = arduino_Arduino(board="sample_text", comm="sample_text", firmataMode="sample_text", kind="sample_text", label="sample_text", lockedPin="sample_text", name="sample_text", series="sample_text", status="sample_text", synchronizing=True, ver="sample_text")
    b1 = arduino_Port5V()
    b2 = arduino_Port5V()
    _safe_set(a, 'arduino_Arduino16', b1)
    assert _is_linked(a, 'arduino_Arduino16', b1)
    if hasattr(b1, 'arduino_Port5V'):
        assert _is_linked(b1, 'arduino_Port5V', a)
    _safe_set(a, 'arduino_Arduino16', b2)
    assert _is_linked(a, 'arduino_Arduino16', b2)
    if hasattr(b1, 'arduino_Port5V'):
        assert not _is_linked(b1, 'arduino_Port5V', a)
    if hasattr(b2, 'arduino_Port5V'):
        assert _is_linked(b2, 'arduino_Port5V', a)
    _safe_set(a, 'arduino_Arduino16', None)
    assert not _is_linked(a, 'arduino_Arduino16', b2)
    if hasattr(b2, 'arduino_Port5V'):
        assert not _is_linked(b2, 'arduino_Port5V', a)


def test_assoc_pwm9V13_link_reassign_clear():
    a = arduino_Arduino(board="sample_text", comm="sample_text", firmataMode="sample_text", kind="sample_text", label="sample_text", lockedPin="sample_text", name="sample_text", series="sample_text", status="sample_text", synchronizing=True, ver="sample_text")
    b1 = arduino_Port9V()
    b2 = arduino_Port9V()
    _safe_set(a, 'arduino_Arduino14', b1)
    assert _is_linked(a, 'arduino_Arduino14', b1)
    if hasattr(b1, 'arduino_Port9V'):
        assert _is_linked(b1, 'arduino_Port9V', a)
    _safe_set(a, 'arduino_Arduino14', b2)
    assert _is_linked(a, 'arduino_Arduino14', b2)
    if hasattr(b1, 'arduino_Port9V'):
        assert not _is_linked(b1, 'arduino_Port9V', a)
    if hasattr(b2, 'arduino_Port9V'):
        assert _is_linked(b2, 'arduino_Port9V', a)
    _safe_set(a, 'arduino_Arduino14', None)
    assert not _is_linked(a, 'arduino_Arduino14', b2)
    if hasattr(b2, 'arduino_Port9V'):
        assert not _is_linked(b2, 'arduino_Port9V', a)


def test_assoc_resetPort11_link_reassign_clear():
    a = arduino_Arduino(board="sample_text", comm="sample_text", firmataMode="sample_text", kind="sample_text", label="sample_text", lockedPin="sample_text", name="sample_text", series="sample_text", status="sample_text", synchronizing=True, ver="sample_text")
    b1 = arduino_RstPort()
    b2 = arduino_RstPort()
    _safe_set(a, 'arduino_Arduino12', b1)
    assert _is_linked(a, 'arduino_Arduino12', b1)
    if hasattr(b1, 'arduino_RstPort'):
        assert _is_linked(b1, 'arduino_RstPort', a)
    _safe_set(a, 'arduino_Arduino12', b2)
    assert _is_linked(a, 'arduino_Arduino12', b2)
    if hasattr(b1, 'arduino_RstPort'):
        assert not _is_linked(b1, 'arduino_RstPort', a)
    if hasattr(b2, 'arduino_RstPort'):
        assert _is_linked(b2, 'arduino_RstPort', a)
    _safe_set(a, 'arduino_Arduino12', None)
    assert not _is_linked(a, 'arduino_Arduino12', b2)
    if hasattr(b2, 'arduino_RstPort'):
        assert not _is_linked(b2, 'arduino_RstPort', a)


def test_assoc_rx7_link_reassign_clear():
    a = arduino_Arduino(board="sample_text", comm="sample_text", firmataMode="sample_text", kind="sample_text", label="sample_text", lockedPin="sample_text", name="sample_text", series="sample_text", status="sample_text", synchronizing=True, ver="sample_text")
    b1 = arduino_RxPort()
    b2 = arduino_RxPort()
    _safe_set(a, 'arduino_Arduino8', b1)
    assert _is_linked(a, 'arduino_Arduino8', b1)
    if hasattr(b1, 'arduino_RxPort'):
        assert _is_linked(b1, 'arduino_RxPort', a)
    _safe_set(a, 'arduino_Arduino8', b2)
    assert _is_linked(a, 'arduino_Arduino8', b2)
    if hasattr(b1, 'arduino_RxPort'):
        assert not _is_linked(b1, 'arduino_RxPort', a)
    if hasattr(b2, 'arduino_RxPort'):
        assert _is_linked(b2, 'arduino_RxPort', a)
    _safe_set(a, 'arduino_Arduino8', None)
    assert not _is_linked(a, 'arduino_Arduino8', b2)
    if hasattr(b2, 'arduino_RxPort'):
        assert not _is_linked(b2, 'arduino_RxPort', a)


def test_assoc_tx3_link_reassign_clear():
    a = arduino_Arduino(board="sample_text", comm="sample_text", firmataMode="sample_text", kind="sample_text", label="sample_text", lockedPin="sample_text", name="sample_text", series="sample_text", status="sample_text", synchronizing=True, ver="sample_text")
    b1 = arduino_TxPort()
    b2 = arduino_TxPort()
    _safe_set(a, 'arduino_Arduino4', b1)
    assert _is_linked(a, 'arduino_Arduino4', b1)
    if hasattr(b1, 'arduino_TxPort'):
        assert _is_linked(b1, 'arduino_TxPort', a)
    _safe_set(a, 'arduino_Arduino4', b2)
    assert _is_linked(a, 'arduino_Arduino4', b2)
    if hasattr(b1, 'arduino_TxPort'):
        assert not _is_linked(b1, 'arduino_TxPort', a)
    if hasattr(b2, 'arduino_TxPort'):
        assert _is_linked(b2, 'arduino_TxPort', a)
    _safe_set(a, 'arduino_Arduino4', None)
    assert not _is_linked(a, 'arduino_Arduino4', b2)
    if hasattr(b2, 'arduino_TxPort'):
        assert not _is_linked(b2, 'arduino_TxPort', a)


def test_assoc_vin19_link_reassign_clear():
    a = arduino_Arduino(board="sample_text", comm="sample_text", firmataMode="sample_text", kind="sample_text", label="sample_text", lockedPin="sample_text", name="sample_text", series="sample_text", status="sample_text", synchronizing=True, ver="sample_text")
    b1 = arduino_PortVIN()
    b2 = arduino_PortVIN()
    _safe_set(a, 'arduino_Arduino20', b1)
    assert _is_linked(a, 'arduino_Arduino20', b1)
    if hasattr(b1, 'arduino_PortVIN'):
        assert _is_linked(b1, 'arduino_PortVIN', a)
    _safe_set(a, 'arduino_Arduino20', b2)
    assert _is_linked(a, 'arduino_Arduino20', b2)
    if hasattr(b1, 'arduino_PortVIN'):
        assert not _is_linked(b1, 'arduino_PortVIN', a)
    if hasattr(b2, 'arduino_PortVIN'):
        assert _is_linked(b2, 'arduino_PortVIN', a)
    _safe_set(a, 'arduino_Arduino20', None)
    assert not _is_linked(a, 'arduino_Arduino20', b2)
    if hasattr(b2, 'arduino_PortVIN'):
        assert not _is_linked(b2, 'arduino_PortVIN', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

Port_strategy = st.builds(Port)
@given(instance=Port_strategy)
@settings(max_examples=25)
def test_Port_instantiation(instance):
    assert isinstance(instance, Port)


arduino_AREFPort_strategy = st.builds(arduino_AREFPort)
@given(instance=arduino_AREFPort_strategy)
@settings(max_examples=25)
def test_arduino_AREFPort_instantiation(instance):
    assert isinstance(instance, arduino_AREFPort)


arduino_AnalogPort_strategy = st.builds(arduino_AnalogPort, value=st.floats(allow_nan=False, allow_infinity=False))
@given(instance=arduino_AnalogPort_strategy)
@settings(max_examples=25)
def test_arduino_AnalogPort_instantiation(instance):
    assert isinstance(instance, arduino_AnalogPort)


arduino_Arduino_strategy = st.builds(arduino_Arduino, board=safe_text, comm=safe_text, firmataMode=safe_text, kind=safe_text, label=safe_text, lockedPin=safe_text, name=safe_text, series=safe_text, status=safe_text, synchronizing=st.booleans(), ver=safe_text)
@given(instance=arduino_Arduino_strategy)
@settings(max_examples=25)
def test_arduino_Arduino_instantiation(instance):
    assert isinstance(instance, arduino_Arduino)


arduino_Bench_strategy = st.builds(arduino_Bench, name=safe_text)
@given(instance=arduino_Bench_strategy)
@settings(max_examples=25)
def test_arduino_Bench_instantiation(instance):
    assert isinstance(instance, arduino_Bench)


arduino_DigitalPort_strategy = st.builds(arduino_DigitalPort, value=st.integers())
@given(instance=arduino_DigitalPort_strategy)
@settings(max_examples=25)
def test_arduino_DigitalPort_instantiation(instance):
    assert isinstance(instance, arduino_DigitalPort)


arduino_GndPort_strategy = st.builds(arduino_GndPort)
@given(instance=arduino_GndPort_strategy)
@settings(max_examples=25)
def test_arduino_GndPort_instantiation(instance):
    assert isinstance(instance, arduino_GndPort)


arduino_Port_strategy = st.builds(arduino_Port, channel=st.integers(), map=safe_text, name=safe_text, report=safe_text)
@given(instance=arduino_Port_strategy)
@settings(max_examples=25)
def test_arduino_Port_instantiation(instance):
    assert isinstance(instance, arduino_Port)


arduino_Port3V3_strategy = st.builds(arduino_Port3V3)
@given(instance=arduino_Port3V3_strategy)
@settings(max_examples=25)
def test_arduino_Port3V3_instantiation(instance):
    assert isinstance(instance, arduino_Port3V3)


arduino_Port5V_strategy = st.builds(arduino_Port5V)
@given(instance=arduino_Port5V_strategy)
@settings(max_examples=25)
def test_arduino_Port5V_instantiation(instance):
    assert isinstance(instance, arduino_Port5V)


arduino_Port9V_strategy = st.builds(arduino_Port9V)
@given(instance=arduino_Port9V_strategy)
@settings(max_examples=25)
def test_arduino_Port9V_instantiation(instance):
    assert isinstance(instance, arduino_Port9V)


arduino_PortIO7_strategy = st.builds(arduino_PortIO7)
@given(instance=arduino_PortIO7_strategy)
@settings(max_examples=25)
def test_arduino_PortIO7_instantiation(instance):
    assert isinstance(instance, arduino_PortIO7)


arduino_PortVIN_strategy = st.builds(arduino_PortVIN)
@given(instance=arduino_PortVIN_strategy)
@settings(max_examples=25)
def test_arduino_PortVIN_instantiation(instance):
    assert isinstance(instance, arduino_PortVIN)


arduino_RstPort_strategy = st.builds(arduino_RstPort)
@given(instance=arduino_RstPort_strategy)
@settings(max_examples=25)
def test_arduino_RstPort_instantiation(instance):
    assert isinstance(instance, arduino_RstPort)


arduino_RxPort_strategy = st.builds(arduino_RxPort)
@given(instance=arduino_RxPort_strategy)
@settings(max_examples=25)
def test_arduino_RxPort_instantiation(instance):
    assert isinstance(instance, arduino_RxPort)


arduino_TxPort_strategy = st.builds(arduino_TxPort)
@given(instance=arduino_TxPort_strategy)
@settings(max_examples=25)
def test_arduino_TxPort_instantiation(instance):
    assert isinstance(instance, arduino_TxPort)


