from python_code import services_CFSService

def test_services_CFSService___init__():
    assert services_CFSService.__init__(services_CFSService('\x00\x00', '', services_CFSService=set()), '', '', services_CFSService=set()) == None

