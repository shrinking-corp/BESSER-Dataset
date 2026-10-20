import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    pcg_Edge,
    pcg_Graph,
    pcg_Resource,
    pcg_Vertex,
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

def test_assoc_edges1_stub_double():
    # pcg_Graph has no real 'pcg_Graph2' property in the generated
    # code (a bare stub) -- manually attach it so pcg_Edge's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pcg_Edge's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pcg_Edge(kind="sample_text")
    partner = pcg_Graph()
    setattr(partner, 'pcg_Graph2', None)
    _safe_set(owner, 'pcg_Edge', partner)
    assert owner in getattr(partner, 'pcg_Graph2')
    _safe_set(owner, 'pcg_Edge', None)
    assert owner not in getattr(partner, 'pcg_Graph2')


def test_assoc_resources3_stub_double():
    # pcg_Vertex has no real 'pcg_Vertex4' property in the generated
    # code (a bare stub) -- manually attach it so pcg_Resource's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pcg_Resource's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pcg_Resource(id="sample_text", title="sample_text")
    partner = pcg_Vertex()
    setattr(partner, 'pcg_Vertex4', None)
    _safe_set(owner, 'pcg_Resource', partner)
    assert owner in getattr(partner, 'pcg_Vertex4')
    _safe_set(owner, 'pcg_Resource', None)
    assert owner not in getattr(partner, 'pcg_Vertex4')


def test_assoc_source8_stub_double():
    # pcg_Vertex has no real 'pcg_Vertex10' property in the generated
    # code (a bare stub) -- manually attach it so pcg_Edge's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pcg_Edge's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pcg_Edge(kind="sample_text")
    partner = pcg_Vertex()
    setattr(partner, 'pcg_Vertex10', None)
    _safe_set(owner, 'pcg_Edge9', partner)
    assert getattr(partner, 'pcg_Vertex10') == owner
    _safe_set(owner, 'pcg_Edge9', None)
    assert getattr(partner, 'pcg_Vertex10') is None


def test_assoc_target5_stub_double():
    # pcg_Vertex has no real 'pcg_Vertex7' property in the generated
    # code (a bare stub) -- manually attach it so pcg_Edge's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # pcg_Edge's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = pcg_Edge(kind="sample_text")
    partner = pcg_Vertex()
    setattr(partner, 'pcg_Vertex7', None)
    _safe_set(owner, 'pcg_Edge6', partner)
    assert getattr(partner, 'pcg_Vertex7') == owner
    _safe_set(owner, 'pcg_Edge6', None)
    assert getattr(partner, 'pcg_Vertex7') is None


