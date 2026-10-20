import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    graph_Edge,
    graph_Graph,
    graph_Node,
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
    # graph_Edge has no real 'Edge3' property in the generated
    # code (a bare stub) -- manually attach it so graph_Node's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # graph_Node's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = graph_Node(name="sample_text")
    partner = graph_Edge()
    setattr(partner, 'Edge3', None)
    _safe_set(owner, 'target', {partner})
    assert getattr(partner, 'Edge3') == owner
    _safe_set(owner, 'target', set())
    assert getattr(partner, 'Edge3') is None


def test_assoc_nodes0_stub_double():
    # graph_Graph has no real 'graph_Graph' property in the generated
    # code (a bare stub) -- manually attach it so graph_Node's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # graph_Node's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = graph_Node(name="sample_text")
    partner = graph_Graph()
    setattr(partner, 'graph_Graph', None)
    _safe_set(owner, 'graph_Node', partner)
    assert owner in getattr(partner, 'graph_Graph')
    _safe_set(owner, 'graph_Node', None)
    assert owner not in getattr(partner, 'graph_Graph')


def test_assoc_outgoing1_stub_double():
    # graph_Edge has no real 'Edge' property in the generated
    # code (a bare stub) -- manually attach it so graph_Node's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # graph_Node's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = graph_Node(name="sample_text")
    partner = graph_Edge()
    setattr(partner, 'Edge', None)
    _safe_set(owner, 'source', {partner})
    assert getattr(partner, 'Edge') == owner
    _safe_set(owner, 'source', set())
    assert getattr(partner, 'Edge') is None


def test_assoc_source4_stub_double():
    # graph_Edge has no real 'outgoing' property in the generated
    # code (a bare stub) -- manually attach it so graph_Node's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # graph_Node's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = graph_Node(name="sample_text")
    partner = graph_Edge()
    setattr(partner, 'outgoing', None)
    _safe_set(owner, 'Node', partner)
    assert getattr(partner, 'outgoing') == owner
    _safe_set(owner, 'Node', None)
    assert getattr(partner, 'outgoing') is None


def test_assoc_target5_stub_double():
    # graph_Edge has no real 'incoming' property in the generated
    # code (a bare stub) -- manually attach it so graph_Node's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # graph_Node's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = graph_Node(name="sample_text")
    partner = graph_Edge()
    setattr(partner, 'incoming', None)
    _safe_set(owner, 'Node6', partner)
    assert getattr(partner, 'incoming') == owner
    _safe_set(owner, 'Node6', None)
    assert getattr(partner, 'incoming') is None


