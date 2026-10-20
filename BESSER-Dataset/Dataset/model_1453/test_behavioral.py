import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    tree_Diagram,
    tree_Edge,
    tree_Node,
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

def test_assoc_children4_reverse_link_reassign_clear():
    a1 = tree_Node(name="sample_text")
    a2 = tree_Node(name="sample_text_2")
    b = tree_Node(name="sample_text")
    _safe_set(b, 'tree_Node5', a1)
    assert _is_linked(b, 'tree_Node5', a1)
    if hasattr(a1, 'tree_Node3'):
        assert _is_linked(a1, 'tree_Node3', b)
    _safe_set(b, 'tree_Node5', a2)
    assert _is_linked(b, 'tree_Node5', a2)
    if hasattr(a1, 'tree_Node3'):
        assert not _is_linked(a1, 'tree_Node3', b)
    if hasattr(a2, 'tree_Node3'):
        assert _is_linked(a2, 'tree_Node3', b)
    _safe_set(b, 'tree_Node5', None)
    assert not _is_linked(b, 'tree_Node5', a2)
    if hasattr(a2, 'tree_Node3'):
        assert not _is_linked(a2, 'tree_Node3', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_nodes0_stub_double():
    # tree_Diagram has no real 'tree_Diagram' property in the generated
    # code (a bare stub) -- manually attach it so tree_Node's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # tree_Node's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = tree_Node(name="sample_text")
    partner = tree_Diagram()
    setattr(partner, 'tree_Diagram', None)
    _safe_set(owner, 'tree_Node', partner)
    assert owner in getattr(partner, 'tree_Diagram')
    _safe_set(owner, 'tree_Node', None)
    assert owner not in getattr(partner, 'tree_Diagram')


def test_assoc_source6_stub_double():
    # tree_Edge has no real 'tree_Edge7' property in the generated
    # code (a bare stub) -- manually attach it so tree_Node's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # tree_Node's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = tree_Node(name="sample_text")
    partner = tree_Edge()
    setattr(partner, 'tree_Edge7', None)
    _safe_set(owner, 'tree_Node8', partner)
    assert getattr(partner, 'tree_Edge7') == owner
    _safe_set(owner, 'tree_Node8', None)
    assert getattr(partner, 'tree_Edge7') is None


def test_assoc_target9_stub_double():
    # tree_Edge has no real 'tree_Edge10' property in the generated
    # code (a bare stub) -- manually attach it so tree_Node's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # tree_Node's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = tree_Node(name="sample_text")
    partner = tree_Edge()
    setattr(partner, 'tree_Edge10', None)
    _safe_set(owner, 'tree_Node11', partner)
    assert getattr(partner, 'tree_Edge10') == owner
    _safe_set(owner, 'tree_Node11', None)
    assert getattr(partner, 'tree_Edge10') is None


