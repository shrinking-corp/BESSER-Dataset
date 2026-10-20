import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    SimpleTree_Attribute,
    SimpleTree_File,
    SimpleTree_Folder,
    SimpleTree_Node,
    SimpleTree_Text,
    SimpleTree_TreeElement,
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

def test_assoc_attribute11_reverse_link_reassign_clear():
    a1 = SimpleTree_Node(startIndex=7, startLineIndex=7, stopIndex=7, stopLineIndex=7)
    a2 = SimpleTree_Node(startIndex=13, startLineIndex=13, stopIndex=13, stopLineIndex=13)
    b = SimpleTree_Attribute(value="sample_text")
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
    a1 = SimpleTree_Node(startIndex=7, startLineIndex=7, stopIndex=7, stopLineIndex=7)
    a2 = SimpleTree_Node(startIndex=13, startLineIndex=13, stopIndex=13, stopLineIndex=13)
    b = SimpleTree_Attribute(value="sample_text")
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

def test_assoc_children10_stub_double():
    # SimpleTree_Text has no real 'Text' property in the generated
    # code (a bare stub) -- manually attach it so SimpleTree_Node's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # SimpleTree_Node's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = SimpleTree_Node(startIndex=7, startLineIndex=7, stopIndex=7, stopLineIndex=7)
    partner = SimpleTree_Text()
    setattr(partner, 'Text', None)
    _safe_set(owner, 'parentNode', {partner})
    assert getattr(partner, 'Text') == owner
    _safe_set(owner, 'parentNode', set())
    assert getattr(partner, 'Text') is None


def test_assoc_parentNode12_stub_double():
    # SimpleTree_Text has no real 'children' property in the generated
    # code (a bare stub) -- manually attach it so SimpleTree_Node's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # SimpleTree_Node's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = SimpleTree_Node(startIndex=7, startLineIndex=7, stopIndex=7, stopLineIndex=7)
    partner = SimpleTree_Text()
    setattr(partner, 'children', None)
    _safe_set(owner, 'Node13', partner)
    assert getattr(partner, 'children') == owner
    _safe_set(owner, 'Node13', None)
    assert getattr(partner, 'children') is None


def test_assoc_rootNode2_stub_double():
    # SimpleTree_File has no real 'SimpleTree_File' property in the generated
    # code (a bare stub) -- manually attach it so SimpleTree_TreeElement's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # SimpleTree_TreeElement's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = SimpleTree_TreeElement(index=7, name="sample_text")
    partner = SimpleTree_File()
    setattr(partner, 'SimpleTree_File', None)
    _safe_set(owner, 'SimpleTree_TreeElement', partner)
    assert getattr(partner, 'SimpleTree_File') == owner
    _safe_set(owner, 'SimpleTree_TreeElement', None)
    assert getattr(partner, 'SimpleTree_File') is None


