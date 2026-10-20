from python_code import dcps_DataReaderWriter
from python_code import dcps_DeadlineQosPolicy
from python_code import dcps_DestinationOrderQosPolicy
from python_code import dcps_DurabilityQosPolicy
from python_code import dcps_HistoryQosPolicy
from python_code import dcps_LatencyBudgetQosPolicy
from python_code import dcps_LivelinessQosPolicy
from python_code import dcps_OwnershipQosPolicy
from python_code import dcps_ReliabilityQosPolicy
from python_code import dcps_ResourceLimitsQosPolicy
from python_code import dcps_UserDataQosPolicy

def test_dcps_DataReaderWriter___init__():
    assert dcps_DataReaderWriter.__init__(dcps_DataReaderWriter(True, dcps_DataReaderWriter23=dcps_DestinationOrderQosPolicy(), dcps_DataReaderWriter25=dcps_DurabilityQosPolicy(), dcps_DataReaderWriter27=dcps_HistoryQosPolicy(), dcps_DataReaderWriter29=dcps_LatencyBudgetQosPolicy(), dcps_DataReaderWriter31=dcps_LivelinessQosPolicy(), dcps_DataReaderWriter33=dcps_OwnershipQosPolicy(), dcps_DataReaderWriter35=dcps_ReliabilityQosPolicy(), dcps_DataReaderWriter=dcps_DeadlineQosPolicy(), dcps_DataReaderWriter37=dcps_ResourceLimitsQosPolicy(), dcps_DataReaderWriter39=dcps_UserDataQosPolicy()), False, dcps_DataReaderWriter23=dcps_DestinationOrderQosPolicy(), dcps_DataReaderWriter25=dcps_DurabilityQosPolicy(), dcps_DataReaderWriter27=dcps_HistoryQosPolicy(), dcps_DataReaderWriter29=dcps_LatencyBudgetQosPolicy(), dcps_DataReaderWriter31=dcps_LivelinessQosPolicy(), dcps_DataReaderWriter33=dcps_OwnershipQosPolicy(), dcps_DataReaderWriter35=dcps_ReliabilityQosPolicy(), dcps_DataReaderWriter=dcps_DeadlineQosPolicy(), dcps_DataReaderWriter37=dcps_ResourceLimitsQosPolicy(), dcps_DataReaderWriter39=dcps_UserDataQosPolicy()) == None


from python_code import dcps_Domain
from python_code import dcps_DomainParticipant

def test_dcps_Domain___init__():
    assert dcps_Domain.__init__(dcps_Domain('', dcps_Domain=dcps_DomainParticipant()), '', dcps_Domain=dcps_DomainParticipant()) == None


from python_code import dcps_EntityFactoryQosPolicy
from python_code import dcps_GroupDataQosPolicy
from python_code import dcps_PartitionQosPolicy
from python_code import dcps_PresentationQosPolicy
from python_code import dcps_PublisherSubscriber

def test_dcps_PublisherSubscriber___init__():
    assert dcps_PublisherSubscriber.__init__(dcps_PublisherSubscriber(0, dcps_PublisherSubscriber=dcps_EntityFactoryQosPolicy(), dcps_PublisherSubscriber12=dcps_GroupDataQosPolicy(), dcps_PublisherSubscriber14=dcps_PresentationQosPolicy(), dcps_PublisherSubscriber16=dcps_PartitionQosPolicy()), 0, dcps_PublisherSubscriber=dcps_EntityFactoryQosPolicy(), dcps_PublisherSubscriber12=dcps_GroupDataQosPolicy(), dcps_PublisherSubscriber14=dcps_PresentationQosPolicy(), dcps_PublisherSubscriber16=dcps_PartitionQosPolicy()) == None

