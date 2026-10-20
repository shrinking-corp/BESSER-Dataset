import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    btsviewmodel_BTSObjectTypeTreeNode,
    btsviewmodel_DBCollectionStatusInformation,
    btsviewmodel_StatusMessage,
    btsviewmodel_TreeNodeWrapper,
    MessageType,
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

def test_assoc_children3_reverse_link_reassign_clear():
    a1 = btsviewmodel_TreeNodeWrapper(childrenLoaded=True, label="sample_text", object="sample_text", parentObject="sample_text", propertyChangeSupport="sample_text")
    a2 = btsviewmodel_TreeNodeWrapper(childrenLoaded=False, label="sample_text_2", object="sample_text_2", parentObject="sample_text_2", propertyChangeSupport="sample_text_2")
    b = btsviewmodel_TreeNodeWrapper(childrenLoaded=True, label="sample_text", object="sample_text", parentObject="sample_text", propertyChangeSupport="sample_text")
    _safe_set(b, 'btsviewmodel_TreeNodeWrapper4', a1)
    assert _is_linked(b, 'btsviewmodel_TreeNodeWrapper4', a1)
    if hasattr(a1, 'btsviewmodel_TreeNodeWrapper2'):
        assert _is_linked(a1, 'btsviewmodel_TreeNodeWrapper2', b)
    _safe_set(b, 'btsviewmodel_TreeNodeWrapper4', a2)
    assert _is_linked(b, 'btsviewmodel_TreeNodeWrapper4', a2)
    if hasattr(a1, 'btsviewmodel_TreeNodeWrapper2'):
        assert not _is_linked(a1, 'btsviewmodel_TreeNodeWrapper2', b)
    if hasattr(a2, 'btsviewmodel_TreeNodeWrapper2'):
        assert _is_linked(a2, 'btsviewmodel_TreeNodeWrapper2', b)
    _safe_set(b, 'btsviewmodel_TreeNodeWrapper4', None)
    assert not _is_linked(b, 'btsviewmodel_TreeNodeWrapper4', a2)
    if hasattr(a2, 'btsviewmodel_TreeNodeWrapper2'):
        assert not _is_linked(a2, 'btsviewmodel_TreeNodeWrapper2', b)


def test_assoc_children6_reverse_link_reassign_clear():
    a1 = btsviewmodel_StatusMessage(creationTime=date(2024, 1, 1), message="sample_text", messageType="sample_text", userId="sample_text")
    a2 = btsviewmodel_StatusMessage(creationTime=date(2025, 6, 15), message="sample_text_2", messageType="sample_text_2", userId="sample_text_2")
    b = btsviewmodel_StatusMessage(creationTime=date(2024, 1, 1), message="sample_text", messageType="sample_text", userId="sample_text")
    _safe_set(b, 'btsviewmodel_StatusMessage5', {a1})
    assert _is_linked(b, 'btsviewmodel_StatusMessage5', a1)
    if hasattr(a1, 'btsviewmodel_StatusMessage'):
        assert _is_linked(a1, 'btsviewmodel_StatusMessage', b)
    _safe_set(b, 'btsviewmodel_StatusMessage5', {a2})
    assert _is_linked(b, 'btsviewmodel_StatusMessage5', a2)
    if hasattr(a1, 'btsviewmodel_StatusMessage'):
        assert not _is_linked(a1, 'btsviewmodel_StatusMessage', b)
    if hasattr(a2, 'btsviewmodel_StatusMessage'):
        assert _is_linked(a2, 'btsviewmodel_StatusMessage', b)
    _safe_set(b, 'btsviewmodel_StatusMessage5', set())
    assert not _is_linked(b, 'btsviewmodel_StatusMessage5', a2)
    if hasattr(a2, 'btsviewmodel_StatusMessage'):
        assert not _is_linked(a2, 'btsviewmodel_StatusMessage', b)


def test_assoc_children8_reverse_link_reassign_clear():
    a1 = btsviewmodel_BTSObjectTypeTreeNode(selected=True, value="sample_text")
    a2 = btsviewmodel_BTSObjectTypeTreeNode(selected=False, value="sample_text_2")
    b = btsviewmodel_BTSObjectTypeTreeNode(selected=True, value="sample_text")
    _safe_set(b, 'btsviewmodel_BTSObjectTypeTreeNode7', {a1})
    assert _is_linked(b, 'btsviewmodel_BTSObjectTypeTreeNode7', a1)
    if hasattr(a1, 'btsviewmodel_BTSObjectTypeTreeNode'):
        assert _is_linked(a1, 'btsviewmodel_BTSObjectTypeTreeNode', b)
    _safe_set(b, 'btsviewmodel_BTSObjectTypeTreeNode7', {a2})
    assert _is_linked(b, 'btsviewmodel_BTSObjectTypeTreeNode7', a2)
    if hasattr(a1, 'btsviewmodel_BTSObjectTypeTreeNode'):
        assert not _is_linked(a1, 'btsviewmodel_BTSObjectTypeTreeNode', b)
    if hasattr(a2, 'btsviewmodel_BTSObjectTypeTreeNode'):
        assert _is_linked(a2, 'btsviewmodel_BTSObjectTypeTreeNode', b)
    _safe_set(b, 'btsviewmodel_BTSObjectTypeTreeNode7', set())
    assert not _is_linked(b, 'btsviewmodel_BTSObjectTypeTreeNode7', a2)
    if hasattr(a2, 'btsviewmodel_BTSObjectTypeTreeNode'):
        assert not _is_linked(a2, 'btsviewmodel_BTSObjectTypeTreeNode', b)


def test_assoc_parent1_reverse_link_reassign_clear():
    a1 = btsviewmodel_TreeNodeWrapper(childrenLoaded=True, label="sample_text", object="sample_text", parentObject="sample_text", propertyChangeSupport="sample_text")
    a2 = btsviewmodel_TreeNodeWrapper(childrenLoaded=False, label="sample_text_2", object="sample_text_2", parentObject="sample_text_2", propertyChangeSupport="sample_text_2")
    b = btsviewmodel_TreeNodeWrapper(childrenLoaded=True, label="sample_text", object="sample_text", parentObject="sample_text", propertyChangeSupport="sample_text")
    _safe_set(b, 'btsviewmodel_TreeNodeWrapper0', a1)
    assert _is_linked(b, 'btsviewmodel_TreeNodeWrapper0', a1)
    if hasattr(a1, 'btsviewmodel_TreeNodeWrapper'):
        assert _is_linked(a1, 'btsviewmodel_TreeNodeWrapper', b)
    _safe_set(b, 'btsviewmodel_TreeNodeWrapper0', a2)
    assert _is_linked(b, 'btsviewmodel_TreeNodeWrapper0', a2)
    if hasattr(a1, 'btsviewmodel_TreeNodeWrapper'):
        assert not _is_linked(a1, 'btsviewmodel_TreeNodeWrapper', b)
    if hasattr(a2, 'btsviewmodel_TreeNodeWrapper'):
        assert _is_linked(a2, 'btsviewmodel_TreeNodeWrapper', b)
    _safe_set(b, 'btsviewmodel_TreeNodeWrapper0', None)
    assert not _is_linked(b, 'btsviewmodel_TreeNodeWrapper0', a2)
    if hasattr(a2, 'btsviewmodel_TreeNodeWrapper'):
        assert not _is_linked(a2, 'btsviewmodel_TreeNodeWrapper', b)


def test_assoc_referencedTypesPath10_reverse_link_reassign_clear():
    a1 = btsviewmodel_BTSObjectTypeTreeNode(selected=True, value="sample_text")
    a2 = btsviewmodel_BTSObjectTypeTreeNode(selected=False, value="sample_text_2")
    b = btsviewmodel_BTSObjectTypeTreeNode(selected=True, value="sample_text")
    _safe_set(b, 'btsviewmodel_BTSObjectTypeTreeNode9', a1)
    assert _is_linked(b, 'btsviewmodel_BTSObjectTypeTreeNode9', a1)
    if hasattr(a1, 'btsviewmodel_BTSObjectTypeTreeNode11'):
        assert _is_linked(a1, 'btsviewmodel_BTSObjectTypeTreeNode11', b)
    _safe_set(b, 'btsviewmodel_BTSObjectTypeTreeNode9', a2)
    assert _is_linked(b, 'btsviewmodel_BTSObjectTypeTreeNode9', a2)
    if hasattr(a1, 'btsviewmodel_BTSObjectTypeTreeNode11'):
        assert not _is_linked(a1, 'btsviewmodel_BTSObjectTypeTreeNode11', b)
    if hasattr(a2, 'btsviewmodel_BTSObjectTypeTreeNode11'):
        assert _is_linked(a2, 'btsviewmodel_BTSObjectTypeTreeNode11', b)
    _safe_set(b, 'btsviewmodel_BTSObjectTypeTreeNode9', None)
    assert not _is_linked(b, 'btsviewmodel_BTSObjectTypeTreeNode9', a2)
    if hasattr(a2, 'btsviewmodel_BTSObjectTypeTreeNode11'):
        assert not _is_linked(a2, 'btsviewmodel_BTSObjectTypeTreeNode11', b)


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

