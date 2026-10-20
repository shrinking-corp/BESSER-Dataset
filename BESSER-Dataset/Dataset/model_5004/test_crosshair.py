from python_code import componentModel_AbstractElement
from python_code import componentModel_ComponentModel

def test_componentModel_AbstractElement___init__():
    assert componentModel_AbstractElement.__init__(componentModel_AbstractElement('', componentModel_AbstractElement=componentModel_ComponentModel()), '', componentModel_AbstractElement=componentModel_ComponentModel()) == None


from python_code import componentModel_AbstractFeatures
from python_code import componentModel_SystemDec

def test_componentModel_AbstractFeatures___init__():
    assert componentModel_AbstractFeatures.__init__(componentModel_AbstractFeatures('', componentModel_AbstractFeatures=componentModel_SystemDec()), '', componentModel_AbstractFeatures=componentModel_SystemDec()) == None


from python_code import componentModel_ComponentFeature
from python_code import componentModel_Port
from python_code import componentModel_PortType

def test_componentModel_Port___init__():
    assert componentModel_Port.__init__(componentModel_Port('', componentModel_Port=componentModel_ComponentFeature(), componentModel_Port37=componentModel_PortType()), '', componentModel_Port=componentModel_ComponentFeature(), componentModel_Port37=componentModel_PortType()) == None


from python_code import componentModel_PortType
from python_code import componentModel_errorModes

def test_componentModel_errorModes___init__():
    assert componentModel_errorModes.__init__(componentModel_errorModes('', componentModel_errorModes=componentModel_PortType()), '', componentModel_errorModes=componentModel_PortType()) == None

