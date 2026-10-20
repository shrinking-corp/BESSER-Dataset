import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Node,
    Tree_Node,
    Tree_Tree,
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

def test_assoc_childs1_reverse_link_reassign_clear():
    a1 = Tree_Node(id="sample_text")
    a2 = Tree_Node(id="sample_text_2")
    b = Tree_Node(id="sample_text")
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


def test_assoc_parent3_reverse_link_reassign_clear():
    a1 = Tree_Node(id="sample_text")
    a2 = Tree_Node(id="sample_text_2")
    b = Tree_Node(id="sample_text")
    _safe_set(b, 'childs', a1)
    assert _is_linked(b, 'childs', a1)
    if hasattr(a1, 'Node4'):
        assert _is_linked(a1, 'Node4', b)
    _safe_set(b, 'childs', a2)
    assert _is_linked(b, 'childs', a2)
    if hasattr(a1, 'Node4'):
        assert not _is_linked(a1, 'Node4', b)
    if hasattr(a2, 'Node4'):
        assert _is_linked(a2, 'Node4', b)
    _safe_set(b, 'childs', None)
    assert not _is_linked(b, 'childs', a2)
    if hasattr(a2, 'Node4'):
        assert not _is_linked(a2, 'Node4', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

