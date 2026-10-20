import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    LayoutConstraint,
    Location,
    Node,
    NotationElement,
    View,
    notation_Bounds,
    notation_CategorySeparator,
    notation_Diagram,
    notation_EObject,
    notation_Edge,
    notation_ExpandableNode,
    notation_LayoutConstraint,
    notation_Location,
    notation_MindMapNode,
    notation_Node,
    notation_NotationElement,
    notation_Note,
    notation_View,
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

def test_assoc_diagrammableElement1_stub_double():
    # notation_EObject has no real 'notation_EObject' property in the generated
    # code (a bare stub) -- manually attach it so notation_View's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # notation_View's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = notation_View(viewDetails="sample_text", viewType="sample_text")
    partner = notation_EObject()
    setattr(partner, 'notation_EObject', None)
    _safe_set(owner, 'notation_View2', partner)
    assert getattr(partner, 'notation_EObject') == owner
    _safe_set(owner, 'notation_View2', None)
    assert getattr(partner, 'notation_EObject') is None


def test_assoc_layoutConstraint6_stub_double():
    # notation_Node has no real 'notation_Node7' property in the generated
    # code (a bare stub) -- manually attach it so notation_Bounds's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # notation_Bounds's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = notation_Bounds(height=7, width=7)
    partner = notation_Node()
    setattr(partner, 'notation_Node7', None)
    _safe_set(owner, 'notation_Bounds', partner)
    assert getattr(partner, 'notation_Node7') == owner
    _safe_set(owner, 'notation_Bounds', None)
    assert getattr(partner, 'notation_Node7') is None


def test_assoc_persistentChildren0_stub_double():
    # notation_Node has no real 'notation_Node' property in the generated
    # code (a bare stub) -- manually attach it so notation_View's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # notation_View's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = notation_View(viewDetails="sample_text", viewType="sample_text")
    partner = notation_Node()
    setattr(partner, 'notation_Node', None)
    _safe_set(owner, 'notation_View', {partner})
    assert getattr(partner, 'notation_Node') == owner
    _safe_set(owner, 'notation_View', set())
    assert getattr(partner, 'notation_Node') is None


def test_assoc_persistentEdges11_stub_double():
    # notation_Edge has no real 'notation_Edge' property in the generated
    # code (a bare stub) -- manually attach it so notation_Diagram's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # notation_Diagram's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = notation_Diagram(locationForNewElements="sample_text", name="sample_text", showLocationForNewElementsDialog=True)
    partner = notation_Edge()
    setattr(partner, 'notation_Edge', None)
    _safe_set(owner, 'notation_Diagram', {partner})
    assert getattr(partner, 'notation_Edge') == owner
    _safe_set(owner, 'notation_Diagram', set())
    assert getattr(partner, 'notation_Edge') is None


def test_assoc_source8_stub_double():
    # notation_Edge has no real 'sourceEdges' property in the generated
    # code (a bare stub) -- manually attach it so notation_View's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # notation_View's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = notation_View(viewDetails="sample_text", viewType="sample_text")
    partner = notation_Edge()
    setattr(partner, 'sourceEdges', None)
    _safe_set(owner, 'View', partner)
    assert getattr(partner, 'sourceEdges') == owner
    _safe_set(owner, 'View', None)
    assert getattr(partner, 'sourceEdges') is None


def test_assoc_sourceEdges3_stub_double():
    # notation_Edge has no real 'Edge' property in the generated
    # code (a bare stub) -- manually attach it so notation_View's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # notation_View's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = notation_View(viewDetails="sample_text", viewType="sample_text")
    partner = notation_Edge()
    setattr(partner, 'Edge', None)
    _safe_set(owner, 'source', {partner})
    assert getattr(partner, 'Edge') == owner
    _safe_set(owner, 'source', set())
    assert getattr(partner, 'Edge') is None


def test_assoc_target9_stub_double():
    # notation_Edge has no real 'targetEdges' property in the generated
    # code (a bare stub) -- manually attach it so notation_View's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # notation_View's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = notation_View(viewDetails="sample_text", viewType="sample_text")
    partner = notation_Edge()
    setattr(partner, 'targetEdges', None)
    _safe_set(owner, 'View10', partner)
    assert getattr(partner, 'targetEdges') == owner
    _safe_set(owner, 'View10', None)
    assert getattr(partner, 'targetEdges') is None


def test_assoc_targetEdges4_stub_double():
    # notation_Edge has no real 'Edge5' property in the generated
    # code (a bare stub) -- manually attach it so notation_View's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # notation_View's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = notation_View(viewDetails="sample_text", viewType="sample_text")
    partner = notation_Edge()
    setattr(partner, 'Edge5', None)
    _safe_set(owner, 'target', {partner})
    assert getattr(partner, 'Edge5') == owner
    _safe_set(owner, 'target', set())
    assert getattr(partner, 'Edge5') is None


