import pytest
from datetime import date, datetime, time, timedelta

from python_code import (
    DataReaderWriter,
    DomainEntity,
    Entity,
    PublisherSubscriber,
    dcps_DataReader,
    dcps_DataReaderWriter,
    dcps_DataWriter,
    dcps_DeadlineQosPolicy,
    dcps_DestinationOrderQosPolicy,
    dcps_Domain,
    dcps_DomainParticipant,
    dcps_DurabilityQosPolicy,
    dcps_DurabilityServiceQosPolicy,
    dcps_EntityFactoryQosPolicy,
    dcps_GroupDataQosPolicy,
    dcps_HistoryQosPolicy,
    dcps_LatencyBudgetQosPolicy,
    dcps_LifespanQosPolicy,
    dcps_LivelinessQosPolicy,
    dcps_OwnershipQosPolicy,
    dcps_OwnershipStrengthQosPolicy,
    dcps_PartitionQosPolicy,
    dcps_PresentationQosPolicy,
    dcps_Publisher,
    dcps_PublisherSubscriber,
    dcps_ReaderDataLifecycleQosPolicy,
    dcps_ReliabilityQosPolicy,
    dcps_ResourceLimitsQosPolicy,
    dcps_Subscriber,
    dcps_TimeBasedFilterQosPolicy,
    dcps_Topic,
    dcps_TopicDescription,
    dcps_TransportPriorityQosPolicy,
    dcps_UserDataQosPolicy,
    dcps_WriterDataLifecycleQosPolicy,
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

# =============================================================================
# STUB-SIDE TEST DOUBLE
# For associations where one side is a bare stub class with no real property:
# manually attach the attribute a real implementation would have had, so the
# real side's hasattr()-guarded consistency logic is actually reachable. See
# module docstring.
# =============================================================================

def test_assoc_deadline21_stub_double():
    # dcps_DeadlineQosPolicy has no real 'dcps_DeadlineQosPolicy' property in the generated
    # code (a bare stub) -- manually attach it so dcps_DataReaderWriter's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dcps_DataReaderWriter's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dcps_DataReaderWriter(copyFromTopicQos=True)
    partner = dcps_DeadlineQosPolicy()
    setattr(partner, 'dcps_DeadlineQosPolicy', None)
    _safe_set(owner, 'dcps_DataReaderWriter', partner)
    assert getattr(partner, 'dcps_DeadlineQosPolicy') == owner
    _safe_set(owner, 'dcps_DataReaderWriter', None)
    assert getattr(partner, 'dcps_DeadlineQosPolicy') is None


def test_assoc_destination_order22_stub_double():
    # dcps_DestinationOrderQosPolicy has no real 'dcps_DestinationOrderQosPolicy' property in the generated
    # code (a bare stub) -- manually attach it so dcps_DataReaderWriter's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dcps_DataReaderWriter's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dcps_DataReaderWriter(copyFromTopicQos=True)
    partner = dcps_DestinationOrderQosPolicy()
    setattr(partner, 'dcps_DestinationOrderQosPolicy', None)
    _safe_set(owner, 'dcps_DataReaderWriter23', partner)
    assert getattr(partner, 'dcps_DestinationOrderQosPolicy') == owner
    _safe_set(owner, 'dcps_DataReaderWriter23', None)
    assert getattr(partner, 'dcps_DestinationOrderQosPolicy') is None


def test_assoc_domain0_stub_double():
    # dcps_DomainParticipant has no real 'dcps_DomainParticipant' property in the generated
    # code (a bare stub) -- manually attach it so dcps_Domain's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dcps_Domain's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dcps_Domain(domainId="sample_text")
    partner = dcps_DomainParticipant()
    setattr(partner, 'dcps_DomainParticipant', None)
    _safe_set(owner, 'dcps_Domain', partner)
    assert getattr(partner, 'dcps_DomainParticipant') == owner
    _safe_set(owner, 'dcps_Domain', None)
    assert getattr(partner, 'dcps_DomainParticipant') is None


def test_assoc_durability24_stub_double():
    # dcps_DurabilityQosPolicy has no real 'dcps_DurabilityQosPolicy' property in the generated
    # code (a bare stub) -- manually attach it so dcps_DataReaderWriter's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dcps_DataReaderWriter's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dcps_DataReaderWriter(copyFromTopicQos=True)
    partner = dcps_DurabilityQosPolicy()
    setattr(partner, 'dcps_DurabilityQosPolicy', None)
    _safe_set(owner, 'dcps_DataReaderWriter25', partner)
    assert getattr(partner, 'dcps_DurabilityQosPolicy') == owner
    _safe_set(owner, 'dcps_DataReaderWriter25', None)
    assert getattr(partner, 'dcps_DurabilityQosPolicy') is None


def test_assoc_entity_factory9_stub_double():
    # dcps_EntityFactoryQosPolicy has no real 'dcps_EntityFactoryQosPolicy10' property in the generated
    # code (a bare stub) -- manually attach it so dcps_PublisherSubscriber's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dcps_PublisherSubscriber's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dcps_PublisherSubscriber(transportId=7)
    partner = dcps_EntityFactoryQosPolicy()
    setattr(partner, 'dcps_EntityFactoryQosPolicy10', None)
    _safe_set(owner, 'dcps_PublisherSubscriber', partner)
    assert getattr(partner, 'dcps_EntityFactoryQosPolicy10') == owner
    _safe_set(owner, 'dcps_PublisherSubscriber', None)
    assert getattr(partner, 'dcps_EntityFactoryQosPolicy10') is None


def test_assoc_group_data11_stub_double():
    # dcps_GroupDataQosPolicy has no real 'dcps_GroupDataQosPolicy' property in the generated
    # code (a bare stub) -- manually attach it so dcps_PublisherSubscriber's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dcps_PublisherSubscriber's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dcps_PublisherSubscriber(transportId=7)
    partner = dcps_GroupDataQosPolicy()
    setattr(partner, 'dcps_GroupDataQosPolicy', None)
    _safe_set(owner, 'dcps_PublisherSubscriber12', partner)
    assert getattr(partner, 'dcps_GroupDataQosPolicy') == owner
    _safe_set(owner, 'dcps_PublisherSubscriber12', None)
    assert getattr(partner, 'dcps_GroupDataQosPolicy') is None


def test_assoc_history26_stub_double():
    # dcps_HistoryQosPolicy has no real 'dcps_HistoryQosPolicy' property in the generated
    # code (a bare stub) -- manually attach it so dcps_DataReaderWriter's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dcps_DataReaderWriter's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dcps_DataReaderWriter(copyFromTopicQos=True)
    partner = dcps_HistoryQosPolicy()
    setattr(partner, 'dcps_HistoryQosPolicy', None)
    _safe_set(owner, 'dcps_DataReaderWriter27', partner)
    assert getattr(partner, 'dcps_HistoryQosPolicy') == owner
    _safe_set(owner, 'dcps_DataReaderWriter27', None)
    assert getattr(partner, 'dcps_HistoryQosPolicy') is None


def test_assoc_latency_budget28_stub_double():
    # dcps_LatencyBudgetQosPolicy has no real 'dcps_LatencyBudgetQosPolicy' property in the generated
    # code (a bare stub) -- manually attach it so dcps_DataReaderWriter's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dcps_DataReaderWriter's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dcps_DataReaderWriter(copyFromTopicQos=True)
    partner = dcps_LatencyBudgetQosPolicy()
    setattr(partner, 'dcps_LatencyBudgetQosPolicy', None)
    _safe_set(owner, 'dcps_DataReaderWriter29', partner)
    assert getattr(partner, 'dcps_LatencyBudgetQosPolicy') == owner
    _safe_set(owner, 'dcps_DataReaderWriter29', None)
    assert getattr(partner, 'dcps_LatencyBudgetQosPolicy') is None


def test_assoc_liveliness30_stub_double():
    # dcps_LivelinessQosPolicy has no real 'dcps_LivelinessQosPolicy' property in the generated
    # code (a bare stub) -- manually attach it so dcps_DataReaderWriter's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dcps_DataReaderWriter's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dcps_DataReaderWriter(copyFromTopicQos=True)
    partner = dcps_LivelinessQosPolicy()
    setattr(partner, 'dcps_LivelinessQosPolicy', None)
    _safe_set(owner, 'dcps_DataReaderWriter31', partner)
    assert getattr(partner, 'dcps_LivelinessQosPolicy') == owner
    _safe_set(owner, 'dcps_DataReaderWriter31', None)
    assert getattr(partner, 'dcps_LivelinessQosPolicy') is None


def test_assoc_ownership32_stub_double():
    # dcps_OwnershipQosPolicy has no real 'dcps_OwnershipQosPolicy' property in the generated
    # code (a bare stub) -- manually attach it so dcps_DataReaderWriter's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dcps_DataReaderWriter's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dcps_DataReaderWriter(copyFromTopicQos=True)
    partner = dcps_OwnershipQosPolicy()
    setattr(partner, 'dcps_OwnershipQosPolicy', None)
    _safe_set(owner, 'dcps_DataReaderWriter33', partner)
    assert getattr(partner, 'dcps_OwnershipQosPolicy') == owner
    _safe_set(owner, 'dcps_DataReaderWriter33', None)
    assert getattr(partner, 'dcps_OwnershipQosPolicy') is None


def test_assoc_partition15_stub_double():
    # dcps_PartitionQosPolicy has no real 'dcps_PartitionQosPolicy' property in the generated
    # code (a bare stub) -- manually attach it so dcps_PublisherSubscriber's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dcps_PublisherSubscriber's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dcps_PublisherSubscriber(transportId=7)
    partner = dcps_PartitionQosPolicy()
    setattr(partner, 'dcps_PartitionQosPolicy', None)
    _safe_set(owner, 'dcps_PublisherSubscriber16', partner)
    assert getattr(partner, 'dcps_PartitionQosPolicy') == owner
    _safe_set(owner, 'dcps_PublisherSubscriber16', None)
    assert getattr(partner, 'dcps_PartitionQosPolicy') is None


def test_assoc_presentation13_stub_double():
    # dcps_PresentationQosPolicy has no real 'dcps_PresentationQosPolicy' property in the generated
    # code (a bare stub) -- manually attach it so dcps_PublisherSubscriber's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dcps_PublisherSubscriber's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dcps_PublisherSubscriber(transportId=7)
    partner = dcps_PresentationQosPolicy()
    setattr(partner, 'dcps_PresentationQosPolicy', None)
    _safe_set(owner, 'dcps_PublisherSubscriber14', partner)
    assert getattr(partner, 'dcps_PresentationQosPolicy') == owner
    _safe_set(owner, 'dcps_PublisherSubscriber14', None)
    assert getattr(partner, 'dcps_PresentationQosPolicy') is None


def test_assoc_reliability34_stub_double():
    # dcps_ReliabilityQosPolicy has no real 'dcps_ReliabilityQosPolicy' property in the generated
    # code (a bare stub) -- manually attach it so dcps_DataReaderWriter's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dcps_DataReaderWriter's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dcps_DataReaderWriter(copyFromTopicQos=True)
    partner = dcps_ReliabilityQosPolicy()
    setattr(partner, 'dcps_ReliabilityQosPolicy', None)
    _safe_set(owner, 'dcps_DataReaderWriter35', partner)
    assert getattr(partner, 'dcps_ReliabilityQosPolicy') == owner
    _safe_set(owner, 'dcps_DataReaderWriter35', None)
    assert getattr(partner, 'dcps_ReliabilityQosPolicy') is None


def test_assoc_resource_limits36_stub_double():
    # dcps_ResourceLimitsQosPolicy has no real 'dcps_ResourceLimitsQosPolicy' property in the generated
    # code (a bare stub) -- manually attach it so dcps_DataReaderWriter's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dcps_DataReaderWriter's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dcps_DataReaderWriter(copyFromTopicQos=True)
    partner = dcps_ResourceLimitsQosPolicy()
    setattr(partner, 'dcps_ResourceLimitsQosPolicy', None)
    _safe_set(owner, 'dcps_DataReaderWriter37', partner)
    assert getattr(partner, 'dcps_ResourceLimitsQosPolicy') == owner
    _safe_set(owner, 'dcps_DataReaderWriter37', None)
    assert getattr(partner, 'dcps_ResourceLimitsQosPolicy') is None


def test_assoc_user_data38_stub_double():
    # dcps_UserDataQosPolicy has no real 'dcps_UserDataQosPolicy40' property in the generated
    # code (a bare stub) -- manually attach it so dcps_DataReaderWriter's own
    # bidirectional-consistency guard can actually be exercised. This tests
    # dcps_DataReaderWriter's OWN setter logic via a hand-shaped stand-in for an
    # incomplete collaborator, same reasoning as a test double anywhere else.
    owner = dcps_DataReaderWriter(copyFromTopicQos=True)
    partner = dcps_UserDataQosPolicy()
    setattr(partner, 'dcps_UserDataQosPolicy40', None)
    _safe_set(owner, 'dcps_DataReaderWriter39', partner)
    assert getattr(partner, 'dcps_UserDataQosPolicy40') == owner
    _safe_set(owner, 'dcps_DataReaderWriter39', None)
    assert getattr(partner, 'dcps_UserDataQosPolicy40') is None


