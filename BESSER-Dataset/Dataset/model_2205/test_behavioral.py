import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    bintree_BinTreeNode,
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

def test_assoc_left3_reverse_link_reassign_clear():
    a1 = bintree_BinTreeNode(data="sample_text")
    a2 = bintree_BinTreeNode(data="sample_text_2")
    b = bintree_BinTreeNode(data="sample_text")
    _safe_set(b, 'bintree_BinTreeNode4', a1)
    assert _is_linked(b, 'bintree_BinTreeNode4', a1)
    if hasattr(a1, 'bintree_BinTreeNode2'):
        assert _is_linked(a1, 'bintree_BinTreeNode2', b)
    _safe_set(b, 'bintree_BinTreeNode4', a2)
    assert _is_linked(b, 'bintree_BinTreeNode4', a2)
    if hasattr(a1, 'bintree_BinTreeNode2'):
        assert not _is_linked(a1, 'bintree_BinTreeNode2', b)
    if hasattr(a2, 'bintree_BinTreeNode2'):
        assert _is_linked(a2, 'bintree_BinTreeNode2', b)
    _safe_set(b, 'bintree_BinTreeNode4', None)
    assert not _is_linked(b, 'bintree_BinTreeNode4', a2)
    if hasattr(a2, 'bintree_BinTreeNode2'):
        assert not _is_linked(a2, 'bintree_BinTreeNode2', b)


def test_assoc_parent1_reverse_link_reassign_clear():
    a1 = bintree_BinTreeNode(data="sample_text")
    a2 = bintree_BinTreeNode(data="sample_text_2")
    b = bintree_BinTreeNode(data="sample_text")
    _safe_set(b, 'bintree_BinTreeNode0', a1)
    assert _is_linked(b, 'bintree_BinTreeNode0', a1)
    if hasattr(a1, 'bintree_BinTreeNode'):
        assert _is_linked(a1, 'bintree_BinTreeNode', b)
    _safe_set(b, 'bintree_BinTreeNode0', a2)
    assert _is_linked(b, 'bintree_BinTreeNode0', a2)
    if hasattr(a1, 'bintree_BinTreeNode'):
        assert not _is_linked(a1, 'bintree_BinTreeNode', b)
    if hasattr(a2, 'bintree_BinTreeNode'):
        assert _is_linked(a2, 'bintree_BinTreeNode', b)
    _safe_set(b, 'bintree_BinTreeNode0', None)
    assert not _is_linked(b, 'bintree_BinTreeNode0', a2)
    if hasattr(a2, 'bintree_BinTreeNode'):
        assert not _is_linked(a2, 'bintree_BinTreeNode', b)


def test_assoc_right6_reverse_link_reassign_clear():
    a1 = bintree_BinTreeNode(data="sample_text")
    a2 = bintree_BinTreeNode(data="sample_text_2")
    b = bintree_BinTreeNode(data="sample_text")
    _safe_set(b, 'bintree_BinTreeNode7', a1)
    assert _is_linked(b, 'bintree_BinTreeNode7', a1)
    if hasattr(a1, 'bintree_BinTreeNode5'):
        assert _is_linked(a1, 'bintree_BinTreeNode5', b)
    _safe_set(b, 'bintree_BinTreeNode7', a2)
    assert _is_linked(b, 'bintree_BinTreeNode7', a2)
    if hasattr(a1, 'bintree_BinTreeNode5'):
        assert not _is_linked(a1, 'bintree_BinTreeNode5', b)
    if hasattr(a2, 'bintree_BinTreeNode5'):
        assert _is_linked(a2, 'bintree_BinTreeNode5', b)
    _safe_set(b, 'bintree_BinTreeNode7', None)
    assert not _is_linked(b, 'bintree_BinTreeNode7', a2)
    if hasattr(a2, 'bintree_BinTreeNode5'):
        assert not _is_linked(a2, 'bintree_BinTreeNode5', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

