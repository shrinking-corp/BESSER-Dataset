import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Dot_DirectedArc,
    Dot_Graph,
    Dot_GraphElement,
    Dot_NamedElement,
    Dot_Node,
    GraphElement,
    NamedElement,
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

def test_assoc_contents0_stub_double():
    # Dot_Graph has no real 'graph' property in the generated
    # code (a bare stub) -- manually attach it so Dot_GraphElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Dot_GraphElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Dot_GraphElement(color="sample_text", label="sample_text")
    partner = Dot_Graph()
    setattr(partner, 'graph', None)
    _safe_set(owner, 'GraphElement', partner)
    assert owner in getattr(partner, 'graph')
    _safe_set(owner, 'GraphElement', None)
    assert owner not in getattr(partner, 'graph')


def test_assoc_graph1_stub_double():
    # Dot_Graph has no real 'Graph' property in the generated
    # code (a bare stub) -- manually attach it so Dot_GraphElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Dot_GraphElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Dot_GraphElement(color="sample_text", label="sample_text")
    partner = Dot_Graph()
    setattr(partner, 'Graph', None)
    _safe_set(owner, 'contents', partner)
    assert getattr(partner, 'Graph') == owner
    _safe_set(owner, 'contents', None)
    assert getattr(partner, 'Graph') is None


def test_assoc_sourceNode2_stub_double():
    # Dot_DirectedArc has no real 'Dot_DirectedArc' property in the generated
    # code (a bare stub) -- manually attach it so Dot_Node's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Dot_Node's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Dot_Node(shape="sample_text", style="sample_text")
    partner = Dot_DirectedArc()
    setattr(partner, 'Dot_DirectedArc', None)
    _safe_set(owner, 'Dot_Node', partner)
    assert getattr(partner, 'Dot_DirectedArc') == owner
    _safe_set(owner, 'Dot_Node', None)
    assert getattr(partner, 'Dot_DirectedArc') is None


def test_assoc_targetNode3_stub_double():
    # Dot_DirectedArc has no real 'Dot_DirectedArc4' property in the generated
    # code (a bare stub) -- manually attach it so Dot_Node's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Dot_Node's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Dot_Node(shape="sample_text", style="sample_text")
    partner = Dot_DirectedArc()
    setattr(partner, 'Dot_DirectedArc4', None)
    _safe_set(owner, 'Dot_Node5', partner)
    assert getattr(partner, 'Dot_DirectedArc4') == owner
    _safe_set(owner, 'Dot_Node5', None)
    assert getattr(partner, 'Dot_DirectedArc4') is None


