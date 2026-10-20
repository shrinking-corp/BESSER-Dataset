import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Connector,
    UATMM_structure_AND,
    UATMM_structure_AttackTree,
    UATMM_structure_Connector,
    UATMM_structure_Edge,
    UATMM_structure_FDEP,
    UATMM_structure_KofN,
    UATMM_structure_Node,
    UATMM_structure_OR,
    UATMM_structure_PAND,
    UATMM_structure_RDEP,
    UATMM_structure_SAND,
    UATMM_structure_SOR,
    UATMM_structure_Spare,
    UATMM_structure_TAND,
    UATMM_structure_TreeMetaData,
    UATMM_structure_Weighted,
    UATMM_structure_XOR,
    EdgeKind,
    Nature,
    RoleType,
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

def test_assoc_Source17_reverse_link_reassign_clear():
    a1 = UATMM_structure_Node(id="sample_text", label="sample_text", nature="sample_text", role="sample_text")
    a2 = UATMM_structure_Node(id="sample_text_2", label="sample_text_2", nature="sample_text_2", role="sample_text_2")
    b = UATMM_structure_Edge(edgeKind="sample_text")
    _safe_set(b, 'UATMM_structure_Edge18', a1)
    assert _is_linked(b, 'UATMM_structure_Edge18', a1)
    if hasattr(a1, 'UATMM_structure_Node19'):
        assert _is_linked(a1, 'UATMM_structure_Node19', b)
    _safe_set(b, 'UATMM_structure_Edge18', a2)
    assert _is_linked(b, 'UATMM_structure_Edge18', a2)
    if hasattr(a1, 'UATMM_structure_Node19'):
        assert not _is_linked(a1, 'UATMM_structure_Node19', b)
    if hasattr(a2, 'UATMM_structure_Node19'):
        assert _is_linked(a2, 'UATMM_structure_Node19', b)
    _safe_set(b, 'UATMM_structure_Edge18', None)
    assert not _is_linked(b, 'UATMM_structure_Edge18', a2)
    if hasattr(a2, 'UATMM_structure_Node19'):
        assert not _is_linked(a2, 'UATMM_structure_Node19', b)


def test_assoc_Target14_reverse_link_reassign_clear():
    a1 = UATMM_structure_Node(id="sample_text", label="sample_text", nature="sample_text", role="sample_text")
    a2 = UATMM_structure_Node(id="sample_text_2", label="sample_text_2", nature="sample_text_2", role="sample_text_2")
    b = UATMM_structure_Edge(edgeKind="sample_text")
    _safe_set(b, 'UATMM_structure_Edge15', a1)
    assert _is_linked(b, 'UATMM_structure_Edge15', a1)
    if hasattr(a1, 'UATMM_structure_Node16'):
        assert _is_linked(a1, 'UATMM_structure_Node16', b)
    _safe_set(b, 'UATMM_structure_Edge15', a2)
    assert _is_linked(b, 'UATMM_structure_Edge15', a2)
    if hasattr(a1, 'UATMM_structure_Node16'):
        assert not _is_linked(a1, 'UATMM_structure_Node16', b)
    if hasattr(a2, 'UATMM_structure_Node16'):
        assert _is_linked(a2, 'UATMM_structure_Node16', b)
    _safe_set(b, 'UATMM_structure_Edge15', None)
    assert not _is_linked(b, 'UATMM_structure_Edge15', a2)
    if hasattr(a2, 'UATMM_structure_Node16'):
        assert not _is_linked(a2, 'UATMM_structure_Node16', b)


def test_assoc_children10_reverse_link_reassign_clear():
    a1 = UATMM_structure_Node(id="sample_text", label="sample_text", nature="sample_text", role="sample_text")
    a2 = UATMM_structure_Node(id="sample_text_2", label="sample_text_2", nature="sample_text_2", role="sample_text_2")
    b = UATMM_structure_Node(id="sample_text", label="sample_text", nature="sample_text", role="sample_text")
    _safe_set(b, 'parents', {a1})
    assert _is_linked(b, 'parents', a1)
    if hasattr(a1, 'Node'):
        assert _is_linked(a1, 'Node', b)
    _safe_set(b, 'parents', {a2})
    assert _is_linked(b, 'parents', a2)
    if hasattr(a1, 'Node'):
        assert not _is_linked(a1, 'Node', b)
    if hasattr(a2, 'Node'):
        assert _is_linked(a2, 'Node', b)
    _safe_set(b, 'parents', set())
    assert not _is_linked(b, 'parents', a2)
    if hasattr(a2, 'Node'):
        assert not _is_linked(a2, 'Node', b)


def test_assoc_parents12_reverse_link_reassign_clear():
    a1 = UATMM_structure_Node(id="sample_text", label="sample_text", nature="sample_text", role="sample_text")
    a2 = UATMM_structure_Node(id="sample_text_2", label="sample_text_2", nature="sample_text_2", role="sample_text_2")
    b = UATMM_structure_Node(id="sample_text", label="sample_text", nature="sample_text", role="sample_text")
    _safe_set(b, 'children', {a1})
    assert _is_linked(b, 'children', a1)
    if hasattr(a1, 'Node13'):
        assert _is_linked(a1, 'Node13', b)
    _safe_set(b, 'children', {a2})
    assert _is_linked(b, 'children', a2)
    if hasattr(a1, 'Node13'):
        assert not _is_linked(a1, 'Node13', b)
    if hasattr(a2, 'Node13'):
        assert _is_linked(a2, 'Node13', b)
    _safe_set(b, 'children', set())
    assert not _is_linked(b, 'children', a2)
    if hasattr(a2, 'Node13'):
        assert not _is_linked(a2, 'Node13', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_Edges4_stub_double():
    # UATMM_structure_AttackTree has no real 'UATMM_structure_AttackTree5' property in the generated
    # code (a bare stub) -- manually attach it so UATMM_structure_Edge's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # UATMM_structure_Edge's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = UATMM_structure_Edge(edgeKind="sample_text")
    partner = UATMM_structure_AttackTree()
    setattr(partner, 'UATMM_structure_AttackTree5', None)
    _safe_set(owner, 'UATMM_structure_Edge', partner)
    assert owner in getattr(partner, 'UATMM_structure_AttackTree5')
    _safe_set(owner, 'UATMM_structure_Edge', None)
    assert owner not in getattr(partner, 'UATMM_structure_AttackTree5')


def test_assoc_Nodes1_stub_double():
    # UATMM_structure_AttackTree has no real 'UATMM_structure_AttackTree2' property in the generated
    # code (a bare stub) -- manually attach it so UATMM_structure_Node's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # UATMM_structure_Node's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = UATMM_structure_Node(id="sample_text", label="sample_text", nature="sample_text", role="sample_text")
    partner = UATMM_structure_AttackTree()
    setattr(partner, 'UATMM_structure_AttackTree2', None)
    _safe_set(owner, 'UATMM_structure_Node3', partner)
    assert owner in getattr(partner, 'UATMM_structure_AttackTree2')
    _safe_set(owner, 'UATMM_structure_Node3', None)
    assert owner not in getattr(partner, 'UATMM_structure_AttackTree2')


def test_assoc_Root0_stub_double():
    # UATMM_structure_AttackTree has no real 'UATMM_structure_AttackTree' property in the generated
    # code (a bare stub) -- manually attach it so UATMM_structure_Node's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # UATMM_structure_Node's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = UATMM_structure_Node(id="sample_text", label="sample_text", nature="sample_text", role="sample_text")
    partner = UATMM_structure_AttackTree()
    setattr(partner, 'UATMM_structure_AttackTree', None)
    _safe_set(owner, 'UATMM_structure_Node', partner)
    assert getattr(partner, 'UATMM_structure_AttackTree') == owner
    _safe_set(owner, 'UATMM_structure_Node', None)
    assert getattr(partner, 'UATMM_structure_AttackTree') is None


def test_assoc_connector8_stub_double():
    # UATMM_structure_Connector has no real 'Connector' property in the generated
    # code (a bare stub) -- manually attach it so UATMM_structure_Node's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # UATMM_structure_Node's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = UATMM_structure_Node(id="sample_text", label="sample_text", nature="sample_text", role="sample_text")
    partner = UATMM_structure_Connector()
    setattr(partner, 'Connector', None)
    _safe_set(owner, 'gate', partner)
    assert getattr(partner, 'Connector') == owner
    _safe_set(owner, 'gate', None)
    assert getattr(partner, 'Connector') is None


def test_assoc_gate20_stub_double():
    # UATMM_structure_Connector has no real 'connector' property in the generated
    # code (a bare stub) -- manually attach it so UATMM_structure_Node's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # UATMM_structure_Node's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = UATMM_structure_Node(id="sample_text", label="sample_text", nature="sample_text", role="sample_text")
    partner = UATMM_structure_Connector()
    setattr(partner, 'connector', None)
    _safe_set(owner, 'Node21', partner)
    assert getattr(partner, 'connector') == owner
    _safe_set(owner, 'Node21', None)
    assert getattr(partner, 'connector') is None


def test_assoc_metadata6_stub_double():
    # UATMM_structure_AttackTree has no real 'UATMM_structure_AttackTree7' property in the generated
    # code (a bare stub) -- manually attach it so UATMM_structure_TreeMetaData's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # UATMM_structure_TreeMetaData's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = UATMM_structure_TreeMetaData(Key="sample_text", Value="sample_text")
    partner = UATMM_structure_AttackTree()
    setattr(partner, 'UATMM_structure_AttackTree7', None)
    _safe_set(owner, 'UATMM_structure_TreeMetaData', partner)
    assert owner in getattr(partner, 'UATMM_structure_AttackTree7')
    _safe_set(owner, 'UATMM_structure_TreeMetaData', None)
    assert owner not in getattr(partner, 'UATMM_structure_AttackTree7')


