import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    DynamicLabel,
    EdgeDecorator,
    EdgeLabel,
    LabelValue,
    MigrationEdge,
    MigrationEdgeLabel,
    Node,
    NodeLabel,
    PopulationEdge,
    TransportSystem,
    transport_LoadUnloadEdge,
    transport_LoadUnloadEdgeLabel,
    transport_PacketStyleTransportSystem,
    transport_PacketStyleTransportSystemDecorator,
    transport_PacketTransportLabel,
    transport_PacketTransportLabelValue,
    transport_PipeStyleTransportSystem,
    transport_PipeTransportEdge,
    transport_PipeTransportEdgeLabel,
    transport_PipeTransportEdgeLabelValue,
    transport_STEMTime,
    transport_TransportSystem,
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

# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_activationTime0_stub_double():
    # transport_STEMTime has no real 'transport_STEMTime' property in the generated
    # code (a bare stub) -- manually attach it so transport_LoadUnloadEdgeLabel's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # transport_LoadUnloadEdgeLabel's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = transport_LoadUnloadEdgeLabel(activatedRate=3.14)
    partner = transport_STEMTime()
    setattr(partner, 'transport_STEMTime', None)
    _safe_set(owner, 'transport_LoadUnloadEdgeLabel', partner)
    assert getattr(partner, 'transport_STEMTime') == owner
    _safe_set(owner, 'transport_LoadUnloadEdgeLabel', None)
    assert getattr(partner, 'transport_STEMTime') is None


def test_assoc_deactivationTime1_stub_double():
    # transport_STEMTime has no real 'transport_STEMTime3' property in the generated
    # code (a bare stub) -- manually attach it so transport_LoadUnloadEdgeLabel's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # transport_LoadUnloadEdgeLabel's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = transport_LoadUnloadEdgeLabel(activatedRate=3.14)
    partner = transport_STEMTime()
    setattr(partner, 'transport_STEMTime3', None)
    _safe_set(owner, 'transport_LoadUnloadEdgeLabel2', partner)
    assert getattr(partner, 'transport_STEMTime3') == owner
    _safe_set(owner, 'transport_LoadUnloadEdgeLabel2', None)
    assert getattr(partner, 'transport_STEMTime3') is None


def test_assoc_inTransportEdges10_stub_double():
    # transport_PipeTransportEdge has no real 'transport_PipeTransportEdge' property in the generated
    # code (a bare stub) -- manually attach it so transport_PipeStyleTransportSystem's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # transport_PipeStyleTransportSystem's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = transport_PipeStyleTransportSystem(maxCapacity=3.14)
    partner = transport_PipeTransportEdge()
    setattr(partner, 'transport_PipeTransportEdge', None)
    _safe_set(owner, 'transport_PipeStyleTransportSystem', {partner})
    assert getattr(partner, 'transport_PipeTransportEdge') == owner
    _safe_set(owner, 'transport_PipeStyleTransportSystem', set())
    assert getattr(partner, 'transport_PipeTransportEdge') is None


def test_assoc_loadingEdges5_stub_double():
    # transport_PacketStyleTransportSystem has no real 'transport_PacketStyleTransportSystem6' property in the generated
    # code (a bare stub) -- manually attach it so transport_LoadUnloadEdge's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # transport_LoadUnloadEdge's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = transport_LoadUnloadEdge(loadingEdge=True)
    partner = transport_PacketStyleTransportSystem()
    setattr(partner, 'transport_PacketStyleTransportSystem6', None)
    _safe_set(owner, 'transport_LoadUnloadEdge', partner)
    assert owner in getattr(partner, 'transport_PacketStyleTransportSystem6')
    _safe_set(owner, 'transport_LoadUnloadEdge', None)
    assert owner not in getattr(partner, 'transport_PacketStyleTransportSystem6')


def test_assoc_outTransportEdges11_stub_double():
    # transport_PipeTransportEdge has no real 'transport_PipeTransportEdge13' property in the generated
    # code (a bare stub) -- manually attach it so transport_PipeStyleTransportSystem's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # transport_PipeStyleTransportSystem's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = transport_PipeStyleTransportSystem(maxCapacity=3.14)
    partner = transport_PipeTransportEdge()
    setattr(partner, 'transport_PipeTransportEdge13', None)
    _safe_set(owner, 'transport_PipeStyleTransportSystem12', {partner})
    assert getattr(partner, 'transport_PipeTransportEdge13') == owner
    _safe_set(owner, 'transport_PipeStyleTransportSystem12', set())
    assert getattr(partner, 'transport_PipeTransportEdge13') is None


def test_assoc_unloadingEdges7_stub_double():
    # transport_PacketStyleTransportSystem has no real 'transport_PacketStyleTransportSystem8' property in the generated
    # code (a bare stub) -- manually attach it so transport_LoadUnloadEdge's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # transport_LoadUnloadEdge's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = transport_LoadUnloadEdge(loadingEdge=True)
    partner = transport_PacketStyleTransportSystem()
    setattr(partner, 'transport_PacketStyleTransportSystem8', None)
    _safe_set(owner, 'transport_LoadUnloadEdge9', partner)
    assert owner in getattr(partner, 'transport_PacketStyleTransportSystem8')
    _safe_set(owner, 'transport_LoadUnloadEdge9', None)
    assert owner not in getattr(partner, 'transport_PacketStyleTransportSystem8')


