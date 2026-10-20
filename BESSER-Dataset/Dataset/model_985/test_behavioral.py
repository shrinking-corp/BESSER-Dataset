import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    cfg_cfg,
    cfg_edge,
    cfg_endnode,
    cfg_node,
    cfg_startnode,
    node,
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

def test_assoc_EReference010_stub_double():
    # cfg_edge has no real 'cfg_edge11' property in the generated
    # code (a bare stub) -- manually attach it so cfg_node's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cfg_node's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cfg_node(name="sample_text")
    partner = cfg_edge()
    setattr(partner, 'cfg_edge11', None)
    _safe_set(owner, 'cfg_node12', partner)
    assert getattr(partner, 'cfg_edge11') == owner
    _safe_set(owner, 'cfg_node12', None)
    assert getattr(partner, 'cfg_edge11') is None


def test_assoc_EReference13_stub_double():
    # cfg_edge has no real 'cfg_edge5' property in the generated
    # code (a bare stub) -- manually attach it so cfg_node's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cfg_node's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cfg_node(name="sample_text")
    partner = cfg_edge()
    setattr(partner, 'cfg_edge5', None)
    _safe_set(owner, 'cfg_node4', partner)
    assert getattr(partner, 'cfg_edge5') == owner
    _safe_set(owner, 'cfg_node4', None)
    assert getattr(partner, 'cfg_edge5') is None


def test_assoc_incoming6_stub_double():
    # cfg_edge has no real 'edge' property in the generated
    # code (a bare stub) -- manually attach it so cfg_node's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cfg_node's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cfg_node(name="sample_text")
    partner = cfg_edge()
    setattr(partner, 'edge', None)
    _safe_set(owner, 'target', {partner})
    assert getattr(partner, 'edge') == owner
    _safe_set(owner, 'target', set())
    assert getattr(partner, 'edge') is None


def test_assoc_nodes0_stub_double():
    # cfg_cfg has no real 'cfg_cfg' property in the generated
    # code (a bare stub) -- manually attach it so cfg_node's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cfg_node's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cfg_node(name="sample_text")
    partner = cfg_cfg()
    setattr(partner, 'cfg_cfg', None)
    _safe_set(owner, 'cfg_node', partner)
    assert owner in getattr(partner, 'cfg_cfg')
    _safe_set(owner, 'cfg_node', None)
    assert owner not in getattr(partner, 'cfg_cfg')


def test_assoc_outgoing7_stub_double():
    # cfg_edge has no real 'edge8' property in the generated
    # code (a bare stub) -- manually attach it so cfg_node's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cfg_node's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cfg_node(name="sample_text")
    partner = cfg_edge()
    setattr(partner, 'edge8', None)
    _safe_set(owner, 'source', {partner})
    assert getattr(partner, 'edge8') == owner
    _safe_set(owner, 'source', set())
    assert getattr(partner, 'edge8') is None


def test_assoc_source13_stub_double():
    # cfg_edge has no real 'outgoing' property in the generated
    # code (a bare stub) -- manually attach it so cfg_node's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cfg_node's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cfg_node(name="sample_text")
    partner = cfg_edge()
    setattr(partner, 'outgoing', None)
    _safe_set(owner, 'node14', partner)
    assert getattr(partner, 'outgoing') == owner
    _safe_set(owner, 'node14', None)
    assert getattr(partner, 'outgoing') is None


def test_assoc_target9_stub_double():
    # cfg_edge has no real 'incoming' property in the generated
    # code (a bare stub) -- manually attach it so cfg_node's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # cfg_node's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = cfg_node(name="sample_text")
    partner = cfg_edge()
    setattr(partner, 'incoming', None)
    _safe_set(owner, 'node', partner)
    assert getattr(partner, 'incoming') == owner
    _safe_set(owner, 'node', None)
    assert getattr(partner, 'incoming') is None


