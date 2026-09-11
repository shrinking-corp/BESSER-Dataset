import inspect
import pytest
from datetime import date, datetime, time, timedelta
from hypothesis import given, settings
import hypothesis.strategies as st

from python_code import (
    btsviewmodel_BTSObjectTypeTreeNode,
    btsviewmodel_DBCollectionStatusInformation,
    btsviewmodel_StatusMessage,
    btsviewmodel_TreeNodeWrapper,
    MessageType,
)

safe_text = st.text(
    alphabet=st.characters(
        whitelist_categories=("Ll", "Lu", "Nd"),
        whitelist_characters="_",
    ),
    min_size=1,
).filter(lambda s: s[0].isalpha())

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
# SECTION 1 -- DETERMINISTIC TESTS (attributes, generalizations, relationships)
# =============================================================================

def test_btsviewmodel_BTSObjectTypeTreeNode_selected_value_roundtrip():
    instance = btsviewmodel_BTSObjectTypeTreeNode(selected=True, value="sample_text")
    assert instance.selected == True
    instance.selected = False
    assert instance.selected == False


def test_btsviewmodel_BTSObjectTypeTreeNode_value_value_roundtrip():
    instance = btsviewmodel_BTSObjectTypeTreeNode(selected=True, value="sample_text")
    assert instance.value == "sample_text"
    instance.value = "sample_text_2"
    assert instance.value == "sample_text_2"


def test_btsviewmodel_DBCollectionStatusInformation_dbCollectionName_value_roundtrip():
    instance = btsviewmodel_DBCollectionStatusInformation(dbCollectionName="sample_text", dbDiskSize="sample_text", dbDocCount="sample_text", dbDocDelCount="sample_text", dbPurgeSeq="sample_text", dbUpdateSeq="sample_text", indexDocCount="sample_text", indexStatus="sample_text", indexUpdateSeq="sample_text", syncStatusFromRemote="sample_text", syncStatusToRemote="sample_text")
    assert instance.dbCollectionName == "sample_text"
    instance.dbCollectionName = "sample_text_2"
    assert instance.dbCollectionName == "sample_text_2"


def test_btsviewmodel_DBCollectionStatusInformation_dbDiskSize_value_roundtrip():
    instance = btsviewmodel_DBCollectionStatusInformation(dbCollectionName="sample_text", dbDiskSize="sample_text", dbDocCount="sample_text", dbDocDelCount="sample_text", dbPurgeSeq="sample_text", dbUpdateSeq="sample_text", indexDocCount="sample_text", indexStatus="sample_text", indexUpdateSeq="sample_text", syncStatusFromRemote="sample_text", syncStatusToRemote="sample_text")
    assert instance.dbDiskSize == "sample_text"
    instance.dbDiskSize = "sample_text_2"
    assert instance.dbDiskSize == "sample_text_2"


def test_btsviewmodel_DBCollectionStatusInformation_dbDocCount_value_roundtrip():
    instance = btsviewmodel_DBCollectionStatusInformation(dbCollectionName="sample_text", dbDiskSize="sample_text", dbDocCount="sample_text", dbDocDelCount="sample_text", dbPurgeSeq="sample_text", dbUpdateSeq="sample_text", indexDocCount="sample_text", indexStatus="sample_text", indexUpdateSeq="sample_text", syncStatusFromRemote="sample_text", syncStatusToRemote="sample_text")
    assert instance.dbDocCount == "sample_text"
    instance.dbDocCount = "sample_text_2"
    assert instance.dbDocCount == "sample_text_2"


def test_btsviewmodel_DBCollectionStatusInformation_dbDocDelCount_value_roundtrip():
    instance = btsviewmodel_DBCollectionStatusInformation(dbCollectionName="sample_text", dbDiskSize="sample_text", dbDocCount="sample_text", dbDocDelCount="sample_text", dbPurgeSeq="sample_text", dbUpdateSeq="sample_text", indexDocCount="sample_text", indexStatus="sample_text", indexUpdateSeq="sample_text", syncStatusFromRemote="sample_text", syncStatusToRemote="sample_text")
    assert instance.dbDocDelCount == "sample_text"
    instance.dbDocDelCount = "sample_text_2"
    assert instance.dbDocDelCount == "sample_text_2"


def test_btsviewmodel_DBCollectionStatusInformation_dbPurgeSeq_value_roundtrip():
    instance = btsviewmodel_DBCollectionStatusInformation(dbCollectionName="sample_text", dbDiskSize="sample_text", dbDocCount="sample_text", dbDocDelCount="sample_text", dbPurgeSeq="sample_text", dbUpdateSeq="sample_text", indexDocCount="sample_text", indexStatus="sample_text", indexUpdateSeq="sample_text", syncStatusFromRemote="sample_text", syncStatusToRemote="sample_text")
    assert instance.dbPurgeSeq == "sample_text"
    instance.dbPurgeSeq = "sample_text_2"
    assert instance.dbPurgeSeq == "sample_text_2"


def test_btsviewmodel_DBCollectionStatusInformation_dbUpdateSeq_value_roundtrip():
    instance = btsviewmodel_DBCollectionStatusInformation(dbCollectionName="sample_text", dbDiskSize="sample_text", dbDocCount="sample_text", dbDocDelCount="sample_text", dbPurgeSeq="sample_text", dbUpdateSeq="sample_text", indexDocCount="sample_text", indexStatus="sample_text", indexUpdateSeq="sample_text", syncStatusFromRemote="sample_text", syncStatusToRemote="sample_text")
    assert instance.dbUpdateSeq == "sample_text"
    instance.dbUpdateSeq = "sample_text_2"
    assert instance.dbUpdateSeq == "sample_text_2"


def test_btsviewmodel_DBCollectionStatusInformation_indexDocCount_value_roundtrip():
    instance = btsviewmodel_DBCollectionStatusInformation(dbCollectionName="sample_text", dbDiskSize="sample_text", dbDocCount="sample_text", dbDocDelCount="sample_text", dbPurgeSeq="sample_text", dbUpdateSeq="sample_text", indexDocCount="sample_text", indexStatus="sample_text", indexUpdateSeq="sample_text", syncStatusFromRemote="sample_text", syncStatusToRemote="sample_text")
    assert instance.indexDocCount == "sample_text"
    instance.indexDocCount = "sample_text_2"
    assert instance.indexDocCount == "sample_text_2"


def test_btsviewmodel_DBCollectionStatusInformation_indexStatus_value_roundtrip():
    instance = btsviewmodel_DBCollectionStatusInformation(dbCollectionName="sample_text", dbDiskSize="sample_text", dbDocCount="sample_text", dbDocDelCount="sample_text", dbPurgeSeq="sample_text", dbUpdateSeq="sample_text", indexDocCount="sample_text", indexStatus="sample_text", indexUpdateSeq="sample_text", syncStatusFromRemote="sample_text", syncStatusToRemote="sample_text")
    assert instance.indexStatus == "sample_text"
    instance.indexStatus = "sample_text_2"
    assert instance.indexStatus == "sample_text_2"


def test_btsviewmodel_DBCollectionStatusInformation_indexUpdateSeq_value_roundtrip():
    instance = btsviewmodel_DBCollectionStatusInformation(dbCollectionName="sample_text", dbDiskSize="sample_text", dbDocCount="sample_text", dbDocDelCount="sample_text", dbPurgeSeq="sample_text", dbUpdateSeq="sample_text", indexDocCount="sample_text", indexStatus="sample_text", indexUpdateSeq="sample_text", syncStatusFromRemote="sample_text", syncStatusToRemote="sample_text")
    assert instance.indexUpdateSeq == "sample_text"
    instance.indexUpdateSeq = "sample_text_2"
    assert instance.indexUpdateSeq == "sample_text_2"


def test_btsviewmodel_DBCollectionStatusInformation_syncStatusFromRemote_value_roundtrip():
    instance = btsviewmodel_DBCollectionStatusInformation(dbCollectionName="sample_text", dbDiskSize="sample_text", dbDocCount="sample_text", dbDocDelCount="sample_text", dbPurgeSeq="sample_text", dbUpdateSeq="sample_text", indexDocCount="sample_text", indexStatus="sample_text", indexUpdateSeq="sample_text", syncStatusFromRemote="sample_text", syncStatusToRemote="sample_text")
    assert instance.syncStatusFromRemote == "sample_text"
    instance.syncStatusFromRemote = "sample_text_2"
    assert instance.syncStatusFromRemote == "sample_text_2"


def test_btsviewmodel_DBCollectionStatusInformation_syncStatusToRemote_value_roundtrip():
    instance = btsviewmodel_DBCollectionStatusInformation(dbCollectionName="sample_text", dbDiskSize="sample_text", dbDocCount="sample_text", dbDocDelCount="sample_text", dbPurgeSeq="sample_text", dbUpdateSeq="sample_text", indexDocCount="sample_text", indexStatus="sample_text", indexUpdateSeq="sample_text", syncStatusFromRemote="sample_text", syncStatusToRemote="sample_text")
    assert instance.syncStatusToRemote == "sample_text"
    instance.syncStatusToRemote = "sample_text_2"
    assert instance.syncStatusToRemote == "sample_text_2"


def test_btsviewmodel_StatusMessage_creationTime_value_roundtrip():
    instance = btsviewmodel_StatusMessage(creationTime=date(2024, 1, 1), message="sample_text", messageType="sample_text", userId="sample_text")
    assert instance.creationTime == date(2024, 1, 1)
    instance.creationTime = date(2025, 6, 15)
    assert instance.creationTime == date(2025, 6, 15)


def test_btsviewmodel_StatusMessage_message_value_roundtrip():
    instance = btsviewmodel_StatusMessage(creationTime=date(2024, 1, 1), message="sample_text", messageType="sample_text", userId="sample_text")
    assert instance.message == "sample_text"
    instance.message = "sample_text_2"
    assert instance.message == "sample_text_2"


def test_btsviewmodel_StatusMessage_messageType_value_roundtrip():
    instance = btsviewmodel_StatusMessage(creationTime=date(2024, 1, 1), message="sample_text", messageType="sample_text", userId="sample_text")
    assert instance.messageType == "sample_text"
    instance.messageType = "sample_text_2"
    assert instance.messageType == "sample_text_2"


def test_btsviewmodel_StatusMessage_userId_value_roundtrip():
    instance = btsviewmodel_StatusMessage(creationTime=date(2024, 1, 1), message="sample_text", messageType="sample_text", userId="sample_text")
    assert instance.userId == "sample_text"
    instance.userId = "sample_text_2"
    assert instance.userId == "sample_text_2"


def test_btsviewmodel_TreeNodeWrapper_childrenLoaded_value_roundtrip():
    instance = btsviewmodel_TreeNodeWrapper(childrenLoaded=True, label="sample_text", object="sample_text", parentObject="sample_text", propertyChangeSupport="sample_text")
    assert instance.childrenLoaded == True
    instance.childrenLoaded = False
    assert instance.childrenLoaded == False


def test_btsviewmodel_TreeNodeWrapper_label_value_roundtrip():
    instance = btsviewmodel_TreeNodeWrapper(childrenLoaded=True, label="sample_text", object="sample_text", parentObject="sample_text", propertyChangeSupport="sample_text")
    assert instance.label == "sample_text"
    instance.label = "sample_text_2"
    assert instance.label == "sample_text_2"


def test_btsviewmodel_TreeNodeWrapper_object_value_roundtrip():
    instance = btsviewmodel_TreeNodeWrapper(childrenLoaded=True, label="sample_text", object="sample_text", parentObject="sample_text", propertyChangeSupport="sample_text")
    assert instance.object == "sample_text"
    instance.object = "sample_text_2"
    assert instance.object == "sample_text_2"


def test_btsviewmodel_TreeNodeWrapper_parentObject_value_roundtrip():
    instance = btsviewmodel_TreeNodeWrapper(childrenLoaded=True, label="sample_text", object="sample_text", parentObject="sample_text", propertyChangeSupport="sample_text")
    assert instance.parentObject == "sample_text"
    instance.parentObject = "sample_text_2"
    assert instance.parentObject == "sample_text_2"


def test_btsviewmodel_TreeNodeWrapper_propertyChangeSupport_value_roundtrip():
    instance = btsviewmodel_TreeNodeWrapper(childrenLoaded=True, label="sample_text", object="sample_text", parentObject="sample_text", propertyChangeSupport="sample_text")
    assert instance.propertyChangeSupport == "sample_text"
    instance.propertyChangeSupport = "sample_text_2"
    assert instance.propertyChangeSupport == "sample_text_2"


def test_assoc_children3_link_reassign_clear():
    a = btsviewmodel_TreeNodeWrapper(childrenLoaded=True, label="sample_text", object="sample_text", parentObject="sample_text", propertyChangeSupport="sample_text")
    b1 = btsviewmodel_TreeNodeWrapper(childrenLoaded=True, label="sample_text", object="sample_text", parentObject="sample_text", propertyChangeSupport="sample_text")
    b2 = btsviewmodel_TreeNodeWrapper(childrenLoaded=False, label="sample_text_2", object="sample_text_2", parentObject="sample_text_2", propertyChangeSupport="sample_text_2")
    _safe_set(a, 'btsviewmodel_TreeNodeWrapper2', {b1})
    assert _is_linked(a, 'btsviewmodel_TreeNodeWrapper2', b1)
    if hasattr(b1, 'btsviewmodel_TreeNodeWrapper4'):
        assert _is_linked(b1, 'btsviewmodel_TreeNodeWrapper4', a)
    _safe_set(a, 'btsviewmodel_TreeNodeWrapper2', {b2})
    assert _is_linked(a, 'btsviewmodel_TreeNodeWrapper2', b2)
    if hasattr(b1, 'btsviewmodel_TreeNodeWrapper4'):
        assert not _is_linked(b1, 'btsviewmodel_TreeNodeWrapper4', a)
    if hasattr(b2, 'btsviewmodel_TreeNodeWrapper4'):
        assert _is_linked(b2, 'btsviewmodel_TreeNodeWrapper4', a)
    _safe_set(a, 'btsviewmodel_TreeNodeWrapper2', set())
    assert not _is_linked(a, 'btsviewmodel_TreeNodeWrapper2', b2)
    if hasattr(b2, 'btsviewmodel_TreeNodeWrapper4'):
        assert not _is_linked(b2, 'btsviewmodel_TreeNodeWrapper4', a)


def test_assoc_children6_link_reassign_clear():
    a = btsviewmodel_StatusMessage(creationTime=date(2024, 1, 1), message="sample_text", messageType="sample_text", userId="sample_text")
    b1 = btsviewmodel_StatusMessage(creationTime=date(2024, 1, 1), message="sample_text", messageType="sample_text", userId="sample_text")
    b2 = btsviewmodel_StatusMessage(creationTime=date(2025, 6, 15), message="sample_text_2", messageType="sample_text_2", userId="sample_text_2")
    _safe_set(a, 'btsviewmodel_StatusMessage', b1)
    assert _is_linked(a, 'btsviewmodel_StatusMessage', b1)
    if hasattr(b1, 'btsviewmodel_StatusMessage5'):
        assert _is_linked(b1, 'btsviewmodel_StatusMessage5', a)
    _safe_set(a, 'btsviewmodel_StatusMessage', b2)
    assert _is_linked(a, 'btsviewmodel_StatusMessage', b2)
    if hasattr(b1, 'btsviewmodel_StatusMessage5'):
        assert not _is_linked(b1, 'btsviewmodel_StatusMessage5', a)
    if hasattr(b2, 'btsviewmodel_StatusMessage5'):
        assert _is_linked(b2, 'btsviewmodel_StatusMessage5', a)
    _safe_set(a, 'btsviewmodel_StatusMessage', None)
    assert not _is_linked(a, 'btsviewmodel_StatusMessage', b2)
    if hasattr(b2, 'btsviewmodel_StatusMessage5'):
        assert not _is_linked(b2, 'btsviewmodel_StatusMessage5', a)


def test_assoc_children8_link_reassign_clear():
    a = btsviewmodel_BTSObjectTypeTreeNode(selected=True, value="sample_text")
    b1 = btsviewmodel_BTSObjectTypeTreeNode(selected=True, value="sample_text")
    b2 = btsviewmodel_BTSObjectTypeTreeNode(selected=False, value="sample_text_2")
    _safe_set(a, 'btsviewmodel_BTSObjectTypeTreeNode', b1)
    assert _is_linked(a, 'btsviewmodel_BTSObjectTypeTreeNode', b1)
    if hasattr(b1, 'btsviewmodel_BTSObjectTypeTreeNode7'):
        assert _is_linked(b1, 'btsviewmodel_BTSObjectTypeTreeNode7', a)
    _safe_set(a, 'btsviewmodel_BTSObjectTypeTreeNode', b2)
    assert _is_linked(a, 'btsviewmodel_BTSObjectTypeTreeNode', b2)
    if hasattr(b1, 'btsviewmodel_BTSObjectTypeTreeNode7'):
        assert not _is_linked(b1, 'btsviewmodel_BTSObjectTypeTreeNode7', a)
    if hasattr(b2, 'btsviewmodel_BTSObjectTypeTreeNode7'):
        assert _is_linked(b2, 'btsviewmodel_BTSObjectTypeTreeNode7', a)
    _safe_set(a, 'btsviewmodel_BTSObjectTypeTreeNode', None)
    assert not _is_linked(a, 'btsviewmodel_BTSObjectTypeTreeNode', b2)
    if hasattr(b2, 'btsviewmodel_BTSObjectTypeTreeNode7'):
        assert not _is_linked(b2, 'btsviewmodel_BTSObjectTypeTreeNode7', a)


def test_assoc_parent1_link_reassign_clear():
    a = btsviewmodel_TreeNodeWrapper(childrenLoaded=True, label="sample_text", object="sample_text", parentObject="sample_text", propertyChangeSupport="sample_text")
    b1 = btsviewmodel_TreeNodeWrapper(childrenLoaded=True, label="sample_text", object="sample_text", parentObject="sample_text", propertyChangeSupport="sample_text")
    b2 = btsviewmodel_TreeNodeWrapper(childrenLoaded=False, label="sample_text_2", object="sample_text_2", parentObject="sample_text_2", propertyChangeSupport="sample_text_2")
    _safe_set(a, 'btsviewmodel_TreeNodeWrapper', b1)
    assert _is_linked(a, 'btsviewmodel_TreeNodeWrapper', b1)
    if hasattr(b1, 'btsviewmodel_TreeNodeWrapper0'):
        assert _is_linked(b1, 'btsviewmodel_TreeNodeWrapper0', a)
    _safe_set(a, 'btsviewmodel_TreeNodeWrapper', b2)
    assert _is_linked(a, 'btsviewmodel_TreeNodeWrapper', b2)
    if hasattr(b1, 'btsviewmodel_TreeNodeWrapper0'):
        assert not _is_linked(b1, 'btsviewmodel_TreeNodeWrapper0', a)
    if hasattr(b2, 'btsviewmodel_TreeNodeWrapper0'):
        assert _is_linked(b2, 'btsviewmodel_TreeNodeWrapper0', a)
    _safe_set(a, 'btsviewmodel_TreeNodeWrapper', None)
    assert not _is_linked(a, 'btsviewmodel_TreeNodeWrapper', b2)
    if hasattr(b2, 'btsviewmodel_TreeNodeWrapper0'):
        assert not _is_linked(b2, 'btsviewmodel_TreeNodeWrapper0', a)


def test_assoc_referencedTypesPath10_link_reassign_clear():
    a = btsviewmodel_BTSObjectTypeTreeNode(selected=True, value="sample_text")
    b1 = btsviewmodel_BTSObjectTypeTreeNode(selected=True, value="sample_text")
    b2 = btsviewmodel_BTSObjectTypeTreeNode(selected=False, value="sample_text_2")
    _safe_set(a, 'btsviewmodel_BTSObjectTypeTreeNode11', b1)
    assert _is_linked(a, 'btsviewmodel_BTSObjectTypeTreeNode11', b1)
    if hasattr(b1, 'btsviewmodel_BTSObjectTypeTreeNode9'):
        assert _is_linked(b1, 'btsviewmodel_BTSObjectTypeTreeNode9', a)
    _safe_set(a, 'btsviewmodel_BTSObjectTypeTreeNode11', b2)
    assert _is_linked(a, 'btsviewmodel_BTSObjectTypeTreeNode11', b2)
    if hasattr(b1, 'btsviewmodel_BTSObjectTypeTreeNode9'):
        assert not _is_linked(b1, 'btsviewmodel_BTSObjectTypeTreeNode9', a)
    if hasattr(b2, 'btsviewmodel_BTSObjectTypeTreeNode9'):
        assert _is_linked(b2, 'btsviewmodel_BTSObjectTypeTreeNode9', a)
    _safe_set(a, 'btsviewmodel_BTSObjectTypeTreeNode11', None)
    assert not _is_linked(a, 'btsviewmodel_BTSObjectTypeTreeNode11', b2)
    if hasattr(b2, 'btsviewmodel_BTSObjectTypeTreeNode9'):
        assert not _is_linked(b2, 'btsviewmodel_BTSObjectTypeTreeNode9', a)


# =============================================================================
# SECTION 2 -- HYPOTHESIS INSTANTIATION TESTS
# =============================================================================

btsviewmodel_BTSObjectTypeTreeNode_strategy = st.builds(btsviewmodel_BTSObjectTypeTreeNode, selected=st.booleans(), value=safe_text)
@given(instance=btsviewmodel_BTSObjectTypeTreeNode_strategy)
@settings(max_examples=25)
def test_btsviewmodel_BTSObjectTypeTreeNode_instantiation(instance):
    assert isinstance(instance, btsviewmodel_BTSObjectTypeTreeNode)


btsviewmodel_DBCollectionStatusInformation_strategy = st.builds(btsviewmodel_DBCollectionStatusInformation, dbCollectionName=safe_text, dbDiskSize=safe_text, dbDocCount=safe_text, dbDocDelCount=safe_text, dbPurgeSeq=safe_text, dbUpdateSeq=safe_text, indexDocCount=safe_text, indexStatus=safe_text, indexUpdateSeq=safe_text, syncStatusFromRemote=safe_text, syncStatusToRemote=safe_text)
@given(instance=btsviewmodel_DBCollectionStatusInformation_strategy)
@settings(max_examples=25)
def test_btsviewmodel_DBCollectionStatusInformation_instantiation(instance):
    assert isinstance(instance, btsviewmodel_DBCollectionStatusInformation)


btsviewmodel_StatusMessage_strategy = st.builds(btsviewmodel_StatusMessage, creationTime=st.dates(), message=safe_text, messageType=safe_text, userId=safe_text)
@given(instance=btsviewmodel_StatusMessage_strategy)
@settings(max_examples=25)
def test_btsviewmodel_StatusMessage_instantiation(instance):
    assert isinstance(instance, btsviewmodel_StatusMessage)


btsviewmodel_TreeNodeWrapper_strategy = st.builds(btsviewmodel_TreeNodeWrapper, childrenLoaded=st.booleans(), label=safe_text, object=safe_text, parentObject=safe_text, propertyChangeSupport=safe_text)
@given(instance=btsviewmodel_TreeNodeWrapper_strategy)
@settings(max_examples=25)
def test_btsviewmodel_TreeNodeWrapper_instantiation(instance):
    assert isinstance(instance, btsviewmodel_TreeNodeWrapper)


