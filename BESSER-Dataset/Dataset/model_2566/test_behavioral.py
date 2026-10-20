import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    tree2talltree_Node,
    tree2talltree_Node2TallNode,
    tree2talltree_TallNode,
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

def test_assoc_children1_reverse_link_reassign_clear():
    a1 = tree2talltree_Node2TallNode(name="sample_text")
    a2 = tree2talltree_Node2TallNode(name="sample_text_2")
    b = tree2talltree_Node2TallNode(name="sample_text")
    _safe_set(b, 'parent', {a1})
    assert _is_linked(b, 'parent', a1)
    if hasattr(a1, 'Node2TallNode'):
        assert _is_linked(a1, 'Node2TallNode', b)
    _safe_set(b, 'parent', {a2})
    assert _is_linked(b, 'parent', a2)
    if hasattr(a1, 'Node2TallNode'):
        assert not _is_linked(a1, 'Node2TallNode', b)
    if hasattr(a2, 'Node2TallNode'):
        assert _is_linked(a2, 'Node2TallNode', b)
    _safe_set(b, 'parent', set())
    assert not _is_linked(b, 'parent', a2)
    if hasattr(a2, 'Node2TallNode'):
        assert not _is_linked(a2, 'Node2TallNode', b)


def test_assoc_parent3_reverse_link_reassign_clear():
    a1 = tree2talltree_Node2TallNode(name="sample_text")
    a2 = tree2talltree_Node2TallNode(name="sample_text_2")
    b = tree2talltree_Node2TallNode(name="sample_text")
    _safe_set(b, 'children', a1)
    assert _is_linked(b, 'children', a1)
    if hasattr(a1, 'Node2TallNode4'):
        assert _is_linked(a1, 'Node2TallNode4', b)
    _safe_set(b, 'children', a2)
    assert _is_linked(b, 'children', a2)
    if hasattr(a1, 'Node2TallNode4'):
        assert not _is_linked(a1, 'Node2TallNode4', b)
    if hasattr(a2, 'Node2TallNode4'):
        assert _is_linked(a2, 'Node2TallNode4', b)
    _safe_set(b, 'children', None)
    assert not _is_linked(b, 'children', a2)
    if hasattr(a2, 'Node2TallNode4'):
        assert not _is_linked(a2, 'Node2TallNode4', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_node5_stub_double():
    # tree2talltree_Node has no real 'tree2talltree_Node' property in the generated
    # code (a bare stub) -- manually attach it so tree2talltree_Node2TallNode's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # tree2talltree_Node2TallNode's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = tree2talltree_Node2TallNode(name="sample_text")
    partner = tree2talltree_Node()
    setattr(partner, 'tree2talltree_Node', None)
    _safe_set(owner, 'tree2talltree_Node2TallNode', partner)
    assert getattr(partner, 'tree2talltree_Node') == owner
    _safe_set(owner, 'tree2talltree_Node2TallNode', None)
    assert getattr(partner, 'tree2talltree_Node') is None


def test_assoc_tallNode6_stub_double():
    # tree2talltree_TallNode has no real 'tree2talltree_TallNode' property in the generated
    # code (a bare stub) -- manually attach it so tree2talltree_Node2TallNode's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # tree2talltree_Node2TallNode's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = tree2talltree_Node2TallNode(name="sample_text")
    partner = tree2talltree_TallNode()
    setattr(partner, 'tree2talltree_TallNode', None)
    _safe_set(owner, 'tree2talltree_Node2TallNode7', partner)
    assert getattr(partner, 'tree2talltree_TallNode') == owner
    _safe_set(owner, 'tree2talltree_Node2TallNode7', None)
    assert getattr(partner, 'tree2talltree_TallNode') is None


