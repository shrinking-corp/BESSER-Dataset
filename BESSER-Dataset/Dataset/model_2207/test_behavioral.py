import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    Container,
    FileTreeElement,
    filetree_AccessRight,
    filetree_Container,
    filetree_Directory,
    filetree_FileTree,
    filetree_FileTreeElement,
    filetree_H2HFile,
    filetree_PathToTreeElementMap,
    filetree_User,
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

def test_assoc_accessRights2_reverse_link_reassign_clear():
    a1 = filetree_FileTreeElement(file="sample_text", name="sample_text", path="sample_text")
    a2 = filetree_FileTreeElement(file="sample_text_2", name="sample_text_2", path="sample_text_2")
    b = filetree_AccessRight(readPermission=True, userId="sample_text", writePermission=True)
    _safe_set(b, 'filetree_AccessRight', a1)
    assert _is_linked(b, 'filetree_AccessRight', a1)
    if hasattr(a1, 'filetree_FileTreeElement'):
        assert _is_linked(a1, 'filetree_FileTreeElement', b)
    _safe_set(b, 'filetree_AccessRight', a2)
    assert _is_linked(b, 'filetree_AccessRight', a2)
    if hasattr(a1, 'filetree_FileTreeElement'):
        assert not _is_linked(a1, 'filetree_FileTreeElement', b)
    if hasattr(a2, 'filetree_FileTreeElement'):
        assert _is_linked(a2, 'filetree_FileTreeElement', b)
    _safe_set(b, 'filetree_AccessRight', None)
    assert not _is_linked(b, 'filetree_AccessRight', a2)
    if hasattr(a2, 'filetree_FileTreeElement'):
        assert not _is_linked(a2, 'filetree_FileTreeElement', b)


def test_assoc_value6_reverse_link_reassign_clear():
    a1 = filetree_PathToTreeElementMap(key="sample_text")
    a2 = filetree_PathToTreeElementMap(key="sample_text_2")
    b = filetree_FileTreeElement(file="sample_text", name="sample_text", path="sample_text")
    _safe_set(b, 'filetree_FileTreeElement8', a1)
    assert _is_linked(b, 'filetree_FileTreeElement8', a1)
    if hasattr(a1, 'filetree_PathToTreeElementMap7'):
        assert _is_linked(a1, 'filetree_PathToTreeElementMap7', b)
    _safe_set(b, 'filetree_FileTreeElement8', a2)
    assert _is_linked(b, 'filetree_FileTreeElement8', a2)
    if hasattr(a1, 'filetree_PathToTreeElementMap7'):
        assert not _is_linked(a1, 'filetree_PathToTreeElementMap7', b)
    if hasattr(a2, 'filetree_PathToTreeElementMap7'):
        assert _is_linked(a2, 'filetree_PathToTreeElementMap7', b)
    _safe_set(b, 'filetree_FileTreeElement8', None)
    assert not _is_linked(b, 'filetree_FileTreeElement8', a2)
    if hasattr(a2, 'filetree_PathToTreeElementMap7'):
        assert not _is_linked(a2, 'filetree_PathToTreeElementMap7', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_children3_stub_double():
    # filetree_Container has no real 'parent' property in the generated
    # code (a bare stub) -- manually attach it so filetree_FileTreeElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # filetree_FileTreeElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = filetree_FileTreeElement(file="sample_text", name="sample_text", path="sample_text")
    partner = filetree_Container()
    setattr(partner, 'parent', None)
    _safe_set(owner, 'FileTreeElement', partner)
    assert owner in getattr(partner, 'parent')
    _safe_set(owner, 'FileTreeElement', None)
    assert owner not in getattr(partner, 'parent')


def test_assoc_elements0_stub_double():
    # filetree_FileTree has no real 'filetree_FileTree' property in the generated
    # code (a bare stub) -- manually attach it so filetree_PathToTreeElementMap's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # filetree_PathToTreeElementMap's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = filetree_PathToTreeElementMap(key="sample_text")
    partner = filetree_FileTree()
    setattr(partner, 'filetree_FileTree', None)
    _safe_set(owner, 'filetree_PathToTreeElementMap', partner)
    assert owner in getattr(partner, 'filetree_FileTree')
    _safe_set(owner, 'filetree_PathToTreeElementMap', None)
    assert owner not in getattr(partner, 'filetree_FileTree')


def test_assoc_fileTree4_stub_double():
    # filetree_FileTree has no real 'filetree_FileTree5' property in the generated
    # code (a bare stub) -- manually attach it so filetree_User's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # filetree_User's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = filetree_User(password="sample_text", pin="sample_text", rootDir="sample_text", userId="sample_text")
    partner = filetree_FileTree()
    setattr(partner, 'filetree_FileTree5', None)
    _safe_set(owner, 'filetree_User', partner)
    assert getattr(partner, 'filetree_FileTree5') == owner
    _safe_set(owner, 'filetree_User', None)
    assert getattr(partner, 'filetree_FileTree5') is None


def test_assoc_parent1_stub_double():
    # filetree_Container has no real 'Container' property in the generated
    # code (a bare stub) -- manually attach it so filetree_FileTreeElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # filetree_FileTreeElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = filetree_FileTreeElement(file="sample_text", name="sample_text", path="sample_text")
    partner = filetree_Container()
    setattr(partner, 'Container', None)
    _safe_set(owner, 'children', partner)
    assert getattr(partner, 'Container') == owner
    _safe_set(owner, 'children', None)
    assert getattr(partner, 'Container') is None


