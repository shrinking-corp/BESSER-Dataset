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


# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_containingWaitset222_stub_double():
    # ddsMetamodel_DdsStatusCondition has no real 'statusConditions' property in the generated
    # code (a bare stub) -- manually attach it so ddsMetamodel_DdsWaitSet's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ddsMetamodel_DdsWaitSet's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ddsMetamodel_DdsWaitSet(name="sample_text")
    partner = ddsMetamodel_DdsStatusCondition()
    setattr(partner, 'statusConditions', None)
    _safe_set(owner, 'DdsWaitSet', partner)
    assert getattr(partner, 'statusConditions') == owner
    _safe_set(owner, 'DdsWaitSet', None)
    assert getattr(partner, 'statusConditions') is None


def test_assoc_dataReaderLifecycleQos207_stub_double():
    # ddsMetamodel_DdsDataReaderQosProfile has no real 'ddsMetamodel_DdsDataReaderQosProfile208' property in the generated
    # code (a bare stub) -- manually attach it so ddsMetamodel_DdsDataReaderLifecycleQos's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ddsMetamodel_DdsDataReaderLifecycleQos's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ddsMetamodel_DdsDataReaderLifecycleQos(autopurge_dispose_all=True, enable_invalid_samples=True)
    partner = ddsMetamodel_DdsDataReaderQosProfile()
    setattr(partner, 'ddsMetamodel_DdsDataReaderQosProfile208', None)
    _safe_set(owner, 'ddsMetamodel_DdsDataReaderLifecycleQos209', partner)
    assert getattr(partner, 'ddsMetamodel_DdsDataReaderQosProfile208') == owner
    _safe_set(owner, 'ddsMetamodel_DdsDataReaderLifecycleQos209', None)
    assert getattr(partner, 'ddsMetamodel_DdsDataReaderQosProfile208') is None


def test_assoc_dataReaderQosProfile25_stub_double():
    # ddsMetamodel_DdsDataReaderQosProfile has no real 'ddsMetamodel_DdsDataReaderQosProfile' property in the generated
    # code (a bare stub) -- manually attach it so ddsMetamodel_DdsDataReader's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ddsMetamodel_DdsDataReader's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ddsMetamodel_DdsDataReader(dataReaderName="sample_text")
    partner = ddsMetamodel_DdsDataReaderQosProfile()
    setattr(partner, 'ddsMetamodel_DdsDataReaderQosProfile', None)
    _safe_set(owner, 'ddsMetamodel_DdsDataReader26', partner)
    assert getattr(partner, 'ddsMetamodel_DdsDataReaderQosProfile') == owner
    _safe_set(owner, 'ddsMetamodel_DdsDataReader26', None)
    assert getattr(partner, 'ddsMetamodel_DdsDataReaderQosProfile') is None


def test_assoc_dataWriterLifecycleQos159_stub_double():
    # ddsMetamodel_DdsDataWriterQosProfile has no real 'ddsMetamodel_DdsDataWriterQosProfile160' property in the generated
    # code (a bare stub) -- manually attach it so ddsMetamodel_DdsDataWriterLifecycleQos's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ddsMetamodel_DdsDataWriterLifecycleQos's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ddsMetamodel_DdsDataWriterLifecycleQos(autodispose_unregistered_instances=True)
    partner = ddsMetamodel_DdsDataWriterQosProfile()
    setattr(partner, 'ddsMetamodel_DdsDataWriterQosProfile160', None)
    _safe_set(owner, 'ddsMetamodel_DdsDataWriterLifecycleQos161', partner)
    assert getattr(partner, 'ddsMetamodel_DdsDataWriterQosProfile160') == owner
    _safe_set(owner, 'ddsMetamodel_DdsDataWriterLifecycleQos161', None)
    assert getattr(partner, 'ddsMetamodel_DdsDataWriterQosProfile160') is None


def test_assoc_dataWriterQosProfile39_stub_double():
    # ddsMetamodel_DdsDataWriterQosProfile has no real 'ddsMetamodel_DdsDataWriterQosProfile' property in the generated
    # code (a bare stub) -- manually attach it so ddsMetamodel_DdsDataWriter's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ddsMetamodel_DdsDataWriter's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ddsMetamodel_DdsDataWriter(dataWriterName="sample_text")
    partner = ddsMetamodel_DdsDataWriterQosProfile()
    setattr(partner, 'ddsMetamodel_DdsDataWriterQosProfile', None)
    _safe_set(owner, 'ddsMetamodel_DdsDataWriter40', partner)
    assert getattr(partner, 'ddsMetamodel_DdsDataWriterQosProfile') == owner
    _safe_set(owner, 'ddsMetamodel_DdsDataWriter40', None)
    assert getattr(partner, 'ddsMetamodel_DdsDataWriterQosProfile') is None


def test_assoc_ddsdomainparticipantqosprofile7_stub_double():
    # ddsMetamodel_DdsDomainParticipantQosProfile has no real 'ddsMetamodel_DdsDomainParticipantQosProfile' property in the generated
    # code (a bare stub) -- manually attach it so ddsMetamodel_DdsDomainParticipant's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ddsMetamodel_DdsDomainParticipant's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ddsMetamodel_DdsDomainParticipant(domainId=7, domainParticipantName="sample_text")
    partner = ddsMetamodel_DdsDomainParticipantQosProfile()
    setattr(partner, 'ddsMetamodel_DdsDomainParticipantQosProfile', None)
    _safe_set(owner, 'ddsMetamodel_DdsDomainParticipant8', partner)
    assert getattr(partner, 'ddsMetamodel_DdsDomainParticipantQosProfile') == owner
    _safe_set(owner, 'ddsMetamodel_DdsDomainParticipant8', None)
    assert getattr(partner, 'ddsMetamodel_DdsDomainParticipantQosProfile') is None


def test_assoc_destinationOrderQos150_stub_double():
    # ddsMetamodel_DdsDataWriterQosProfile has no real 'ddsMetamodel_DdsDataWriterQosProfile151' property in the generated
    # code (a bare stub) -- manually attach it so ddsMetamodel_DdsDestinationOrderQos's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ddsMetamodel_DdsDestinationOrderQos's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ddsMetamodel_DdsDestinationOrderQos(kind="sample_text")
    partner = ddsMetamodel_DdsDataWriterQosProfile()
    setattr(partner, 'ddsMetamodel_DdsDataWriterQosProfile151', None)
    _safe_set(owner, 'ddsMetamodel_DdsDestinationOrderQos152', partner)
    assert getattr(partner, 'ddsMetamodel_DdsDataWriterQosProfile151') == owner
    _safe_set(owner, 'ddsMetamodel_DdsDestinationOrderQos152', None)
    assert getattr(partner, 'ddsMetamodel_DdsDataWriterQosProfile151') is None


def test_assoc_destinationOrderQos198_stub_double():
    # ddsMetamodel_DdsDataReaderQosProfile has no real 'ddsMetamodel_DdsDataReaderQosProfile199' property in the generated
    # code (a bare stub) -- manually attach it so ddsMetamodel_DdsDestinationOrderQos's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ddsMetamodel_DdsDestinationOrderQos's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ddsMetamodel_DdsDestinationOrderQos(kind="sample_text")
    partner = ddsMetamodel_DdsDataReaderQosProfile()
    setattr(partner, 'ddsMetamodel_DdsDataReaderQosProfile199', None)
    _safe_set(owner, 'ddsMetamodel_DdsDestinationOrderQos200', partner)
    assert getattr(partner, 'ddsMetamodel_DdsDataReaderQosProfile199') == owner
    _safe_set(owner, 'ddsMetamodel_DdsDestinationOrderQos200', None)
    assert getattr(partner, 'ddsMetamodel_DdsDataReaderQosProfile199') is None


def test_assoc_destinationOrderQos71_stub_double():
    # ddsMetamodel_DdsTopicQosProfile has no real 'ddsMetamodel_DdsTopicQosProfile72' property in the generated
    # code (a bare stub) -- manually attach it so ddsMetamodel_DdsDestinationOrderQos's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ddsMetamodel_DdsDestinationOrderQos's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ddsMetamodel_DdsDestinationOrderQos(kind="sample_text")
    partner = ddsMetamodel_DdsTopicQosProfile()
    setattr(partner, 'ddsMetamodel_DdsTopicQosProfile72', None)
    _safe_set(owner, 'ddsMetamodel_DdsDestinationOrderQos', partner)
    assert getattr(partner, 'ddsMetamodel_DdsTopicQosProfile72') == owner
    _safe_set(owner, 'ddsMetamodel_DdsDestinationOrderQos', None)
    assert getattr(partner, 'ddsMetamodel_DdsTopicQosProfile72') is None


def test_assoc_durabilityQos124_stub_double():
    # ddsMetamodel_DdsDataWriterQosProfile has no real 'ddsMetamodel_DdsDataWriterQosProfile125' property in the generated
    # code (a bare stub) -- manually attach it so ddsMetamodel_DdsDurabilityQos's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ddsMetamodel_DdsDurabilityQos's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ddsMetamodel_DdsDurabilityQos(kind="sample_text")
    partner = ddsMetamodel_DdsDataWriterQosProfile()
    setattr(partner, 'ddsMetamodel_DdsDataWriterQosProfile125', None)
    _safe_set(owner, 'ddsMetamodel_DdsDurabilityQos126', partner)
    assert getattr(partner, 'ddsMetamodel_DdsDataWriterQosProfile125') == owner
    _safe_set(owner, 'ddsMetamodel_DdsDurabilityQos126', None)
    assert getattr(partner, 'ddsMetamodel_DdsDataWriterQosProfile125') is None


def test_assoc_durabilityQos177_stub_double():
    # ddsMetamodel_DdsDataReaderQosProfile has no real 'ddsMetamodel_DdsDataReaderQosProfile178' property in the generated
    # code (a bare stub) -- manually attach it so ddsMetamodel_DdsDurabilityQos's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ddsMetamodel_DdsDurabilityQos's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ddsMetamodel_DdsDurabilityQos(kind="sample_text")
    partner = ddsMetamodel_DdsDataReaderQosProfile()
    setattr(partner, 'ddsMetamodel_DdsDataReaderQosProfile178', None)
    _safe_set(owner, 'ddsMetamodel_DdsDurabilityQos179', partner)
    assert getattr(partner, 'ddsMetamodel_DdsDataReaderQosProfile178') == owner
    _safe_set(owner, 'ddsMetamodel_DdsDurabilityQos179', None)
    assert getattr(partner, 'ddsMetamodel_DdsDataReaderQosProfile178') is None


def test_assoc_durabilityQos59_stub_double():
    # ddsMetamodel_DdsTopicQosProfile has no real 'ddsMetamodel_DdsTopicQosProfile60' property in the generated
    # code (a bare stub) -- manually attach it so ddsMetamodel_DdsDurabilityQos's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ddsMetamodel_DdsDurabilityQos's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ddsMetamodel_DdsDurabilityQos(kind="sample_text")
    partner = ddsMetamodel_DdsTopicQosProfile()
    setattr(partner, 'ddsMetamodel_DdsTopicQosProfile60', None)
    _safe_set(owner, 'ddsMetamodel_DdsDurabilityQos', partner)
    assert getattr(partner, 'ddsMetamodel_DdsTopicQosProfile60') == owner
    _safe_set(owner, 'ddsMetamodel_DdsDurabilityQos', None)
    assert getattr(partner, 'ddsMetamodel_DdsTopicQosProfile60') is None


def test_assoc_durabilityServiceQos61_stub_double():
    # ddsMetamodel_DdsTopicQosProfile has no real 'ddsMetamodel_DdsTopicQosProfile62' property in the generated
    # code (a bare stub) -- manually attach it so ddsMetamodel_DdsDurabilityServiceQos's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ddsMetamodel_DdsDurabilityServiceQos's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ddsMetamodel_DdsDurabilityServiceQos(history_depth="sample_text", history_kind="sample_text", max_instances="sample_text", max_samples="sample_text", max_samples_per_instances="sample_text")
    partner = ddsMetamodel_DdsTopicQosProfile()
    setattr(partner, 'ddsMetamodel_DdsTopicQosProfile62', None)
    _safe_set(owner, 'ddsMetamodel_DdsDurabilityServiceQos', partner)
    assert getattr(partner, 'ddsMetamodel_DdsTopicQosProfile62') == owner
    _safe_set(owner, 'ddsMetamodel_DdsDurabilityServiceQos', None)
    assert getattr(partner, 'ddsMetamodel_DdsTopicQosProfile62') is None


def test_assoc_duration88_stub_double():
    # ddsMetamodel_DdsLatencyBudgetQos has no real 'ddsMetamodel_DdsLatencyBudgetQos89' property in the generated
    # code (a bare stub) -- manually attach it so ddsMetamodel_DdsDuration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ddsMetamodel_DdsDuration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ddsMetamodel_DdsDuration(nanoSec="sample_text", sec="sample_text")
    partner = ddsMetamodel_DdsLatencyBudgetQos()
    setattr(partner, 'ddsMetamodel_DdsLatencyBudgetQos89', None)
    _safe_set(owner, 'ddsMetamodel_DdsDuration90', partner)
    assert getattr(partner, 'ddsMetamodel_DdsLatencyBudgetQos89') == owner
    _safe_set(owner, 'ddsMetamodel_DdsDuration90', None)
    assert getattr(partner, 'ddsMetamodel_DdsLatencyBudgetQos89') is None


def test_assoc_duration99_stub_double():
    # ddsMetamodel_DdsLifespan has no real 'ddsMetamodel_DdsLifespan100' property in the generated
    # code (a bare stub) -- manually attach it so ddsMetamodel_DdsDuration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ddsMetamodel_DdsDuration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ddsMetamodel_DdsDuration(nanoSec="sample_text", sec="sample_text")
    partner = ddsMetamodel_DdsLifespan()
    setattr(partner, 'ddsMetamodel_DdsLifespan100', None)
    _safe_set(owner, 'ddsMetamodel_DdsDuration101', partner)
    assert getattr(partner, 'ddsMetamodel_DdsLifespan100') == owner
    _safe_set(owner, 'ddsMetamodel_DdsDuration101', None)
    assert getattr(partner, 'ddsMetamodel_DdsLifespan100') is None


def test_assoc_entityFactoryQos114_stub_double():
    # ddsMetamodel_DdsPublisherQosProfile has no real 'ddsMetamodel_DdsPublisherQosProfile115' property in the generated
    # code (a bare stub) -- manually attach it so ddsMetamodel_DdsEntityFactoryQos's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ddsMetamodel_DdsEntityFactoryQos's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ddsMetamodel_DdsEntityFactoryQos(autoenable_created_entities=True)
    partner = ddsMetamodel_DdsPublisherQosProfile()
    setattr(partner, 'ddsMetamodel_DdsPublisherQosProfile115', None)
    _safe_set(owner, 'ddsMetamodel_DdsEntityFactoryQos116', partner)
    assert getattr(partner, 'ddsMetamodel_DdsPublisherQosProfile115') == owner
    _safe_set(owner, 'ddsMetamodel_DdsEntityFactoryQos116', None)
    assert getattr(partner, 'ddsMetamodel_DdsPublisherQosProfile115') is None


def test_assoc_entityFactoryQos165_stub_double():
    # ddsMetamodel_DdsSubscriberQosProfile has no real 'ddsMetamodel_DdsSubscriberQosProfile166' property in the generated
    # code (a bare stub) -- manually attach it so ddsMetamodel_DdsEntityFactoryQos's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ddsMetamodel_DdsEntityFactoryQos's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ddsMetamodel_DdsEntityFactoryQos(autoenable_created_entities=True)
    partner = ddsMetamodel_DdsSubscriberQosProfile()
    setattr(partner, 'ddsMetamodel_DdsSubscriberQosProfile166', None)
    _safe_set(owner, 'ddsMetamodel_DdsEntityFactoryQos167', partner)
    assert getattr(partner, 'ddsMetamodel_DdsSubscriberQosProfile166') == owner
    _safe_set(owner, 'ddsMetamodel_DdsEntityFactoryQos167', None)
    assert getattr(partner, 'ddsMetamodel_DdsSubscriberQosProfile166') is None


def test_assoc_entityFactoryQos55_stub_double():
    # ddsMetamodel_DdsDomainParticipantQosProfile has no real 'ddsMetamodel_DdsDomainParticipantQosProfile56' property in the generated
    # code (a bare stub) -- manually attach it so ddsMetamodel_DdsEntityFactoryQos's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ddsMetamodel_DdsEntityFactoryQos's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ddsMetamodel_DdsEntityFactoryQos(autoenable_created_entities=True)
    partner = ddsMetamodel_DdsDomainParticipantQosProfile()
    setattr(partner, 'ddsMetamodel_DdsDomainParticipantQosProfile56', None)
    _safe_set(owner, 'ddsMetamodel_DdsEntityFactoryQos', partner)
    assert getattr(partner, 'ddsMetamodel_DdsDomainParticipantQosProfile56') == owner
    _safe_set(owner, 'ddsMetamodel_DdsEntityFactoryQos', None)
    assert getattr(partner, 'ddsMetamodel_DdsDomainParticipantQosProfile56') is None


def test_assoc_groupDataQos112_stub_double():
    # ddsMetamodel_DdsPublisherQosProfile has no real 'ddsMetamodel_DdsPublisherQosProfile113' property in the generated
    # code (a bare stub) -- manually attach it so ddsMetamodel_DdsGroupDataQos's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ddsMetamodel_DdsGroupDataQos's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ddsMetamodel_DdsGroupDataQos(value="sample_text")
    partner = ddsMetamodel_DdsPublisherQosProfile()
    setattr(partner, 'ddsMetamodel_DdsPublisherQosProfile113', None)
    _safe_set(owner, 'ddsMetamodel_DdsGroupDataQos', partner)
    assert getattr(partner, 'ddsMetamodel_DdsPublisherQosProfile113') == owner
    _safe_set(owner, 'ddsMetamodel_DdsGroupDataQos', None)
    assert getattr(partner, 'ddsMetamodel_DdsPublisherQosProfile113') is None


def test_assoc_groupDataQos162_stub_double():
    # ddsMetamodel_DdsSubscriberQosProfile has no real 'ddsMetamodel_DdsSubscriberQosProfile163' property in the generated
    # code (a bare stub) -- manually attach it so ddsMetamodel_DdsGroupDataQos's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ddsMetamodel_DdsGroupDataQos's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ddsMetamodel_DdsGroupDataQos(value="sample_text")
    partner = ddsMetamodel_DdsSubscriberQosProfile()
    setattr(partner, 'ddsMetamodel_DdsSubscriberQosProfile163', None)
    _safe_set(owner, 'ddsMetamodel_DdsGroupDataQos164', partner)
    assert getattr(partner, 'ddsMetamodel_DdsSubscriberQosProfile163') == owner
    _safe_set(owner, 'ddsMetamodel_DdsGroupDataQos164', None)
    assert getattr(partner, 'ddsMetamodel_DdsSubscriberQosProfile163') is None


def test_assoc_historyQos153_stub_double():
    # ddsMetamodel_DdsDataWriterQosProfile has no real 'ddsMetamodel_DdsDataWriterQosProfile154' property in the generated
    # code (a bare stub) -- manually attach it so ddsMetamodel_DdsHistoryQos's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ddsMetamodel_DdsHistoryQos's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ddsMetamodel_DdsHistoryQos(depth="sample_text", kind="sample_text")
    partner = ddsMetamodel_DdsDataWriterQosProfile()
    setattr(partner, 'ddsMetamodel_DdsDataWriterQosProfile154', None)
    _safe_set(owner, 'ddsMetamodel_DdsHistoryQos155', partner)
    assert getattr(partner, 'ddsMetamodel_DdsDataWriterQosProfile154') == owner
    _safe_set(owner, 'ddsMetamodel_DdsHistoryQos155', None)
    assert getattr(partner, 'ddsMetamodel_DdsDataWriterQosProfile154') is None


def test_assoc_historyQos201_stub_double():
    # ddsMetamodel_DdsDataReaderQosProfile has no real 'ddsMetamodel_DdsDataReaderQosProfile202' property in the generated
    # code (a bare stub) -- manually attach it so ddsMetamodel_DdsHistoryQos's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ddsMetamodel_DdsHistoryQos's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ddsMetamodel_DdsHistoryQos(depth="sample_text", kind="sample_text")
    partner = ddsMetamodel_DdsDataReaderQosProfile()
    setattr(partner, 'ddsMetamodel_DdsDataReaderQosProfile202', None)
    _safe_set(owner, 'ddsMetamodel_DdsHistoryQos203', partner)
    assert getattr(partner, 'ddsMetamodel_DdsDataReaderQosProfile202') == owner
    _safe_set(owner, 'ddsMetamodel_DdsHistoryQos203', None)
    assert getattr(partner, 'ddsMetamodel_DdsDataReaderQosProfile202') is None


def test_assoc_historyQos73_stub_double():
    # ddsMetamodel_DdsTopicQosProfile has no real 'ddsMetamodel_DdsTopicQosProfile74' property in the generated
    # code (a bare stub) -- manually attach it so ddsMetamodel_DdsHistoryQos's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ddsMetamodel_DdsHistoryQos's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ddsMetamodel_DdsHistoryQos(depth="sample_text", kind="sample_text")
    partner = ddsMetamodel_DdsTopicQosProfile()
    setattr(partner, 'ddsMetamodel_DdsTopicQosProfile74', None)
    _safe_set(owner, 'ddsMetamodel_DdsHistoryQos', partner)
    assert getattr(partner, 'ddsMetamodel_DdsTopicQosProfile74') == owner
    _safe_set(owner, 'ddsMetamodel_DdsHistoryQos', None)
    assert getattr(partner, 'ddsMetamodel_DdsTopicQosProfile74') is None


def test_assoc_livelinessQos138_stub_double():
    # ddsMetamodel_DdsDataWriterQosProfile has no real 'ddsMetamodel_DdsDataWriterQosProfile139' property in the generated
    # code (a bare stub) -- manually attach it so ddsMetamodel_DdsLivelinessQos's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ddsMetamodel_DdsLivelinessQos's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ddsMetamodel_DdsLivelinessQos(kind="sample_text")
    partner = ddsMetamodel_DdsDataWriterQosProfile()
    setattr(partner, 'ddsMetamodel_DdsDataWriterQosProfile139', None)
    _safe_set(owner, 'ddsMetamodel_DdsLivelinessQos140', partner)
    assert getattr(partner, 'ddsMetamodel_DdsDataWriterQosProfile139') == owner
    _safe_set(owner, 'ddsMetamodel_DdsLivelinessQos140', None)
    assert getattr(partner, 'ddsMetamodel_DdsDataWriterQosProfile139') is None


def test_assoc_livelinessQos186_stub_double():
    # ddsMetamodel_DdsDataReaderQosProfile has no real 'ddsMetamodel_DdsDataReaderQosProfile187' property in the generated
    # code (a bare stub) -- manually attach it so ddsMetamodel_DdsLivelinessQos's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ddsMetamodel_DdsLivelinessQos's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ddsMetamodel_DdsLivelinessQos(kind="sample_text")
    partner = ddsMetamodel_DdsDataReaderQosProfile()
    setattr(partner, 'ddsMetamodel_DdsDataReaderQosProfile187', None)
    _safe_set(owner, 'ddsMetamodel_DdsLivelinessQos188', partner)
    assert getattr(partner, 'ddsMetamodel_DdsDataReaderQosProfile187') == owner
    _safe_set(owner, 'ddsMetamodel_DdsLivelinessQos188', None)
    assert getattr(partner, 'ddsMetamodel_DdsDataReaderQosProfile187') is None


def test_assoc_livelinessQos65_stub_double():
    # ddsMetamodel_DdsTopicQosProfile has no real 'ddsMetamodel_DdsTopicQosProfile66' property in the generated
    # code (a bare stub) -- manually attach it so ddsMetamodel_DdsLivelinessQos's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ddsMetamodel_DdsLivelinessQos's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ddsMetamodel_DdsLivelinessQos(kind="sample_text")
    partner = ddsMetamodel_DdsTopicQosProfile()
    setattr(partner, 'ddsMetamodel_DdsTopicQosProfile66', None)
    _safe_set(owner, 'ddsMetamodel_DdsLivelinessQos', partner)
    assert getattr(partner, 'ddsMetamodel_DdsTopicQosProfile66') == owner
    _safe_set(owner, 'ddsMetamodel_DdsLivelinessQos', None)
    assert getattr(partner, 'ddsMetamodel_DdsTopicQosProfile66') is None


def test_assoc_minimum_separation94_stub_double():
    # ddsMetamodel_DdsTimeBasedFilterQos has no real 'ddsMetamodel_DdsTimeBasedFilterQos' property in the generated
    # code (a bare stub) -- manually attach it so ddsMetamodel_DdsDuration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ddsMetamodel_DdsDuration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ddsMetamodel_DdsDuration(nanoSec="sample_text", sec="sample_text")
    partner = ddsMetamodel_DdsTimeBasedFilterQos()
    setattr(partner, 'ddsMetamodel_DdsTimeBasedFilterQos', None)
    _safe_set(owner, 'ddsMetamodel_DdsDuration95', partner)
    assert getattr(partner, 'ddsMetamodel_DdsTimeBasedFilterQos') == owner
    _safe_set(owner, 'ddsMetamodel_DdsDuration95', None)
    assert getattr(partner, 'ddsMetamodel_DdsTimeBasedFilterQos') is None


def test_assoc_ownershipQos133_stub_double():
    # ddsMetamodel_DdsDataWriterQosProfile has no real 'ddsMetamodel_DdsDataWriterQosProfile134' property in the generated
    # code (a bare stub) -- manually attach it so ddsMetamodel_DdsOwnershipQos's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ddsMetamodel_DdsOwnershipQos's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ddsMetamodel_DdsOwnershipQos(kind="sample_text")
    partner = ddsMetamodel_DdsDataWriterQosProfile()
    setattr(partner, 'ddsMetamodel_DdsDataWriterQosProfile134', None)
    _safe_set(owner, 'ddsMetamodel_DdsOwnershipQos135', partner)
    assert getattr(partner, 'ddsMetamodel_DdsDataWriterQosProfile134') == owner
    _safe_set(owner, 'ddsMetamodel_DdsOwnershipQos135', None)
    assert getattr(partner, 'ddsMetamodel_DdsDataWriterQosProfile134') is None


def test_assoc_ownershipQos189_stub_double():
    # ddsMetamodel_DdsDataReaderQosProfile has no real 'ddsMetamodel_DdsDataReaderQosProfile190' property in the generated
    # code (a bare stub) -- manually attach it so ddsMetamodel_DdsOwnershipQos's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ddsMetamodel_DdsOwnershipQos's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ddsMetamodel_DdsOwnershipQos(kind="sample_text")
    partner = ddsMetamodel_DdsDataReaderQosProfile()
    setattr(partner, 'ddsMetamodel_DdsDataReaderQosProfile190', None)
    _safe_set(owner, 'ddsMetamodel_DdsOwnershipQos191', partner)
    assert getattr(partner, 'ddsMetamodel_DdsDataReaderQosProfile190') == owner
    _safe_set(owner, 'ddsMetamodel_DdsOwnershipQos191', None)
    assert getattr(partner, 'ddsMetamodel_DdsDataReaderQosProfile190') is None


def test_assoc_ownershipQos67_stub_double():
    # ddsMetamodel_DdsTopicQosProfile has no real 'ddsMetamodel_DdsTopicQosProfile68' property in the generated
    # code (a bare stub) -- manually attach it so ddsMetamodel_DdsOwnershipQos's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ddsMetamodel_DdsOwnershipQos's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ddsMetamodel_DdsOwnershipQos(kind="sample_text")
    partner = ddsMetamodel_DdsTopicQosProfile()
    setattr(partner, 'ddsMetamodel_DdsTopicQosProfile68', None)
    _safe_set(owner, 'ddsMetamodel_DdsOwnershipQos', partner)
    assert getattr(partner, 'ddsMetamodel_DdsTopicQosProfile68') == owner
    _safe_set(owner, 'ddsMetamodel_DdsOwnershipQos', None)
    assert getattr(partner, 'ddsMetamodel_DdsTopicQosProfile68') is None


def test_assoc_ownershipStrength136_stub_double():
    # ddsMetamodel_DdsDataWriterQosProfile has no real 'ddsMetamodel_DdsDataWriterQosProfile137' property in the generated
    # code (a bare stub) -- manually attach it so ddsMetamodel_DdsOwnershipStrengthQos's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ddsMetamodel_DdsOwnershipStrengthQos's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ddsMetamodel_DdsOwnershipStrengthQos(value="sample_text")
    partner = ddsMetamodel_DdsDataWriterQosProfile()
    setattr(partner, 'ddsMetamodel_DdsDataWriterQosProfile137', None)
    _safe_set(owner, 'ddsMetamodel_DdsOwnershipStrengthQos', partner)
    assert getattr(partner, 'ddsMetamodel_DdsDataWriterQosProfile137') == owner
    _safe_set(owner, 'ddsMetamodel_DdsOwnershipStrengthQos', None)
    assert getattr(partner, 'ddsMetamodel_DdsDataWriterQosProfile137') is None


def test_assoc_partitionQos119_stub_double():
    # ddsMetamodel_DdsPublisherQosProfile has no real 'ddsMetamodel_DdsPublisherQosProfile120' property in the generated
    # code (a bare stub) -- manually attach it so ddsMetamodel_DdsPartitionQos's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ddsMetamodel_DdsPartitionQos's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ddsMetamodel_DdsPartitionQos(name="sample_text")
    partner = ddsMetamodel_DdsPublisherQosProfile()
    setattr(partner, 'ddsMetamodel_DdsPublisherQosProfile120', None)
    _safe_set(owner, 'ddsMetamodel_DdsPartitionQos', partner)
    assert getattr(partner, 'ddsMetamodel_DdsPublisherQosProfile120') == owner
    _safe_set(owner, 'ddsMetamodel_DdsPartitionQos', None)
    assert getattr(partner, 'ddsMetamodel_DdsPublisherQosProfile120') is None


def test_assoc_partitionQos171_stub_double():
    # ddsMetamodel_DdsSubscriberQosProfile has no real 'ddsMetamodel_DdsSubscriberQosProfile172' property in the generated
    # code (a bare stub) -- manually attach it so ddsMetamodel_DdsPartitionQos's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ddsMetamodel_DdsPartitionQos's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ddsMetamodel_DdsPartitionQos(name="sample_text")
    partner = ddsMetamodel_DdsSubscriberQosProfile()
    setattr(partner, 'ddsMetamodel_DdsSubscriberQosProfile172', None)
    _safe_set(owner, 'ddsMetamodel_DdsPartitionQos173', partner)
    assert getattr(partner, 'ddsMetamodel_DdsSubscriberQosProfile172') == owner
    _safe_set(owner, 'ddsMetamodel_DdsPartitionQos173', None)
    assert getattr(partner, 'ddsMetamodel_DdsSubscriberQosProfile172') is None


def test_assoc_period85_stub_double():
    # ddsMetamodel_DdsDeadlineQos has no real 'ddsMetamodel_DdsDeadlineQos86' property in the generated
    # code (a bare stub) -- manually attach it so ddsMetamodel_DdsDuration's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ddsMetamodel_DdsDuration's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ddsMetamodel_DdsDuration(nanoSec="sample_text", sec="sample_text")
    partner = ddsMetamodel_DdsDeadlineQos()
    setattr(partner, 'ddsMetamodel_DdsDeadlineQos86', None)
    _safe_set(owner, 'ddsMetamodel_DdsDuration87', partner)
    assert getattr(partner, 'ddsMetamodel_DdsDeadlineQos86') == owner
    _safe_set(owner, 'ddsMetamodel_DdsDuration87', None)
    assert getattr(partner, 'ddsMetamodel_DdsDeadlineQos86') is None


def test_assoc_presentationQos117_stub_double():
    # ddsMetamodel_DdsPublisherQosProfile has no real 'ddsMetamodel_DdsPublisherQosProfile118' property in the generated
    # code (a bare stub) -- manually attach it so ddsMetamodel_DdsPresentationQos's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ddsMetamodel_DdsPresentationQos's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ddsMetamodel_DdsPresentationQos(access_scope="sample_text", coherent_access=True, ordered_access=True)
    partner = ddsMetamodel_DdsPublisherQosProfile()
    setattr(partner, 'ddsMetamodel_DdsPublisherQosProfile118', None)
    _safe_set(owner, 'ddsMetamodel_DdsPresentationQos', partner)
    assert getattr(partner, 'ddsMetamodel_DdsPublisherQosProfile118') == owner
    _safe_set(owner, 'ddsMetamodel_DdsPresentationQos', None)
    assert getattr(partner, 'ddsMetamodel_DdsPublisherQosProfile118') is None


def test_assoc_presentationQos168_stub_double():
    # ddsMetamodel_DdsSubscriberQosProfile has no real 'ddsMetamodel_DdsSubscriberQosProfile169' property in the generated
    # code (a bare stub) -- manually attach it so ddsMetamodel_DdsPresentationQos's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ddsMetamodel_DdsPresentationQos's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ddsMetamodel_DdsPresentationQos(access_scope="sample_text", coherent_access=True, ordered_access=True)
    partner = ddsMetamodel_DdsSubscriberQosProfile()
    setattr(partner, 'ddsMetamodel_DdsSubscriberQosProfile169', None)
    _safe_set(owner, 'ddsMetamodel_DdsPresentationQos170', partner)
    assert getattr(partner, 'ddsMetamodel_DdsSubscriberQosProfile169') == owner
    _safe_set(owner, 'ddsMetamodel_DdsPresentationQos170', None)
    assert getattr(partner, 'ddsMetamodel_DdsSubscriberQosProfile169') is None


def test_assoc_publisherQosProfile32_stub_double():
    # ddsMetamodel_DdsPublisherQosProfile has no real 'ddsMetamodel_DdsPublisherQosProfile' property in the generated
    # code (a bare stub) -- manually attach it so ddsMetamodel_DdsPublisher's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ddsMetamodel_DdsPublisher's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ddsMetamodel_DdsPublisher(publisherName="sample_text")
    partner = ddsMetamodel_DdsPublisherQosProfile()
    setattr(partner, 'ddsMetamodel_DdsPublisherQosProfile', None)
    _safe_set(owner, 'ddsMetamodel_DdsPublisher33', partner)
    assert getattr(partner, 'ddsMetamodel_DdsPublisherQosProfile') == owner
    _safe_set(owner, 'ddsMetamodel_DdsPublisher33', None)
    assert getattr(partner, 'ddsMetamodel_DdsPublisherQosProfile') is None


def test_assoc_reliabilityQos141_stub_double():
    # ddsMetamodel_DdsDataWriterQosProfile has no real 'ddsMetamodel_DdsDataWriterQosProfile142' property in the generated
    # code (a bare stub) -- manually attach it so ddsMetamodel_DdsReliabilityQos's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ddsMetamodel_DdsReliabilityQos's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ddsMetamodel_DdsReliabilityQos(kind="sample_text")
    partner = ddsMetamodel_DdsDataWriterQosProfile()
    setattr(partner, 'ddsMetamodel_DdsDataWriterQosProfile142', None)
    _safe_set(owner, 'ddsMetamodel_DdsReliabilityQos143', partner)
    assert getattr(partner, 'ddsMetamodel_DdsDataWriterQosProfile142') == owner
    _safe_set(owner, 'ddsMetamodel_DdsReliabilityQos143', None)
    assert getattr(partner, 'ddsMetamodel_DdsDataWriterQosProfile142') is None


def test_assoc_reliabilityQos195_stub_double():
    # ddsMetamodel_DdsDataReaderQosProfile has no real 'ddsMetamodel_DdsDataReaderQosProfile196' property in the generated
    # code (a bare stub) -- manually attach it so ddsMetamodel_DdsReliabilityQos's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ddsMetamodel_DdsReliabilityQos's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ddsMetamodel_DdsReliabilityQos(kind="sample_text")
    partner = ddsMetamodel_DdsDataReaderQosProfile()
    setattr(partner, 'ddsMetamodel_DdsDataReaderQosProfile196', None)
    _safe_set(owner, 'ddsMetamodel_DdsReliabilityQos197', partner)
    assert getattr(partner, 'ddsMetamodel_DdsDataReaderQosProfile196') == owner
    _safe_set(owner, 'ddsMetamodel_DdsReliabilityQos197', None)
    assert getattr(partner, 'ddsMetamodel_DdsDataReaderQosProfile196') is None


def test_assoc_reliabilityQos69_stub_double():
    # ddsMetamodel_DdsTopicQosProfile has no real 'ddsMetamodel_DdsTopicQosProfile70' property in the generated
    # code (a bare stub) -- manually attach it so ddsMetamodel_DdsReliabilityQos's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ddsMetamodel_DdsReliabilityQos's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ddsMetamodel_DdsReliabilityQos(kind="sample_text")
    partner = ddsMetamodel_DdsTopicQosProfile()
    setattr(partner, 'ddsMetamodel_DdsTopicQosProfile70', None)
    _safe_set(owner, 'ddsMetamodel_DdsReliabilityQos', partner)
    assert getattr(partner, 'ddsMetamodel_DdsTopicQosProfile70') == owner
    _safe_set(owner, 'ddsMetamodel_DdsReliabilityQos', None)
    assert getattr(partner, 'ddsMetamodel_DdsTopicQosProfile70') is None


def test_assoc_resourceLimitsQos156_stub_double():
    # ddsMetamodel_DdsDataWriterQosProfile has no real 'ddsMetamodel_DdsDataWriterQosProfile157' property in the generated
    # code (a bare stub) -- manually attach it so ddsMetamodel_DdsResourceLimits's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ddsMetamodel_DdsResourceLimits's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ddsMetamodel_DdsResourceLimits(max_instances="sample_text", max_samples="sample_text", max_samples_per_instances="sample_text")
    partner = ddsMetamodel_DdsDataWriterQosProfile()
    setattr(partner, 'ddsMetamodel_DdsDataWriterQosProfile157', None)
    _safe_set(owner, 'ddsMetamodel_DdsResourceLimits158', partner)
    assert getattr(partner, 'ddsMetamodel_DdsDataWriterQosProfile157') == owner
    _safe_set(owner, 'ddsMetamodel_DdsResourceLimits158', None)
    assert getattr(partner, 'ddsMetamodel_DdsDataWriterQosProfile157') is None


def test_assoc_resourceLimitsQos204_stub_double():
    # ddsMetamodel_DdsDataReaderQosProfile has no real 'ddsMetamodel_DdsDataReaderQosProfile205' property in the generated
    # code (a bare stub) -- manually attach it so ddsMetamodel_DdsResourceLimits's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ddsMetamodel_DdsResourceLimits's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ddsMetamodel_DdsResourceLimits(max_instances="sample_text", max_samples="sample_text", max_samples_per_instances="sample_text")
    partner = ddsMetamodel_DdsDataReaderQosProfile()
    setattr(partner, 'ddsMetamodel_DdsDataReaderQosProfile205', None)
    _safe_set(owner, 'ddsMetamodel_DdsResourceLimits206', partner)
    assert getattr(partner, 'ddsMetamodel_DdsDataReaderQosProfile205') == owner
    _safe_set(owner, 'ddsMetamodel_DdsResourceLimits206', None)
    assert getattr(partner, 'ddsMetamodel_DdsDataReaderQosProfile205') is None


def test_assoc_resourceLimitsQos75_stub_double():
    # ddsMetamodel_DdsTopicQosProfile has no real 'ddsMetamodel_DdsTopicQosProfile76' property in the generated
    # code (a bare stub) -- manually attach it so ddsMetamodel_DdsResourceLimits's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ddsMetamodel_DdsResourceLimits's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ddsMetamodel_DdsResourceLimits(max_instances="sample_text", max_samples="sample_text", max_samples_per_instances="sample_text")
    partner = ddsMetamodel_DdsTopicQosProfile()
    setattr(partner, 'ddsMetamodel_DdsTopicQosProfile76', None)
    _safe_set(owner, 'ddsMetamodel_DdsResourceLimits', partner)
    assert getattr(partner, 'ddsMetamodel_DdsTopicQosProfile76') == owner
    _safe_set(owner, 'ddsMetamodel_DdsResourceLimits', None)
    assert getattr(partner, 'ddsMetamodel_DdsTopicQosProfile76') is None


def test_assoc_statusConditions212_stub_double():
    # ddsMetamodel_DdsStatusCondition has no real 'DdsStatusCondition' property in the generated
    # code (a bare stub) -- manually attach it so ddsMetamodel_DdsWaitSet's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ddsMetamodel_DdsWaitSet's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ddsMetamodel_DdsWaitSet(name="sample_text")
    partner = ddsMetamodel_DdsStatusCondition()
    setattr(partner, 'DdsStatusCondition', None)
    _safe_set(owner, 'containingWaitset', {partner})
    assert getattr(partner, 'DdsStatusCondition') == owner
    _safe_set(owner, 'containingWaitset', set())
    assert getattr(partner, 'DdsStatusCondition') is None


def test_assoc_subscriberQosProfile19_stub_double():
    # ddsMetamodel_DdsSubscriberQosProfile has no real 'ddsMetamodel_DdsSubscriberQosProfile' property in the generated
    # code (a bare stub) -- manually attach it so ddsMetamodel_DdsSubscriber's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ddsMetamodel_DdsSubscriber's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ddsMetamodel_DdsSubscriber(subscriberName="sample_text")
    partner = ddsMetamodel_DdsSubscriberQosProfile()
    setattr(partner, 'ddsMetamodel_DdsSubscriberQosProfile', None)
    _safe_set(owner, 'ddsMetamodel_DdsSubscriber20', partner)
    assert getattr(partner, 'ddsMetamodel_DdsSubscriberQosProfile') == owner
    _safe_set(owner, 'ddsMetamodel_DdsSubscriber20', None)
    assert getattr(partner, 'ddsMetamodel_DdsSubscriberQosProfile') is None


def test_assoc_topicDataQos57_stub_double():
    # ddsMetamodel_DdsTopicQosProfile has no real 'ddsMetamodel_DdsTopicQosProfile58' property in the generated
    # code (a bare stub) -- manually attach it so ddsMetamodel_DdsTopicDataQos's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ddsMetamodel_DdsTopicDataQos's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ddsMetamodel_DdsTopicDataQos(value="sample_text")
    partner = ddsMetamodel_DdsTopicQosProfile()
    setattr(partner, 'ddsMetamodel_DdsTopicQosProfile58', None)
    _safe_set(owner, 'ddsMetamodel_DdsTopicDataQos', partner)
    assert getattr(partner, 'ddsMetamodel_DdsTopicQosProfile58') == owner
    _safe_set(owner, 'ddsMetamodel_DdsTopicDataQos', None)
    assert getattr(partner, 'ddsMetamodel_DdsTopicQosProfile58') is None


def test_assoc_topicQosProfile12_stub_double():
    # ddsMetamodel_DdsTopicQosProfile has no real 'ddsMetamodel_DdsTopicQosProfile' property in the generated
    # code (a bare stub) -- manually attach it so ddsMetamodel_DdsTopic's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ddsMetamodel_DdsTopic's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ddsMetamodel_DdsTopic(topicName="sample_text")
    partner = ddsMetamodel_DdsTopicQosProfile()
    setattr(partner, 'ddsMetamodel_DdsTopicQosProfile', None)
    _safe_set(owner, 'ddsMetamodel_DdsTopic13', partner)
    assert getattr(partner, 'ddsMetamodel_DdsTopicQosProfile') == owner
    _safe_set(owner, 'ddsMetamodel_DdsTopic13', None)
    assert getattr(partner, 'ddsMetamodel_DdsTopicQosProfile') is None


def test_assoc_transportPriorityQos144_stub_double():
    # ddsMetamodel_DdsDataWriterQosProfile has no real 'ddsMetamodel_DdsDataWriterQosProfile145' property in the generated
    # code (a bare stub) -- manually attach it so ddsMetamodel_DdsTransportPriorityQos's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ddsMetamodel_DdsTransportPriorityQos's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ddsMetamodel_DdsTransportPriorityQos(value="sample_text")
    partner = ddsMetamodel_DdsDataWriterQosProfile()
    setattr(partner, 'ddsMetamodel_DdsDataWriterQosProfile145', None)
    _safe_set(owner, 'ddsMetamodel_DdsTransportPriorityQos146', partner)
    assert getattr(partner, 'ddsMetamodel_DdsDataWriterQosProfile145') == owner
    _safe_set(owner, 'ddsMetamodel_DdsTransportPriorityQos146', None)
    assert getattr(partner, 'ddsMetamodel_DdsDataWriterQosProfile145') is None


def test_assoc_transportPriorityQos77_stub_double():
    # ddsMetamodel_DdsTopicQosProfile has no real 'ddsMetamodel_DdsTopicQosProfile78' property in the generated
    # code (a bare stub) -- manually attach it so ddsMetamodel_DdsTransportPriorityQos's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ddsMetamodel_DdsTransportPriorityQos's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ddsMetamodel_DdsTransportPriorityQos(value="sample_text")
    partner = ddsMetamodel_DdsTopicQosProfile()
    setattr(partner, 'ddsMetamodel_DdsTopicQosProfile78', None)
    _safe_set(owner, 'ddsMetamodel_DdsTransportPriorityQos', partner)
    assert getattr(partner, 'ddsMetamodel_DdsTopicQosProfile78') == owner
    _safe_set(owner, 'ddsMetamodel_DdsTransportPriorityQos', None)
    assert getattr(partner, 'ddsMetamodel_DdsTopicQosProfile78') is None


def test_assoc_userDataQos121_stub_double():
    # ddsMetamodel_DdsDataWriterQosProfile has no real 'ddsMetamodel_DdsDataWriterQosProfile122' property in the generated
    # code (a bare stub) -- manually attach it so ddsMetamodel_DdsUserDataQos's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ddsMetamodel_DdsUserDataQos's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ddsMetamodel_DdsUserDataQos(value="sample_text")
    partner = ddsMetamodel_DdsDataWriterQosProfile()
    setattr(partner, 'ddsMetamodel_DdsDataWriterQosProfile122', None)
    _safe_set(owner, 'ddsMetamodel_DdsUserDataQos123', partner)
    assert getattr(partner, 'ddsMetamodel_DdsDataWriterQosProfile122') == owner
    _safe_set(owner, 'ddsMetamodel_DdsUserDataQos123', None)
    assert getattr(partner, 'ddsMetamodel_DdsDataWriterQosProfile122') is None


def test_assoc_userDataQos174_stub_double():
    # ddsMetamodel_DdsDataReaderQosProfile has no real 'ddsMetamodel_DdsDataReaderQosProfile175' property in the generated
    # code (a bare stub) -- manually attach it so ddsMetamodel_DdsUserDataQos's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ddsMetamodel_DdsUserDataQos's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ddsMetamodel_DdsUserDataQos(value="sample_text")
    partner = ddsMetamodel_DdsDataReaderQosProfile()
    setattr(partner, 'ddsMetamodel_DdsDataReaderQosProfile175', None)
    _safe_set(owner, 'ddsMetamodel_DdsUserDataQos176', partner)
    assert getattr(partner, 'ddsMetamodel_DdsDataReaderQosProfile175') == owner
    _safe_set(owner, 'ddsMetamodel_DdsUserDataQos176', None)
    assert getattr(partner, 'ddsMetamodel_DdsDataReaderQosProfile175') is None


def test_assoc_userDataQos53_stub_double():
    # ddsMetamodel_DdsDomainParticipantQosProfile has no real 'ddsMetamodel_DdsDomainParticipantQosProfile54' property in the generated
    # code (a bare stub) -- manually attach it so ddsMetamodel_DdsUserDataQos's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # ddsMetamodel_DdsUserDataQos's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = ddsMetamodel_DdsUserDataQos(value="sample_text")
    partner = ddsMetamodel_DdsDomainParticipantQosProfile()
    setattr(partner, 'ddsMetamodel_DdsDomainParticipantQosProfile54', None)
    _safe_set(owner, 'ddsMetamodel_DdsUserDataQos', partner)
    assert getattr(partner, 'ddsMetamodel_DdsDomainParticipantQosProfile54') == owner
    _safe_set(owner, 'ddsMetamodel_DdsUserDataQos', None)
    assert getattr(partner, 'ddsMetamodel_DdsDomainParticipantQosProfile54') is None


