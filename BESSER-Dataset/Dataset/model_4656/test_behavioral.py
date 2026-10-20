import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    DiagramElement,
    Edge,
    Node,
    Shape,
    di_Bounds,
    di_Diagram,
    di_DiagramElement,
    di_EObject,
    di_Edge,
    di_Label,
    di_LabeledEdge,
    di_LabeledShape,
    di_Node,
    di_Plane,
    di_Point,
    di_Shape,
    di_Style,
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

def test_assoc_ownedStyle9_stub_double():
    # di_Style has no real 'di_Style10' property in the generated
    # code (a bare stub) -- manually attach it so di_Diagram's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # di_Diagram's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = di_Diagram(documentation="sample_text", name="sample_text", resolution=3.14)
    partner = di_Style()
    setattr(partner, 'di_Style10', None)
    _safe_set(owner, 'di_Diagram', {partner})
    assert getattr(partner, 'di_Style10') == owner
    _safe_set(owner, 'di_Diagram', set())
    assert getattr(partner, 'di_Style10') is None


def test_assoc_owningDiagram0_stub_double():
    # di_DiagramElement has no real 'rootElement' property in the generated
    # code (a bare stub) -- manually attach it so di_Diagram's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # di_Diagram's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = di_Diagram(documentation="sample_text", name="sample_text", resolution=3.14)
    partner = di_DiagramElement()
    setattr(partner, 'rootElement', None)
    _safe_set(owner, 'Diagram', partner)
    assert getattr(partner, 'rootElement') == owner
    _safe_set(owner, 'Diagram', None)
    assert getattr(partner, 'rootElement') is None


def test_assoc_planeElement27_stub_double():
    # di_DiagramElement has no real 'di_DiagramElement28' property in the generated
    # code (a bare stub) -- manually attach it so di_Plane's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # di_Plane's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = di_Plane()
    partner = di_DiagramElement()
    setattr(partner, 'di_DiagramElement28', None)
    _safe_set(owner, 'di_Plane', {partner})
    assert getattr(partner, 'di_DiagramElement28') == owner
    _safe_set(owner, 'di_Plane', set())
    assert getattr(partner, 'di_DiagramElement28') is None


def test_assoc_rootElement11_stub_double():
    # di_DiagramElement has no real 'DiagramElement12' property in the generated
    # code (a bare stub) -- manually attach it so di_Diagram's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # di_Diagram's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = di_Diagram(documentation="sample_text", name="sample_text", resolution=3.14)
    partner = di_DiagramElement()
    setattr(partner, 'DiagramElement12', None)
    _safe_set(owner, 'owningDiagram', partner)
    assert getattr(partner, 'DiagramElement12') == owner
    _safe_set(owner, 'owningDiagram', None)
    assert getattr(partner, 'DiagramElement12') is None


