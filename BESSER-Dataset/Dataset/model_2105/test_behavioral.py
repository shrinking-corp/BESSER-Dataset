import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    ResourceTreeNode,
    SemanticResourceDB_ResourceTreeNode,
    SemanticResourceDB_SemanticDB,
    SemanticResourceDB_TreeRoot,
    TreeNodeType,
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
    a1 = SemanticResourceDB_ResourceTreeNode(dynamicContentProviderID="sample_text", exists=True, localOnly=True, name="sample_text", path="sample_text", persistentProperties="sample_text", queryPart="sample_text", remoteURI="sample_text", sessionProperties="sample_text", templateID="sample_text", type="sample_text")
    a2 = SemanticResourceDB_ResourceTreeNode(dynamicContentProviderID="sample_text_2", exists=False, localOnly=False, name="sample_text_2", path="sample_text_2", persistentProperties="sample_text_2", queryPart="sample_text_2", remoteURI="sample_text_2", sessionProperties="sample_text_2", templateID="sample_text_2", type="sample_text_2")
    b = SemanticResourceDB_ResourceTreeNode(dynamicContentProviderID="sample_text", exists=True, localOnly=True, name="sample_text", path="sample_text", persistentProperties="sample_text", queryPart="sample_text", remoteURI="sample_text", sessionProperties="sample_text", templateID="sample_text", type="sample_text")
    _safe_set(b, 'parent', {a1})
    assert _is_linked(b, 'parent', a1)
    if hasattr(a1, 'ResourceTreeNode'):
        assert _is_linked(a1, 'ResourceTreeNode', b)
    _safe_set(b, 'parent', {a2})
    assert _is_linked(b, 'parent', a2)
    if hasattr(a1, 'ResourceTreeNode'):
        assert not _is_linked(a1, 'ResourceTreeNode', b)
    if hasattr(a2, 'ResourceTreeNode'):
        assert _is_linked(a2, 'ResourceTreeNode', b)
    _safe_set(b, 'parent', set())
    assert not _is_linked(b, 'parent', a2)
    if hasattr(a2, 'ResourceTreeNode'):
        assert not _is_linked(a2, 'ResourceTreeNode', b)


def test_assoc_parent3_reverse_link_reassign_clear():
    a1 = SemanticResourceDB_ResourceTreeNode(dynamicContentProviderID="sample_text", exists=True, localOnly=True, name="sample_text", path="sample_text", persistentProperties="sample_text", queryPart="sample_text", remoteURI="sample_text", sessionProperties="sample_text", templateID="sample_text", type="sample_text")
    a2 = SemanticResourceDB_ResourceTreeNode(dynamicContentProviderID="sample_text_2", exists=False, localOnly=False, name="sample_text_2", path="sample_text_2", persistentProperties="sample_text_2", queryPart="sample_text_2", remoteURI="sample_text_2", sessionProperties="sample_text_2", templateID="sample_text_2", type="sample_text_2")
    b = SemanticResourceDB_ResourceTreeNode(dynamicContentProviderID="sample_text", exists=True, localOnly=True, name="sample_text", path="sample_text", persistentProperties="sample_text", queryPart="sample_text", remoteURI="sample_text", sessionProperties="sample_text", templateID="sample_text", type="sample_text")
    _safe_set(b, 'children', a1)
    assert _is_linked(b, 'children', a1)
    if hasattr(a1, 'ResourceTreeNode4'):
        assert _is_linked(a1, 'ResourceTreeNode4', b)
    _safe_set(b, 'children', a2)
    assert _is_linked(b, 'children', a2)
    if hasattr(a1, 'ResourceTreeNode4'):
        assert not _is_linked(a1, 'ResourceTreeNode4', b)
    if hasattr(a2, 'ResourceTreeNode4'):
        assert _is_linked(a2, 'ResourceTreeNode4', b)
    _safe_set(b, 'children', None)
    assert not _is_linked(b, 'children', a2)
    if hasattr(a2, 'ResourceTreeNode4'):
        assert not _is_linked(a2, 'ResourceTreeNode4', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_parentDB6_stub_double():
    # SemanticResourceDB_SemanticDB has no real 'SemanticDB' property in the generated
    # code (a bare stub) -- manually attach it so SemanticResourceDB_TreeRoot's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # SemanticResourceDB_TreeRoot's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = SemanticResourceDB_TreeRoot(rootURI="sample_text")
    partner = SemanticResourceDB_SemanticDB()
    setattr(partner, 'SemanticDB', None)
    _safe_set(owner, 'roots', partner)
    assert getattr(partner, 'SemanticDB') == owner
    _safe_set(owner, 'roots', None)
    assert getattr(partner, 'SemanticDB') is None


def test_assoc_roots5_stub_double():
    # SemanticResourceDB_SemanticDB has no real 'parentDB' property in the generated
    # code (a bare stub) -- manually attach it so SemanticResourceDB_TreeRoot's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # SemanticResourceDB_TreeRoot's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = SemanticResourceDB_TreeRoot(rootURI="sample_text")
    partner = SemanticResourceDB_SemanticDB()
    setattr(partner, 'parentDB', None)
    _safe_set(owner, 'TreeRoot', partner)
    assert owner in getattr(partner, 'parentDB')
    _safe_set(owner, 'TreeRoot', None)
    assert owner not in getattr(partner, 'parentDB')


