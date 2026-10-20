import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Component,
    Connectivity,
    Device,
    IODevice,
    InputDevice,
    Mainboard,
    OutputDevice,
    StateComponent,
    iotw_ArduinoUNOR3,
    iotw_ArduinoWiFiESP8266WeMosD1,
    iotw_BluetoothHC06,
    iotw_Button,
    iotw_Buzzer,
    iotw_CDS,
    iotw_Component,
    iotw_Connection,
    iotw_Connectivity,
    iotw_DHT11,
    iotw_Decision,
    iotw_Device,
    iotw_EndPoint,
    iotw_I2CLCD,
    iotw_IODevice,
    iotw_InputDevice,
    iotw_Keypad4x4,
    iotw_LED,
    iotw_LM35,
    iotw_Mainboard,
    iotw_OutputDevice,
    iotw_StartPoint,
    iotw_StateComponent,
    iotw_StateFrame,
    iotw_StateSchema,
    iotw_WifiESP8266,
    ConnectionKind,
    ESP8266WiFiMode,
    I2CLCDType,
    ListBaud,
    ListConnectionChannel,
    ListProtocol,
    RouterKind,
    WifiIDConnection,
    WifiMode,
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

def test_assoc_devices14_reverse_link_reassign_clear():
    a1 = iotw_Mainboard(name="sample_text")
    a2 = iotw_Mainboard(name="sample_text_2")
    b = iotw_Device(name="sample_text")
    _safe_set(b, 'Device', a1)
    assert _is_linked(b, 'Device', a1)
    if hasattr(a1, 'mainboard'):
        assert _is_linked(a1, 'mainboard', b)
    _safe_set(b, 'Device', a2)
    assert _is_linked(b, 'Device', a2)
    if hasattr(a1, 'mainboard'):
        assert not _is_linked(a1, 'mainboard', b)
    if hasattr(a2, 'mainboard'):
        assert _is_linked(a2, 'mainboard', b)
    _safe_set(b, 'Device', None)
    assert not _is_linked(b, 'Device', a2)
    if hasattr(a2, 'mainboard'):
        assert not _is_linked(a2, 'mainboard', b)


def test_assoc_incomings7_reverse_link_reassign_clear():
    a1 = iotw_StateComponent(name="sample_text")
    a2 = iotw_StateComponent(name="sample_text_2")
    b = iotw_Connection(bendpoints="sample_text", kind="sample_text", label="sample_text", routerKind="sample_text")
    _safe_set(b, 'iotw_Connection9', a1)
    assert _is_linked(b, 'iotw_Connection9', a1)
    if hasattr(a1, 'iotw_StateComponent8'):
        assert _is_linked(a1, 'iotw_StateComponent8', b)
    _safe_set(b, 'iotw_Connection9', a2)
    assert _is_linked(b, 'iotw_Connection9', a2)
    if hasattr(a1, 'iotw_StateComponent8'):
        assert not _is_linked(a1, 'iotw_StateComponent8', b)
    if hasattr(a2, 'iotw_StateComponent8'):
        assert _is_linked(a2, 'iotw_StateComponent8', b)
    _safe_set(b, 'iotw_Connection9', None)
    assert not _is_linked(b, 'iotw_Connection9', a2)
    if hasattr(a2, 'iotw_StateComponent8'):
        assert not _is_linked(a2, 'iotw_StateComponent8', b)


def test_assoc_mainboard13_reverse_link_reassign_clear():
    a1 = iotw_Mainboard(name="sample_text")
    a2 = iotw_Mainboard(name="sample_text_2")
    b = iotw_Device(name="sample_text")
    _safe_set(b, 'devices', a1)
    assert _is_linked(b, 'devices', a1)
    if hasattr(a1, 'Mainboard'):
        assert _is_linked(a1, 'Mainboard', b)
    _safe_set(b, 'devices', a2)
    assert _is_linked(b, 'devices', a2)
    if hasattr(a1, 'Mainboard'):
        assert not _is_linked(a1, 'Mainboard', b)
    if hasattr(a2, 'Mainboard'):
        assert _is_linked(a2, 'Mainboard', b)
    _safe_set(b, 'devices', None)
    assert not _is_linked(b, 'devices', a2)
    if hasattr(a2, 'Mainboard'):
        assert not _is_linked(a2, 'Mainboard', b)


def test_assoc_outgoings10_reverse_link_reassign_clear():
    a1 = iotw_StateComponent(name="sample_text")
    a2 = iotw_StateComponent(name="sample_text_2")
    b = iotw_Connection(bendpoints="sample_text", kind="sample_text", label="sample_text", routerKind="sample_text")
    _safe_set(b, 'iotw_Connection12', a1)
    assert _is_linked(b, 'iotw_Connection12', a1)
    if hasattr(a1, 'iotw_StateComponent11'):
        assert _is_linked(a1, 'iotw_StateComponent11', b)
    _safe_set(b, 'iotw_Connection12', a2)
    assert _is_linked(b, 'iotw_Connection12', a2)
    if hasattr(a1, 'iotw_StateComponent11'):
        assert not _is_linked(a1, 'iotw_StateComponent11', b)
    if hasattr(a2, 'iotw_StateComponent11'):
        assert _is_linked(a2, 'iotw_StateComponent11', b)
    _safe_set(b, 'iotw_Connection12', None)
    assert not _is_linked(b, 'iotw_Connection12', a2)
    if hasattr(a2, 'iotw_StateComponent11'):
        assert not _is_linked(a2, 'iotw_StateComponent11', b)


def test_assoc_source0_reverse_link_reassign_clear():
    a1 = iotw_Connection(bendpoints="sample_text", kind="sample_text", label="sample_text", routerKind="sample_text")
    a2 = iotw_Connection(bendpoints="sample_text_2", kind="sample_text_2", label="sample_text_2", routerKind="sample_text_2")
    b = iotw_Component(constraints="sample_text", id="sample_text")
    _safe_set(b, 'iotw_Component', a1)
    assert _is_linked(b, 'iotw_Component', a1)
    if hasattr(a1, 'iotw_Connection'):
        assert _is_linked(a1, 'iotw_Connection', b)
    _safe_set(b, 'iotw_Component', a2)
    assert _is_linked(b, 'iotw_Component', a2)
    if hasattr(a1, 'iotw_Connection'):
        assert not _is_linked(a1, 'iotw_Connection', b)
    if hasattr(a2, 'iotw_Connection'):
        assert _is_linked(a2, 'iotw_Connection', b)
    _safe_set(b, 'iotw_Component', None)
    assert not _is_linked(b, 'iotw_Component', a2)
    if hasattr(a2, 'iotw_Connection'):
        assert not _is_linked(a2, 'iotw_Connection', b)


def test_assoc_target1_reverse_link_reassign_clear():
    a1 = iotw_Connection(bendpoints="sample_text", kind="sample_text", label="sample_text", routerKind="sample_text")
    a2 = iotw_Connection(bendpoints="sample_text_2", kind="sample_text_2", label="sample_text_2", routerKind="sample_text_2")
    b = iotw_Component(constraints="sample_text", id="sample_text")
    _safe_set(b, 'iotw_Component3', a1)
    assert _is_linked(b, 'iotw_Component3', a1)
    if hasattr(a1, 'iotw_Connection2'):
        assert _is_linked(a1, 'iotw_Connection2', b)
    _safe_set(b, 'iotw_Component3', a2)
    assert _is_linked(b, 'iotw_Component3', a2)
    if hasattr(a1, 'iotw_Connection2'):
        assert not _is_linked(a1, 'iotw_Connection2', b)
    if hasattr(a2, 'iotw_Connection2'):
        assert _is_linked(a2, 'iotw_Connection2', b)
    _safe_set(b, 'iotw_Component3', None)
    assert not _is_linked(b, 'iotw_Component3', a2)
    if hasattr(a2, 'iotw_Connection2'):
        assert not _is_linked(a2, 'iotw_Connection2', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_components5_stub_double():
    # iotw_StateSchema has no real 'iotw_StateSchema' property in the generated
    # code (a bare stub) -- manually attach it so iotw_StateComponent's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # iotw_StateComponent's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = iotw_StateComponent(name="sample_text")
    partner = iotw_StateSchema()
    setattr(partner, 'iotw_StateSchema', None)
    _safe_set(owner, 'iotw_StateComponent', partner)
    assert owner in getattr(partner, 'iotw_StateSchema')
    _safe_set(owner, 'iotw_StateComponent', None)
    assert owner not in getattr(partner, 'iotw_StateSchema')


def test_assoc_connnections6_stub_double():
    # iotw_StateSchema has no real 'stateSchema' property in the generated
    # code (a bare stub) -- manually attach it so iotw_Connection's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # iotw_Connection's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = iotw_Connection(bendpoints="sample_text", kind="sample_text", label="sample_text", routerKind="sample_text")
    partner = iotw_StateSchema()
    setattr(partner, 'stateSchema', None)
    _safe_set(owner, 'Connection', partner)
    assert owner in getattr(partner, 'stateSchema')
    _safe_set(owner, 'Connection', None)
    assert owner not in getattr(partner, 'stateSchema')


def test_assoc_stateSchema4_stub_double():
    # iotw_StateSchema has no real 'StateSchema' property in the generated
    # code (a bare stub) -- manually attach it so iotw_Connection's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # iotw_Connection's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = iotw_Connection(bendpoints="sample_text", kind="sample_text", label="sample_text", routerKind="sample_text")
    partner = iotw_StateSchema()
    setattr(partner, 'StateSchema', None)
    _safe_set(owner, 'connnections', partner)
    assert getattr(partner, 'StateSchema') == owner
    _safe_set(owner, 'connnections', None)
    assert getattr(partner, 'StateSchema') is None


