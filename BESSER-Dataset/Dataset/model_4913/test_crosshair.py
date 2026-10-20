from python_code import services_CFSService

def test_services_CFSService___init__():
    assert services_CFSService.__init__(services_CFSService('', '\x00'), '\x00\x00', '') == None


from python_code import services_DerivedResource
from python_code import services_DistributionEntry
from python_code import services_NetXResource
from python_code import services_ServiceDistribution

def test_services_DistributionEntry___init__():
    assert services_DistributionEntry.__init__(services_DistributionEntry('', services_DistributionEntry9=services_DerivedResource(), services_DistributionEntry=services_NetXResource(), services_DistributionEntry30=services_ServiceDistribution()), '', services_DistributionEntry9=services_DerivedResource(), services_DistributionEntry=services_NetXResource(), services_DistributionEntry30=services_ServiceDistribution()) == None


from python_code import services_RFSService

def test_services_RFSService___init__():
    assert services_RFSService.__init__(services_RFSService('', services_RFSService=set(), services_RFSService13=set()), '', services_RFSService=set(), services_RFSService13=set()) == None

