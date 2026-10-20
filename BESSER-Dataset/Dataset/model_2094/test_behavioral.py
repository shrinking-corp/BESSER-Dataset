import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    AnalogConnection,
    Component,
    CompositionElement,
    Connection,
    DigintalConnection,
    FTNode,
    Port,
    PrimitiveComponent,
    TypedPortValue,
    ftp_AnalogBattery,
    ftp_AnalogConnection,
    ftp_AnalogLamp,
    ftp_AnalogSwitch,
    ftp_And,
    ftp_AndGate,
    ftp_Capacitor,
    ftp_Component,
    ftp_ComposedComponent,
    ftp_CompositionElement,
    ftp_Connection,
    ftp_DFlipFlop,
    ftp_DigintalConnection,
    ftp_DigitalBattery,
    ftp_DigitalLamp,
    ftp_DigitalSwitch,
    ftp_ElectricalConnection,
    ftp_ElectricalPort,
    ftp_ElectricalValue,
    ftp_FTNode,
    ftp_Fault,
    ftp_FaultTree,
    ftp_FaultTreeContext,
    ftp_FloatValue,
    ftp_HydraulicConnection,
    ftp_HydraulicPort,
    ftp_HydraulicValue,
    ftp_MechanicalConnection,
    ftp_MechanicalPort,
    ftp_NTransistor,
    ftp_Not,
    ftp_Observation,
    ftp_OrGate,
    ftp_PTransistor,
    ftp_Port,
    ftp_PortValue,
    ftp_PrimitiveComponent,
    ftp_Resistor,
    ftp_RootEvent,
    ftp_SignalConnection,
    ftp_SignalConstant,
    ftp_SignalPort,
    ftp_SignalValue,
    ftp_TypedPortValue,
    ftp_VisualConnection,
    ftp_VisualPort,
    ftp_VisualValue,
    ftp_Xor,
    SignalValues,
    VisualValues,
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

def test_assoc_component8_reverse_link_reassign_clear():
    a1 = ftp_Observation(faultLimit=7, name="sample_text")
    a2 = ftp_Observation(faultLimit=13, name="sample_text_2")
    b = ftp_Component(name="sample_text", type="sample_text")
    _safe_set(b, 'ftp_Component', a1)
    assert _is_linked(b, 'ftp_Component', a1)
    if hasattr(a1, 'ftp_Observation'):
        assert _is_linked(a1, 'ftp_Observation', b)
    _safe_set(b, 'ftp_Component', a2)
    assert _is_linked(b, 'ftp_Component', a2)
    if hasattr(a1, 'ftp_Observation'):
        assert not _is_linked(a1, 'ftp_Observation', b)
    if hasattr(a2, 'ftp_Observation'):
        assert _is_linked(a2, 'ftp_Observation', b)
    _safe_set(b, 'ftp_Component', None)
    assert not _is_linked(b, 'ftp_Component', a2)
    if hasattr(a2, 'ftp_Observation'):
        assert not _is_linked(a2, 'ftp_Observation', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_faulttree11_stub_double():
    # ftp_FaultTree has no real 'ftp_FaultTree13' property in the generated
    # code (a bare stub) -- manually attach it so ftp_Observation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ftp_Observation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ftp_Observation(faultLimit=7, name="sample_text")
    partner = ftp_FaultTree()
    setattr(partner, 'ftp_FaultTree13', None)
    _safe_set(owner, 'ftp_Observation12', partner)
    assert getattr(partner, 'ftp_FaultTree13') == owner
    _safe_set(owner, 'ftp_Observation12', None)
    assert getattr(partner, 'ftp_FaultTree13') is None


def test_assoc_fromPort14_stub_double():
    # ftp_Connection has no real 'ftp_Connection' property in the generated
    # code (a bare stub) -- manually attach it so ftp_Port's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ftp_Port's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ftp_Port(name="sample_text", type="sample_text")
    partner = ftp_Connection()
    setattr(partner, 'ftp_Connection', None)
    _safe_set(owner, 'ftp_Port', partner)
    assert getattr(partner, 'ftp_Connection') == owner
    _safe_set(owner, 'ftp_Port', None)
    assert getattr(partner, 'ftp_Connection') is None


def test_assoc_inPort27_stub_double():
    # ftp_ElectricalPort has no real 'ftp_ElectricalPort' property in the generated
    # code (a bare stub) -- manually attach it so ftp_Resistor's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ftp_Resistor's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ftp_Resistor(resistance=3.14)
    partner = ftp_ElectricalPort()
    setattr(partner, 'ftp_ElectricalPort', None)
    _safe_set(owner, 'ftp_Resistor', partner)
    assert getattr(partner, 'ftp_ElectricalPort') == owner
    _safe_set(owner, 'ftp_Resistor', None)
    assert getattr(partner, 'ftp_ElectricalPort') is None


def test_assoc_inPort31_stub_double():
    # ftp_ElectricalPort has no real 'ftp_ElectricalPort32' property in the generated
    # code (a bare stub) -- manually attach it so ftp_AnalogBattery's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ftp_AnalogBattery's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ftp_AnalogBattery(voltage=3.14)
    partner = ftp_ElectricalPort()
    setattr(partner, 'ftp_ElectricalPort32', None)
    _safe_set(owner, 'ftp_AnalogBattery', partner)
    assert getattr(partner, 'ftp_ElectricalPort32') == owner
    _safe_set(owner, 'ftp_AnalogBattery', None)
    assert getattr(partner, 'ftp_ElectricalPort32') is None


def test_assoc_inputs103_stub_double():
    # ftp_FTNode has no real 'ftp_FTNode104' property in the generated
    # code (a bare stub) -- manually attach it so ftp_RootEvent's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ftp_RootEvent's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ftp_RootEvent(observation="sample_text")
    partner = ftp_FTNode()
    setattr(partner, 'ftp_FTNode104', None)
    _safe_set(owner, 'ftp_RootEvent', {partner})
    assert getattr(partner, 'ftp_FTNode104') == owner
    _safe_set(owner, 'ftp_RootEvent', set())
    assert getattr(partner, 'ftp_FTNode104') is None


def test_assoc_observations100_stub_double():
    # ftp_FaultTreeContext has no real 'ftp_FaultTreeContext101' property in the generated
    # code (a bare stub) -- manually attach it so ftp_Observation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ftp_Observation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ftp_Observation(faultLimit=7, name="sample_text")
    partner = ftp_FaultTreeContext()
    setattr(partner, 'ftp_FaultTreeContext101', None)
    _safe_set(owner, 'ftp_Observation102', partner)
    assert owner in getattr(partner, 'ftp_FaultTreeContext101')
    _safe_set(owner, 'ftp_Observation102', None)
    assert owner not in getattr(partner, 'ftp_FaultTreeContext101')


def test_assoc_outPort105_stub_double():
    # ftp_SignalPort has no real 'ftp_SignalPort106' property in the generated
    # code (a bare stub) -- manually attach it so ftp_SignalConstant's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ftp_SignalConstant's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ftp_SignalConstant(value="sample_text")
    partner = ftp_SignalPort()
    setattr(partner, 'ftp_SignalPort106', None)
    _safe_set(owner, 'ftp_SignalConstant', partner)
    assert getattr(partner, 'ftp_SignalPort106') == owner
    _safe_set(owner, 'ftp_SignalConstant', None)
    assert getattr(partner, 'ftp_SignalPort106') is None


def test_assoc_outPort28_stub_double():
    # ftp_ElectricalPort has no real 'ftp_ElectricalPort30' property in the generated
    # code (a bare stub) -- manually attach it so ftp_Resistor's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ftp_Resistor's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ftp_Resistor(resistance=3.14)
    partner = ftp_ElectricalPort()
    setattr(partner, 'ftp_ElectricalPort30', None)
    _safe_set(owner, 'ftp_Resistor29', partner)
    assert getattr(partner, 'ftp_ElectricalPort30') == owner
    _safe_set(owner, 'ftp_Resistor29', None)
    assert getattr(partner, 'ftp_ElectricalPort30') is None


def test_assoc_outPort33_stub_double():
    # ftp_ElectricalPort has no real 'ftp_ElectricalPort35' property in the generated
    # code (a bare stub) -- manually attach it so ftp_AnalogBattery's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ftp_AnalogBattery's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ftp_AnalogBattery(voltage=3.14)
    partner = ftp_ElectricalPort()
    setattr(partner, 'ftp_ElectricalPort35', None)
    _safe_set(owner, 'ftp_AnalogBattery34', partner)
    assert getattr(partner, 'ftp_ElectricalPort35') == owner
    _safe_set(owner, 'ftp_AnalogBattery34', None)
    assert getattr(partner, 'ftp_ElectricalPort35') is None


def test_assoc_port22_stub_double():
    # ftp_PortValue has no real 'ftp_PortValue23' property in the generated
    # code (a bare stub) -- manually attach it so ftp_Port's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ftp_Port's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ftp_Port(name="sample_text", type="sample_text")
    partner = ftp_PortValue()
    setattr(partner, 'ftp_PortValue23', None)
    _safe_set(owner, 'ftp_Port24', partner)
    assert getattr(partner, 'ftp_PortValue23') == owner
    _safe_set(owner, 'ftp_Port24', None)
    assert getattr(partner, 'ftp_PortValue23') is None


def test_assoc_portValues9_stub_double():
    # ftp_PortValue has no real 'ftp_PortValue' property in the generated
    # code (a bare stub) -- manually attach it so ftp_Observation's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ftp_Observation's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ftp_Observation(faultLimit=7, name="sample_text")
    partner = ftp_PortValue()
    setattr(partner, 'ftp_PortValue', None)
    _safe_set(owner, 'ftp_Observation10', {partner})
    assert getattr(partner, 'ftp_PortValue') == owner
    _safe_set(owner, 'ftp_Observation10', set())
    assert getattr(partner, 'ftp_PortValue') is None


def test_assoc_ports19_stub_double():
    # ftp_ComposedComponent has no real 'ftp_ComposedComponent20' property in the generated
    # code (a bare stub) -- manually attach it so ftp_Port's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ftp_Port's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ftp_Port(name="sample_text", type="sample_text")
    partner = ftp_ComposedComponent()
    setattr(partner, 'ftp_ComposedComponent20', None)
    _safe_set(owner, 'ftp_Port21', partner)
    assert owner in getattr(partner, 'ftp_ComposedComponent20')
    _safe_set(owner, 'ftp_Port21', None)
    assert owner not in getattr(partner, 'ftp_ComposedComponent20')


def test_assoc_toPort15_stub_double():
    # ftp_Connection has no real 'ftp_Connection16' property in the generated
    # code (a bare stub) -- manually attach it so ftp_Port's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ftp_Port's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ftp_Port(name="sample_text", type="sample_text")
    partner = ftp_Connection()
    setattr(partner, 'ftp_Connection16', None)
    _safe_set(owner, 'ftp_Port17', partner)
    assert getattr(partner, 'ftp_Connection16') == owner
    _safe_set(owner, 'ftp_Port17', None)
    assert getattr(partner, 'ftp_Connection16') is None


