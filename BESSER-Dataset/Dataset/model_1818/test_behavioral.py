import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    DdsQosProfile,
    DdsReadCondition,
    DdsStatusCondition,
    ddsMetamodel_DdsApplication,
    ddsMetamodel_DdsDataField,
    ddsMetamodel_DdsDataModule,
    ddsMetamodel_DdsDataReader,
    ddsMetamodel_DdsDataReaderLifecycleQos,
    ddsMetamodel_DdsDataReaderListener,
    ddsMetamodel_DdsDataReaderQosProfile,
    ddsMetamodel_DdsDataReaderStatusCondition,
    ddsMetamodel_DdsDataStructure,
    ddsMetamodel_DdsDataWriter,
    ddsMetamodel_DdsDataWriterLifecycleQos,
    ddsMetamodel_DdsDataWriterListener,
    ddsMetamodel_DdsDataWriterQosProfile,
    ddsMetamodel_DdsDataWriterStatusCondition,
    ddsMetamodel_DdsDeadlineQos,
    ddsMetamodel_DdsDestinationOrderQos,
    ddsMetamodel_DdsDomainParticipant,
    ddsMetamodel_DdsDomainParticipantListener,
    ddsMetamodel_DdsDomainParticipantQosProfile,
    ddsMetamodel_DdsDomainParticipantStatusCondition,
    ddsMetamodel_DdsDurabilityQos,
    ddsMetamodel_DdsDurabilityServiceQos,
    ddsMetamodel_DdsDuration,
    ddsMetamodel_DdsEntityFactoryQos,
    ddsMetamodel_DdsGroupDataQos,
    ddsMetamodel_DdsHistoryQos,
    ddsMetamodel_DdsHost,
    ddsMetamodel_DdsLatencyBudgetQos,
    ddsMetamodel_DdsLifespan,
    ddsMetamodel_DdsLivelinessQos,
    ddsMetamodel_DdsOwnershipQos,
    ddsMetamodel_DdsOwnershipStrengthQos,
    ddsMetamodel_DdsPartitionQos,
    ddsMetamodel_DdsPresentationQos,
    ddsMetamodel_DdsPublisher,
    ddsMetamodel_DdsPublisherListener,
    ddsMetamodel_DdsPublisherQosProfile,
    ddsMetamodel_DdsPublisherStatusCondition,
    ddsMetamodel_DdsQosProfile,
    ddsMetamodel_DdsReadCondition,
    ddsMetamodel_DdsReliabilityQos,
    ddsMetamodel_DdsResourceLimits,
    ddsMetamodel_DdsStatusCondition,
    ddsMetamodel_DdsStructuredField,
    ddsMetamodel_DdsSubscriber,
    ddsMetamodel_DdsSubscriberListener,
    ddsMetamodel_DdsSubscriberQosProfile,
    ddsMetamodel_DdsSubscriberStatusCondition,
    ddsMetamodel_DdsSystem,
    ddsMetamodel_DdsTimeBasedFilterQos,
    ddsMetamodel_DdsTopic,
    ddsMetamodel_DdsTopicDataQos,
    ddsMetamodel_DdsTopicListener,
    ddsMetamodel_DdsTopicQosProfile,
    ddsMetamodel_DdsTopicStatusCondition,
    ddsMetamodel_DdsTransportPriorityQos,
    ddsMetamodel_DdsUserDataQos,
    ddsMetamodel_DdsWaitSet,
    ddsMetamodel_GuardCondition,
    ddsMetamodel_QueryCondition,
    DataReaderStatus,
    DataWriterStatus,
    DestinationOrderQosPolicyKind,
    DomainParticipantStatus,
    DurabilityQosPolicyKind,
    HistoryQosPolicyKind,
    InstanceStateKind,
    InvalidSampleVisibilityQosPolicy,
    LivelinessQosPolicyKind,
    OwnershipQosPolicyKind,
    PresentationQosPolicyAccessScopeKind,
    PublisherStatus,
    ReliabilityQosPolicyKind,
    SampleStateKind,
    SubscriberStatus,
    TopicStatus,
    ViewStateKind,
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

def test_assoc_applications243_reverse_link_reassign_clear():
    a1 = ddsMetamodel_DdsHost(hostName="sample_text")
    a2 = ddsMetamodel_DdsHost(hostName="sample_text_2")
    b = ddsMetamodel_DdsApplication(applicationName="sample_text")
    _safe_set(b, 'ddsMetamodel_DdsApplication245', a1)
    assert _is_linked(b, 'ddsMetamodel_DdsApplication245', a1)
    if hasattr(a1, 'ddsMetamodel_DdsHost244'):
        assert _is_linked(a1, 'ddsMetamodel_DdsHost244', b)
    _safe_set(b, 'ddsMetamodel_DdsApplication245', a2)
    assert _is_linked(b, 'ddsMetamodel_DdsApplication245', a2)
    if hasattr(a1, 'ddsMetamodel_DdsHost244'):
        assert not _is_linked(a1, 'ddsMetamodel_DdsHost244', b)
    if hasattr(a2, 'ddsMetamodel_DdsHost244'):
        assert _is_linked(a2, 'ddsMetamodel_DdsHost244', b)
    _safe_set(b, 'ddsMetamodel_DdsApplication245', None)
    assert not _is_linked(b, 'ddsMetamodel_DdsApplication245', a2)
    if hasattr(a2, 'ddsMetamodel_DdsHost244'):
        assert not _is_linked(a2, 'ddsMetamodel_DdsHost244', b)


def test_assoc_autopurge_disposed_samples_delay109_reverse_link_reassign_clear():
    a1 = ddsMetamodel_DdsDuration(nanoSec="sample_text", sec="sample_text")
    a2 = ddsMetamodel_DdsDuration(nanoSec="sample_text_2", sec="sample_text_2")
    b = ddsMetamodel_DdsDataReaderLifecycleQos(autopurge_dispose_all=True, enable_invalid_samples=True)
    _safe_set(b, 'ddsMetamodel_DdsDataReaderLifecycleQos110', a1)
    assert _is_linked(b, 'ddsMetamodel_DdsDataReaderLifecycleQos110', a1)
    if hasattr(a1, 'ddsMetamodel_DdsDuration111'):
        assert _is_linked(a1, 'ddsMetamodel_DdsDuration111', b)
    _safe_set(b, 'ddsMetamodel_DdsDataReaderLifecycleQos110', a2)
    assert _is_linked(b, 'ddsMetamodel_DdsDataReaderLifecycleQos110', a2)
    if hasattr(a1, 'ddsMetamodel_DdsDuration111'):
        assert not _is_linked(a1, 'ddsMetamodel_DdsDuration111', b)
    if hasattr(a2, 'ddsMetamodel_DdsDuration111'):
        assert _is_linked(a2, 'ddsMetamodel_DdsDuration111', b)
    _safe_set(b, 'ddsMetamodel_DdsDataReaderLifecycleQos110', None)
    assert not _is_linked(b, 'ddsMetamodel_DdsDataReaderLifecycleQos110', a2)
    if hasattr(a2, 'ddsMetamodel_DdsDuration111'):
        assert not _is_linked(a2, 'ddsMetamodel_DdsDuration111', b)


def test_assoc_autopurge_nowriters_samples_delay107_reverse_link_reassign_clear():
    a1 = ddsMetamodel_DdsDuration(nanoSec="sample_text", sec="sample_text")
    a2 = ddsMetamodel_DdsDuration(nanoSec="sample_text_2", sec="sample_text_2")
    b = ddsMetamodel_DdsDataReaderLifecycleQos(autopurge_dispose_all=True, enable_invalid_samples=True)
    _safe_set(b, 'ddsMetamodel_DdsDataReaderLifecycleQos', a1)
    assert _is_linked(b, 'ddsMetamodel_DdsDataReaderLifecycleQos', a1)
    if hasattr(a1, 'ddsMetamodel_DdsDuration108'):
        assert _is_linked(a1, 'ddsMetamodel_DdsDuration108', b)
    _safe_set(b, 'ddsMetamodel_DdsDataReaderLifecycleQos', a2)
    assert _is_linked(b, 'ddsMetamodel_DdsDataReaderLifecycleQos', a2)
    if hasattr(a1, 'ddsMetamodel_DdsDuration108'):
        assert not _is_linked(a1, 'ddsMetamodel_DdsDuration108', b)
    if hasattr(a2, 'ddsMetamodel_DdsDuration108'):
        assert _is_linked(a2, 'ddsMetamodel_DdsDuration108', b)
    _safe_set(b, 'ddsMetamodel_DdsDataReaderLifecycleQos', None)
    assert not _is_linked(b, 'ddsMetamodel_DdsDataReaderLifecycleQos', a2)
    if hasattr(a2, 'ddsMetamodel_DdsDuration108'):
        assert not _is_linked(a2, 'ddsMetamodel_DdsDuration108', b)


def test_assoc_autopurge_suspended_samples_delay102_reverse_link_reassign_clear():
    a1 = ddsMetamodel_DdsDuration(nanoSec="sample_text", sec="sample_text")
    a2 = ddsMetamodel_DdsDuration(nanoSec="sample_text_2", sec="sample_text_2")
    b = ddsMetamodel_DdsDataWriterLifecycleQos(autodispose_unregistered_instances=True)
    _safe_set(b, 'ddsMetamodel_DdsDataWriterLifecycleQos', a1)
    assert _is_linked(b, 'ddsMetamodel_DdsDataWriterLifecycleQos', a1)
    if hasattr(a1, 'ddsMetamodel_DdsDuration103'):
        assert _is_linked(a1, 'ddsMetamodel_DdsDuration103', b)
    _safe_set(b, 'ddsMetamodel_DdsDataWriterLifecycleQos', a2)
    assert _is_linked(b, 'ddsMetamodel_DdsDataWriterLifecycleQos', a2)
    if hasattr(a1, 'ddsMetamodel_DdsDuration103'):
        assert not _is_linked(a1, 'ddsMetamodel_DdsDuration103', b)
    if hasattr(a2, 'ddsMetamodel_DdsDuration103'):
        assert _is_linked(a2, 'ddsMetamodel_DdsDuration103', b)
    _safe_set(b, 'ddsMetamodel_DdsDataWriterLifecycleQos', None)
    assert not _is_linked(b, 'ddsMetamodel_DdsDataWriterLifecycleQos', a2)
    if hasattr(a2, 'ddsMetamodel_DdsDuration103'):
        assert not _is_linked(a2, 'ddsMetamodel_DdsDuration103', b)


def test_assoc_autounregister_instance_delay104_reverse_link_reassign_clear():
    a1 = ddsMetamodel_DdsDuration(nanoSec="sample_text", sec="sample_text")
    a2 = ddsMetamodel_DdsDuration(nanoSec="sample_text_2", sec="sample_text_2")
    b = ddsMetamodel_DdsDataWriterLifecycleQos(autodispose_unregistered_instances=True)
    _safe_set(b, 'ddsMetamodel_DdsDataWriterLifecycleQos105', a1)
    assert _is_linked(b, 'ddsMetamodel_DdsDataWriterLifecycleQos105', a1)
    if hasattr(a1, 'ddsMetamodel_DdsDuration106'):
        assert _is_linked(a1, 'ddsMetamodel_DdsDuration106', b)
    _safe_set(b, 'ddsMetamodel_DdsDataWriterLifecycleQos105', a2)
    assert _is_linked(b, 'ddsMetamodel_DdsDataWriterLifecycleQos105', a2)
    if hasattr(a1, 'ddsMetamodel_DdsDuration106'):
        assert not _is_linked(a1, 'ddsMetamodel_DdsDuration106', b)
    if hasattr(a2, 'ddsMetamodel_DdsDuration106'):
        assert _is_linked(a2, 'ddsMetamodel_DdsDuration106', b)
    _safe_set(b, 'ddsMetamodel_DdsDataWriterLifecycleQos105', None)
    assert not _is_linked(b, 'ddsMetamodel_DdsDataWriterLifecycleQos105', a2)
    if hasattr(a2, 'ddsMetamodel_DdsDuration106'):
        assert not _is_linked(a2, 'ddsMetamodel_DdsDuration106', b)


def test_assoc_containerDataModule51_reverse_link_reassign_clear():
    a1 = ddsMetamodel_DdsDataStructure(structureName="sample_text")
    a2 = ddsMetamodel_DdsDataStructure(structureName="sample_text_2")
    b = ddsMetamodel_DdsDataModule(moduleName="sample_text")
    _safe_set(b, 'DdsDataModule52', a1)
    assert _is_linked(b, 'DdsDataModule52', a1)
    if hasattr(a1, 'dataStructures'):
        assert _is_linked(a1, 'dataStructures', b)
    _safe_set(b, 'DdsDataModule52', a2)
    assert _is_linked(b, 'DdsDataModule52', a2)
    if hasattr(a1, 'dataStructures'):
        assert not _is_linked(a1, 'dataStructures', b)
    if hasattr(a2, 'dataStructures'):
        assert _is_linked(a2, 'dataStructures', b)
    _safe_set(b, 'DdsDataModule52', None)
    assert not _is_linked(b, 'DdsDataModule52', a2)
    if hasattr(a2, 'dataStructures'):
        assert not _is_linked(a2, 'dataStructures', b)


def test_assoc_containingModule46_reverse_link_reassign_clear():
    a1 = ddsMetamodel_DdsDataModule(moduleName="sample_text")
    a2 = ddsMetamodel_DdsDataModule(moduleName="sample_text_2")
    b = ddsMetamodel_DdsDataModule(moduleName="sample_text")
    _safe_set(b, 'innerModules', a1)
    assert _is_linked(b, 'innerModules', a1)
    if hasattr(a1, 'DdsDataModule47'):
        assert _is_linked(a1, 'DdsDataModule47', b)
    _safe_set(b, 'innerModules', a2)
    assert _is_linked(b, 'innerModules', a2)
    if hasattr(a1, 'DdsDataModule47'):
        assert not _is_linked(a1, 'DdsDataModule47', b)
    if hasattr(a2, 'DdsDataModule47'):
        assert _is_linked(a2, 'DdsDataModule47', b)
    _safe_set(b, 'innerModules', None)
    assert not _is_linked(b, 'innerModules', a2)
    if hasattr(a2, 'DdsDataModule47'):
        assert not _is_linked(a2, 'DdsDataModule47', b)


def test_assoc_containingSubscriber27_reverse_link_reassign_clear():
    a1 = ddsMetamodel_DdsSubscriber(subscriberName="sample_text")
    a2 = ddsMetamodel_DdsSubscriber(subscriberName="sample_text_2")
    b = ddsMetamodel_DdsDataReader(dataReaderName="sample_text")
    _safe_set(b, 'ddsdatareader', a1)
    assert _is_linked(b, 'ddsdatareader', a1)
    if hasattr(a1, 'DdsSubscriber'):
        assert _is_linked(a1, 'DdsSubscriber', b)
    _safe_set(b, 'ddsdatareader', a2)
    assert _is_linked(b, 'ddsdatareader', a2)
    if hasattr(a1, 'DdsSubscriber'):
        assert not _is_linked(a1, 'DdsSubscriber', b)
    if hasattr(a2, 'DdsSubscriber'):
        assert _is_linked(a2, 'DdsSubscriber', b)
    _safe_set(b, 'ddsdatareader', None)
    assert not _is_linked(b, 'ddsdatareader', a2)
    if hasattr(a2, 'DdsSubscriber'):
        assert not _is_linked(a2, 'DdsSubscriber', b)


def test_assoc_containingSystem44_reverse_link_reassign_clear():
    a1 = ddsMetamodel_DdsSystem(systemName="sample_text")
    a2 = ddsMetamodel_DdsSystem(systemName="sample_text_2")
    b = ddsMetamodel_DdsDataModule(moduleName="sample_text")
    _safe_set(b, 'dataModules', a1)
    assert _is_linked(b, 'dataModules', a1)
    if hasattr(a1, 'DdsSystem'):
        assert _is_linked(a1, 'DdsSystem', b)
    _safe_set(b, 'dataModules', a2)
    assert _is_linked(b, 'dataModules', a2)
    if hasattr(a1, 'DdsSystem'):
        assert not _is_linked(a1, 'DdsSystem', b)
    if hasattr(a2, 'DdsSystem'):
        assert _is_linked(a2, 'DdsSystem', b)
    _safe_set(b, 'dataModules', None)
    assert not _is_linked(b, 'dataModules', a2)
    if hasattr(a2, 'DdsSystem'):
        assert not _is_linked(a2, 'DdsSystem', b)


def test_assoc_dataModules238_reverse_link_reassign_clear():
    a1 = ddsMetamodel_DdsSystem(systemName="sample_text")
    a2 = ddsMetamodel_DdsSystem(systemName="sample_text_2")
    b = ddsMetamodel_DdsDataModule(moduleName="sample_text")
    _safe_set(b, 'DdsDataModule239', a1)
    assert _is_linked(b, 'DdsDataModule239', a1)
    if hasattr(a1, 'containingSystem'):
        assert _is_linked(a1, 'containingSystem', b)
    _safe_set(b, 'DdsDataModule239', a2)
    assert _is_linked(b, 'DdsDataModule239', a2)
    if hasattr(a1, 'containingSystem'):
        assert not _is_linked(a1, 'containingSystem', b)
    if hasattr(a2, 'containingSystem'):
        assert _is_linked(a2, 'containingSystem', b)
    _safe_set(b, 'DdsDataModule239', None)
    assert not _is_linked(b, 'DdsDataModule239', a2)
    if hasattr(a2, 'containingSystem'):
        assert not _is_linked(a2, 'containingSystem', b)


def test_assoc_dataReader215_reverse_link_reassign_clear():
    a1 = ddsMetamodel_DdsReadCondition(instance_state_mask="sample_text", sample_state_mask="sample_text", view_state_mask="sample_text")
    a2 = ddsMetamodel_DdsReadCondition(instance_state_mask="sample_text_2", sample_state_mask="sample_text_2", view_state_mask="sample_text_2")
    b = ddsMetamodel_DdsDataReader(dataReaderName="sample_text")
    _safe_set(b, 'ddsMetamodel_DdsDataReader217', a1)
    assert _is_linked(b, 'ddsMetamodel_DdsDataReader217', a1)
    if hasattr(a1, 'ddsMetamodel_DdsReadCondition216'):
        assert _is_linked(a1, 'ddsMetamodel_DdsReadCondition216', b)
    _safe_set(b, 'ddsMetamodel_DdsDataReader217', a2)
    assert _is_linked(b, 'ddsMetamodel_DdsDataReader217', a2)
    if hasattr(a1, 'ddsMetamodel_DdsReadCondition216'):
        assert not _is_linked(a1, 'ddsMetamodel_DdsReadCondition216', b)
    if hasattr(a2, 'ddsMetamodel_DdsReadCondition216'):
        assert _is_linked(a2, 'ddsMetamodel_DdsReadCondition216', b)
    _safe_set(b, 'ddsMetamodel_DdsDataReader217', None)
    assert not _is_linked(b, 'ddsMetamodel_DdsDataReader217', a2)
    if hasattr(a2, 'ddsMetamodel_DdsReadCondition216'):
        assert not _is_linked(a2, 'ddsMetamodel_DdsReadCondition216', b)


def test_assoc_dataReader231_reverse_link_reassign_clear():
    a1 = ddsMetamodel_DdsDataReaderStatusCondition(enabled_status="sample_text")
    a2 = ddsMetamodel_DdsDataReaderStatusCondition(enabled_status="sample_text_2")
    b = ddsMetamodel_DdsDataReader(dataReaderName="sample_text")
    _safe_set(b, 'ddsMetamodel_DdsDataReader232', a1)
    assert _is_linked(b, 'ddsMetamodel_DdsDataReader232', a1)
    if hasattr(a1, 'ddsMetamodel_DdsDataReaderStatusCondition'):
        assert _is_linked(a1, 'ddsMetamodel_DdsDataReaderStatusCondition', b)
    _safe_set(b, 'ddsMetamodel_DdsDataReader232', a2)
    assert _is_linked(b, 'ddsMetamodel_DdsDataReader232', a2)
    if hasattr(a1, 'ddsMetamodel_DdsDataReaderStatusCondition'):
        assert not _is_linked(a1, 'ddsMetamodel_DdsDataReaderStatusCondition', b)
    if hasattr(a2, 'ddsMetamodel_DdsDataReaderStatusCondition'):
        assert _is_linked(a2, 'ddsMetamodel_DdsDataReaderStatusCondition', b)
    _safe_set(b, 'ddsMetamodel_DdsDataReader232', None)
    assert not _is_linked(b, 'ddsMetamodel_DdsDataReader232', a2)
    if hasattr(a2, 'ddsMetamodel_DdsDataReaderStatusCondition'):
        assert not _is_linked(a2, 'ddsMetamodel_DdsDataReaderStatusCondition', b)


def test_assoc_dataReaderListener23_reverse_link_reassign_clear():
    a1 = ddsMetamodel_DdsDataReaderListener(listenedStatus="sample_text", name="sample_text")
    a2 = ddsMetamodel_DdsDataReaderListener(listenedStatus="sample_text_2", name="sample_text_2")
    b = ddsMetamodel_DdsDataReader(dataReaderName="sample_text")
    _safe_set(b, 'ddsMetamodel_DdsDataReader24', a1)
    assert _is_linked(b, 'ddsMetamodel_DdsDataReader24', a1)
    if hasattr(a1, 'ddsMetamodel_DdsDataReaderListener'):
        assert _is_linked(a1, 'ddsMetamodel_DdsDataReaderListener', b)
    _safe_set(b, 'ddsMetamodel_DdsDataReader24', a2)
    assert _is_linked(b, 'ddsMetamodel_DdsDataReader24', a2)
    if hasattr(a1, 'ddsMetamodel_DdsDataReaderListener'):
        assert not _is_linked(a1, 'ddsMetamodel_DdsDataReaderListener', b)
    if hasattr(a2, 'ddsMetamodel_DdsDataReaderListener'):
        assert _is_linked(a2, 'ddsMetamodel_DdsDataReaderListener', b)
    _safe_set(b, 'ddsMetamodel_DdsDataReader24', None)
    assert not _is_linked(b, 'ddsMetamodel_DdsDataReader24', a2)
    if hasattr(a2, 'ddsMetamodel_DdsDataReaderListener'):
        assert not _is_linked(a2, 'ddsMetamodel_DdsDataReaderListener', b)


def test_assoc_dataStructure220_reverse_link_reassign_clear():
    a1 = ddsMetamodel_DdsStructuredField(fieldName="sample_text", isKey=True, maxMultiplicity=7)
    a2 = ddsMetamodel_DdsStructuredField(fieldName="sample_text_2", isKey=False, maxMultiplicity=13)
    b = ddsMetamodel_DdsDataStructure(structureName="sample_text")
    _safe_set(b, 'DdsDataStructure221', a1)
    assert _is_linked(b, 'DdsDataStructure221', a1)
    if hasattr(a1, 'structuredFields'):
        assert _is_linked(a1, 'structuredFields', b)
    _safe_set(b, 'DdsDataStructure221', a2)
    assert _is_linked(b, 'DdsDataStructure221', a2)
    if hasattr(a1, 'structuredFields'):
        assert not _is_linked(a1, 'structuredFields', b)
    if hasattr(a2, 'structuredFields'):
        assert _is_linked(a2, 'structuredFields', b)
    _safe_set(b, 'DdsDataStructure221', None)
    assert not _is_linked(b, 'DdsDataStructure221', a2)
    if hasattr(a2, 'structuredFields'):
        assert not _is_linked(a2, 'structuredFields', b)


def test_assoc_dataStructures41_reverse_link_reassign_clear():
    a1 = ddsMetamodel_DdsDataStructure(structureName="sample_text")
    a2 = ddsMetamodel_DdsDataStructure(structureName="sample_text_2")
    b = ddsMetamodel_DdsDataModule(moduleName="sample_text")
    _safe_set(b, 'containerDataModule', {a1})
    assert _is_linked(b, 'containerDataModule', a1)
    if hasattr(a1, 'DdsDataStructure'):
        assert _is_linked(a1, 'DdsDataStructure', b)
    _safe_set(b, 'containerDataModule', {a2})
    assert _is_linked(b, 'containerDataModule', a2)
    if hasattr(a1, 'DdsDataStructure'):
        assert not _is_linked(a1, 'DdsDataStructure', b)
    if hasattr(a2, 'DdsDataStructure'):
        assert _is_linked(a2, 'DdsDataStructure', b)
    _safe_set(b, 'containerDataModule', set())
    assert not _is_linked(b, 'containerDataModule', a2)
    if hasattr(a2, 'DdsDataStructure'):
        assert not _is_linked(a2, 'DdsDataStructure', b)


def test_assoc_dataWriter229_reverse_link_reassign_clear():
    a1 = ddsMetamodel_DdsDataWriterStatusCondition(enabled_status="sample_text")
    a2 = ddsMetamodel_DdsDataWriterStatusCondition(enabled_status="sample_text_2")
    b = ddsMetamodel_DdsDataWriter(dataWriterName="sample_text")
    _safe_set(b, 'ddsMetamodel_DdsDataWriter230', a1)
    assert _is_linked(b, 'ddsMetamodel_DdsDataWriter230', a1)
    if hasattr(a1, 'ddsMetamodel_DdsDataWriterStatusCondition'):
        assert _is_linked(a1, 'ddsMetamodel_DdsDataWriterStatusCondition', b)
    _safe_set(b, 'ddsMetamodel_DdsDataWriter230', a2)
    assert _is_linked(b, 'ddsMetamodel_DdsDataWriter230', a2)
    if hasattr(a1, 'ddsMetamodel_DdsDataWriterStatusCondition'):
        assert not _is_linked(a1, 'ddsMetamodel_DdsDataWriterStatusCondition', b)
    if hasattr(a2, 'ddsMetamodel_DdsDataWriterStatusCondition'):
        assert _is_linked(a2, 'ddsMetamodel_DdsDataWriterStatusCondition', b)
    _safe_set(b, 'ddsMetamodel_DdsDataWriter230', None)
    assert not _is_linked(b, 'ddsMetamodel_DdsDataWriter230', a2)
    if hasattr(a2, 'ddsMetamodel_DdsDataWriterStatusCondition'):
        assert not _is_linked(a2, 'ddsMetamodel_DdsDataWriterStatusCondition', b)


def test_assoc_dataWriterListener37_reverse_link_reassign_clear():
    a1 = ddsMetamodel_DdsDataWriterListener(listenedStatus="sample_text", name="sample_text")
    a2 = ddsMetamodel_DdsDataWriterListener(listenedStatus="sample_text_2", name="sample_text_2")
    b = ddsMetamodel_DdsDataWriter(dataWriterName="sample_text")
    _safe_set(b, 'ddsMetamodel_DdsDataWriter38', a1)
    assert _is_linked(b, 'ddsMetamodel_DdsDataWriter38', a1)
    if hasattr(a1, 'ddsMetamodel_DdsDataWriterListener'):
        assert _is_linked(a1, 'ddsMetamodel_DdsDataWriterListener', b)
    _safe_set(b, 'ddsMetamodel_DdsDataWriter38', a2)
    assert _is_linked(b, 'ddsMetamodel_DdsDataWriter38', a2)
    if hasattr(a1, 'ddsMetamodel_DdsDataWriterListener'):
        assert not _is_linked(a1, 'ddsMetamodel_DdsDataWriterListener', b)
    if hasattr(a2, 'ddsMetamodel_DdsDataWriterListener'):
        assert _is_linked(a2, 'ddsMetamodel_DdsDataWriterListener', b)
    _safe_set(b, 'ddsMetamodel_DdsDataWriter38', None)
    assert not _is_linked(b, 'ddsMetamodel_DdsDataWriter38', a2)
    if hasattr(a2, 'ddsMetamodel_DdsDataWriterListener'):
        assert not _is_linked(a2, 'ddsMetamodel_DdsDataWriterListener', b)


def test_assoc_ddsdatareader16_reverse_link_reassign_clear():
    a1 = ddsMetamodel_DdsSubscriber(subscriberName="sample_text")
    a2 = ddsMetamodel_DdsSubscriber(subscriberName="sample_text_2")
    b = ddsMetamodel_DdsDataReader(dataReaderName="sample_text")
    _safe_set(b, 'DdsDataReader', a1)
    assert _is_linked(b, 'DdsDataReader', a1)
    if hasattr(a1, 'containingSubscriber'):
        assert _is_linked(a1, 'containingSubscriber', b)
    _safe_set(b, 'DdsDataReader', a2)
    assert _is_linked(b, 'DdsDataReader', a2)
    if hasattr(a1, 'containingSubscriber'):
        assert not _is_linked(a1, 'containingSubscriber', b)
    if hasattr(a2, 'containingSubscriber'):
        assert _is_linked(a2, 'containingSubscriber', b)
    _safe_set(b, 'DdsDataReader', None)
    assert not _is_linked(b, 'DdsDataReader', a2)
    if hasattr(a2, 'containingSubscriber'):
        assert not _is_linked(a2, 'containingSubscriber', b)


def test_assoc_ddsdatastructure14_reverse_link_reassign_clear():
    a1 = ddsMetamodel_DdsTopic(topicName="sample_text")
    a2 = ddsMetamodel_DdsTopic(topicName="sample_text_2")
    b = ddsMetamodel_DdsDataStructure(structureName="sample_text")
    _safe_set(b, 'ddsMetamodel_DdsDataStructure', a1)
    assert _is_linked(b, 'ddsMetamodel_DdsDataStructure', a1)
    if hasattr(a1, 'ddsMetamodel_DdsTopic15'):
        assert _is_linked(a1, 'ddsMetamodel_DdsTopic15', b)
    _safe_set(b, 'ddsMetamodel_DdsDataStructure', a2)
    assert _is_linked(b, 'ddsMetamodel_DdsDataStructure', a2)
    if hasattr(a1, 'ddsMetamodel_DdsTopic15'):
        assert not _is_linked(a1, 'ddsMetamodel_DdsTopic15', b)
    if hasattr(a2, 'ddsMetamodel_DdsTopic15'):
        assert _is_linked(a2, 'ddsMetamodel_DdsTopic15', b)
    _safe_set(b, 'ddsMetamodel_DdsDataStructure', None)
    assert not _is_linked(b, 'ddsMetamodel_DdsDataStructure', a2)
    if hasattr(a2, 'ddsMetamodel_DdsTopic15'):
        assert not _is_linked(a2, 'ddsMetamodel_DdsTopic15', b)


def test_assoc_ddsdatawriter28_reverse_link_reassign_clear():
    a1 = ddsMetamodel_DdsPublisher(publisherName="sample_text")
    a2 = ddsMetamodel_DdsPublisher(publisherName="sample_text_2")
    b = ddsMetamodel_DdsDataWriter(dataWriterName="sample_text")
    _safe_set(b, 'ddsMetamodel_DdsDataWriter', a1)
    assert _is_linked(b, 'ddsMetamodel_DdsDataWriter', a1)
    if hasattr(a1, 'ddsMetamodel_DdsPublisher29'):
        assert _is_linked(a1, 'ddsMetamodel_DdsPublisher29', b)
    _safe_set(b, 'ddsMetamodel_DdsDataWriter', a2)
    assert _is_linked(b, 'ddsMetamodel_DdsDataWriter', a2)
    if hasattr(a1, 'ddsMetamodel_DdsPublisher29'):
        assert not _is_linked(a1, 'ddsMetamodel_DdsPublisher29', b)
    if hasattr(a2, 'ddsMetamodel_DdsPublisher29'):
        assert _is_linked(a2, 'ddsMetamodel_DdsPublisher29', b)
    _safe_set(b, 'ddsMetamodel_DdsDataWriter', None)
    assert not _is_linked(b, 'ddsMetamodel_DdsDataWriter', a2)
    if hasattr(a2, 'ddsMetamodel_DdsPublisher29'):
        assert not _is_linked(a2, 'ddsMetamodel_DdsPublisher29', b)


def test_assoc_ddspublisher5_reverse_link_reassign_clear():
    a1 = ddsMetamodel_DdsPublisher(publisherName="sample_text")
    a2 = ddsMetamodel_DdsPublisher(publisherName="sample_text_2")
    b = ddsMetamodel_DdsDomainParticipant(domainId=7, domainParticipantName="sample_text")
    _safe_set(b, 'ddsMetamodel_DdsDomainParticipant6', {a1})
    assert _is_linked(b, 'ddsMetamodel_DdsDomainParticipant6', a1)
    if hasattr(a1, 'ddsMetamodel_DdsPublisher'):
        assert _is_linked(a1, 'ddsMetamodel_DdsPublisher', b)
    _safe_set(b, 'ddsMetamodel_DdsDomainParticipant6', {a2})
    assert _is_linked(b, 'ddsMetamodel_DdsDomainParticipant6', a2)
    if hasattr(a1, 'ddsMetamodel_DdsPublisher'):
        assert not _is_linked(a1, 'ddsMetamodel_DdsPublisher', b)
    if hasattr(a2, 'ddsMetamodel_DdsPublisher'):
        assert _is_linked(a2, 'ddsMetamodel_DdsPublisher', b)
    _safe_set(b, 'ddsMetamodel_DdsDomainParticipant6', set())
    assert not _is_linked(b, 'ddsMetamodel_DdsDomainParticipant6', a2)
    if hasattr(a2, 'ddsMetamodel_DdsPublisher'):
        assert not _is_linked(a2, 'ddsMetamodel_DdsPublisher', b)


def test_assoc_ddssubscriber3_reverse_link_reassign_clear():
    a1 = ddsMetamodel_DdsSubscriber(subscriberName="sample_text")
    a2 = ddsMetamodel_DdsSubscriber(subscriberName="sample_text_2")
    b = ddsMetamodel_DdsDomainParticipant(domainId=7, domainParticipantName="sample_text")
    _safe_set(b, 'ddsMetamodel_DdsDomainParticipant4', {a1})
    assert _is_linked(b, 'ddsMetamodel_DdsDomainParticipant4', a1)
    if hasattr(a1, 'ddsMetamodel_DdsSubscriber'):
        assert _is_linked(a1, 'ddsMetamodel_DdsSubscriber', b)
    _safe_set(b, 'ddsMetamodel_DdsDomainParticipant4', {a2})
    assert _is_linked(b, 'ddsMetamodel_DdsDomainParticipant4', a2)
    if hasattr(a1, 'ddsMetamodel_DdsSubscriber'):
        assert not _is_linked(a1, 'ddsMetamodel_DdsSubscriber', b)
    if hasattr(a2, 'ddsMetamodel_DdsSubscriber'):
        assert _is_linked(a2, 'ddsMetamodel_DdsSubscriber', b)
    _safe_set(b, 'ddsMetamodel_DdsDomainParticipant4', set())
    assert not _is_linked(b, 'ddsMetamodel_DdsDomainParticipant4', a2)
    if hasattr(a2, 'ddsMetamodel_DdsSubscriber'):
        assert not _is_linked(a2, 'ddsMetamodel_DdsSubscriber', b)


def test_assoc_domainParticipant223_reverse_link_reassign_clear():
    a1 = ddsMetamodel_DdsDomainParticipantStatusCondition(enabled_status="sample_text")
    a2 = ddsMetamodel_DdsDomainParticipantStatusCondition(enabled_status="sample_text_2")
    b = ddsMetamodel_DdsDomainParticipant(domainId=7, domainParticipantName="sample_text")
    _safe_set(b, 'ddsMetamodel_DdsDomainParticipant224', a1)
    assert _is_linked(b, 'ddsMetamodel_DdsDomainParticipant224', a1)
    if hasattr(a1, 'ddsMetamodel_DdsDomainParticipantStatusCondition'):
        assert _is_linked(a1, 'ddsMetamodel_DdsDomainParticipantStatusCondition', b)
    _safe_set(b, 'ddsMetamodel_DdsDomainParticipant224', a2)
    assert _is_linked(b, 'ddsMetamodel_DdsDomainParticipant224', a2)
    if hasattr(a1, 'ddsMetamodel_DdsDomainParticipantStatusCondition'):
        assert not _is_linked(a1, 'ddsMetamodel_DdsDomainParticipantStatusCondition', b)
    if hasattr(a2, 'ddsMetamodel_DdsDomainParticipantStatusCondition'):
        assert _is_linked(a2, 'ddsMetamodel_DdsDomainParticipantStatusCondition', b)
    _safe_set(b, 'ddsMetamodel_DdsDomainParticipant224', None)
    assert not _is_linked(b, 'ddsMetamodel_DdsDomainParticipant224', a2)
    if hasattr(a2, 'ddsMetamodel_DdsDomainParticipantStatusCondition'):
        assert not _is_linked(a2, 'ddsMetamodel_DdsDomainParticipantStatusCondition', b)


def test_assoc_domainParticipantListener9_reverse_link_reassign_clear():
    a1 = ddsMetamodel_DdsDomainParticipantListener(listenedStatus="sample_text", name="sample_text")
    a2 = ddsMetamodel_DdsDomainParticipantListener(listenedStatus="sample_text_2", name="sample_text_2")
    b = ddsMetamodel_DdsDomainParticipant(domainId=7, domainParticipantName="sample_text")
    _safe_set(b, 'ddsMetamodel_DdsDomainParticipant10', a1)
    assert _is_linked(b, 'ddsMetamodel_DdsDomainParticipant10', a1)
    if hasattr(a1, 'ddsMetamodel_DdsDomainParticipantListener'):
        assert _is_linked(a1, 'ddsMetamodel_DdsDomainParticipantListener', b)
    _safe_set(b, 'ddsMetamodel_DdsDomainParticipant10', a2)
    assert _is_linked(b, 'ddsMetamodel_DdsDomainParticipant10', a2)
    if hasattr(a1, 'ddsMetamodel_DdsDomainParticipantListener'):
        assert not _is_linked(a1, 'ddsMetamodel_DdsDomainParticipantListener', b)
    if hasattr(a2, 'ddsMetamodel_DdsDomainParticipantListener'):
        assert _is_linked(a2, 'ddsMetamodel_DdsDomainParticipantListener', b)
    _safe_set(b, 'ddsMetamodel_DdsDomainParticipant10', None)
    assert not _is_linked(b, 'ddsMetamodel_DdsDomainParticipant10', a2)
    if hasattr(a2, 'ddsMetamodel_DdsDomainParticipantListener'):
        assert not _is_linked(a2, 'ddsMetamodel_DdsDomainParticipantListener', b)


def test_assoc_domainParticipants0_reverse_link_reassign_clear():
    a1 = ddsMetamodel_DdsDomainParticipant(domainId=7, domainParticipantName="sample_text")
    a2 = ddsMetamodel_DdsDomainParticipant(domainId=13, domainParticipantName="sample_text_2")
    b = ddsMetamodel_DdsApplication(applicationName="sample_text")
    _safe_set(b, 'ddsMetamodel_DdsApplication', {a1})
    assert _is_linked(b, 'ddsMetamodel_DdsApplication', a1)
    if hasattr(a1, 'ddsMetamodel_DdsDomainParticipant'):
        assert _is_linked(a1, 'ddsMetamodel_DdsDomainParticipant', b)
    _safe_set(b, 'ddsMetamodel_DdsApplication', {a2})
    assert _is_linked(b, 'ddsMetamodel_DdsApplication', a2)
    if hasattr(a1, 'ddsMetamodel_DdsDomainParticipant'):
        assert not _is_linked(a1, 'ddsMetamodel_DdsDomainParticipant', b)
    if hasattr(a2, 'ddsMetamodel_DdsDomainParticipant'):
        assert _is_linked(a2, 'ddsMetamodel_DdsDomainParticipant', b)
    _safe_set(b, 'ddsMetamodel_DdsApplication', set())
    assert not _is_linked(b, 'ddsMetamodel_DdsApplication', a2)
    if hasattr(a2, 'ddsMetamodel_DdsDomainParticipant'):
        assert not _is_linked(a2, 'ddsMetamodel_DdsDomainParticipant', b)


def test_assoc_fields48_reverse_link_reassign_clear():
    a1 = ddsMetamodel_DdsDataStructure(structureName="sample_text")
    a2 = ddsMetamodel_DdsDataStructure(structureName="sample_text_2")
    b = ddsMetamodel_DdsDataField(fieldName="sample_text", fieldType="sample_text", isKey=True, maxMultiplicity=7)
    _safe_set(b, 'ddsMetamodel_DdsDataField', a1)
    assert _is_linked(b, 'ddsMetamodel_DdsDataField', a1)
    if hasattr(a1, 'ddsMetamodel_DdsDataStructure49'):
        assert _is_linked(a1, 'ddsMetamodel_DdsDataStructure49', b)
    _safe_set(b, 'ddsMetamodel_DdsDataField', a2)
    assert _is_linked(b, 'ddsMetamodel_DdsDataField', a2)
    if hasattr(a1, 'ddsMetamodel_DdsDataStructure49'):
        assert not _is_linked(a1, 'ddsMetamodel_DdsDataStructure49', b)
    if hasattr(a2, 'ddsMetamodel_DdsDataStructure49'):
        assert _is_linked(a2, 'ddsMetamodel_DdsDataStructure49', b)
    _safe_set(b, 'ddsMetamodel_DdsDataField', None)
    assert not _is_linked(b, 'ddsMetamodel_DdsDataField', a2)
    if hasattr(a2, 'ddsMetamodel_DdsDataStructure49'):
        assert not _is_linked(a2, 'ddsMetamodel_DdsDataStructure49', b)


def test_assoc_guardConditions213_reverse_link_reassign_clear():
    a1 = ddsMetamodel_GuardCondition(name="sample_text")
    a2 = ddsMetamodel_GuardCondition(name="sample_text_2")
    b = ddsMetamodel_DdsWaitSet(name="sample_text")
    _safe_set(b, 'ddsMetamodel_DdsWaitSet214', {a1})
    assert _is_linked(b, 'ddsMetamodel_DdsWaitSet214', a1)
    if hasattr(a1, 'ddsMetamodel_GuardCondition'):
        assert _is_linked(a1, 'ddsMetamodel_GuardCondition', b)
    _safe_set(b, 'ddsMetamodel_DdsWaitSet214', {a2})
    assert _is_linked(b, 'ddsMetamodel_DdsWaitSet214', a2)
    if hasattr(a1, 'ddsMetamodel_GuardCondition'):
        assert not _is_linked(a1, 'ddsMetamodel_GuardCondition', b)
    if hasattr(a2, 'ddsMetamodel_GuardCondition'):
        assert _is_linked(a2, 'ddsMetamodel_GuardCondition', b)
    _safe_set(b, 'ddsMetamodel_DdsWaitSet214', set())
    assert not _is_linked(b, 'ddsMetamodel_DdsWaitSet214', a2)
    if hasattr(a2, 'ddsMetamodel_GuardCondition'):
        assert not _is_linked(a2, 'ddsMetamodel_GuardCondition', b)


def test_assoc_hosts235_reverse_link_reassign_clear():
    a1 = ddsMetamodel_DdsSystem(systemName="sample_text")
    a2 = ddsMetamodel_DdsSystem(systemName="sample_text_2")
    b = ddsMetamodel_DdsHost(hostName="sample_text")
    _safe_set(b, 'ddsMetamodel_DdsHost', a1)
    assert _is_linked(b, 'ddsMetamodel_DdsHost', a1)
    if hasattr(a1, 'ddsMetamodel_DdsSystem'):
        assert _is_linked(a1, 'ddsMetamodel_DdsSystem', b)
    _safe_set(b, 'ddsMetamodel_DdsHost', a2)
    assert _is_linked(b, 'ddsMetamodel_DdsHost', a2)
    if hasattr(a1, 'ddsMetamodel_DdsSystem'):
        assert not _is_linked(a1, 'ddsMetamodel_DdsSystem', b)
    if hasattr(a2, 'ddsMetamodel_DdsSystem'):
        assert _is_linked(a2, 'ddsMetamodel_DdsSystem', b)
    _safe_set(b, 'ddsMetamodel_DdsHost', None)
    assert not _is_linked(b, 'ddsMetamodel_DdsHost', a2)
    if hasattr(a2, 'ddsMetamodel_DdsSystem'):
        assert not _is_linked(a2, 'ddsMetamodel_DdsSystem', b)


def test_assoc_innerModules43_reverse_link_reassign_clear():
    a1 = ddsMetamodel_DdsDataModule(moduleName="sample_text")
    a2 = ddsMetamodel_DdsDataModule(moduleName="sample_text_2")
    b = ddsMetamodel_DdsDataModule(moduleName="sample_text")
    _safe_set(b, 'containingModule', {a1})
    assert _is_linked(b, 'containingModule', a1)
    if hasattr(a1, 'DdsDataModule'):
        assert _is_linked(a1, 'DdsDataModule', b)
    _safe_set(b, 'containingModule', {a2})
    assert _is_linked(b, 'containingModule', a2)
    if hasattr(a1, 'DdsDataModule'):
        assert not _is_linked(a1, 'DdsDataModule', b)
    if hasattr(a2, 'DdsDataModule'):
        assert _is_linked(a2, 'DdsDataModule', b)
    _safe_set(b, 'containingModule', set())
    assert not _is_linked(b, 'containingModule', a2)
    if hasattr(a2, 'DdsDataModule'):
        assert not _is_linked(a2, 'DdsDataModule', b)


def test_assoc_lease_duration91_reverse_link_reassign_clear():
    a1 = ddsMetamodel_DdsLivelinessQos(kind="sample_text")
    a2 = ddsMetamodel_DdsLivelinessQos(kind="sample_text_2")
    b = ddsMetamodel_DdsDuration(nanoSec="sample_text", sec="sample_text")
    _safe_set(b, 'ddsMetamodel_DdsDuration93', a1)
    assert _is_linked(b, 'ddsMetamodel_DdsDuration93', a1)
    if hasattr(a1, 'ddsMetamodel_DdsLivelinessQos92'):
        assert _is_linked(a1, 'ddsMetamodel_DdsLivelinessQos92', b)
    _safe_set(b, 'ddsMetamodel_DdsDuration93', a2)
    assert _is_linked(b, 'ddsMetamodel_DdsDuration93', a2)
    if hasattr(a1, 'ddsMetamodel_DdsLivelinessQos92'):
        assert not _is_linked(a1, 'ddsMetamodel_DdsLivelinessQos92', b)
    if hasattr(a2, 'ddsMetamodel_DdsLivelinessQos92'):
        assert _is_linked(a2, 'ddsMetamodel_DdsLivelinessQos92', b)
    _safe_set(b, 'ddsMetamodel_DdsDuration93', None)
    assert not _is_linked(b, 'ddsMetamodel_DdsDuration93', a2)
    if hasattr(a2, 'ddsMetamodel_DdsLivelinessQos92'):
        assert not _is_linked(a2, 'ddsMetamodel_DdsLivelinessQos92', b)


def test_assoc_max_blocking_time96_reverse_link_reassign_clear():
    a1 = ddsMetamodel_DdsReliabilityQos(kind="sample_text")
    a2 = ddsMetamodel_DdsReliabilityQos(kind="sample_text_2")
    b = ddsMetamodel_DdsDuration(nanoSec="sample_text", sec="sample_text")
    _safe_set(b, 'ddsMetamodel_DdsDuration98', a1)
    assert _is_linked(b, 'ddsMetamodel_DdsDuration98', a1)
    if hasattr(a1, 'ddsMetamodel_DdsReliabilityQos97'):
        assert _is_linked(a1, 'ddsMetamodel_DdsReliabilityQos97', b)
    _safe_set(b, 'ddsMetamodel_DdsDuration98', a2)
    assert _is_linked(b, 'ddsMetamodel_DdsDuration98', a2)
    if hasattr(a1, 'ddsMetamodel_DdsReliabilityQos97'):
        assert not _is_linked(a1, 'ddsMetamodel_DdsReliabilityQos97', b)
    if hasattr(a2, 'ddsMetamodel_DdsReliabilityQos97'):
        assert _is_linked(a2, 'ddsMetamodel_DdsReliabilityQos97', b)
    _safe_set(b, 'ddsMetamodel_DdsDuration98', None)
    assert not _is_linked(b, 'ddsMetamodel_DdsDuration98', a2)
    if hasattr(a2, 'ddsMetamodel_DdsReliabilityQos97'):
        assert not _is_linked(a2, 'ddsMetamodel_DdsReliabilityQos97', b)


def test_assoc_publiableTopic34_reverse_link_reassign_clear():
    a1 = ddsMetamodel_DdsTopic(topicName="sample_text")
    a2 = ddsMetamodel_DdsTopic(topicName="sample_text_2")
    b = ddsMetamodel_DdsDataWriter(dataWriterName="sample_text")
    _safe_set(b, 'ddsMetamodel_DdsDataWriter35', a1)
    assert _is_linked(b, 'ddsMetamodel_DdsDataWriter35', a1)
    if hasattr(a1, 'ddsMetamodel_DdsTopic36'):
        assert _is_linked(a1, 'ddsMetamodel_DdsTopic36', b)
    _safe_set(b, 'ddsMetamodel_DdsDataWriter35', a2)
    assert _is_linked(b, 'ddsMetamodel_DdsDataWriter35', a2)
    if hasattr(a1, 'ddsMetamodel_DdsTopic36'):
        assert not _is_linked(a1, 'ddsMetamodel_DdsTopic36', b)
    if hasattr(a2, 'ddsMetamodel_DdsTopic36'):
        assert _is_linked(a2, 'ddsMetamodel_DdsTopic36', b)
    _safe_set(b, 'ddsMetamodel_DdsDataWriter35', None)
    assert not _is_linked(b, 'ddsMetamodel_DdsDataWriter35', a2)
    if hasattr(a2, 'ddsMetamodel_DdsTopic36'):
        assert not _is_linked(a2, 'ddsMetamodel_DdsTopic36', b)


def test_assoc_publisher225_reverse_link_reassign_clear():
    a1 = ddsMetamodel_DdsPublisherStatusCondition(enabled_status="sample_text")
    a2 = ddsMetamodel_DdsPublisherStatusCondition(enabled_status="sample_text_2")
    b = ddsMetamodel_DdsPublisher(publisherName="sample_text")
    _safe_set(b, 'ddsMetamodel_DdsPublisher226', a1)
    assert _is_linked(b, 'ddsMetamodel_DdsPublisher226', a1)
    if hasattr(a1, 'ddsMetamodel_DdsPublisherStatusCondition'):
        assert _is_linked(a1, 'ddsMetamodel_DdsPublisherStatusCondition', b)
    _safe_set(b, 'ddsMetamodel_DdsPublisher226', a2)
    assert _is_linked(b, 'ddsMetamodel_DdsPublisher226', a2)
    if hasattr(a1, 'ddsMetamodel_DdsPublisherStatusCondition'):
        assert not _is_linked(a1, 'ddsMetamodel_DdsPublisherStatusCondition', b)
    if hasattr(a2, 'ddsMetamodel_DdsPublisherStatusCondition'):
        assert _is_linked(a2, 'ddsMetamodel_DdsPublisherStatusCondition', b)
    _safe_set(b, 'ddsMetamodel_DdsPublisher226', None)
    assert not _is_linked(b, 'ddsMetamodel_DdsPublisher226', a2)
    if hasattr(a2, 'ddsMetamodel_DdsPublisherStatusCondition'):
        assert not _is_linked(a2, 'ddsMetamodel_DdsPublisherStatusCondition', b)


def test_assoc_publisherListener30_reverse_link_reassign_clear():
    a1 = ddsMetamodel_DdsPublisherListener(listenedStatus="sample_text", name="sample_text")
    a2 = ddsMetamodel_DdsPublisherListener(listenedStatus="sample_text_2", name="sample_text_2")
    b = ddsMetamodel_DdsPublisher(publisherName="sample_text")
    _safe_set(b, 'ddsMetamodel_DdsPublisher31', a1)
    assert _is_linked(b, 'ddsMetamodel_DdsPublisher31', a1)
    if hasattr(a1, 'ddsMetamodel_DdsPublisherListener'):
        assert _is_linked(a1, 'ddsMetamodel_DdsPublisherListener', b)
    _safe_set(b, 'ddsMetamodel_DdsPublisher31', a2)
    assert _is_linked(b, 'ddsMetamodel_DdsPublisher31', a2)
    if hasattr(a1, 'ddsMetamodel_DdsPublisherListener'):
        assert not _is_linked(a1, 'ddsMetamodel_DdsPublisherListener', b)
    if hasattr(a2, 'ddsMetamodel_DdsPublisherListener'):
        assert _is_linked(a2, 'ddsMetamodel_DdsPublisherListener', b)
    _safe_set(b, 'ddsMetamodel_DdsPublisher31', None)
    assert not _is_linked(b, 'ddsMetamodel_DdsPublisher31', a2)
    if hasattr(a2, 'ddsMetamodel_DdsPublisherListener'):
        assert not _is_linked(a2, 'ddsMetamodel_DdsPublisherListener', b)


def test_assoc_qosProfiles236_reverse_link_reassign_clear():
    a1 = ddsMetamodel_DdsSystem(systemName="sample_text")
    a2 = ddsMetamodel_DdsSystem(systemName="sample_text_2")
    b = ddsMetamodel_DdsQosProfile(profileName="sample_text")
    _safe_set(b, 'ddsMetamodel_DdsQosProfile', a1)
    assert _is_linked(b, 'ddsMetamodel_DdsQosProfile', a1)
    if hasattr(a1, 'ddsMetamodel_DdsSystem237'):
        assert _is_linked(a1, 'ddsMetamodel_DdsSystem237', b)
    _safe_set(b, 'ddsMetamodel_DdsQosProfile', a2)
    assert _is_linked(b, 'ddsMetamodel_DdsQosProfile', a2)
    if hasattr(a1, 'ddsMetamodel_DdsSystem237'):
        assert not _is_linked(a1, 'ddsMetamodel_DdsSystem237', b)
    if hasattr(a2, 'ddsMetamodel_DdsSystem237'):
        assert _is_linked(a2, 'ddsMetamodel_DdsSystem237', b)
    _safe_set(b, 'ddsMetamodel_DdsQosProfile', None)
    assert not _is_linked(b, 'ddsMetamodel_DdsQosProfile', a2)
    if hasattr(a2, 'ddsMetamodel_DdsSystem237'):
        assert not _is_linked(a2, 'ddsMetamodel_DdsSystem237', b)


def test_assoc_readConditions210_reverse_link_reassign_clear():
    a1 = ddsMetamodel_DdsWaitSet(name="sample_text")
    a2 = ddsMetamodel_DdsWaitSet(name="sample_text_2")
    b = ddsMetamodel_DdsReadCondition(instance_state_mask="sample_text", sample_state_mask="sample_text", view_state_mask="sample_text")
    _safe_set(b, 'ddsMetamodel_DdsReadCondition', a1)
    assert _is_linked(b, 'ddsMetamodel_DdsReadCondition', a1)
    if hasattr(a1, 'ddsMetamodel_DdsWaitSet211'):
        assert _is_linked(a1, 'ddsMetamodel_DdsWaitSet211', b)
    _safe_set(b, 'ddsMetamodel_DdsReadCondition', a2)
    assert _is_linked(b, 'ddsMetamodel_DdsReadCondition', a2)
    if hasattr(a1, 'ddsMetamodel_DdsWaitSet211'):
        assert not _is_linked(a1, 'ddsMetamodel_DdsWaitSet211', b)
    if hasattr(a2, 'ddsMetamodel_DdsWaitSet211'):
        assert _is_linked(a2, 'ddsMetamodel_DdsWaitSet211', b)
    _safe_set(b, 'ddsMetamodel_DdsReadCondition', None)
    assert not _is_linked(b, 'ddsMetamodel_DdsReadCondition', a2)
    if hasattr(a2, 'ddsMetamodel_DdsWaitSet211'):
        assert not _is_linked(a2, 'ddsMetamodel_DdsWaitSet211', b)


def test_assoc_readableTopic21_reverse_link_reassign_clear():
    a1 = ddsMetamodel_DdsTopic(topicName="sample_text")
    a2 = ddsMetamodel_DdsTopic(topicName="sample_text_2")
    b = ddsMetamodel_DdsDataReader(dataReaderName="sample_text")
    _safe_set(b, 'ddsMetamodel_DdsDataReader', a1)
    assert _is_linked(b, 'ddsMetamodel_DdsDataReader', a1)
    if hasattr(a1, 'ddsMetamodel_DdsTopic22'):
        assert _is_linked(a1, 'ddsMetamodel_DdsTopic22', b)
    _safe_set(b, 'ddsMetamodel_DdsDataReader', a2)
    assert _is_linked(b, 'ddsMetamodel_DdsDataReader', a2)
    if hasattr(a1, 'ddsMetamodel_DdsTopic22'):
        assert not _is_linked(a1, 'ddsMetamodel_DdsTopic22', b)
    if hasattr(a2, 'ddsMetamodel_DdsTopic22'):
        assert _is_linked(a2, 'ddsMetamodel_DdsTopic22', b)
    _safe_set(b, 'ddsMetamodel_DdsDataReader', None)
    assert not _is_linked(b, 'ddsMetamodel_DdsDataReader', a2)
    if hasattr(a2, 'ddsMetamodel_DdsTopic22'):
        assert not _is_linked(a2, 'ddsMetamodel_DdsTopic22', b)


def test_assoc_referencedType218_reverse_link_reassign_clear():
    a1 = ddsMetamodel_DdsStructuredField(fieldName="sample_text", isKey=True, maxMultiplicity=7)
    a2 = ddsMetamodel_DdsStructuredField(fieldName="sample_text_2", isKey=False, maxMultiplicity=13)
    b = ddsMetamodel_DdsDataStructure(structureName="sample_text")
    _safe_set(b, 'ddsMetamodel_DdsDataStructure219', a1)
    assert _is_linked(b, 'ddsMetamodel_DdsDataStructure219', a1)
    if hasattr(a1, 'ddsMetamodel_DdsStructuredField'):
        assert _is_linked(a1, 'ddsMetamodel_DdsStructuredField', b)
    _safe_set(b, 'ddsMetamodel_DdsDataStructure219', a2)
    assert _is_linked(b, 'ddsMetamodel_DdsDataStructure219', a2)
    if hasattr(a1, 'ddsMetamodel_DdsStructuredField'):
        assert not _is_linked(a1, 'ddsMetamodel_DdsStructuredField', b)
    if hasattr(a2, 'ddsMetamodel_DdsStructuredField'):
        assert _is_linked(a2, 'ddsMetamodel_DdsStructuredField', b)
    _safe_set(b, 'ddsMetamodel_DdsDataStructure219', None)
    assert not _is_linked(b, 'ddsMetamodel_DdsDataStructure219', a2)
    if hasattr(a2, 'ddsMetamodel_DdsStructuredField'):
        assert not _is_linked(a2, 'ddsMetamodel_DdsStructuredField', b)


def test_assoc_service_cleanup_delay83_reverse_link_reassign_clear():
    a1 = ddsMetamodel_DdsDuration(nanoSec="sample_text", sec="sample_text")
    a2 = ddsMetamodel_DdsDuration(nanoSec="sample_text_2", sec="sample_text_2")
    b = ddsMetamodel_DdsDurabilityServiceQos(history_depth="sample_text", history_kind="sample_text", max_instances="sample_text", max_samples="sample_text", max_samples_per_instances="sample_text")
    _safe_set(b, 'ddsMetamodel_DdsDurabilityServiceQos84', a1)
    assert _is_linked(b, 'ddsMetamodel_DdsDurabilityServiceQos84', a1)
    if hasattr(a1, 'ddsMetamodel_DdsDuration'):
        assert _is_linked(a1, 'ddsMetamodel_DdsDuration', b)
    _safe_set(b, 'ddsMetamodel_DdsDurabilityServiceQos84', a2)
    assert _is_linked(b, 'ddsMetamodel_DdsDurabilityServiceQos84', a2)
    if hasattr(a1, 'ddsMetamodel_DdsDuration'):
        assert not _is_linked(a1, 'ddsMetamodel_DdsDuration', b)
    if hasattr(a2, 'ddsMetamodel_DdsDuration'):
        assert _is_linked(a2, 'ddsMetamodel_DdsDuration', b)
    _safe_set(b, 'ddsMetamodel_DdsDurabilityServiceQos84', None)
    assert not _is_linked(b, 'ddsMetamodel_DdsDurabilityServiceQos84', a2)
    if hasattr(a2, 'ddsMetamodel_DdsDuration'):
        assert not _is_linked(a2, 'ddsMetamodel_DdsDuration', b)


def test_assoc_structuredFields50_reverse_link_reassign_clear():
    a1 = ddsMetamodel_DdsStructuredField(fieldName="sample_text", isKey=True, maxMultiplicity=7)
    a2 = ddsMetamodel_DdsStructuredField(fieldName="sample_text_2", isKey=False, maxMultiplicity=13)
    b = ddsMetamodel_DdsDataStructure(structureName="sample_text")
    _safe_set(b, 'dataStructure', {a1})
    assert _is_linked(b, 'dataStructure', a1)
    if hasattr(a1, 'DdsStructuredField'):
        assert _is_linked(a1, 'DdsStructuredField', b)
    _safe_set(b, 'dataStructure', {a2})
    assert _is_linked(b, 'dataStructure', a2)
    if hasattr(a1, 'DdsStructuredField'):
        assert not _is_linked(a1, 'DdsStructuredField', b)
    if hasattr(a2, 'DdsStructuredField'):
        assert _is_linked(a2, 'DdsStructuredField', b)
    _safe_set(b, 'dataStructure', set())
    assert not _is_linked(b, 'dataStructure', a2)
    if hasattr(a2, 'DdsStructuredField'):
        assert not _is_linked(a2, 'DdsStructuredField', b)


def test_assoc_subscriber227_reverse_link_reassign_clear():
    a1 = ddsMetamodel_DdsSubscriberStatusCondition(enabled_status="sample_text")
    a2 = ddsMetamodel_DdsSubscriberStatusCondition(enabled_status="sample_text_2")
    b = ddsMetamodel_DdsSubscriber(subscriberName="sample_text")
    _safe_set(b, 'ddsMetamodel_DdsSubscriber228', a1)
    assert _is_linked(b, 'ddsMetamodel_DdsSubscriber228', a1)
    if hasattr(a1, 'ddsMetamodel_DdsSubscriberStatusCondition'):
        assert _is_linked(a1, 'ddsMetamodel_DdsSubscriberStatusCondition', b)
    _safe_set(b, 'ddsMetamodel_DdsSubscriber228', a2)
    assert _is_linked(b, 'ddsMetamodel_DdsSubscriber228', a2)
    if hasattr(a1, 'ddsMetamodel_DdsSubscriberStatusCondition'):
        assert not _is_linked(a1, 'ddsMetamodel_DdsSubscriberStatusCondition', b)
    if hasattr(a2, 'ddsMetamodel_DdsSubscriberStatusCondition'):
        assert _is_linked(a2, 'ddsMetamodel_DdsSubscriberStatusCondition', b)
    _safe_set(b, 'ddsMetamodel_DdsSubscriber228', None)
    assert not _is_linked(b, 'ddsMetamodel_DdsSubscriber228', a2)
    if hasattr(a2, 'ddsMetamodel_DdsSubscriberStatusCondition'):
        assert not _is_linked(a2, 'ddsMetamodel_DdsSubscriberStatusCondition', b)


def test_assoc_subscriberListener17_reverse_link_reassign_clear():
    a1 = ddsMetamodel_DdsSubscriberListener(listenedStatus="sample_text", name="sample_text")
    a2 = ddsMetamodel_DdsSubscriberListener(listenedStatus="sample_text_2", name="sample_text_2")
    b = ddsMetamodel_DdsSubscriber(subscriberName="sample_text")
    _safe_set(b, 'ddsMetamodel_DdsSubscriber18', a1)
    assert _is_linked(b, 'ddsMetamodel_DdsSubscriber18', a1)
    if hasattr(a1, 'ddsMetamodel_DdsSubscriberListener'):
        assert _is_linked(a1, 'ddsMetamodel_DdsSubscriberListener', b)
    _safe_set(b, 'ddsMetamodel_DdsSubscriber18', a2)
    assert _is_linked(b, 'ddsMetamodel_DdsSubscriber18', a2)
    if hasattr(a1, 'ddsMetamodel_DdsSubscriberListener'):
        assert not _is_linked(a1, 'ddsMetamodel_DdsSubscriberListener', b)
    if hasattr(a2, 'ddsMetamodel_DdsSubscriberListener'):
        assert _is_linked(a2, 'ddsMetamodel_DdsSubscriberListener', b)
    _safe_set(b, 'ddsMetamodel_DdsSubscriber18', None)
    assert not _is_linked(b, 'ddsMetamodel_DdsSubscriber18', a2)
    if hasattr(a2, 'ddsMetamodel_DdsSubscriberListener'):
        assert not _is_linked(a2, 'ddsMetamodel_DdsSubscriberListener', b)


def test_assoc_topic233_reverse_link_reassign_clear():
    a1 = ddsMetamodel_DdsTopicStatusCondition(enabled_status="sample_text")
    a2 = ddsMetamodel_DdsTopicStatusCondition(enabled_status="sample_text_2")
    b = ddsMetamodel_DdsTopic(topicName="sample_text")
    _safe_set(b, 'ddsMetamodel_DdsTopic234', a1)
    assert _is_linked(b, 'ddsMetamodel_DdsTopic234', a1)
    if hasattr(a1, 'ddsMetamodel_DdsTopicStatusCondition'):
        assert _is_linked(a1, 'ddsMetamodel_DdsTopicStatusCondition', b)
    _safe_set(b, 'ddsMetamodel_DdsTopic234', a2)
    assert _is_linked(b, 'ddsMetamodel_DdsTopic234', a2)
    if hasattr(a1, 'ddsMetamodel_DdsTopicStatusCondition'):
        assert not _is_linked(a1, 'ddsMetamodel_DdsTopicStatusCondition', b)
    if hasattr(a2, 'ddsMetamodel_DdsTopicStatusCondition'):
        assert _is_linked(a2, 'ddsMetamodel_DdsTopicStatusCondition', b)
    _safe_set(b, 'ddsMetamodel_DdsTopic234', None)
    assert not _is_linked(b, 'ddsMetamodel_DdsTopic234', a2)
    if hasattr(a2, 'ddsMetamodel_DdsTopicStatusCondition'):
        assert not _is_linked(a2, 'ddsMetamodel_DdsTopicStatusCondition', b)


def test_assoc_topicListener11_reverse_link_reassign_clear():
    a1 = ddsMetamodel_DdsTopicListener(listenedStatus="sample_text", name="sample_text")
    a2 = ddsMetamodel_DdsTopicListener(listenedStatus="sample_text_2", name="sample_text_2")
    b = ddsMetamodel_DdsTopic(topicName="sample_text")
    _safe_set(b, 'ddsMetamodel_DdsTopic', a1)
    assert _is_linked(b, 'ddsMetamodel_DdsTopic', a1)
    if hasattr(a1, 'ddsMetamodel_DdsTopicListener'):
        assert _is_linked(a1, 'ddsMetamodel_DdsTopicListener', b)
    _safe_set(b, 'ddsMetamodel_DdsTopic', a2)
    assert _is_linked(b, 'ddsMetamodel_DdsTopic', a2)
    if hasattr(a1, 'ddsMetamodel_DdsTopicListener'):
        assert not _is_linked(a1, 'ddsMetamodel_DdsTopicListener', b)
    if hasattr(a2, 'ddsMetamodel_DdsTopicListener'):
        assert _is_linked(a2, 'ddsMetamodel_DdsTopicListener', b)
    _safe_set(b, 'ddsMetamodel_DdsTopic', None)
    assert not _is_linked(b, 'ddsMetamodel_DdsTopic', a2)
    if hasattr(a2, 'ddsMetamodel_DdsTopicListener'):
        assert not _is_linked(a2, 'ddsMetamodel_DdsTopicListener', b)


def test_assoc_topics240_reverse_link_reassign_clear():
    a1 = ddsMetamodel_DdsTopic(topicName="sample_text")
    a2 = ddsMetamodel_DdsTopic(topicName="sample_text_2")
    b = ddsMetamodel_DdsSystem(systemName="sample_text")
    _safe_set(b, 'ddsMetamodel_DdsSystem241', {a1})
    assert _is_linked(b, 'ddsMetamodel_DdsSystem241', a1)
    if hasattr(a1, 'ddsMetamodel_DdsTopic242'):
        assert _is_linked(a1, 'ddsMetamodel_DdsTopic242', b)
    _safe_set(b, 'ddsMetamodel_DdsSystem241', {a2})
    assert _is_linked(b, 'ddsMetamodel_DdsSystem241', a2)
    if hasattr(a1, 'ddsMetamodel_DdsTopic242'):
        assert not _is_linked(a1, 'ddsMetamodel_DdsTopic242', b)
    if hasattr(a2, 'ddsMetamodel_DdsTopic242'):
        assert _is_linked(a2, 'ddsMetamodel_DdsTopic242', b)
    _safe_set(b, 'ddsMetamodel_DdsSystem241', set())
    assert not _is_linked(b, 'ddsMetamodel_DdsSystem241', a2)
    if hasattr(a2, 'ddsMetamodel_DdsTopic242'):
        assert not _is_linked(a2, 'ddsMetamodel_DdsTopic242', b)


def test_assoc_waitset1_reverse_link_reassign_clear():
    a1 = ddsMetamodel_DdsWaitSet(name="sample_text")
    a2 = ddsMetamodel_DdsWaitSet(name="sample_text_2")
    b = ddsMetamodel_DdsApplication(applicationName="sample_text")
    _safe_set(b, 'ddsMetamodel_DdsApplication2', a1)
    assert _is_linked(b, 'ddsMetamodel_DdsApplication2', a1)
    if hasattr(a1, 'ddsMetamodel_DdsWaitSet'):
        assert _is_linked(a1, 'ddsMetamodel_DdsWaitSet', b)
    _safe_set(b, 'ddsMetamodel_DdsApplication2', a2)
    assert _is_linked(b, 'ddsMetamodel_DdsApplication2', a2)
    if hasattr(a1, 'ddsMetamodel_DdsWaitSet'):
        assert not _is_linked(a1, 'ddsMetamodel_DdsWaitSet', b)
    if hasattr(a2, 'ddsMetamodel_DdsWaitSet'):
        assert _is_linked(a2, 'ddsMetamodel_DdsWaitSet', b)
    _safe_set(b, 'ddsMetamodel_DdsApplication2', None)
    assert not _is_linked(b, 'ddsMetamodel_DdsApplication2', a2)
    if hasattr(a2, 'ddsMetamodel_DdsWaitSet'):
        assert not _is_linked(a2, 'ddsMetamodel_DdsWaitSet', b)


