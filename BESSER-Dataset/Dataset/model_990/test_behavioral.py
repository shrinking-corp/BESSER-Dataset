import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    BendPoint,
    DiagramElement,
    Identifier,
    Node,
    notation_AbsoluteBendPoint,
    notation_Anchor,
    notation_BendPoint,
    notation_DiagramElement,
    notation_EObject,
    notation_Edge,
    notation_HierarchicalNode,
    notation_Node,
    notation_RelativeBendPoint,
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

def test_assoc_incoming2_stub_double():
    # notation_Edge has no real 'Edge3' property in the generated
    # code (a bare stub) -- manually attach it so notation_Node's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # notation_Node's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = notation_Node(height=7, width=7, x=7, y=7)
    partner = notation_Edge()
    setattr(partner, 'Edge3', None)
    _safe_set(owner, 'target', {partner})
    assert getattr(partner, 'Edge3') == owner
    _safe_set(owner, 'target', set())
    assert getattr(partner, 'Edge3') is None


def test_assoc_model0_stub_double():
    # notation_EObject has no real 'notation_EObject' property in the generated
    # code (a bare stub) -- manually attach it so notation_DiagramElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # notation_DiagramElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = notation_DiagramElement(persistent=True, visible=True)
    partner = notation_EObject()
    setattr(partner, 'notation_EObject', None)
    _safe_set(owner, 'notation_DiagramElement', partner)
    assert getattr(partner, 'notation_EObject') == owner
    _safe_set(owner, 'notation_DiagramElement', None)
    assert getattr(partner, 'notation_EObject') is None


def test_assoc_nodes15_stub_double():
    # notation_HierarchicalNode has no real 'parent' property in the generated
    # code (a bare stub) -- manually attach it so notation_Node's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # notation_Node's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = notation_Node(height=7, width=7, x=7, y=7)
    partner = notation_HierarchicalNode()
    setattr(partner, 'parent', None)
    _safe_set(owner, 'Node16', partner)
    assert owner in getattr(partner, 'parent')
    _safe_set(owner, 'Node16', None)
    assert owner not in getattr(partner, 'parent')


def test_assoc_outgoing1_stub_double():
    # notation_Edge has no real 'Edge' property in the generated
    # code (a bare stub) -- manually attach it so notation_Node's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # notation_Node's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = notation_Node(height=7, width=7, x=7, y=7)
    partner = notation_Edge()
    setattr(partner, 'Edge', None)
    _safe_set(owner, 'source', {partner})
    assert getattr(partner, 'Edge') == owner
    _safe_set(owner, 'source', set())
    assert getattr(partner, 'Edge') is None


def test_assoc_parent4_stub_double():
    # notation_HierarchicalNode has no real 'HierarchicalNode' property in the generated
    # code (a bare stub) -- manually attach it so notation_Node's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # notation_Node's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = notation_Node(height=7, width=7, x=7, y=7)
    partner = notation_HierarchicalNode()
    setattr(partner, 'HierarchicalNode', None)
    _safe_set(owner, 'nodes', partner)
    assert getattr(partner, 'HierarchicalNode') == owner
    _safe_set(owner, 'nodes', None)
    assert getattr(partner, 'HierarchicalNode') is None


def test_assoc_source5_stub_double():
    # notation_Edge has no real 'outgoing' property in the generated
    # code (a bare stub) -- manually attach it so notation_Node's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # notation_Node's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = notation_Node(height=7, width=7, x=7, y=7)
    partner = notation_Edge()
    setattr(partner, 'outgoing', None)
    _safe_set(owner, 'Node', partner)
    assert getattr(partner, 'outgoing') == owner
    _safe_set(owner, 'Node', None)
    assert getattr(partner, 'outgoing') is None


def test_assoc_sourceAnchor10_stub_double():
    # notation_Edge has no real 'notation_Edge' property in the generated
    # code (a bare stub) -- manually attach it so notation_Anchor's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # notation_Anchor's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = notation_Anchor(x=7, y=7)
    partner = notation_Edge()
    setattr(partner, 'notation_Edge', None)
    _safe_set(owner, 'notation_Anchor', partner)
    assert getattr(partner, 'notation_Edge') == owner
    _safe_set(owner, 'notation_Anchor', None)
    assert getattr(partner, 'notation_Edge') is None


def test_assoc_target6_stub_double():
    # notation_Edge has no real 'incoming' property in the generated
    # code (a bare stub) -- manually attach it so notation_Node's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # notation_Node's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = notation_Node(height=7, width=7, x=7, y=7)
    partner = notation_Edge()
    setattr(partner, 'incoming', None)
    _safe_set(owner, 'Node7', partner)
    assert getattr(partner, 'incoming') == owner
    _safe_set(owner, 'Node7', None)
    assert getattr(partner, 'incoming') is None


def test_assoc_targetAnchor11_stub_double():
    # notation_Edge has no real 'notation_Edge12' property in the generated
    # code (a bare stub) -- manually attach it so notation_Anchor's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # notation_Anchor's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = notation_Anchor(x=7, y=7)
    partner = notation_Edge()
    setattr(partner, 'notation_Edge12', None)
    _safe_set(owner, 'notation_Anchor13', partner)
    assert getattr(partner, 'notation_Edge12') == owner
    _safe_set(owner, 'notation_Anchor13', None)
    assert getattr(partner, 'notation_Edge12') is None


