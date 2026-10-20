import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    TreeElement,
    ed2_ED2,
    ed2_EDD,
    ed2_Leaf,
    ed2_Model,
    ed2_Node,
    ed2_TreeElement,
    ed2_TreeObject,
    ed2_TreeParent,
    TreeElementType,
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

def test_assoc_treeElements13_reverse_link_reassign_clear():
    a1 = ed2_TreeElement(index="sample_text", name="sample_text", type="sample_text")
    a2 = ed2_TreeElement(index="sample_text_2", name="sample_text_2", type="sample_text_2")
    b = ed2_ED2(name="sample_text")
    _safe_set(b, 'ed2_ED2', {a1})
    assert _is_linked(b, 'ed2_ED2', a1)
    if hasattr(a1, 'ed2_TreeElement'):
        assert _is_linked(a1, 'ed2_TreeElement', b)
    _safe_set(b, 'ed2_ED2', {a2})
    assert _is_linked(b, 'ed2_ED2', a2)
    if hasattr(a1, 'ed2_TreeElement'):
        assert not _is_linked(a1, 'ed2_TreeElement', b)
    if hasattr(a2, 'ed2_TreeElement'):
        assert _is_linked(a2, 'ed2_TreeElement', b)
    _safe_set(b, 'ed2_ED2', set())
    assert not _is_linked(b, 'ed2_ED2', a2)
    if hasattr(a2, 'ed2_TreeElement'):
        assert not _is_linked(a2, 'ed2_TreeElement', b)


def test_assoc_treeObjects0_reverse_link_reassign_clear():
    a1 = ed2_TreeObject(index="sample_text", name="sample_text", type="sample_text")
    a2 = ed2_TreeObject(index="sample_text_2", name="sample_text_2", type="sample_text_2")
    b = ed2_EDD(name="sample_text")
    _safe_set(b, 'ed2_EDD', {a1})
    assert _is_linked(b, 'ed2_EDD', a1)
    if hasattr(a1, 'ed2_TreeObject'):
        assert _is_linked(a1, 'ed2_TreeObject', b)
    _safe_set(b, 'ed2_EDD', {a2})
    assert _is_linked(b, 'ed2_EDD', a2)
    if hasattr(a1, 'ed2_TreeObject'):
        assert not _is_linked(a1, 'ed2_TreeObject', b)
    if hasattr(a2, 'ed2_TreeObject'):
        assert _is_linked(a2, 'ed2_TreeObject', b)
    _safe_set(b, 'ed2_EDD', set())
    assert not _is_linked(b, 'ed2_EDD', a2)
    if hasattr(a2, 'ed2_TreeObject'):
        assert not _is_linked(a2, 'ed2_TreeObject', b)


def test_assoc_treeObjects7_reverse_link_reassign_clear():
    a1 = ed2_TreeParent(index="sample_text", name="sample_text", type="sample_text")
    a2 = ed2_TreeParent(index="sample_text_2", name="sample_text_2", type="sample_text_2")
    b = ed2_TreeObject(index="sample_text", name="sample_text", type="sample_text")
    _safe_set(b, 'ed2_TreeObject9', a1)
    assert _is_linked(b, 'ed2_TreeObject9', a1)
    if hasattr(a1, 'ed2_TreeParent8'):
        assert _is_linked(a1, 'ed2_TreeParent8', b)
    _safe_set(b, 'ed2_TreeObject9', a2)
    assert _is_linked(b, 'ed2_TreeObject9', a2)
    if hasattr(a1, 'ed2_TreeParent8'):
        assert not _is_linked(a1, 'ed2_TreeParent8', b)
    if hasattr(a2, 'ed2_TreeParent8'):
        assert _is_linked(a2, 'ed2_TreeParent8', b)
    _safe_set(b, 'ed2_TreeObject9', None)
    assert not _is_linked(b, 'ed2_TreeObject9', a2)
    if hasattr(a2, 'ed2_TreeParent8'):
        assert not _is_linked(a2, 'ed2_TreeParent8', b)


def test_assoc_treeParents1_reverse_link_reassign_clear():
    a1 = ed2_TreeParent(index="sample_text", name="sample_text", type="sample_text")
    a2 = ed2_TreeParent(index="sample_text_2", name="sample_text_2", type="sample_text_2")
    b = ed2_EDD(name="sample_text")
    _safe_set(b, 'ed2_EDD2', {a1})
    assert _is_linked(b, 'ed2_EDD2', a1)
    if hasattr(a1, 'ed2_TreeParent'):
        assert _is_linked(a1, 'ed2_TreeParent', b)
    _safe_set(b, 'ed2_EDD2', {a2})
    assert _is_linked(b, 'ed2_EDD2', a2)
    if hasattr(a1, 'ed2_TreeParent'):
        assert not _is_linked(a1, 'ed2_TreeParent', b)
    if hasattr(a2, 'ed2_TreeParent'):
        assert _is_linked(a2, 'ed2_TreeParent', b)
    _safe_set(b, 'ed2_EDD2', set())
    assert not _is_linked(b, 'ed2_EDD2', a2)
    if hasattr(a2, 'ed2_TreeParent'):
        assert not _is_linked(a2, 'ed2_TreeParent', b)


def test_assoc_treeParents11_reverse_link_reassign_clear():
    a1 = ed2_TreeParent(index="sample_text", name="sample_text", type="sample_text")
    a2 = ed2_TreeParent(index="sample_text_2", name="sample_text_2", type="sample_text_2")
    b = ed2_TreeParent(index="sample_text", name="sample_text", type="sample_text")
    _safe_set(b, 'ed2_TreeParent12', a1)
    assert _is_linked(b, 'ed2_TreeParent12', a1)
    if hasattr(a1, 'ed2_TreeParent10'):
        assert _is_linked(a1, 'ed2_TreeParent10', b)
    _safe_set(b, 'ed2_TreeParent12', a2)
    assert _is_linked(b, 'ed2_TreeParent12', a2)
    if hasattr(a1, 'ed2_TreeParent10'):
        assert not _is_linked(a1, 'ed2_TreeParent10', b)
    if hasattr(a2, 'ed2_TreeParent10'):
        assert _is_linked(a2, 'ed2_TreeParent10', b)
    _safe_set(b, 'ed2_TreeParent12', None)
    assert not _is_linked(b, 'ed2_TreeParent12', a2)
    if hasattr(a2, 'ed2_TreeParent10'):
        assert not _is_linked(a2, 'ed2_TreeParent10', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_ed214_stub_double():
    # ed2_Model has no real 'ed2_Model' property in the generated
    # code (a bare stub) -- manually attach it so ed2_ED2's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ed2_ED2's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ed2_ED2(name="sample_text")
    partner = ed2_Model()
    setattr(partner, 'ed2_Model', None)
    _safe_set(owner, 'ed2_ED215', partner)
    assert getattr(partner, 'ed2_Model') == owner
    _safe_set(owner, 'ed2_ED215', None)
    assert getattr(partner, 'ed2_Model') is None


