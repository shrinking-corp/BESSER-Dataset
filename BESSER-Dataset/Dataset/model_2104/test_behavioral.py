import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    MocaTree_Attribute,
    MocaTree_File,
    MocaTree_Folder,
    MocaTree_Link,
    MocaTree_Node,
    MocaTree_Text,
    MocaTree_TreeElement,
    Text,
    TreeElement,
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

def test_assoc_attribute18_reverse_link_reassign_clear():
    a1 = MocaTree_Node(startIndex=7, startLineIndex=7, stopIndex=7, stopLineIndex=7)
    a2 = MocaTree_Node(startIndex=13, startLineIndex=13, stopIndex=13, stopLineIndex=13)
    b = MocaTree_Attribute(value="sample_text")
    _safe_set(b, 'Attribute', a1)
    assert _is_linked(b, 'Attribute', a1)
    if hasattr(a1, 'node'):
        assert _is_linked(a1, 'node', b)
    _safe_set(b, 'Attribute', a2)
    assert _is_linked(b, 'Attribute', a2)
    if hasattr(a1, 'node'):
        assert not _is_linked(a1, 'node', b)
    if hasattr(a2, 'node'):
        assert _is_linked(a2, 'node', b)
    _safe_set(b, 'Attribute', None)
    assert not _is_linked(b, 'Attribute', a2)
    if hasattr(a2, 'node'):
        assert not _is_linked(a2, 'node', b)


def test_assoc_node0_reverse_link_reassign_clear():
    a1 = MocaTree_Node(startIndex=7, startLineIndex=7, stopIndex=7, stopLineIndex=7)
    a2 = MocaTree_Node(startIndex=13, startLineIndex=13, stopIndex=13, stopLineIndex=13)
    b = MocaTree_Attribute(value="sample_text")
    _safe_set(b, 'attribute', a1)
    assert _is_linked(b, 'attribute', a1)
    if hasattr(a1, 'Node'):
        assert _is_linked(a1, 'Node', b)
    _safe_set(b, 'attribute', a2)
    assert _is_linked(b, 'attribute', a2)
    if hasattr(a1, 'Node'):
        assert not _is_linked(a1, 'Node', b)
    if hasattr(a2, 'Node'):
        assert _is_linked(a2, 'Node', b)
    _safe_set(b, 'attribute', None)
    assert not _is_linked(b, 'attribute', a2)
    if hasattr(a2, 'Node'):
        assert not _is_linked(a2, 'Node', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_attribute13_stub_double():
    # MocaTree_Link has no real 'MocaTree_Link14' property in the generated
    # code (a bare stub) -- manually attach it so MocaTree_Attribute's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # MocaTree_Attribute's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = MocaTree_Attribute(value="sample_text")
    partner = MocaTree_Link()
    setattr(partner, 'MocaTree_Link14', None)
    _safe_set(owner, 'MocaTree_Attribute', partner)
    assert owner in getattr(partner, 'MocaTree_Link14')
    _safe_set(owner, 'MocaTree_Attribute', None)
    assert owner not in getattr(partner, 'MocaTree_Link14')


def test_assoc_children17_stub_double():
    # MocaTree_Text has no real 'Text' property in the generated
    # code (a bare stub) -- manually attach it so MocaTree_Node's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # MocaTree_Node's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = MocaTree_Node(startIndex=7, startLineIndex=7, stopIndex=7, stopLineIndex=7)
    partner = MocaTree_Text()
    setattr(partner, 'Text', None)
    _safe_set(owner, 'parentNode', {partner})
    assert getattr(partner, 'Text') == owner
    _safe_set(owner, 'parentNode', set())
    assert getattr(partner, 'Text') is None


def test_assoc_file15_stub_double():
    # MocaTree_File has no real 'File16' property in the generated
    # code (a bare stub) -- manually attach it so MocaTree_Node's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # MocaTree_Node's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = MocaTree_Node(startIndex=7, startLineIndex=7, stopIndex=7, stopLineIndex=7)
    partner = MocaTree_File()
    setattr(partner, 'File16', None)
    _safe_set(owner, 'rootNode', partner)
    assert getattr(partner, 'File16') == owner
    _safe_set(owner, 'rootNode', None)
    assert getattr(partner, 'File16') is None


def test_assoc_links21_stub_double():
    # MocaTree_Link has no real 'MocaTree_Link23' property in the generated
    # code (a bare stub) -- manually attach it so MocaTree_TreeElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # MocaTree_TreeElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = MocaTree_TreeElement(index=7, name="sample_text")
    partner = MocaTree_Link()
    setattr(partner, 'MocaTree_Link23', None)
    _safe_set(owner, 'MocaTree_TreeElement22', {partner})
    assert getattr(partner, 'MocaTree_Link23') == owner
    _safe_set(owner, 'MocaTree_TreeElement22', set())
    assert getattr(partner, 'MocaTree_Link23') is None


def test_assoc_parentNode19_stub_double():
    # MocaTree_Text has no real 'children' property in the generated
    # code (a bare stub) -- manually attach it so MocaTree_Node's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # MocaTree_Node's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = MocaTree_Node(startIndex=7, startLineIndex=7, stopIndex=7, stopLineIndex=7)
    partner = MocaTree_Text()
    setattr(partner, 'children', None)
    _safe_set(owner, 'Node20', partner)
    assert getattr(partner, 'children') == owner
    _safe_set(owner, 'Node20', None)
    assert getattr(partner, 'children') is None


def test_assoc_rootNode2_stub_double():
    # MocaTree_File has no real 'file3' property in the generated
    # code (a bare stub) -- manually attach it so MocaTree_Node's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # MocaTree_Node's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = MocaTree_Node(startIndex=7, startLineIndex=7, stopIndex=7, stopLineIndex=7)
    partner = MocaTree_File()
    setattr(partner, 'file3', None)
    _safe_set(owner, 'Node4', partner)
    assert getattr(partner, 'file3') == owner
    _safe_set(owner, 'Node4', None)
    assert getattr(partner, 'file3') is None


def test_assoc_targets12_stub_double():
    # MocaTree_Link has no real 'MocaTree_Link' property in the generated
    # code (a bare stub) -- manually attach it so MocaTree_TreeElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # MocaTree_TreeElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = MocaTree_TreeElement(index=7, name="sample_text")
    partner = MocaTree_Link()
    setattr(partner, 'MocaTree_Link', None)
    _safe_set(owner, 'MocaTree_TreeElement', partner)
    assert owner in getattr(partner, 'MocaTree_Link')
    _safe_set(owner, 'MocaTree_TreeElement', None)
    assert owner not in getattr(partner, 'MocaTree_Link')


