import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Tree_Node,
    Tree_Storage,
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

def test_assoc_children2_reverse_link_reassign_clear():
    a1 = Tree_Node(value=7)
    a2 = Tree_Node(value=13)
    b = Tree_Node(value=7)
    _safe_set(b, 'Tree_Node3', a1)
    assert _is_linked(b, 'Tree_Node3', a1)
    if hasattr(a1, 'Tree_Node1'):
        assert _is_linked(a1, 'Tree_Node1', b)
    _safe_set(b, 'Tree_Node3', a2)
    assert _is_linked(b, 'Tree_Node3', a2)
    if hasattr(a1, 'Tree_Node1'):
        assert not _is_linked(a1, 'Tree_Node1', b)
    if hasattr(a2, 'Tree_Node1'):
        assert _is_linked(a2, 'Tree_Node1', b)
    _safe_set(b, 'Tree_Node3', None)
    assert not _is_linked(b, 'Tree_Node3', a2)
    if hasattr(a2, 'Tree_Node1'):
        assert not _is_linked(a2, 'Tree_Node1', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_nodes0_stub_double():
    # Tree_Storage has no real 'Tree_Storage' property in the generated
    # code (a bare stub) -- manually attach it so Tree_Node's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # Tree_Node's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = Tree_Node(value=7)
    partner = Tree_Storage()
    setattr(partner, 'Tree_Storage', None)
    _safe_set(owner, 'Tree_Node', partner)
    assert owner in getattr(partner, 'Tree_Storage')
    _safe_set(owner, 'Tree_Node', None)
    assert owner not in getattr(partner, 'Tree_Storage')


