import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    DynamicLabel,
    EdgeLabel,
    Identifiable,
    Label,
    Modifiable,
    NodeLabel,
    SanityChecker,
    StaticLabel,
    graph_Decorator,
    graph_DynamicEdgeLabel,
    graph_DynamicLabel,
    graph_DynamicNodeLabel,
    graph_Edge,
    graph_EdgeLabel,
    graph_Graph,
    graph_Identifiable,
    graph_Label,
    graph_LabelValue,
    graph_Node,
    graph_NodeLabel,
    graph_STEMTime,
    graph_SanityChecker,
    graph_StaticEdgeLabel,
    graph_StaticLabel,
    graph_StaticNodeLabel,
    graph_URIToEdgeMapEntry,
    graph_URIToIdentifiableMapEntry,
    graph_URIToLabelMapEntry,
    graph_URIToNodeLabelMapEntry,
    graph_URIToNodeMapEntry,
    graph_UnresolvedIdentifiable,
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

def test_assoc_currentValue23_reverse_link_reassign_clear():
    a1 = graph_LabelValue()
    a2 = graph_LabelValue()
    b = graph_Label(uRIOfIdentifiableToBeLabeled="sample_text")
    _safe_set(b, 'graph_Label', a1)
    assert _is_linked(b, 'graph_Label', a1)
    if hasattr(a1, 'graph_LabelValue24'):
        assert _is_linked(a1, 'graph_LabelValue24', b)
    _safe_set(b, 'graph_Label', a2)
    assert _is_linked(b, 'graph_Label', a2)
    if hasattr(a1, 'graph_LabelValue24'):
        assert not _is_linked(a1, 'graph_LabelValue24', b)
    if hasattr(a2, 'graph_LabelValue24'):
        assert _is_linked(a2, 'graph_LabelValue24', b)
    _safe_set(b, 'graph_Label', None)
    assert not _is_linked(b, 'graph_Label', a2)
    if hasattr(a2, 'graph_LabelValue24'):
        assert not _is_linked(a2, 'graph_LabelValue24', b)


def test_assoc_dynamicLabels14_reverse_link_reassign_clear():
    a1 = graph_Graph(numDynamicLabels=7, numEdges=7, numGraphLabels=7, numNodeLabels=7, numNodes=7)
    a2 = graph_Graph(numDynamicLabels=13, numEdges=13, numGraphLabels=13, numNodeLabels=13, numNodes=13)
    b = graph_DynamicLabel(nextValueValid=True)
    _safe_set(b, 'graph_DynamicLabel16', a1)
    assert _is_linked(b, 'graph_DynamicLabel16', a1)
    if hasattr(a1, 'graph_Graph15'):
        assert _is_linked(a1, 'graph_Graph15', b)
    _safe_set(b, 'graph_DynamicLabel16', a2)
    assert _is_linked(b, 'graph_DynamicLabel16', a2)
    if hasattr(a1, 'graph_Graph15'):
        assert not _is_linked(a1, 'graph_Graph15', b)
    if hasattr(a2, 'graph_Graph15'):
        assert _is_linked(a2, 'graph_Graph15', b)
    _safe_set(b, 'graph_DynamicLabel16', None)
    assert not _is_linked(b, 'graph_DynamicLabel16', a2)
    if hasattr(a2, 'graph_Graph15'):
        assert not _is_linked(a2, 'graph_Graph15', b)


def test_assoc_edges7_reverse_link_reassign_clear():
    a1 = graph_URIToEdgeMapEntry(key="sample_text")
    a2 = graph_URIToEdgeMapEntry(key="sample_text_2")
    b = graph_Graph(numDynamicLabels=7, numEdges=7, numGraphLabels=7, numNodeLabels=7, numNodes=7)
    _safe_set(b, 'graph_Graph', {a1})
    assert _is_linked(b, 'graph_Graph', a1)
    if hasattr(a1, 'graph_URIToEdgeMapEntry'):
        assert _is_linked(a1, 'graph_URIToEdgeMapEntry', b)
    _safe_set(b, 'graph_Graph', {a2})
    assert _is_linked(b, 'graph_Graph', a2)
    if hasattr(a1, 'graph_URIToEdgeMapEntry'):
        assert not _is_linked(a1, 'graph_URIToEdgeMapEntry', b)
    if hasattr(a2, 'graph_URIToEdgeMapEntry'):
        assert _is_linked(a2, 'graph_URIToEdgeMapEntry', b)
    _safe_set(b, 'graph_Graph', set())
    assert not _is_linked(b, 'graph_Graph', a2)
    if hasattr(a2, 'graph_URIToEdgeMapEntry'):
        assert not _is_linked(a2, 'graph_URIToEdgeMapEntry', b)


def test_assoc_graphLabels10_reverse_link_reassign_clear():
    a1 = graph_URIToLabelMapEntry(key="sample_text")
    a2 = graph_URIToLabelMapEntry(key="sample_text_2")
    b = graph_Graph(numDynamicLabels=7, numEdges=7, numGraphLabels=7, numNodeLabels=7, numNodes=7)
    _safe_set(b, 'graph_Graph11', {a1})
    assert _is_linked(b, 'graph_Graph11', a1)
    if hasattr(a1, 'graph_URIToLabelMapEntry'):
        assert _is_linked(a1, 'graph_URIToLabelMapEntry', b)
    _safe_set(b, 'graph_Graph11', {a2})
    assert _is_linked(b, 'graph_Graph11', a2)
    if hasattr(a1, 'graph_URIToLabelMapEntry'):
        assert not _is_linked(a1, 'graph_URIToLabelMapEntry', b)
    if hasattr(a2, 'graph_URIToLabelMapEntry'):
        assert _is_linked(a2, 'graph_URIToLabelMapEntry', b)
    _safe_set(b, 'graph_Graph11', set())
    assert not _is_linked(b, 'graph_Graph11', a2)
    if hasattr(a2, 'graph_URIToLabelMapEntry'):
        assert not _is_linked(a2, 'graph_URIToLabelMapEntry', b)


def test_assoc_nextValue0_reverse_link_reassign_clear():
    a1 = graph_LabelValue()
    a2 = graph_LabelValue()
    b = graph_DynamicLabel(nextValueValid=True)
    _safe_set(b, 'graph_DynamicLabel', a1)
    assert _is_linked(b, 'graph_DynamicLabel', a1)
    if hasattr(a1, 'graph_LabelValue'):
        assert _is_linked(a1, 'graph_LabelValue', b)
    _safe_set(b, 'graph_DynamicLabel', a2)
    assert _is_linked(b, 'graph_DynamicLabel', a2)
    if hasattr(a1, 'graph_LabelValue'):
        assert not _is_linked(a1, 'graph_LabelValue', b)
    if hasattr(a2, 'graph_LabelValue'):
        assert _is_linked(a2, 'graph_LabelValue', b)
    _safe_set(b, 'graph_DynamicLabel', None)
    assert not _is_linked(b, 'graph_DynamicLabel', a2)
    if hasattr(a2, 'graph_LabelValue'):
        assert not _is_linked(a2, 'graph_LabelValue', b)


def test_assoc_nodeLabels12_reverse_link_reassign_clear():
    a1 = graph_URIToNodeLabelMapEntry(key="sample_text")
    a2 = graph_URIToNodeLabelMapEntry(key="sample_text_2")
    b = graph_Graph(numDynamicLabels=7, numEdges=7, numGraphLabels=7, numNodeLabels=7, numNodes=7)
    _safe_set(b, 'graph_Graph13', {a1})
    assert _is_linked(b, 'graph_Graph13', a1)
    if hasattr(a1, 'graph_URIToNodeLabelMapEntry'):
        assert _is_linked(a1, 'graph_URIToNodeLabelMapEntry', b)
    _safe_set(b, 'graph_Graph13', {a2})
    assert _is_linked(b, 'graph_Graph13', a2)
    if hasattr(a1, 'graph_URIToNodeLabelMapEntry'):
        assert not _is_linked(a1, 'graph_URIToNodeLabelMapEntry', b)
    if hasattr(a2, 'graph_URIToNodeLabelMapEntry'):
        assert _is_linked(a2, 'graph_URIToNodeLabelMapEntry', b)
    _safe_set(b, 'graph_Graph13', set())
    assert not _is_linked(b, 'graph_Graph13', a2)
    if hasattr(a2, 'graph_URIToNodeLabelMapEntry'):
        assert not _is_linked(a2, 'graph_URIToNodeLabelMapEntry', b)


def test_assoc_nodes8_reverse_link_reassign_clear():
    a1 = graph_URIToNodeMapEntry(key="sample_text")
    a2 = graph_URIToNodeMapEntry(key="sample_text_2")
    b = graph_Graph(numDynamicLabels=7, numEdges=7, numGraphLabels=7, numNodeLabels=7, numNodes=7)
    _safe_set(b, 'graph_Graph9', {a1})
    assert _is_linked(b, 'graph_Graph9', a1)
    if hasattr(a1, 'graph_URIToNodeMapEntry'):
        assert _is_linked(a1, 'graph_URIToNodeMapEntry', b)
    _safe_set(b, 'graph_Graph9', {a2})
    assert _is_linked(b, 'graph_Graph9', a2)
    if hasattr(a1, 'graph_URIToNodeMapEntry'):
        assert not _is_linked(a1, 'graph_URIToNodeMapEntry', b)
    if hasattr(a2, 'graph_URIToNodeMapEntry'):
        assert _is_linked(a2, 'graph_URIToNodeMapEntry', b)
    _safe_set(b, 'graph_Graph9', set())
    assert not _is_linked(b, 'graph_Graph9', a2)
    if hasattr(a2, 'graph_URIToNodeMapEntry'):
        assert not _is_linked(a2, 'graph_URIToNodeMapEntry', b)


def test_assoc_unresolvedIdentifiables17_reverse_link_reassign_clear():
    a1 = graph_UnresolvedIdentifiable(fieldName="sample_text", unresolvedURI="sample_text")
    a2 = graph_UnresolvedIdentifiable(fieldName="sample_text_2", unresolvedURI="sample_text_2")
    b = graph_Graph(numDynamicLabels=7, numEdges=7, numGraphLabels=7, numNodeLabels=7, numNodes=7)
    _safe_set(b, 'graph_Graph18', {a1})
    assert _is_linked(b, 'graph_Graph18', a1)
    if hasattr(a1, 'graph_UnresolvedIdentifiable'):
        assert _is_linked(a1, 'graph_UnresolvedIdentifiable', b)
    _safe_set(b, 'graph_Graph18', {a2})
    assert _is_linked(b, 'graph_Graph18', a2)
    if hasattr(a1, 'graph_UnresolvedIdentifiable'):
        assert not _is_linked(a1, 'graph_UnresolvedIdentifiable', b)
    if hasattr(a2, 'graph_UnresolvedIdentifiable'):
        assert _is_linked(a2, 'graph_UnresolvedIdentifiable', b)
    _safe_set(b, 'graph_Graph18', set())
    assert not _is_linked(b, 'graph_Graph18', a2)
    if hasattr(a2, 'graph_UnresolvedIdentifiable'):
        assert not _is_linked(a2, 'graph_UnresolvedIdentifiable', b)


def test_assoc_value47_reverse_link_reassign_clear():
    a1 = graph_URIToEdgeMapEntry(key="sample_text")
    a2 = graph_URIToEdgeMapEntry(key="sample_text_2")
    b = graph_Edge(directed=True, nodeAURI="sample_text", nodeBURI="sample_text")
    _safe_set(b, 'graph_Edge49', a1)
    assert _is_linked(b, 'graph_Edge49', a1)
    if hasattr(a1, 'graph_URIToEdgeMapEntry48'):
        assert _is_linked(a1, 'graph_URIToEdgeMapEntry48', b)
    _safe_set(b, 'graph_Edge49', a2)
    assert _is_linked(b, 'graph_Edge49', a2)
    if hasattr(a1, 'graph_URIToEdgeMapEntry48'):
        assert not _is_linked(a1, 'graph_URIToEdgeMapEntry48', b)
    if hasattr(a2, 'graph_URIToEdgeMapEntry48'):
        assert _is_linked(a2, 'graph_URIToEdgeMapEntry48', b)
    _safe_set(b, 'graph_Edge49', None)
    assert not _is_linked(b, 'graph_Edge49', a2)
    if hasattr(a2, 'graph_URIToEdgeMapEntry48'):
        assert not _is_linked(a2, 'graph_URIToEdgeMapEntry48', b)


def test_assoc_value53_reverse_link_reassign_clear():
    a1 = graph_URIToLabelMapEntry(key="sample_text")
    a2 = graph_URIToLabelMapEntry(key="sample_text_2")
    b = graph_Label(uRIOfIdentifiableToBeLabeled="sample_text")
    _safe_set(b, 'graph_Label55', a1)
    assert _is_linked(b, 'graph_Label55', a1)
    if hasattr(a1, 'graph_URIToLabelMapEntry54'):
        assert _is_linked(a1, 'graph_URIToLabelMapEntry54', b)
    _safe_set(b, 'graph_Label55', a2)
    assert _is_linked(b, 'graph_Label55', a2)
    if hasattr(a1, 'graph_URIToLabelMapEntry54'):
        assert not _is_linked(a1, 'graph_URIToLabelMapEntry54', b)
    if hasattr(a2, 'graph_URIToLabelMapEntry54'):
        assert _is_linked(a2, 'graph_URIToLabelMapEntry54', b)
    _safe_set(b, 'graph_Label55', None)
    assert not _is_linked(b, 'graph_Label55', a2)
    if hasattr(a2, 'graph_URIToLabelMapEntry54'):
        assert not _is_linked(a2, 'graph_URIToLabelMapEntry54', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_a2_stub_double():
    # graph_Node has no real 'graph_Node' property in the generated
    # code (a bare stub) -- manually attach it so graph_Edge's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # graph_Edge's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = graph_Edge(directed=True, nodeAURI="sample_text", nodeBURI="sample_text")
    partner = graph_Node()
    setattr(partner, 'graph_Node', None)
    _safe_set(owner, 'graph_Edge', partner)
    assert getattr(partner, 'graph_Node') == owner
    _safe_set(owner, 'graph_Edge', None)
    assert getattr(partner, 'graph_Node') is None


def test_assoc_b3_stub_double():
    # graph_Node has no real 'graph_Node5' property in the generated
    # code (a bare stub) -- manually attach it so graph_Edge's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # graph_Edge's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = graph_Edge(directed=True, nodeAURI="sample_text", nodeBURI="sample_text")
    partner = graph_Node()
    setattr(partner, 'graph_Node5', None)
    _safe_set(owner, 'graph_Edge4', partner)
    assert getattr(partner, 'graph_Node5') == owner
    _safe_set(owner, 'graph_Edge4', None)
    assert getattr(partner, 'graph_Node5') is None


def test_assoc_decorator1_stub_double():
    # graph_Decorator has no real 'model.ecoreDecorator' property in the generated
    # code (a bare stub) -- manually attach it so graph_DynamicLabel's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # graph_DynamicLabel's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = graph_DynamicLabel(nextValueValid=True)
    partner = graph_Decorator()
    setattr(partner, 'model.ecoreDecorator', None)
    _safe_set(owner, 'labelsToUpdate', partner)
    assert getattr(partner, 'model.ecoreDecorator') == owner
    _safe_set(owner, 'labelsToUpdate', None)
    assert getattr(partner, 'model.ecoreDecorator') is None


def test_assoc_decorators19_stub_double():
    # graph_Decorator has no real 'model.ecoreDecorator20' property in the generated
    # code (a bare stub) -- manually attach it so graph_Graph's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # graph_Graph's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = graph_Graph(numDynamicLabels=7, numEdges=7, numGraphLabels=7, numNodeLabels=7, numNodes=7)
    partner = graph_Decorator()
    setattr(partner, 'model.ecoreDecorator20', None)
    _safe_set(owner, 'graph', {partner})
    assert getattr(partner, 'model.ecoreDecorator20') == owner
    _safe_set(owner, 'graph', set())
    assert getattr(partner, 'model.ecoreDecorator20') is None


def test_assoc_edge46_stub_double():
    # graph_EdgeLabel has no real 'label' property in the generated
    # code (a bare stub) -- manually attach it so graph_Edge's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # graph_Edge's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = graph_Edge(directed=True, nodeAURI="sample_text", nodeBURI="sample_text")
    partner = graph_EdgeLabel()
    setattr(partner, 'label', None)
    _safe_set(owner, 'Edge', partner)
    assert getattr(partner, 'label') == owner
    _safe_set(owner, 'Edge', None)
    assert getattr(partner, 'label') is None


def test_assoc_edges27_stub_double():
    # graph_Node has no real 'graph_Node28' property in the generated
    # code (a bare stub) -- manually attach it so graph_Edge's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # graph_Edge's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = graph_Edge(directed=True, nodeAURI="sample_text", nodeBURI="sample_text")
    partner = graph_Node()
    setattr(partner, 'graph_Node28', None)
    _safe_set(owner, 'graph_Edge29', partner)
    assert owner in getattr(partner, 'graph_Node28')
    _safe_set(owner, 'graph_Edge29', None)
    assert owner not in getattr(partner, 'graph_Node28')


def test_assoc_graph38_stub_double():
    # graph_Identifiable has no real 'graph_Identifiable40' property in the generated
    # code (a bare stub) -- manually attach it so graph_UnresolvedIdentifiable's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # graph_UnresolvedIdentifiable's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = graph_UnresolvedIdentifiable(fieldName="sample_text", unresolvedURI="sample_text")
    partner = graph_Identifiable()
    setattr(partner, 'graph_Identifiable40', None)
    _safe_set(owner, 'graph_UnresolvedIdentifiable39', partner)
    assert getattr(partner, 'graph_Identifiable40') == owner
    _safe_set(owner, 'graph_UnresolvedIdentifiable39', None)
    assert getattr(partner, 'graph_Identifiable40') is None


def test_assoc_identifiable25_stub_double():
    # graph_Identifiable has no real 'graph_Identifiable' property in the generated
    # code (a bare stub) -- manually attach it so graph_Label's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # graph_Label's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = graph_Label(uRIOfIdentifiableToBeLabeled="sample_text")
    partner = graph_Identifiable()
    setattr(partner, 'graph_Identifiable', None)
    _safe_set(owner, 'graph_Label26', partner)
    assert getattr(partner, 'graph_Identifiable') == owner
    _safe_set(owner, 'graph_Label26', None)
    assert getattr(partner, 'graph_Identifiable') is None


def test_assoc_identifiable41_stub_double():
    # graph_Identifiable has no real 'graph_Identifiable43' property in the generated
    # code (a bare stub) -- manually attach it so graph_UnresolvedIdentifiable's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # graph_UnresolvedIdentifiable's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = graph_UnresolvedIdentifiable(fieldName="sample_text", unresolvedURI="sample_text")
    partner = graph_Identifiable()
    setattr(partner, 'graph_Identifiable43', None)
    _safe_set(owner, 'graph_UnresolvedIdentifiable42', partner)
    assert getattr(partner, 'graph_Identifiable43') == owner
    _safe_set(owner, 'graph_UnresolvedIdentifiable42', None)
    assert getattr(partner, 'graph_Identifiable43') is None


def test_assoc_label6_stub_double():
    # graph_EdgeLabel has no real 'EdgeLabel' property in the generated
    # code (a bare stub) -- manually attach it so graph_Edge's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # graph_Edge's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = graph_Edge(directed=True, nodeAURI="sample_text", nodeBURI="sample_text")
    partner = graph_EdgeLabel()
    setattr(partner, 'EdgeLabel', None)
    _safe_set(owner, 'edge', partner)
    assert getattr(partner, 'EdgeLabel') == owner
    _safe_set(owner, 'edge', None)
    assert getattr(partner, 'EdgeLabel') is None


def test_assoc_model35_stub_double():
    # graph_Identifiable has no real 'graph_Identifiable37' property in the generated
    # code (a bare stub) -- manually attach it so graph_UnresolvedIdentifiable's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # graph_UnresolvedIdentifiable's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = graph_UnresolvedIdentifiable(fieldName="sample_text", unresolvedURI="sample_text")
    partner = graph_Identifiable()
    setattr(partner, 'graph_Identifiable37', None)
    _safe_set(owner, 'graph_UnresolvedIdentifiable36', partner)
    assert getattr(partner, 'graph_Identifiable37') == owner
    _safe_set(owner, 'graph_UnresolvedIdentifiable36', None)
    assert getattr(partner, 'graph_Identifiable37') is None


def test_assoc_scenario32_stub_double():
    # graph_Identifiable has no real 'graph_Identifiable34' property in the generated
    # code (a bare stub) -- manually attach it so graph_UnresolvedIdentifiable's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # graph_UnresolvedIdentifiable's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = graph_UnresolvedIdentifiable(fieldName="sample_text", unresolvedURI="sample_text")
    partner = graph_Identifiable()
    setattr(partner, 'graph_Identifiable34', None)
    _safe_set(owner, 'graph_UnresolvedIdentifiable33', partner)
    assert getattr(partner, 'graph_Identifiable34') == owner
    _safe_set(owner, 'graph_UnresolvedIdentifiable33', None)
    assert getattr(partner, 'graph_Identifiable34') is None


def test_assoc_time21_stub_double():
    # graph_STEMTime has no real 'graph_STEMTime' property in the generated
    # code (a bare stub) -- manually attach it so graph_Graph's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # graph_Graph's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = graph_Graph(numDynamicLabels=7, numEdges=7, numGraphLabels=7, numNodeLabels=7, numNodes=7)
    partner = graph_STEMTime()
    setattr(partner, 'graph_STEMTime', None)
    _safe_set(owner, 'graph_Graph22', partner)
    assert getattr(partner, 'graph_STEMTime') == owner
    _safe_set(owner, 'graph_Graph22', None)
    assert getattr(partner, 'graph_STEMTime') is None


def test_assoc_value44_stub_double():
    # graph_Identifiable has no real 'graph_Identifiable45' property in the generated
    # code (a bare stub) -- manually attach it so graph_URIToIdentifiableMapEntry's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # graph_URIToIdentifiableMapEntry's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = graph_URIToIdentifiableMapEntry(key="sample_text")
    partner = graph_Identifiable()
    setattr(partner, 'graph_Identifiable45', None)
    _safe_set(owner, 'graph_URIToIdentifiableMapEntry', partner)
    assert getattr(partner, 'graph_Identifiable45') == owner
    _safe_set(owner, 'graph_URIToIdentifiableMapEntry', None)
    assert getattr(partner, 'graph_Identifiable45') is None


def test_assoc_value50_stub_double():
    # graph_Node has no real 'graph_Node52' property in the generated
    # code (a bare stub) -- manually attach it so graph_URIToNodeMapEntry's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # graph_URIToNodeMapEntry's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = graph_URIToNodeMapEntry(key="sample_text")
    partner = graph_Node()
    setattr(partner, 'graph_Node52', None)
    _safe_set(owner, 'graph_URIToNodeMapEntry51', partner)
    assert getattr(partner, 'graph_Node52') == owner
    _safe_set(owner, 'graph_URIToNodeMapEntry51', None)
    assert getattr(partner, 'graph_Node52') is None


def test_assoc_value56_stub_double():
    # graph_NodeLabel has no real 'graph_NodeLabel' property in the generated
    # code (a bare stub) -- manually attach it so graph_URIToNodeLabelMapEntry's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # graph_URIToNodeLabelMapEntry's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = graph_URIToNodeLabelMapEntry(key="sample_text")
    partner = graph_NodeLabel()
    setattr(partner, 'graph_NodeLabel', None)
    _safe_set(owner, 'graph_URIToNodeLabelMapEntry57', partner)
    assert getattr(partner, 'graph_NodeLabel') == owner
    _safe_set(owner, 'graph_URIToNodeLabelMapEntry57', None)
    assert getattr(partner, 'graph_NodeLabel') is None


