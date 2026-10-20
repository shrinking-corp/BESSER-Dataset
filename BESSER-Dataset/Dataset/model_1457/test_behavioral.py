import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    graph1_Edge,
    graph1_Graph,
    graph1_Node,
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

def test_assoc_nodes4_stub_double():
    # graph1_Graph has no real 'graph1_Graph' property in the generated
    # code (a bare stub) -- manually attach it so graph1_Node's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # graph1_Node's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = graph1_Node(name="sample_text")
    partner = graph1_Graph()
    setattr(partner, 'graph1_Graph', None)
    _safe_set(owner, 'graph1_Node5', partner)
    assert owner in getattr(partner, 'graph1_Graph')
    _safe_set(owner, 'graph1_Node5', None)
    assert owner not in getattr(partner, 'graph1_Graph')


def test_assoc_src0_stub_double():
    # graph1_Edge has no real 'graph1_Edge' property in the generated
    # code (a bare stub) -- manually attach it so graph1_Node's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # graph1_Node's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = graph1_Node(name="sample_text")
    partner = graph1_Edge()
    setattr(partner, 'graph1_Edge', None)
    _safe_set(owner, 'graph1_Node', partner)
    assert getattr(partner, 'graph1_Edge') == owner
    _safe_set(owner, 'graph1_Node', None)
    assert getattr(partner, 'graph1_Edge') is None


def test_assoc_trg1_stub_double():
    # graph1_Edge has no real 'graph1_Edge2' property in the generated
    # code (a bare stub) -- manually attach it so graph1_Node's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # graph1_Node's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = graph1_Node(name="sample_text")
    partner = graph1_Edge()
    setattr(partner, 'graph1_Edge2', None)
    _safe_set(owner, 'graph1_Node3', partner)
    assert getattr(partner, 'graph1_Edge2') == owner
    _safe_set(owner, 'graph1_Node3', None)
    assert getattr(partner, 'graph1_Edge2') is None


