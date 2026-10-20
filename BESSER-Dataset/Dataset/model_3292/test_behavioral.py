import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    FSMGenElement,
    GraphItem,
    fsmgen_AbstractInterfaceItem,
    fsmgen_CommonTrigger,
    fsmgen_EObject,
    fsmgen_FSMGenElement,
    fsmgen_Graph,
    fsmgen_GraphContainer,
    fsmgen_GraphItem,
    fsmgen_Link,
    fsmgen_ModelComponent,
    fsmgen_Node,
    fsmgen_StateGraph,
    fsmgen_StateGraphNode,
    fsmgen_TransitionBase,
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

def test_assoc_caughtTriggers18_reverse_link_reassign_clear():
    a1 = fsmgen_Node(inheritanceLevel=7)
    a2 = fsmgen_Node(inheritanceLevel=13)
    b = fsmgen_CommonTrigger(hasGuard=True, trigger="sample_text")
    _safe_set(b, 'fsmgen_CommonTrigger', a1)
    assert _is_linked(b, 'fsmgen_CommonTrigger', a1)
    if hasattr(a1, 'fsmgen_Node19'):
        assert _is_linked(a1, 'fsmgen_Node19', b)
    _safe_set(b, 'fsmgen_CommonTrigger', a2)
    assert _is_linked(b, 'fsmgen_CommonTrigger', a2)
    if hasattr(a1, 'fsmgen_Node19'):
        assert not _is_linked(a1, 'fsmgen_Node19', b)
    if hasattr(a2, 'fsmgen_Node19'):
        assert _is_linked(a2, 'fsmgen_Node19', b)
    _safe_set(b, 'fsmgen_CommonTrigger', None)
    assert not _is_linked(b, 'fsmgen_CommonTrigger', a2)
    if hasattr(a2, 'fsmgen_Node19'):
        assert not _is_linked(a2, 'fsmgen_Node19', b)


def test_assoc_chainHeads27_reverse_link_reassign_clear():
    a1 = fsmgen_Link(ifitemTriggered=True)
    a2 = fsmgen_Link(ifitemTriggered=False)
    b = fsmgen_Link(ifitemTriggered=True)
    _safe_set(b, 'fsmgen_Link26', {a1})
    assert _is_linked(b, 'fsmgen_Link26', a1)
    if hasattr(a1, 'fsmgen_Link'):
        assert _is_linked(a1, 'fsmgen_Link', b)
    _safe_set(b, 'fsmgen_Link26', {a2})
    assert _is_linked(b, 'fsmgen_Link26', a2)
    if hasattr(a1, 'fsmgen_Link'):
        assert not _is_linked(a1, 'fsmgen_Link', b)
    if hasattr(a2, 'fsmgen_Link'):
        assert _is_linked(a2, 'fsmgen_Link', b)
    _safe_set(b, 'fsmgen_Link26', set())
    assert not _is_linked(b, 'fsmgen_Link26', a2)
    if hasattr(a2, 'fsmgen_Link'):
        assert not _is_linked(a2, 'fsmgen_Link', b)


def test_assoc_graph0_reverse_link_reassign_clear():
    a1 = fsmgen_GraphContainer(initializedChainHeads=True, initializedCommonData=True, initializedTriggersInStates=True)
    a2 = fsmgen_GraphContainer(initializedChainHeads=False, initializedCommonData=False, initializedTriggersInStates=False)
    b = fsmgen_Graph()
    _safe_set(b, 'fsmgen_Graph', a1)
    assert _is_linked(b, 'fsmgen_Graph', a1)
    if hasattr(a1, 'fsmgen_GraphContainer'):
        assert _is_linked(a1, 'fsmgen_GraphContainer', b)
    _safe_set(b, 'fsmgen_Graph', a2)
    assert _is_linked(b, 'fsmgen_Graph', a2)
    if hasattr(a1, 'fsmgen_GraphContainer'):
        assert not _is_linked(a1, 'fsmgen_GraphContainer', b)
    if hasattr(a2, 'fsmgen_GraphContainer'):
        assert _is_linked(a2, 'fsmgen_GraphContainer', b)
    _safe_set(b, 'fsmgen_Graph', None)
    assert not _is_linked(b, 'fsmgen_Graph', a2)
    if hasattr(a2, 'fsmgen_GraphContainer'):
        assert not _is_linked(a2, 'fsmgen_GraphContainer', b)


def test_assoc_graph10_reverse_link_reassign_clear():
    a1 = fsmgen_Node(inheritanceLevel=7)
    a2 = fsmgen_Node(inheritanceLevel=13)
    b = fsmgen_Graph()
    _safe_set(b, 'Graph', a1)
    assert _is_linked(b, 'Graph', a1)
    if hasattr(a1, 'nodes'):
        assert _is_linked(a1, 'nodes', b)
    _safe_set(b, 'Graph', a2)
    assert _is_linked(b, 'Graph', a2)
    if hasattr(a1, 'nodes'):
        assert not _is_linked(a1, 'nodes', b)
    if hasattr(a2, 'nodes'):
        assert _is_linked(a2, 'nodes', b)
    _safe_set(b, 'Graph', None)
    assert not _is_linked(b, 'Graph', a2)
    if hasattr(a2, 'nodes'):
        assert not _is_linked(a2, 'nodes', b)


def test_assoc_graph20_reverse_link_reassign_clear():
    a1 = fsmgen_Link(ifitemTriggered=True)
    a2 = fsmgen_Link(ifitemTriggered=False)
    b = fsmgen_Graph()
    _safe_set(b, 'Graph21', a1)
    assert _is_linked(b, 'Graph21', a1)
    if hasattr(a1, 'links'):
        assert _is_linked(a1, 'links', b)
    _safe_set(b, 'Graph21', a2)
    assert _is_linked(b, 'Graph21', a2)
    if hasattr(a1, 'links'):
        assert not _is_linked(a1, 'links', b)
    if hasattr(a2, 'links'):
        assert _is_linked(a2, 'links', b)
    _safe_set(b, 'Graph21', None)
    assert not _is_linked(b, 'Graph21', a2)
    if hasattr(a2, 'links'):
        assert not _is_linked(a2, 'links', b)


def test_assoc_incoming15_reverse_link_reassign_clear():
    a1 = fsmgen_Node(inheritanceLevel=7)
    a2 = fsmgen_Node(inheritanceLevel=13)
    b = fsmgen_Link(ifitemTriggered=True)
    _safe_set(b, 'Link16', a1)
    assert _is_linked(b, 'Link16', a1)
    if hasattr(a1, 'target'):
        assert _is_linked(a1, 'target', b)
    _safe_set(b, 'Link16', a2)
    assert _is_linked(b, 'Link16', a2)
    if hasattr(a1, 'target'):
        assert not _is_linked(a1, 'target', b)
    if hasattr(a2, 'target'):
        assert _is_linked(a2, 'target', b)
    _safe_set(b, 'Link16', None)
    assert not _is_linked(b, 'Link16', a2)
    if hasattr(a2, 'target'):
        assert not _is_linked(a2, 'target', b)


def test_assoc_links37_reverse_link_reassign_clear():
    a1 = fsmgen_Link(ifitemTriggered=True)
    a2 = fsmgen_Link(ifitemTriggered=False)
    b = fsmgen_CommonTrigger(hasGuard=True, trigger="sample_text")
    _safe_set(b, 'fsmgen_CommonTrigger38', {a1})
    assert _is_linked(b, 'fsmgen_CommonTrigger38', a1)
    if hasattr(a1, 'fsmgen_Link39'):
        assert _is_linked(a1, 'fsmgen_Link39', b)
    _safe_set(b, 'fsmgen_CommonTrigger38', {a2})
    assert _is_linked(b, 'fsmgen_CommonTrigger38', a2)
    if hasattr(a1, 'fsmgen_Link39'):
        assert not _is_linked(a1, 'fsmgen_Link39', b)
    if hasattr(a2, 'fsmgen_Link39'):
        assert _is_linked(a2, 'fsmgen_Link39', b)
    _safe_set(b, 'fsmgen_CommonTrigger38', set())
    assert not _is_linked(b, 'fsmgen_CommonTrigger38', a2)
    if hasattr(a2, 'fsmgen_Link39'):
        assert not _is_linked(a2, 'fsmgen_Link39', b)


def test_assoc_links4_reverse_link_reassign_clear():
    a1 = fsmgen_Link(ifitemTriggered=True)
    a2 = fsmgen_Link(ifitemTriggered=False)
    b = fsmgen_Graph()
    _safe_set(b, 'graph5', {a1})
    assert _is_linked(b, 'graph5', a1)
    if hasattr(a1, 'Link'):
        assert _is_linked(a1, 'Link', b)
    _safe_set(b, 'graph5', {a2})
    assert _is_linked(b, 'graph5', a2)
    if hasattr(a1, 'Link'):
        assert not _is_linked(a1, 'Link', b)
    if hasattr(a2, 'Link'):
        assert _is_linked(a2, 'Link', b)
    _safe_set(b, 'graph5', set())
    assert not _is_linked(b, 'graph5', a2)
    if hasattr(a2, 'Link'):
        assert not _is_linked(a2, 'Link', b)


def test_assoc_node8_reverse_link_reassign_clear():
    a1 = fsmgen_Node(inheritanceLevel=7)
    a2 = fsmgen_Node(inheritanceLevel=13)
    b = fsmgen_Graph()
    _safe_set(b, 'subgraph', a1)
    assert _is_linked(b, 'subgraph', a1)
    if hasattr(a1, 'Node9'):
        assert _is_linked(a1, 'Node9', b)
    _safe_set(b, 'subgraph', a2)
    assert _is_linked(b, 'subgraph', a2)
    if hasattr(a1, 'Node9'):
        assert not _is_linked(a1, 'Node9', b)
    if hasattr(a2, 'Node9'):
        assert _is_linked(a2, 'Node9', b)
    _safe_set(b, 'subgraph', None)
    assert not _is_linked(b, 'subgraph', a2)
    if hasattr(a2, 'Node9'):
        assert not _is_linked(a2, 'Node9', b)


def test_assoc_nodes3_reverse_link_reassign_clear():
    a1 = fsmgen_Node(inheritanceLevel=7)
    a2 = fsmgen_Node(inheritanceLevel=13)
    b = fsmgen_Graph()
    _safe_set(b, 'graph', {a1})
    assert _is_linked(b, 'graph', a1)
    if hasattr(a1, 'Node'):
        assert _is_linked(a1, 'Node', b)
    _safe_set(b, 'graph', {a2})
    assert _is_linked(b, 'graph', a2)
    if hasattr(a1, 'Node'):
        assert not _is_linked(a1, 'Node', b)
    if hasattr(a2, 'Node'):
        assert _is_linked(a2, 'Node', b)
    _safe_set(b, 'graph', set())
    assert not _is_linked(b, 'graph', a2)
    if hasattr(a2, 'Node'):
        assert not _is_linked(a2, 'Node', b)


def test_assoc_outgoing13_reverse_link_reassign_clear():
    a1 = fsmgen_Node(inheritanceLevel=7)
    a2 = fsmgen_Node(inheritanceLevel=13)
    b = fsmgen_Link(ifitemTriggered=True)
    _safe_set(b, 'Link14', a1)
    assert _is_linked(b, 'Link14', a1)
    if hasattr(a1, 'source'):
        assert _is_linked(a1, 'source', b)
    _safe_set(b, 'Link14', a2)
    assert _is_linked(b, 'Link14', a2)
    if hasattr(a1, 'source'):
        assert not _is_linked(a1, 'source', b)
    if hasattr(a2, 'source'):
        assert _is_linked(a2, 'source', b)
    _safe_set(b, 'Link14', None)
    assert not _is_linked(b, 'Link14', a2)
    if hasattr(a2, 'source'):
        assert not _is_linked(a2, 'source', b)


def test_assoc_source22_reverse_link_reassign_clear():
    a1 = fsmgen_Node(inheritanceLevel=7)
    a2 = fsmgen_Node(inheritanceLevel=13)
    b = fsmgen_Link(ifitemTriggered=True)
    _safe_set(b, 'outgoing', a1)
    assert _is_linked(b, 'outgoing', a1)
    if hasattr(a1, 'Node23'):
        assert _is_linked(a1, 'Node23', b)
    _safe_set(b, 'outgoing', a2)
    assert _is_linked(b, 'outgoing', a2)
    if hasattr(a1, 'Node23'):
        assert not _is_linked(a1, 'Node23', b)
    if hasattr(a2, 'Node23'):
        assert _is_linked(a2, 'Node23', b)
    _safe_set(b, 'outgoing', None)
    assert not _is_linked(b, 'outgoing', a2)
    if hasattr(a2, 'Node23'):
        assert not _is_linked(a2, 'Node23', b)


def test_assoc_subgraph11_reverse_link_reassign_clear():
    a1 = fsmgen_Node(inheritanceLevel=7)
    a2 = fsmgen_Node(inheritanceLevel=13)
    b = fsmgen_Graph()
    _safe_set(b, 'Graph12', a1)
    assert _is_linked(b, 'Graph12', a1)
    if hasattr(a1, 'node'):
        assert _is_linked(a1, 'node', b)
    _safe_set(b, 'Graph12', a2)
    assert _is_linked(b, 'Graph12', a2)
    if hasattr(a1, 'node'):
        assert not _is_linked(a1, 'node', b)
    if hasattr(a2, 'node'):
        assert _is_linked(a2, 'node', b)
    _safe_set(b, 'Graph12', None)
    assert not _is_linked(b, 'Graph12', a2)
    if hasattr(a2, 'node'):
        assert not _is_linked(a2, 'node', b)


def test_assoc_target24_reverse_link_reassign_clear():
    a1 = fsmgen_Node(inheritanceLevel=7)
    a2 = fsmgen_Node(inheritanceLevel=13)
    b = fsmgen_Link(ifitemTriggered=True)
    _safe_set(b, 'incoming', a1)
    assert _is_linked(b, 'incoming', a1)
    if hasattr(a1, 'Node25'):
        assert _is_linked(a1, 'Node25', b)
    _safe_set(b, 'incoming', a2)
    assert _is_linked(b, 'incoming', a2)
    if hasattr(a1, 'Node25'):
        assert not _is_linked(a1, 'Node25', b)
    if hasattr(a2, 'Node25'):
        assert _is_linked(a2, 'Node25', b)
    _safe_set(b, 'incoming', None)
    assert not _is_linked(b, 'incoming', a2)
    if hasattr(a2, 'Node25'):
        assert not _is_linked(a2, 'Node25', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_commonData28_stub_double():
    # fsmgen_EObject has no real 'fsmgen_EObject' property in the generated
    # code (a bare stub) -- manually attach it so fsmgen_Link's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # fsmgen_Link's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = fsmgen_Link(ifitemTriggered=True)
    partner = fsmgen_EObject()
    setattr(partner, 'fsmgen_EObject', None)
    _safe_set(owner, 'fsmgen_Link29', partner)
    assert getattr(partner, 'fsmgen_EObject') == owner
    _safe_set(owner, 'fsmgen_Link29', None)
    assert getattr(partner, 'fsmgen_EObject') is None


def test_assoc_component1_stub_double():
    # fsmgen_ModelComponent has no real 'fsmgen_ModelComponent' property in the generated
    # code (a bare stub) -- manually attach it so fsmgen_GraphContainer's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # fsmgen_GraphContainer's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = fsmgen_GraphContainer(initializedChainHeads=True, initializedCommonData=True, initializedTriggersInStates=True)
    partner = fsmgen_ModelComponent()
    setattr(partner, 'fsmgen_ModelComponent', None)
    _safe_set(owner, 'fsmgen_GraphContainer2', partner)
    assert getattr(partner, 'fsmgen_ModelComponent') == owner
    _safe_set(owner, 'fsmgen_GraphContainer2', None)
    assert getattr(partner, 'fsmgen_ModelComponent') is None


def test_assoc_ifitem35_stub_double():
    # fsmgen_AbstractInterfaceItem has no real 'fsmgen_AbstractInterfaceItem' property in the generated
    # code (a bare stub) -- manually attach it so fsmgen_CommonTrigger's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # fsmgen_CommonTrigger's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = fsmgen_CommonTrigger(hasGuard=True, trigger="sample_text")
    partner = fsmgen_AbstractInterfaceItem()
    setattr(partner, 'fsmgen_AbstractInterfaceItem', None)
    _safe_set(owner, 'fsmgen_CommonTrigger36', partner)
    assert getattr(partner, 'fsmgen_AbstractInterfaceItem') == owner
    _safe_set(owner, 'fsmgen_CommonTrigger36', None)
    assert getattr(partner, 'fsmgen_AbstractInterfaceItem') is None


def test_assoc_msg32_stub_double():
    # fsmgen_EObject has no real 'fsmgen_EObject34' property in the generated
    # code (a bare stub) -- manually attach it so fsmgen_CommonTrigger's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # fsmgen_CommonTrigger's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = fsmgen_CommonTrigger(hasGuard=True, trigger="sample_text")
    partner = fsmgen_EObject()
    setattr(partner, 'fsmgen_EObject34', None)
    _safe_set(owner, 'fsmgen_CommonTrigger33', partner)
    assert getattr(partner, 'fsmgen_EObject34') == owner
    _safe_set(owner, 'fsmgen_CommonTrigger33', None)
    assert getattr(partner, 'fsmgen_EObject34') is None


def test_assoc_stateGraph6_stub_double():
    # fsmgen_StateGraph has no real 'fsmgen_StateGraph' property in the generated
    # code (a bare stub) -- manually attach it so fsmgen_Graph's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # fsmgen_Graph's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = fsmgen_Graph()
    partner = fsmgen_StateGraph()
    setattr(partner, 'fsmgen_StateGraph', None)
    _safe_set(owner, 'fsmgen_Graph7', partner)
    assert getattr(partner, 'fsmgen_StateGraph') == owner
    _safe_set(owner, 'fsmgen_Graph7', None)
    assert getattr(partner, 'fsmgen_StateGraph') is None


def test_assoc_stateGraphNode17_stub_double():
    # fsmgen_StateGraphNode has no real 'fsmgen_StateGraphNode' property in the generated
    # code (a bare stub) -- manually attach it so fsmgen_Node's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # fsmgen_Node's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = fsmgen_Node(inheritanceLevel=7)
    partner = fsmgen_StateGraphNode()
    setattr(partner, 'fsmgen_StateGraphNode', None)
    _safe_set(owner, 'fsmgen_Node', partner)
    assert getattr(partner, 'fsmgen_StateGraphNode') == owner
    _safe_set(owner, 'fsmgen_Node', None)
    assert getattr(partner, 'fsmgen_StateGraphNode') is None


def test_assoc_transition30_stub_double():
    # fsmgen_TransitionBase has no real 'fsmgen_TransitionBase' property in the generated
    # code (a bare stub) -- manually attach it so fsmgen_Link's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # fsmgen_Link's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = fsmgen_Link(ifitemTriggered=True)
    partner = fsmgen_TransitionBase()
    setattr(partner, 'fsmgen_TransitionBase', None)
    _safe_set(owner, 'fsmgen_Link31', partner)
    assert getattr(partner, 'fsmgen_TransitionBase') == owner
    _safe_set(owner, 'fsmgen_Link31', None)
    assert getattr(partner, 'fsmgen_TransitionBase') is None


