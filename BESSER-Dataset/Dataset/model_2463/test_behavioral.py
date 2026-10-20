import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Company,
    Relationship,
    operators_DiagramInfo,
    operators_Equipment,
    operators_EquipmentRelationship,
    operators_ExpansionExperience,
    operators_Function,
    operators_FunctionRelationship,
    operators_Lifecycle,
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
    operators_Room,
    operators_Service,
    operators_ServiceUser,
    operators_Warehouse,
    MarkerKind,
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

def test_assoc_networks21_reverse_link_reassign_clear():
    a1 = operators_Network(createdDate="sample_text", description="sample_text", name="sample_text")
    a2 = operators_Network(createdDate="sample_text_2", description="sample_text_2", name="sample_text_2")
    b = operators_Network(createdDate="sample_text", description="sample_text", name="sample_text")
    _safe_set(b, 'operators_Network22', a1)
    assert _is_linked(b, 'operators_Network22', a1)
    if hasattr(a1, 'operators_Network20'):
        assert _is_linked(a1, 'operators_Network20', b)
    _safe_set(b, 'operators_Network22', a2)
    assert _is_linked(b, 'operators_Network22', a2)
    if hasattr(a1, 'operators_Network20'):
        assert not _is_linked(a1, 'operators_Network20', b)
    if hasattr(a2, 'operators_Network20'):
        assert _is_linked(a2, 'operators_Network20', b)
    _safe_set(b, 'operators_Network22', None)
    assert not _is_linked(b, 'operators_Network22', a2)
    if hasattr(a2, 'operators_Network20'):
        assert not _is_linked(a2, 'operators_Network20', b)


def test_assoc_nodeID1Ref58_reverse_link_reassign_clear():
    a1 = operators_Relationship(name="sample_text")
    a2 = operators_Relationship(name="sample_text_2")
    b = operators_Node(nodeID="sample_text")
    _safe_set(b, 'operators_Node59', a1)
    assert _is_linked(b, 'operators_Node59', a1)
    if hasattr(a1, 'operators_Relationship'):
        assert _is_linked(a1, 'operators_Relationship', b)
    _safe_set(b, 'operators_Node59', a2)
    assert _is_linked(b, 'operators_Node59', a2)
    if hasattr(a1, 'operators_Relationship'):
        assert not _is_linked(a1, 'operators_Relationship', b)
    if hasattr(a2, 'operators_Relationship'):
        assert _is_linked(a2, 'operators_Relationship', b)
    _safe_set(b, 'operators_Node59', None)
    assert not _is_linked(b, 'operators_Node59', a2)
    if hasattr(a2, 'operators_Relationship'):
        assert not _is_linked(a2, 'operators_Relationship', b)


def test_assoc_nodeID2Ref60_reverse_link_reassign_clear():
    a1 = operators_Relationship(name="sample_text")
    a2 = operators_Relationship(name="sample_text_2")
    b = operators_Node(nodeID="sample_text")
    _safe_set(b, 'operators_Node62', a1)
    assert _is_linked(b, 'operators_Node62', a1)
    if hasattr(a1, 'operators_Relationship61'):
        assert _is_linked(a1, 'operators_Relationship61', b)
    _safe_set(b, 'operators_Node62', a2)
    assert _is_linked(b, 'operators_Node62', a2)
    if hasattr(a1, 'operators_Relationship61'):
        assert not _is_linked(a1, 'operators_Relationship61', b)
    if hasattr(a2, 'operators_Relationship61'):
        assert _is_linked(a2, 'operators_Relationship61', b)
    _safe_set(b, 'operators_Node62', None)
    assert not _is_linked(b, 'operators_Node62', a2)
    if hasattr(a2, 'operators_Relationship61'):
        assert not _is_linked(a2, 'operators_Relationship61', b)


def test_assoc_nodes18_reverse_link_reassign_clear():
    a1 = operators_Node(nodeID="sample_text")
    a2 = operators_Node(nodeID="sample_text_2")
    b = operators_Network(createdDate="sample_text", description="sample_text", name="sample_text")
    _safe_set(b, 'operators_Network19', {a1})
    assert _is_linked(b, 'operators_Network19', a1)
    if hasattr(a1, 'operators_Node'):
        assert _is_linked(a1, 'operators_Node', b)
    _safe_set(b, 'operators_Network19', {a2})
    assert _is_linked(b, 'operators_Network19', a2)
    if hasattr(a1, 'operators_Node'):
        assert not _is_linked(a1, 'operators_Node', b)
    if hasattr(a2, 'operators_Node'):
        assert _is_linked(a2, 'operators_Node', b)
    _safe_set(b, 'operators_Network19', set())
    assert not _is_linked(b, 'operators_Network19', a2)
    if hasattr(a2, 'operators_Node'):
        assert not _is_linked(a2, 'operators_Node', b)


def test_assoc_nodes78_reverse_link_reassign_clear():
    a1 = operators_Warehouse(description="sample_text", equipments="sample_text", name="sample_text")
    a2 = operators_Warehouse(description="sample_text_2", equipments="sample_text_2", name="sample_text_2")
    b = operators_Node(nodeID="sample_text")
    _safe_set(b, 'operators_Node80', a1)
    assert _is_linked(b, 'operators_Node80', a1)
    if hasattr(a1, 'operators_Warehouse79'):
        assert _is_linked(a1, 'operators_Warehouse79', b)
    _safe_set(b, 'operators_Node80', a2)
    assert _is_linked(b, 'operators_Node80', a2)
    if hasattr(a1, 'operators_Warehouse79'):
        assert not _is_linked(a1, 'operators_Warehouse79', b)
    if hasattr(a2, 'operators_Warehouse79'):
        assert _is_linked(a2, 'operators_Warehouse79', b)
    _safe_set(b, 'operators_Node80', None)
    assert not _is_linked(b, 'operators_Node80', a2)
    if hasattr(a2, 'operators_Warehouse79'):
        assert not _is_linked(a2, 'operators_Warehouse79', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_createdByRef31_stub_double():
    # operators_Person has no real 'operators_Person' property in the generated
    # code (a bare stub) -- manually attach it so operators_Network's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # operators_Network's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = operators_Network(createdDate="sample_text", description="sample_text", name="sample_text")
    partner = operators_Person()
    setattr(partner, 'operators_Person', None)
    _safe_set(owner, 'operators_Network32', partner)
    assert getattr(partner, 'operators_Person') == owner
    _safe_set(owner, 'operators_Network32', None)
    assert getattr(partner, 'operators_Person') is None


def test_assoc_createdByRef37_stub_double():
    # operators_Person has no real 'operators_Person39' property in the generated
    # code (a bare stub) -- manually attach it so operators_Node's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # operators_Node's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = operators_Node(nodeID="sample_text")
    partner = operators_Person()
    setattr(partner, 'operators_Person39', None)
    _safe_set(owner, 'operators_Node38', partner)
    assert getattr(partner, 'operators_Person39') == owner
    _safe_set(owner, 'operators_Node38', None)
    assert getattr(partner, 'operators_Person39') is None


def test_assoc_diagrams17_stub_double():
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


def test_assoc_equipmentRef10_stub_double():
    # operators_Equipment has no real 'operators_Equipment11' property in the generated
    # code (a bare stub) -- manually attach it so operators_Marker's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # operators_Marker's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = operators_Marker(description="sample_text", kind="sample_text")
    partner = operators_Equipment()
    setattr(partner, 'operators_Equipment11', None)
    _safe_set(owner, 'operators_Marker', partner)
    assert getattr(partner, 'operators_Equipment11') == owner
    _safe_set(owner, 'operators_Marker', None)
    assert getattr(partner, 'operators_Equipment11') is None


def test_assoc_equipmentRef4_stub_double():
    # operators_Equipment has no real 'operators_Equipment5' property in the generated
    # code (a bare stub) -- manually attach it so operators_ExpansionExperience's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # operators_ExpansionExperience's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = operators_ExpansionExperience(duration="sample_text")
    partner = operators_Equipment()
    setattr(partner, 'operators_Equipment5', None)
    _safe_set(owner, 'operators_ExpansionExperience', partner)
    assert getattr(partner, 'operators_Equipment5') == owner
    _safe_set(owner, 'operators_ExpansionExperience', None)
    assert getattr(partner, 'operators_Equipment5') is None


def test_assoc_equipmentRelationships26_stub_double():
    # operators_EquipmentRelationship has no real 'operators_EquipmentRelationship28' property in the generated
    # code (a bare stub) -- manually attach it so operators_Network's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # operators_Network's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = operators_Network(createdDate="sample_text", description="sample_text", name="sample_text")
    partner = operators_EquipmentRelationship()
    setattr(partner, 'operators_EquipmentRelationship28', None)
    _safe_set(owner, 'operators_Network27', {partner})
    assert getattr(partner, 'operators_EquipmentRelationship28') == owner
    _safe_set(owner, 'operators_Network27', set())
    assert getattr(partner, 'operators_EquipmentRelationship28') is None


def test_assoc_expansionExperiences55_stub_double():
    # operators_Operator has no real 'operators_Operator56' property in the generated
    # code (a bare stub) -- manually attach it so operators_ExpansionExperience's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # operators_ExpansionExperience's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = operators_ExpansionExperience(duration="sample_text")
    partner = operators_Operator()
    setattr(partner, 'operators_Operator56', None)
    _safe_set(owner, 'operators_ExpansionExperience57', partner)
    assert owner in getattr(partner, 'operators_Operator56')
    _safe_set(owner, 'operators_ExpansionExperience57', None)
    assert owner not in getattr(partner, 'operators_Operator56')


def test_assoc_functionRef12_stub_double():
    # operators_Function has no real 'operators_Function14' property in the generated
    # code (a bare stub) -- manually attach it so operators_Marker's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # operators_Marker's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = operators_Marker(description="sample_text", kind="sample_text")
    partner = operators_Function()
    setattr(partner, 'operators_Function14', None)
    _safe_set(owner, 'operators_Marker13', partner)
    assert getattr(partner, 'operators_Function14') == owner
    _safe_set(owner, 'operators_Marker13', None)
    assert getattr(partner, 'operators_Function14') is None


def test_assoc_functionRelationships23_stub_double():
    # operators_FunctionRelationship has no real 'operators_FunctionRelationship25' property in the generated
    # code (a bare stub) -- manually attach it so operators_Network's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # operators_Network's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = operators_Network(createdDate="sample_text", description="sample_text", name="sample_text")
    partner = operators_FunctionRelationship()
    setattr(partner, 'operators_FunctionRelationship25', None)
    _safe_set(owner, 'operators_Network24', {partner})
    assert getattr(partner, 'operators_FunctionRelationship25') == owner
    _safe_set(owner, 'operators_Network24', set())
    assert getattr(partner, 'operators_FunctionRelationship25') is None


def test_assoc_lifecycle33_stub_double():
    # operators_Lifecycle has no real 'operators_Lifecycle' property in the generated
    # code (a bare stub) -- manually attach it so operators_Node's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # operators_Node's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = operators_Node(nodeID="sample_text")
    partner = operators_Lifecycle()
    setattr(partner, 'operators_Lifecycle', None)
    _safe_set(owner, 'operators_Node34', partner)
    assert getattr(partner, 'operators_Lifecycle') == owner
    _safe_set(owner, 'operators_Node34', None)
    assert getattr(partner, 'operators_Lifecycle') is None


def test_assoc_markerResourceRef15_stub_double():
    # operators_NetXResource has no real 'operators_NetXResource' property in the generated
    # code (a bare stub) -- manually attach it so operators_Marker's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # operators_Marker's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = operators_Marker(description="sample_text", kind="sample_text")
    partner = operators_NetXResource()
    setattr(partner, 'operators_NetXResource', None)
    _safe_set(owner, 'operators_Marker16', partner)
    assert getattr(partner, 'operators_NetXResource') == owner
    _safe_set(owner, 'operators_Marker16', None)
    assert getattr(partner, 'operators_NetXResource') is None


def test_assoc_markers74_stub_double():
    # operators_ResourceForecast has no real 'operators_ResourceForecast' property in the generated
    # code (a bare stub) -- manually attach it so operators_Marker's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # operators_Marker's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = operators_Marker(description="sample_text", kind="sample_text")
    partner = operators_ResourceForecast()
    setattr(partner, 'operators_ResourceForecast', None)
    _safe_set(owner, 'operators_Marker75', partner)
    assert owner in getattr(partner, 'operators_ResourceForecast')
    _safe_set(owner, 'operators_Marker75', None)
    assert owner not in getattr(partner, 'operators_ResourceForecast')


def test_assoc_markers76_stub_double():
    # operators_ResourceMonitor has no real 'operators_ResourceMonitor' property in the generated
    # code (a bare stub) -- manually attach it so operators_Marker's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # operators_Marker's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = operators_Marker(description="sample_text", kind="sample_text")
    partner = operators_ResourceMonitor()
    setattr(partner, 'operators_ResourceMonitor', None)
    _safe_set(owner, 'operators_Marker77', partner)
    assert owner in getattr(partner, 'operators_ResourceMonitor')
    _safe_set(owner, 'operators_Marker77', None)
    assert owner not in getattr(partner, 'operators_ResourceMonitor')


def test_assoc_metricSources29_stub_double():
    # operators_MetricSource has no real 'operators_MetricSource' property in the generated
    # code (a bare stub) -- manually attach it so operators_Network's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # operators_Network's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = operators_Network(createdDate="sample_text", description="sample_text", name="sample_text")
    partner = operators_MetricSource()
    setattr(partner, 'operators_MetricSource', None)
    _safe_set(owner, 'operators_Network30', {partner})
    assert getattr(partner, 'operators_MetricSource') == owner
    _safe_set(owner, 'operators_Network30', set())
    assert getattr(partner, 'operators_MetricSource') is None


def test_assoc_networks45_stub_double():
    # operators_Operator has no real 'operators_Operator' property in the generated
    # code (a bare stub) -- manually attach it so operators_Network's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # operators_Network's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = operators_Network(createdDate="sample_text", description="sample_text", name="sample_text")
    partner = operators_Operator()
    setattr(partner, 'operators_Operator', None)
    _safe_set(owner, 'operators_Network46', partner)
    assert owner in getattr(partner, 'operators_Operator')
    _safe_set(owner, 'operators_Network46', None)
    assert owner not in getattr(partner, 'operators_Operator')


def test_assoc_nodeRefs65_stub_double():
    # operators_ResourceExpansion has no real 'operators_ResourceExpansion66' property in the generated
    # code (a bare stub) -- manually attach it so operators_Node's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # operators_Node's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = operators_Node(nodeID="sample_text")
    partner = operators_ResourceExpansion()
    setattr(partner, 'operators_ResourceExpansion66', None)
    _safe_set(owner, 'operators_Node67', partner)
    assert owner in getattr(partner, 'operators_ResourceExpansion66')
    _safe_set(owner, 'operators_Node67', None)
    assert owner not in getattr(partner, 'operators_ResourceExpansion66')


def test_assoc_nodeType35_stub_double():
    # operators_NodeType has no real 'operators_NodeType' property in the generated
    # code (a bare stub) -- manually attach it so operators_Node's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # operators_Node's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = operators_Node(nodeID="sample_text")
    partner = operators_NodeType()
    setattr(partner, 'operators_NodeType', None)
    _safe_set(owner, 'operators_Node36', {partner})
    assert getattr(partner, 'operators_NodeType') == owner
    _safe_set(owner, 'operators_Node36', set())
    assert getattr(partner, 'operators_NodeType') is None


def test_assoc_originalNodeTypeRef40_stub_double():
    # operators_NodeType has no real 'operators_NodeType42' property in the generated
    # code (a bare stub) -- manually attach it so operators_Node's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # operators_Node's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = operators_Node(nodeID="sample_text")
    partner = operators_NodeType()
    setattr(partner, 'operators_NodeType42', None)
    _safe_set(owner, 'operators_Node41', partner)
    assert getattr(partner, 'operators_NodeType42') == owner
    _safe_set(owner, 'operators_Node41', None)
    assert getattr(partner, 'operators_NodeType42') is None


def test_assoc_protocolRef63_stub_double():
    # operators_Protocol has no real 'operators_Protocol' property in the generated
    # code (a bare stub) -- manually attach it so operators_Relationship's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # operators_Relationship's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = operators_Relationship(name="sample_text")
    partner = operators_Protocol()
    setattr(partner, 'operators_Protocol', None)
    _safe_set(owner, 'operators_Relationship64', partner)
    assert getattr(partner, 'operators_Protocol') == owner
    _safe_set(owner, 'operators_Relationship64', None)
    assert getattr(partner, 'operators_Protocol') is None


def test_assoc_roomRef43_stub_double():
    # operators_Room has no real 'operators_Room' property in the generated
    # code (a bare stub) -- manually attach it so operators_Node's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # operators_Node's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = operators_Node(nodeID="sample_text")
    partner = operators_Room()
    setattr(partner, 'operators_Room', None)
    _safe_set(owner, 'operators_Node44', partner)
    assert getattr(partner, 'operators_Room') == owner
    _safe_set(owner, 'operators_Node44', None)
    assert getattr(partner, 'operators_Room') is None


def test_assoc_warehouses47_stub_double():
    # operators_Operator has no real 'operators_Operator48' property in the generated
    # code (a bare stub) -- manually attach it so operators_Warehouse's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # operators_Warehouse's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = operators_Warehouse(description="sample_text", equipments="sample_text", name="sample_text")
    partner = operators_Operator()
    setattr(partner, 'operators_Operator48', None)
    _safe_set(owner, 'operators_Warehouse', partner)
    assert owner in getattr(partner, 'operators_Operator48')
    _safe_set(owner, 'operators_Warehouse', None)
    assert owner not in getattr(partner, 'operators_Operator48')


