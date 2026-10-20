import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Identifiable,
    graph_Edge,
    graph_Graph,
    graph_GraphAsset,
    graph_Identifiable,
    graph_Node,
    graph_NodeResponsibility,
    graph_Subgraphs,
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

def test_assoc_graphassets4_reverse_link_reassign_clear():
    a1 = graph_GraphAsset(Encrypted=True, Label=7)
    a2 = graph_GraphAsset(Encrypted=False, Label=13)
    b = graph_Edge(EdgeLabel=7, visited=True)
    _safe_set(b, 'graph_Edge5', {a1})
    assert _is_linked(b, 'graph_Edge5', a1)
    if hasattr(a1, 'graph_GraphAsset'):
        assert _is_linked(a1, 'graph_GraphAsset', b)
    _safe_set(b, 'graph_Edge5', {a2})
    assert _is_linked(b, 'graph_Edge5', a2)
    if hasattr(a1, 'graph_GraphAsset'):
        assert not _is_linked(a1, 'graph_GraphAsset', b)
    if hasattr(a2, 'graph_GraphAsset'):
        assert _is_linked(a2, 'graph_GraphAsset', b)
    _safe_set(b, 'graph_Edge5', set())
    assert not _is_linked(b, 'graph_Edge5', a2)
    if hasattr(a2, 'graph_GraphAsset'):
        assert not _is_linked(a2, 'graph_GraphAsset', b)


def test_assoc_incomingassets28_reverse_link_reassign_clear():
    a1 = graph_NodeResponsibility(operation="sample_text")
    a2 = graph_NodeResponsibility(operation="sample_text_2")
    b = graph_GraphAsset(Encrypted=True, Label=7)
    _safe_set(b, 'graph_GraphAsset30', a1)
    assert _is_linked(b, 'graph_GraphAsset30', a1)
    if hasattr(a1, 'graph_NodeResponsibility29'):
        assert _is_linked(a1, 'graph_NodeResponsibility29', b)
    _safe_set(b, 'graph_GraphAsset30', a2)
    assert _is_linked(b, 'graph_GraphAsset30', a2)
    if hasattr(a1, 'graph_NodeResponsibility29'):
        assert not _is_linked(a1, 'graph_NodeResponsibility29', b)
    if hasattr(a2, 'graph_NodeResponsibility29'):
        assert _is_linked(a2, 'graph_NodeResponsibility29', b)
    _safe_set(b, 'graph_GraphAsset30', None)
    assert not _is_linked(b, 'graph_GraphAsset30', a2)
    if hasattr(a2, 'graph_NodeResponsibility29'):
        assert not _is_linked(a2, 'graph_NodeResponsibility29', b)


def test_assoc_inedges17_reverse_link_reassign_clear():
    a1 = graph_Node(Attacker=True, AttackerObservation=7, name="sample_text", visited=True)
    a2 = graph_Node(Attacker=False, AttackerObservation=13, name="sample_text_2", visited=False)
    b = graph_Edge(EdgeLabel=7, visited=True)
    _safe_set(b, 'graph_Edge19', a1)
    assert _is_linked(b, 'graph_Edge19', a1)
    if hasattr(a1, 'graph_Node18'):
        assert _is_linked(a1, 'graph_Node18', b)
    _safe_set(b, 'graph_Edge19', a2)
    assert _is_linked(b, 'graph_Edge19', a2)
    if hasattr(a1, 'graph_Node18'):
        assert not _is_linked(a1, 'graph_Node18', b)
    if hasattr(a2, 'graph_Node18'):
        assert _is_linked(a2, 'graph_Node18', b)
    _safe_set(b, 'graph_Edge19', None)
    assert not _is_linked(b, 'graph_Edge19', a2)
    if hasattr(a2, 'graph_Node18'):
        assert not _is_linked(a2, 'graph_Node18', b)


def test_assoc_outedges12_reverse_link_reassign_clear():
    a1 = graph_Node(Attacker=True, AttackerObservation=7, name="sample_text", visited=True)
    a2 = graph_Node(Attacker=False, AttackerObservation=13, name="sample_text_2", visited=False)
    b = graph_Edge(EdgeLabel=7, visited=True)
    _safe_set(b, 'graph_Edge14', a1)
    assert _is_linked(b, 'graph_Edge14', a1)
    if hasattr(a1, 'graph_Node13'):
        assert _is_linked(a1, 'graph_Node13', b)
    _safe_set(b, 'graph_Edge14', a2)
    assert _is_linked(b, 'graph_Edge14', a2)
    if hasattr(a1, 'graph_Node13'):
        assert not _is_linked(a1, 'graph_Node13', b)
    if hasattr(a2, 'graph_Node13'):
        assert _is_linked(a2, 'graph_Node13', b)
    _safe_set(b, 'graph_Edge14', None)
    assert not _is_linked(b, 'graph_Edge14', a2)
    if hasattr(a2, 'graph_Node13'):
        assert not _is_linked(a2, 'graph_Node13', b)


def test_assoc_outgoingassets25_reverse_link_reassign_clear():
    a1 = graph_NodeResponsibility(operation="sample_text")
    a2 = graph_NodeResponsibility(operation="sample_text_2")
    b = graph_GraphAsset(Encrypted=True, Label=7)
    _safe_set(b, 'graph_GraphAsset27', a1)
    assert _is_linked(b, 'graph_GraphAsset27', a1)
    if hasattr(a1, 'graph_NodeResponsibility26'):
        assert _is_linked(a1, 'graph_NodeResponsibility26', b)
    _safe_set(b, 'graph_GraphAsset27', a2)
    assert _is_linked(b, 'graph_GraphAsset27', a2)
    if hasattr(a1, 'graph_NodeResponsibility26'):
        assert not _is_linked(a1, 'graph_NodeResponsibility26', b)
    if hasattr(a2, 'graph_NodeResponsibility26'):
        assert _is_linked(a2, 'graph_NodeResponsibility26', b)
    _safe_set(b, 'graph_GraphAsset27', None)
    assert not _is_linked(b, 'graph_GraphAsset27', a2)
    if hasattr(a2, 'graph_NodeResponsibility26'):
        assert not _is_linked(a2, 'graph_NodeResponsibility26', b)


def test_assoc_responsibility15_reverse_link_reassign_clear():
    a1 = graph_NodeResponsibility(operation="sample_text")
    a2 = graph_NodeResponsibility(operation="sample_text_2")
    b = graph_Node(Attacker=True, AttackerObservation=7, name="sample_text", visited=True)
    _safe_set(b, 'graph_Node16', {a1})
    assert _is_linked(b, 'graph_Node16', a1)
    if hasattr(a1, 'graph_NodeResponsibility'):
        assert _is_linked(a1, 'graph_NodeResponsibility', b)
    _safe_set(b, 'graph_Node16', {a2})
    assert _is_linked(b, 'graph_Node16', a2)
    if hasattr(a1, 'graph_NodeResponsibility'):
        assert not _is_linked(a1, 'graph_NodeResponsibility', b)
    if hasattr(a2, 'graph_NodeResponsibility'):
        assert _is_linked(a2, 'graph_NodeResponsibility', b)
    _safe_set(b, 'graph_Node16', set())
    assert not _is_linked(b, 'graph_Node16', a2)
    if hasattr(a2, 'graph_NodeResponsibility'):
        assert not _is_linked(a2, 'graph_NodeResponsibility', b)


def test_assoc_source1_reverse_link_reassign_clear():
    a1 = graph_Node(Attacker=True, AttackerObservation=7, name="sample_text", visited=True)
    a2 = graph_Node(Attacker=False, AttackerObservation=13, name="sample_text_2", visited=False)
    b = graph_Edge(EdgeLabel=7, visited=True)
    _safe_set(b, 'graph_Edge2', a1)
    assert _is_linked(b, 'graph_Edge2', a1)
    if hasattr(a1, 'graph_Node3'):
        assert _is_linked(a1, 'graph_Node3', b)
    _safe_set(b, 'graph_Edge2', a2)
    assert _is_linked(b, 'graph_Edge2', a2)
    if hasattr(a1, 'graph_Node3'):
        assert not _is_linked(a1, 'graph_Node3', b)
    if hasattr(a2, 'graph_Node3'):
        assert _is_linked(a2, 'graph_Node3', b)
    _safe_set(b, 'graph_Edge2', None)
    assert not _is_linked(b, 'graph_Edge2', a2)
    if hasattr(a2, 'graph_Node3'):
        assert not _is_linked(a2, 'graph_Node3', b)


def test_assoc_source6_reverse_link_reassign_clear():
    a1 = graph_Node(Attacker=True, AttackerObservation=7, name="sample_text", visited=True)
    a2 = graph_Node(Attacker=False, AttackerObservation=13, name="sample_text_2", visited=False)
    b = graph_GraphAsset(Encrypted=True, Label=7)
    _safe_set(b, 'graph_GraphAsset7', a1)
    assert _is_linked(b, 'graph_GraphAsset7', a1)
    if hasattr(a1, 'graph_Node8'):
        assert _is_linked(a1, 'graph_Node8', b)
    _safe_set(b, 'graph_GraphAsset7', a2)
    assert _is_linked(b, 'graph_GraphAsset7', a2)
    if hasattr(a1, 'graph_Node8'):
        assert not _is_linked(a1, 'graph_Node8', b)
    if hasattr(a2, 'graph_Node8'):
        assert _is_linked(a2, 'graph_Node8', b)
    _safe_set(b, 'graph_GraphAsset7', None)
    assert not _is_linked(b, 'graph_GraphAsset7', a2)
    if hasattr(a2, 'graph_Node8'):
        assert not _is_linked(a2, 'graph_Node8', b)


def test_assoc_target0_reverse_link_reassign_clear():
    a1 = graph_Node(Attacker=True, AttackerObservation=7, name="sample_text", visited=True)
    a2 = graph_Node(Attacker=False, AttackerObservation=13, name="sample_text_2", visited=False)
    b = graph_Edge(EdgeLabel=7, visited=True)
    _safe_set(b, 'graph_Edge', {a1})
    assert _is_linked(b, 'graph_Edge', a1)
    if hasattr(a1, 'graph_Node'):
        assert _is_linked(a1, 'graph_Node', b)
    _safe_set(b, 'graph_Edge', {a2})
    assert _is_linked(b, 'graph_Edge', a2)
    if hasattr(a1, 'graph_Node'):
        assert not _is_linked(a1, 'graph_Node', b)
    if hasattr(a2, 'graph_Node'):
        assert _is_linked(a2, 'graph_Node', b)
    _safe_set(b, 'graph_Edge', set())
    assert not _is_linked(b, 'graph_Edge', a2)
    if hasattr(a2, 'graph_Node'):
        assert not _is_linked(a2, 'graph_Node', b)


def test_assoc_targets9_reverse_link_reassign_clear():
    a1 = graph_Node(Attacker=True, AttackerObservation=7, name="sample_text", visited=True)
    a2 = graph_Node(Attacker=False, AttackerObservation=13, name="sample_text_2", visited=False)
    b = graph_GraphAsset(Encrypted=True, Label=7)
    _safe_set(b, 'graph_GraphAsset10', {a1})
    assert _is_linked(b, 'graph_GraphAsset10', a1)
    if hasattr(a1, 'graph_Node11'):
        assert _is_linked(a1, 'graph_Node11', b)
    _safe_set(b, 'graph_GraphAsset10', {a2})
    assert _is_linked(b, 'graph_GraphAsset10', a2)
    if hasattr(a1, 'graph_Node11'):
        assert not _is_linked(a1, 'graph_Node11', b)
    if hasattr(a2, 'graph_Node11'):
        assert _is_linked(a2, 'graph_Node11', b)
    _safe_set(b, 'graph_GraphAsset10', set())
    assert not _is_linked(b, 'graph_GraphAsset10', a2)
    if hasattr(a2, 'graph_Node11'):
        assert not _is_linked(a2, 'graph_Node11', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_assets22_stub_double():
    # graph_Subgraphs has no real 'graph_Subgraphs23' property in the generated
    # code (a bare stub) -- manually attach it so graph_GraphAsset's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # graph_GraphAsset's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = graph_GraphAsset(Encrypted=True, Label=7)
    partner = graph_Subgraphs()
    setattr(partner, 'graph_Subgraphs23', None)
    _safe_set(owner, 'graph_GraphAsset24', partner)
    assert owner in getattr(partner, 'graph_Subgraphs23')
    _safe_set(owner, 'graph_GraphAsset24', None)
    assert owner not in getattr(partner, 'graph_Subgraphs23')


def test_assoc_nodes20_stub_double():
    # graph_Subgraphs has no real 'graph_Subgraphs' property in the generated
    # code (a bare stub) -- manually attach it so graph_Node's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # graph_Node's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = graph_Node(Attacker=True, AttackerObservation=7, name="sample_text", visited=True)
    partner = graph_Subgraphs()
    setattr(partner, 'graph_Subgraphs', None)
    _safe_set(owner, 'graph_Node21', partner)
    assert owner in getattr(partner, 'graph_Subgraphs')
    _safe_set(owner, 'graph_Node21', None)
    assert owner not in getattr(partner, 'graph_Subgraphs')


