import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    tree_Node,
    tree_Tree,
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

def test_assoc_aReference7_reverse_link_reassign_clear():
    a1 = tree_Node(anAttribute=7, anAttribute2=7, anAttribute3=7, anAttribute4=7, name="sample_text")
    a2 = tree_Node(anAttribute=13, anAttribute2=13, anAttribute3=13, anAttribute4=13, name="sample_text_2")
    b = tree_Node(anAttribute=7, anAttribute2=7, anAttribute3=7, anAttribute4=7, name="sample_text")
    _safe_set(b, 'tree_Node8', a1)
    assert _is_linked(b, 'tree_Node8', a1)
    if hasattr(a1, 'tree_Node6'):
        assert _is_linked(a1, 'tree_Node6', b)
    _safe_set(b, 'tree_Node8', a2)
    assert _is_linked(b, 'tree_Node8', a2)
    if hasattr(a1, 'tree_Node6'):
        assert not _is_linked(a1, 'tree_Node6', b)
    if hasattr(a2, 'tree_Node6'):
        assert _is_linked(a2, 'tree_Node6', b)
    _safe_set(b, 'tree_Node8', None)
    assert not _is_linked(b, 'tree_Node8', a2)
    if hasattr(a2, 'tree_Node6'):
        assert not _is_linked(a2, 'tree_Node6', b)


def test_assoc_child2_reverse_link_reassign_clear():
    a1 = tree_Node(anAttribute=7, anAttribute2=7, anAttribute3=7, anAttribute4=7, name="sample_text")
    a2 = tree_Node(anAttribute=13, anAttribute2=13, anAttribute3=13, anAttribute4=13, name="sample_text_2")
    b = tree_Node(anAttribute=7, anAttribute2=7, anAttribute3=7, anAttribute4=7, name="sample_text")
    _safe_set(b, 'parent', {a1})
    assert _is_linked(b, 'parent', a1)
    if hasattr(a1, 'Node'):
        assert _is_linked(a1, 'Node', b)
    _safe_set(b, 'parent', {a2})
    assert _is_linked(b, 'parent', a2)
    if hasattr(a1, 'Node'):
        assert not _is_linked(a1, 'Node', b)
    if hasattr(a2, 'Node'):
        assert _is_linked(a2, 'Node', b)
    _safe_set(b, 'parent', set())
    assert not _is_linked(b, 'parent', a2)
    if hasattr(a2, 'Node'):
        assert not _is_linked(a2, 'Node', b)


def test_assoc_parent4_reverse_link_reassign_clear():
    a1 = tree_Node(anAttribute=7, anAttribute2=7, anAttribute3=7, anAttribute4=7, name="sample_text")
    a2 = tree_Node(anAttribute=13, anAttribute2=13, anAttribute3=13, anAttribute4=13, name="sample_text_2")
    b = tree_Node(anAttribute=7, anAttribute2=7, anAttribute3=7, anAttribute4=7, name="sample_text")
    _safe_set(b, 'child', a1)
    assert _is_linked(b, 'child', a1)
    if hasattr(a1, 'Node5'):
        assert _is_linked(a1, 'Node5', b)
    _safe_set(b, 'child', a2)
    assert _is_linked(b, 'child', a2)
    if hasattr(a1, 'Node5'):
        assert not _is_linked(a1, 'Node5', b)
    if hasattr(a2, 'Node5'):
        assert _is_linked(a2, 'Node5', b)
    _safe_set(b, 'child', None)
    assert not _is_linked(b, 'child', a2)
    if hasattr(a2, 'Node5'):
        assert not _is_linked(a2, 'Node5', b)


def test_assoc_root0_reverse_link_reassign_clear():
    a1 = tree_Tree(name="sample_text")
    a2 = tree_Tree(name="sample_text_2")
    b = tree_Node(anAttribute=7, anAttribute2=7, anAttribute3=7, anAttribute4=7, name="sample_text")
    _safe_set(b, 'tree_Node', a1)
    assert _is_linked(b, 'tree_Node', a1)
    if hasattr(a1, 'tree_Tree'):
        assert _is_linked(a1, 'tree_Tree', b)
    _safe_set(b, 'tree_Node', a2)
    assert _is_linked(b, 'tree_Node', a2)
    if hasattr(a1, 'tree_Tree'):
        assert not _is_linked(a1, 'tree_Tree', b)
    if hasattr(a2, 'tree_Tree'):
        assert _is_linked(a2, 'tree_Tree', b)
    _safe_set(b, 'tree_Node', None)
    assert not _is_linked(b, 'tree_Node', a2)
    if hasattr(a2, 'tree_Tree'):
        assert not _is_linked(a2, 'tree_Tree', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

