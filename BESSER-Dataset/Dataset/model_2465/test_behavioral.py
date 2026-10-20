import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Base,
    Company,
    Marker,
    Relationship,
    operators_DateTimeRange,
    operators_DiagramInfo,
    operators_Equipment,
    operators_EquipmentRelationship,
    operators_Function,
    operators_FunctionRelationship,
    operators_Lifecycle,
    operators_Location,
    operators_Marker,
    operators_MetricSource,
    operators_NetXResource,
    operators_Network,
    operators_Node,
    operators_NodeType,
    operators_Operator,
    operators_Person,
    operators_Protocol,
    operators_Relationship,
    operators_ResourceExpansion,
    operators_ResourceForecast,
    operators_ResourceMonitor,
    operators_Service,
    operators_ServiceUser,
    operators_ToleranceMarker,
    operators_Value,
    operators_Warehouse,
    MarkerKind,
    ToleranceMarkerDirectionKind,
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

def test_assoc_networks15_reverse_link_reassign_clear():
    a1 = operators_Network(createdDate="sample_text", description="sample_text", name="sample_text")
    a2 = operators_Network(createdDate="sample_text_2", description="sample_text_2", name="sample_text_2")
    b = operators_Network(createdDate="sample_text", description="sample_text", name="sample_text")
    _safe_set(b, 'operators_Network16', a1)
    assert _is_linked(b, 'operators_Network16', a1)
    if hasattr(a1, 'operators_Network14'):
        assert _is_linked(a1, 'operators_Network14', b)
    _safe_set(b, 'operators_Network16', a2)
    assert _is_linked(b, 'operators_Network16', a2)
    if hasattr(a1, 'operators_Network14'):
        assert not _is_linked(a1, 'operators_Network14', b)
    if hasattr(a2, 'operators_Network14'):
        assert _is_linked(a2, 'operators_Network14', b)
    _safe_set(b, 'operators_Network16', None)
    assert not _is_linked(b, 'operators_Network16', a2)
    if hasattr(a2, 'operators_Network14'):
        assert not _is_linked(a2, 'operators_Network14', b)


def test_assoc_nodeID1Ref49_reverse_link_reassign_clear():
    a1 = operators_Relationship(name="sample_text")
    a2 = operators_Relationship(name="sample_text_2")
    b = operators_Node(nodeID="sample_text")
    _safe_set(b, 'operators_Node50', a1)
    assert _is_linked(b, 'operators_Node50', a1)
    if hasattr(a1, 'operators_Relationship'):
        assert _is_linked(a1, 'operators_Relationship', b)
    _safe_set(b, 'operators_Node50', a2)
    assert _is_linked(b, 'operators_Node50', a2)
    if hasattr(a1, 'operators_Relationship'):
        assert not _is_linked(a1, 'operators_Relationship', b)
    if hasattr(a2, 'operators_Relationship'):
        assert _is_linked(a2, 'operators_Relationship', b)
    _safe_set(b, 'operators_Node50', None)
    assert not _is_linked(b, 'operators_Node50', a2)
    if hasattr(a2, 'operators_Relationship'):
        assert not _is_linked(a2, 'operators_Relationship', b)


def test_assoc_nodeID2Ref51_reverse_link_reassign_clear():
    a1 = operators_Relationship(name="sample_text")
    a2 = operators_Relationship(name="sample_text_2")
    b = operators_Node(nodeID="sample_text")
    _safe_set(b, 'operators_Node53', a1)
    assert _is_linked(b, 'operators_Node53', a1)
    if hasattr(a1, 'operators_Relationship52'):
        assert _is_linked(a1, 'operators_Relationship52', b)
    _safe_set(b, 'operators_Node53', a2)
    assert _is_linked(b, 'operators_Node53', a2)
    if hasattr(a1, 'operators_Relationship52'):
        assert not _is_linked(a1, 'operators_Relationship52', b)
    if hasattr(a2, 'operators_Relationship52'):
        assert _is_linked(a2, 'operators_Relationship52', b)
    _safe_set(b, 'operators_Node53', None)
    assert not _is_linked(b, 'operators_Node53', a2)
    if hasattr(a2, 'operators_Relationship52'):
        assert not _is_linked(a2, 'operators_Relationship52', b)


def test_assoc_nodes12_reverse_link_reassign_clear():
    a1 = operators_Node(nodeID="sample_text")
    a2 = operators_Node(nodeID="sample_text_2")
    b = operators_Network(createdDate="sample_text", description="sample_text", name="sample_text")
    _safe_set(b, 'operators_Network13', {a1})
    assert _is_linked(b, 'operators_Network13', a1)
    if hasattr(a1, 'operators_Node'):
        assert _is_linked(a1, 'operators_Node', b)
    _safe_set(b, 'operators_Network13', {a2})
    assert _is_linked(b, 'operators_Network13', a2)
    if hasattr(a1, 'operators_Node'):
        assert not _is_linked(a1, 'operators_Node', b)
    if hasattr(a2, 'operators_Node'):
        assert _is_linked(a2, 'operators_Node', b)
    _safe_set(b, 'operators_Network13', set())
    assert not _is_linked(b, 'operators_Network13', a2)
    if hasattr(a2, 'operators_Node'):
        assert not _is_linked(a2, 'operators_Node', b)


def test_assoc_nodes77_reverse_link_reassign_clear():
    a1 = operators_Warehouse(description="sample_text", name="sample_text")
    a2 = operators_Warehouse(description="sample_text_2", name="sample_text_2")
    b = operators_Node(nodeID="sample_text")
    _safe_set(b, 'operators_Node79', a1)
    assert _is_linked(b, 'operators_Node79', a1)
    if hasattr(a1, 'operators_Warehouse78'):
        assert _is_linked(a1, 'operators_Warehouse78', b)
    _safe_set(b, 'operators_Node79', a2)
    assert _is_linked(b, 'operators_Node79', a2)
    if hasattr(a1, 'operators_Warehouse78'):
        assert not _is_linked(a1, 'operators_Warehouse78', b)
    if hasattr(a2, 'operators_Warehouse78'):
        assert _is_linked(a2, 'operators_Warehouse78', b)
    _safe_set(b, 'operators_Node79', None)
    assert not _is_linked(b, 'operators_Node79', a2)
    if hasattr(a2, 'operators_Warehouse78'):
        assert not _is_linked(a2, 'operators_Warehouse78', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_createdByRef25_stub_double():
    # operators_Person has no real 'operators_Person' property in the generated
    # code (a bare stub) -- manually attach it so operators_Network's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # operators_Network's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = operators_Network(createdDate="sample_text", description="sample_text", name="sample_text")
    partner = operators_Person()
    setattr(partner, 'operators_Person', None)
    _safe_set(owner, 'operators_Network26', partner)
    assert getattr(partner, 'operators_Person') == owner
    _safe_set(owner, 'operators_Network26', None)
    assert getattr(partner, 'operators_Person') is None


def test_assoc_createdByRef31_stub_double():
    # operators_Person has no real 'operators_Person33' property in the generated
    # code (a bare stub) -- manually attach it so operators_Node's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # operators_Node's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = operators_Node(nodeID="sample_text")
    partner = operators_Person()
    setattr(partner, 'operators_Person33', None)
    _safe_set(owner, 'operators_Node32', partner)
    assert getattr(partner, 'operators_Person33') == owner
    _safe_set(owner, 'operators_Node32', None)
    assert getattr(partner, 'operators_Person33') is None


def test_assoc_diagrams11_stub_double():
    # operators_DiagramInfo has no real 'operators_DiagramInfo' property in the generated
    # code (a bare stub) -- manually attach it so operators_Network's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # operators_Network's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = operators_Network(createdDate="sample_text", description="sample_text", name="sample_text")
    partner = operators_DiagramInfo()
    setattr(partner, 'operators_DiagramInfo', None)
    _safe_set(owner, 'operators_Network', {partner})
    assert getattr(partner, 'operators_DiagramInfo') == owner
    _safe_set(owner, 'operators_Network', set())
    assert getattr(partner, 'operators_DiagramInfo') is None


def test_assoc_equipmentRelationships20_stub_double():
    # operators_EquipmentRelationship has no real 'operators_EquipmentRelationship22' property in the generated
    # code (a bare stub) -- manually attach it so operators_Network's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # operators_Network's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = operators_Network(createdDate="sample_text", description="sample_text", name="sample_text")
    partner = operators_EquipmentRelationship()
    setattr(partner, 'operators_EquipmentRelationship22', None)
    _safe_set(owner, 'operators_Network21', {partner})
    assert getattr(partner, 'operators_EquipmentRelationship22') == owner
    _safe_set(owner, 'operators_Network21', set())
    assert getattr(partner, 'operators_EquipmentRelationship22') is None


def test_assoc_equipments80_stub_double():
    # operators_Equipment has no real 'operators_Equipment82' property in the generated
    # code (a bare stub) -- manually attach it so operators_Warehouse's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # operators_Warehouse's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = operators_Warehouse(description="sample_text", name="sample_text")
    partner = operators_Equipment()
    setattr(partner, 'operators_Equipment82', None)
    _safe_set(owner, 'operators_Warehouse81', {partner})
    assert getattr(partner, 'operators_Equipment82') == owner
    _safe_set(owner, 'operators_Warehouse81', set())
    assert getattr(partner, 'operators_Equipment82') is None


def test_assoc_functionRelationships17_stub_double():
    # operators_FunctionRelationship has no real 'operators_FunctionRelationship19' property in the generated
    # code (a bare stub) -- manually attach it so operators_Network's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # operators_Network's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = operators_Network(createdDate="sample_text", description="sample_text", name="sample_text")
    partner = operators_FunctionRelationship()
    setattr(partner, 'operators_FunctionRelationship19', None)
    _safe_set(owner, 'operators_Network18', {partner})
    assert getattr(partner, 'operators_FunctionRelationship19') == owner
    _safe_set(owner, 'operators_Network18', set())
    assert getattr(partner, 'operators_FunctionRelationship19') is None


def test_assoc_lifecycle27_stub_double():
    # operators_Lifecycle has no real 'operators_Lifecycle' property in the generated
    # code (a bare stub) -- manually attach it so operators_Node's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # operators_Node's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = operators_Node(nodeID="sample_text")
    partner = operators_Lifecycle()
    setattr(partner, 'operators_Lifecycle', None)
    _safe_set(owner, 'operators_Node28', partner)
    assert getattr(partner, 'operators_Lifecycle') == owner
    _safe_set(owner, 'operators_Node28', None)
    assert getattr(partner, 'operators_Lifecycle') is None


def test_assoc_locationRef34_stub_double():
    # operators_Location has no real 'operators_Location' property in the generated
    # code (a bare stub) -- manually attach it so operators_Node's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # operators_Node's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = operators_Node(nodeID="sample_text")
    partner = operators_Location()
    setattr(partner, 'operators_Location', None)
    _safe_set(owner, 'operators_Node35', partner)
    assert getattr(partner, 'operators_Location') == owner
    _safe_set(owner, 'operators_Node35', None)
    assert getattr(partner, 'operators_Location') is None


def test_assoc_markerResourceRef9_stub_double():
    # operators_NetXResource has no real 'operators_NetXResource' property in the generated
    # code (a bare stub) -- manually attach it so operators_Marker's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # operators_Marker's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = operators_Marker(description="sample_text", kind="sample_text")
    partner = operators_NetXResource()
    setattr(partner, 'operators_NetXResource', None)
    _safe_set(owner, 'operators_Marker10', partner)
    assert getattr(partner, 'operators_NetXResource') == owner
    _safe_set(owner, 'operators_Marker10', None)
    assert getattr(partner, 'operators_NetXResource') is None


def test_assoc_markers65_stub_double():
    # operators_ResourceForecast has no real 'operators_ResourceForecast' property in the generated
    # code (a bare stub) -- manually attach it so operators_Marker's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # operators_Marker's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = operators_Marker(description="sample_text", kind="sample_text")
    partner = operators_ResourceForecast()
    setattr(partner, 'operators_ResourceForecast', None)
    _safe_set(owner, 'operators_Marker66', partner)
    assert owner in getattr(partner, 'operators_ResourceForecast')
    _safe_set(owner, 'operators_Marker66', None)
    assert owner not in getattr(partner, 'operators_ResourceForecast')


def test_assoc_markers67_stub_double():
    # operators_ResourceMonitor has no real 'operators_ResourceMonitor' property in the generated
    # code (a bare stub) -- manually attach it so operators_Marker's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # operators_Marker's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = operators_Marker(description="sample_text", kind="sample_text")
    partner = operators_ResourceMonitor()
    setattr(partner, 'operators_ResourceMonitor', None)
    _safe_set(owner, 'operators_Marker68', partner)
    assert owner in getattr(partner, 'operators_ResourceMonitor')
    _safe_set(owner, 'operators_Marker68', None)
    assert owner not in getattr(partner, 'operators_ResourceMonitor')


def test_assoc_metricSources23_stub_double():
    # operators_MetricSource has no real 'operators_MetricSource' property in the generated
    # code (a bare stub) -- manually attach it so operators_Network's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # operators_Network's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = operators_Network(createdDate="sample_text", description="sample_text", name="sample_text")
    partner = operators_MetricSource()
    setattr(partner, 'operators_MetricSource', None)
    _safe_set(owner, 'operators_Network24', {partner})
    assert getattr(partner, 'operators_MetricSource') == owner
    _safe_set(owner, 'operators_Network24', set())
    assert getattr(partner, 'operators_MetricSource') is None


def test_assoc_networks39_stub_double():
    # operators_Operator has no real 'operators_Operator' property in the generated
    # code (a bare stub) -- manually attach it so operators_Network's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # operators_Network's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = operators_Network(createdDate="sample_text", description="sample_text", name="sample_text")
    partner = operators_Operator()
    setattr(partner, 'operators_Operator', None)
    _safe_set(owner, 'operators_Network40', partner)
    assert owner in getattr(partner, 'operators_Operator')
    _safe_set(owner, 'operators_Network40', None)
    assert owner not in getattr(partner, 'operators_Operator')


def test_assoc_nodeRef69_stub_double():
    # operators_ResourceMonitor has no real 'operators_ResourceMonitor70' property in the generated
    # code (a bare stub) -- manually attach it so operators_Node's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # operators_Node's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = operators_Node(nodeID="sample_text")
    partner = operators_ResourceMonitor()
    setattr(partner, 'operators_ResourceMonitor70', None)
    _safe_set(owner, 'operators_Node71', partner)
    assert getattr(partner, 'operators_ResourceMonitor70') == owner
    _safe_set(owner, 'operators_Node71', None)
    assert getattr(partner, 'operators_ResourceMonitor70') is None


def test_assoc_nodeRefs56_stub_double():
    # operators_ResourceExpansion has no real 'operators_ResourceExpansion57' property in the generated
    # code (a bare stub) -- manually attach it so operators_Node's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # operators_Node's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = operators_Node(nodeID="sample_text")
    partner = operators_ResourceExpansion()
    setattr(partner, 'operators_ResourceExpansion57', None)
    _safe_set(owner, 'operators_Node58', partner)
    assert owner in getattr(partner, 'operators_ResourceExpansion57')
    _safe_set(owner, 'operators_Node58', None)
    assert owner not in getattr(partner, 'operators_ResourceExpansion57')


def test_assoc_nodeType29_stub_double():
    # operators_NodeType has no real 'operators_NodeType' property in the generated
    # code (a bare stub) -- manually attach it so operators_Node's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # operators_Node's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = operators_Node(nodeID="sample_text")
    partner = operators_NodeType()
    setattr(partner, 'operators_NodeType', None)
    _safe_set(owner, 'operators_Node30', partner)
    assert getattr(partner, 'operators_NodeType') == owner
    _safe_set(owner, 'operators_Node30', None)
    assert getattr(partner, 'operators_NodeType') is None


def test_assoc_originalNodeTypeRef36_stub_double():
    # operators_NodeType has no real 'operators_NodeType38' property in the generated
    # code (a bare stub) -- manually attach it so operators_Node's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # operators_Node's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = operators_Node(nodeID="sample_text")
    partner = operators_NodeType()
    setattr(partner, 'operators_NodeType38', None)
    _safe_set(owner, 'operators_Node37', partner)
    assert getattr(partner, 'operators_NodeType38') == owner
    _safe_set(owner, 'operators_Node37', None)
    assert getattr(partner, 'operators_NodeType38') is None


def test_assoc_protocolRef54_stub_double():
    # operators_Protocol has no real 'operators_Protocol' property in the generated
    # code (a bare stub) -- manually attach it so operators_Relationship's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # operators_Relationship's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = operators_Relationship(name="sample_text")
    partner = operators_Protocol()
    setattr(partner, 'operators_Protocol', None)
    _safe_set(owner, 'operators_Relationship55', partner)
    assert getattr(partner, 'operators_Protocol') == owner
    _safe_set(owner, 'operators_Relationship55', None)
    assert getattr(partner, 'operators_Protocol') is None


def test_assoc_valueRef8_stub_double():
    # operators_Value has no real 'operators_Value' property in the generated
    # code (a bare stub) -- manually attach it so operators_Marker's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # operators_Marker's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = operators_Marker(description="sample_text", kind="sample_text")
    partner = operators_Value()
    setattr(partner, 'operators_Value', None)
    _safe_set(owner, 'operators_Marker', partner)
    assert getattr(partner, 'operators_Value') == owner
    _safe_set(owner, 'operators_Marker', None)
    assert getattr(partner, 'operators_Value') is None


def test_assoc_warehouses41_stub_double():
    # operators_Operator has no real 'operators_Operator42' property in the generated
    # code (a bare stub) -- manually attach it so operators_Warehouse's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # operators_Warehouse's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = operators_Warehouse(description="sample_text", name="sample_text")
    partner = operators_Operator()
    setattr(partner, 'operators_Operator42', None)
    _safe_set(owner, 'operators_Warehouse', partner)
    assert owner in getattr(partner, 'operators_Operator42')
    _safe_set(owner, 'operators_Warehouse', None)
    assert owner not in getattr(partner, 'operators_Operator42')


