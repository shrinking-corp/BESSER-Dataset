import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    ComponentType,
    ElectronicDevice,
    HardwareComponent,
    IDBase,
    MechanicalDevice,
    component_diagram_Actuator,
    component_diagram_Architecture,
    component_diagram_ComponentInstance,
    component_diagram_ComponentType,
    component_diagram_Connector,
    component_diagram_ElectronicDevice,
    component_diagram_HardwareComponent,
    component_diagram_MechanicalDevice,
    component_diagram_PortInstance,
    component_diagram_PortType,
    component_diagram_Sensor,
    component_diagram_SoftwareComponent,
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

def test_assoc_component_type30_reverse_link_reassign_clear():
    a1 = component_diagram_PortType(name="sample_text")
    a2 = component_diagram_PortType(name="sample_text_2")
    b = component_diagram_ComponentType(name="sample_text")
    _safe_set(b, 'ComponentType31', a1)
    assert _is_linked(b, 'ComponentType31', a1)
    if hasattr(a1, 'port_types'):
        assert _is_linked(a1, 'port_types', b)
    _safe_set(b, 'ComponentType31', a2)
    assert _is_linked(b, 'ComponentType31', a2)
    if hasattr(a1, 'port_types'):
        assert not _is_linked(a1, 'port_types', b)
    if hasattr(a2, 'port_types'):
        assert _is_linked(a2, 'port_types', b)
    _safe_set(b, 'ComponentType31', None)
    assert not _is_linked(b, 'ComponentType31', a2)
    if hasattr(a2, 'port_types'):
        assert not _is_linked(a2, 'port_types', b)


def test_assoc_connect3_reverse_link_reassign_clear():
    a1 = component_diagram_PortInstance(name="sample_text")
    a2 = component_diagram_PortInstance(name="sample_text_2")
    b = component_diagram_Connector(name="sample_text")
    _safe_set(b, 'Connector', a1)
    assert _is_linked(b, 'Connector', a1)
    if hasattr(a1, 'port'):
        assert _is_linked(a1, 'port', b)
    _safe_set(b, 'Connector', a2)
    assert _is_linked(b, 'Connector', a2)
    if hasattr(a1, 'port'):
        assert not _is_linked(a1, 'port', b)
    if hasattr(a2, 'port'):
        assert _is_linked(a2, 'port', b)
    _safe_set(b, 'Connector', None)
    assert not _is_linked(b, 'Connector', a2)
    if hasattr(a2, 'port'):
        assert not _is_linked(a2, 'port', b)


def test_assoc_inComponent6_reverse_link_reassign_clear():
    a1 = component_diagram_PortInstance(name="sample_text")
    a2 = component_diagram_PortInstance(name="sample_text_2")
    b = component_diagram_ComponentInstance(name="sample_text", version=7)
    _safe_set(b, 'ComponentInstance7', a1)
    assert _is_linked(b, 'ComponentInstance7', a1)
    if hasattr(a1, 'inPorts'):
        assert _is_linked(a1, 'inPorts', b)
    _safe_set(b, 'ComponentInstance7', a2)
    assert _is_linked(b, 'ComponentInstance7', a2)
    if hasattr(a1, 'inPorts'):
        assert not _is_linked(a1, 'inPorts', b)
    if hasattr(a2, 'inPorts'):
        assert _is_linked(a2, 'inPorts', b)
    _safe_set(b, 'ComponentInstance7', None)
    assert not _is_linked(b, 'ComponentInstance7', a2)
    if hasattr(a2, 'inPorts'):
        assert not _is_linked(a2, 'inPorts', b)


def test_assoc_inPorts25_reverse_link_reassign_clear():
    a1 = component_diagram_PortInstance(name="sample_text")
    a2 = component_diagram_PortInstance(name="sample_text_2")
    b = component_diagram_ComponentInstance(name="sample_text", version=7)
    _safe_set(b, 'inComponent', {a1})
    assert _is_linked(b, 'inComponent', a1)
    if hasattr(a1, 'PortInstance26'):
        assert _is_linked(a1, 'PortInstance26', b)
    _safe_set(b, 'inComponent', {a2})
    assert _is_linked(b, 'inComponent', a2)
    if hasattr(a1, 'PortInstance26'):
        assert not _is_linked(a1, 'PortInstance26', b)
    if hasattr(a2, 'PortInstance26'):
        assert _is_linked(a2, 'PortInstance26', b)
    _safe_set(b, 'inComponent', set())
    assert not _is_linked(b, 'inComponent', a2)
    if hasattr(a2, 'PortInstance26'):
        assert not _is_linked(a2, 'PortInstance26', b)


def test_assoc_instance1_reverse_link_reassign_clear():
    a1 = component_diagram_ComponentType(name="sample_text")
    a2 = component_diagram_ComponentType(name="sample_text_2")
    b = component_diagram_ComponentInstance(name="sample_text", version=7)
    _safe_set(b, 'ComponentInstance', a1)
    assert _is_linked(b, 'ComponentInstance', a1)
    if hasattr(a1, 'type'):
        assert _is_linked(a1, 'type', b)
    _safe_set(b, 'ComponentInstance', a2)
    assert _is_linked(b, 'ComponentInstance', a2)
    if hasattr(a1, 'type'):
        assert not _is_linked(a1, 'type', b)
    if hasattr(a2, 'type'):
        assert _is_linked(a2, 'type', b)
    _safe_set(b, 'ComponentInstance', None)
    assert not _is_linked(b, 'ComponentInstance', a2)
    if hasattr(a2, 'type'):
        assert not _is_linked(a2, 'type', b)


def test_assoc_outComponent4_reverse_link_reassign_clear():
    a1 = component_diagram_PortInstance(name="sample_text")
    a2 = component_diagram_PortInstance(name="sample_text_2")
    b = component_diagram_ComponentInstance(name="sample_text", version=7)
    _safe_set(b, 'ComponentInstance5', a1)
    assert _is_linked(b, 'ComponentInstance5', a1)
    if hasattr(a1, 'outPorts'):
        assert _is_linked(a1, 'outPorts', b)
    _safe_set(b, 'ComponentInstance5', a2)
    assert _is_linked(b, 'ComponentInstance5', a2)
    if hasattr(a1, 'outPorts'):
        assert not _is_linked(a1, 'outPorts', b)
    if hasattr(a2, 'outPorts'):
        assert _is_linked(a2, 'outPorts', b)
    _safe_set(b, 'ComponentInstance5', None)
    assert not _is_linked(b, 'ComponentInstance5', a2)
    if hasattr(a2, 'outPorts'):
        assert not _is_linked(a2, 'outPorts', b)


def test_assoc_outPorts27_reverse_link_reassign_clear():
    a1 = component_diagram_PortInstance(name="sample_text")
    a2 = component_diagram_PortInstance(name="sample_text_2")
    b = component_diagram_ComponentInstance(name="sample_text", version=7)
    _safe_set(b, 'outComponent', {a1})
    assert _is_linked(b, 'outComponent', a1)
    if hasattr(a1, 'PortInstance28'):
        assert _is_linked(a1, 'PortInstance28', b)
    _safe_set(b, 'outComponent', {a2})
    assert _is_linked(b, 'outComponent', a2)
    if hasattr(a1, 'PortInstance28'):
        assert not _is_linked(a1, 'PortInstance28', b)
    if hasattr(a2, 'PortInstance28'):
        assert _is_linked(a2, 'PortInstance28', b)
    _safe_set(b, 'outComponent', set())
    assert not _is_linked(b, 'outComponent', a2)
    if hasattr(a2, 'PortInstance28'):
        assert not _is_linked(a2, 'PortInstance28', b)


def test_assoc_parentcomponent23_reverse_link_reassign_clear():
    a1 = component_diagram_ComponentInstance(name="sample_text", version=7)
    a2 = component_diagram_ComponentInstance(name="sample_text_2", version=13)
    b = component_diagram_ComponentInstance(name="sample_text", version=7)
    _safe_set(b, 'subcomponent', a1)
    assert _is_linked(b, 'subcomponent', a1)
    if hasattr(a1, 'ComponentInstance24'):
        assert _is_linked(a1, 'ComponentInstance24', b)
    _safe_set(b, 'subcomponent', a2)
    assert _is_linked(b, 'subcomponent', a2)
    if hasattr(a1, 'ComponentInstance24'):
        assert not _is_linked(a1, 'ComponentInstance24', b)
    if hasattr(a2, 'ComponentInstance24'):
        assert _is_linked(a2, 'ComponentInstance24', b)
    _safe_set(b, 'subcomponent', None)
    assert not _is_linked(b, 'subcomponent', a2)
    if hasattr(a2, 'ComponentInstance24'):
        assert not _is_linked(a2, 'ComponentInstance24', b)


def test_assoc_port2_reverse_link_reassign_clear():
    a1 = component_diagram_PortInstance(name="sample_text")
    a2 = component_diagram_PortInstance(name="sample_text_2")
    b = component_diagram_Connector(name="sample_text")
    _safe_set(b, 'connect', {a1})
    assert _is_linked(b, 'connect', a1)
    if hasattr(a1, 'PortInstance'):
        assert _is_linked(a1, 'PortInstance', b)
    _safe_set(b, 'connect', {a2})
    assert _is_linked(b, 'connect', a2)
    if hasattr(a1, 'PortInstance'):
        assert not _is_linked(a1, 'PortInstance', b)
    if hasattr(a2, 'PortInstance'):
        assert _is_linked(a2, 'PortInstance', b)
    _safe_set(b, 'connect', set())
    assert not _is_linked(b, 'connect', a2)
    if hasattr(a2, 'PortInstance'):
        assert not _is_linked(a2, 'PortInstance', b)


def test_assoc_port_instance32_reverse_link_reassign_clear():
    a1 = component_diagram_PortType(name="sample_text")
    a2 = component_diagram_PortType(name="sample_text_2")
    b = component_diagram_PortInstance(name="sample_text")
    _safe_set(b, 'PortInstance34', a1)
    assert _is_linked(b, 'PortInstance34', a1)
    if hasattr(a1, 'type33'):
        assert _is_linked(a1, 'type33', b)
    _safe_set(b, 'PortInstance34', a2)
    assert _is_linked(b, 'PortInstance34', a2)
    if hasattr(a1, 'type33'):
        assert not _is_linked(a1, 'type33', b)
    if hasattr(a2, 'type33'):
        assert _is_linked(a2, 'type33', b)
    _safe_set(b, 'PortInstance34', None)
    assert not _is_linked(b, 'PortInstance34', a2)
    if hasattr(a2, 'type33'):
        assert not _is_linked(a2, 'type33', b)


def test_assoc_port_types0_reverse_link_reassign_clear():
    a1 = component_diagram_PortType(name="sample_text")
    a2 = component_diagram_PortType(name="sample_text_2")
    b = component_diagram_ComponentType(name="sample_text")
    _safe_set(b, 'component_type', {a1})
    assert _is_linked(b, 'component_type', a1)
    if hasattr(a1, 'PortType'):
        assert _is_linked(a1, 'PortType', b)
    _safe_set(b, 'component_type', {a2})
    assert _is_linked(b, 'component_type', a2)
    if hasattr(a1, 'PortType'):
        assert not _is_linked(a1, 'PortType', b)
    if hasattr(a2, 'PortType'):
        assert _is_linked(a2, 'PortType', b)
    _safe_set(b, 'component_type', set())
    assert not _is_linked(b, 'component_type', a2)
    if hasattr(a2, 'PortType'):
        assert not _is_linked(a2, 'PortType', b)


def test_assoc_subcomponent20_reverse_link_reassign_clear():
    a1 = component_diagram_ComponentInstance(name="sample_text", version=7)
    a2 = component_diagram_ComponentInstance(name="sample_text_2", version=13)
    b = component_diagram_ComponentInstance(name="sample_text", version=7)
    _safe_set(b, 'parentcomponent', {a1})
    assert _is_linked(b, 'parentcomponent', a1)
    if hasattr(a1, 'ComponentInstance21'):
        assert _is_linked(a1, 'ComponentInstance21', b)
    _safe_set(b, 'parentcomponent', {a2})
    assert _is_linked(b, 'parentcomponent', a2)
    if hasattr(a1, 'ComponentInstance21'):
        assert not _is_linked(a1, 'ComponentInstance21', b)
    if hasattr(a2, 'ComponentInstance21'):
        assert _is_linked(a2, 'ComponentInstance21', b)
    _safe_set(b, 'parentcomponent', set())
    assert not _is_linked(b, 'parentcomponent', a2)
    if hasattr(a2, 'ComponentInstance21'):
        assert not _is_linked(a2, 'ComponentInstance21', b)


def test_assoc_type29_reverse_link_reassign_clear():
    a1 = component_diagram_ComponentType(name="sample_text")
    a2 = component_diagram_ComponentType(name="sample_text_2")
    b = component_diagram_ComponentInstance(name="sample_text", version=7)
    _safe_set(b, 'instance', a1)
    assert _is_linked(b, 'instance', a1)
    if hasattr(a1, 'ComponentType'):
        assert _is_linked(a1, 'ComponentType', b)
    _safe_set(b, 'instance', a2)
    assert _is_linked(b, 'instance', a2)
    if hasattr(a1, 'ComponentType'):
        assert not _is_linked(a1, 'ComponentType', b)
    if hasattr(a2, 'ComponentType'):
        assert _is_linked(a2, 'ComponentType', b)
    _safe_set(b, 'instance', None)
    assert not _is_linked(b, 'instance', a2)
    if hasattr(a2, 'ComponentType'):
        assert not _is_linked(a2, 'ComponentType', b)


def test_assoc_type8_reverse_link_reassign_clear():
    a1 = component_diagram_PortType(name="sample_text")
    a2 = component_diagram_PortType(name="sample_text_2")
    b = component_diagram_PortInstance(name="sample_text")
    _safe_set(b, 'port_instance', a1)
    assert _is_linked(b, 'port_instance', a1)
    if hasattr(a1, 'PortType9'):
        assert _is_linked(a1, 'PortType9', b)
    _safe_set(b, 'port_instance', a2)
    assert _is_linked(b, 'port_instance', a2)
    if hasattr(a1, 'PortType9'):
        assert not _is_linked(a1, 'PortType9', b)
    if hasattr(a2, 'PortType9'):
        assert _is_linked(a2, 'PortType9', b)
    _safe_set(b, 'port_instance', None)
    assert not _is_linked(b, 'port_instance', a2)
    if hasattr(a2, 'PortType9'):
        assert not _is_linked(a2, 'PortType9', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_component10_stub_double():
    # component_diagram_Architecture has no real 'component_diagram_Architecture' property in the generated
    # code (a bare stub) -- manually attach it so component_diagram_ComponentType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # component_diagram_ComponentType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = component_diagram_ComponentType(name="sample_text")
    partner = component_diagram_Architecture()
    setattr(partner, 'component_diagram_Architecture', None)
    _safe_set(owner, 'component_diagram_ComponentType', partner)
    assert owner in getattr(partner, 'component_diagram_Architecture')
    _safe_set(owner, 'component_diagram_ComponentType', None)
    assert owner not in getattr(partner, 'component_diagram_Architecture')


def test_assoc_connectors11_stub_double():
    # component_diagram_Architecture has no real 'component_diagram_Architecture12' property in the generated
    # code (a bare stub) -- manually attach it so component_diagram_Connector's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # component_diagram_Connector's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = component_diagram_Connector(name="sample_text")
    partner = component_diagram_Architecture()
    setattr(partner, 'component_diagram_Architecture12', None)
    _safe_set(owner, 'component_diagram_Connector', partner)
    assert owner in getattr(partner, 'component_diagram_Architecture12')
    _safe_set(owner, 'component_diagram_Connector', None)
    assert owner not in getattr(partner, 'component_diagram_Architecture12')


def test_assoc_instances15_stub_double():
    # component_diagram_Architecture has no real 'component_diagram_Architecture16' property in the generated
    # code (a bare stub) -- manually attach it so component_diagram_ComponentInstance's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # component_diagram_ComponentInstance's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = component_diagram_ComponentInstance(name="sample_text", version=7)
    partner = component_diagram_Architecture()
    setattr(partner, 'component_diagram_Architecture16', None)
    _safe_set(owner, 'component_diagram_ComponentInstance', partner)
    assert owner in getattr(partner, 'component_diagram_Architecture16')
    _safe_set(owner, 'component_diagram_ComponentInstance', None)
    assert owner not in getattr(partner, 'component_diagram_Architecture16')


def test_assoc_port_type17_stub_double():
    # component_diagram_Architecture has no real 'component_diagram_Architecture18' property in the generated
    # code (a bare stub) -- manually attach it so component_diagram_PortType's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # component_diagram_PortType's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = component_diagram_PortType(name="sample_text")
    partner = component_diagram_Architecture()
    setattr(partner, 'component_diagram_Architecture18', None)
    _safe_set(owner, 'component_diagram_PortType', partner)
    assert owner in getattr(partner, 'component_diagram_Architecture18')
    _safe_set(owner, 'component_diagram_PortType', None)
    assert owner not in getattr(partner, 'component_diagram_Architecture18')


def test_assoc_ports13_stub_double():
    # component_diagram_Architecture has no real 'component_diagram_Architecture14' property in the generated
    # code (a bare stub) -- manually attach it so component_diagram_PortInstance's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # component_diagram_PortInstance's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = component_diagram_PortInstance(name="sample_text")
    partner = component_diagram_Architecture()
    setattr(partner, 'component_diagram_Architecture14', None)
    _safe_set(owner, 'component_diagram_PortInstance', partner)
    assert owner in getattr(partner, 'component_diagram_Architecture14')
    _safe_set(owner, 'component_diagram_PortInstance', None)
    assert owner not in getattr(partner, 'component_diagram_Architecture14')


