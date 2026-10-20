from python_code import services_CFSService

def test_services_CFSService___init__():
    assert services_CFSService.__init__(services_CFSService('', '\x00'), '\x00\x00', '') == None


from python_code import services_RFSService

def test_services_RFSService___init__():
    assert services_RFSService.__init__(services_RFSService('', services_RFSService=set(), services_RFSService2=set()), '', services_RFSService=set(), services_RFSService2=set()) == None

