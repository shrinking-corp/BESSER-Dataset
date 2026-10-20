from python_code import micro_Attribute
from python_code import micro_Model

def test_micro_Attribute___init__():
    assert micro_Attribute.__init__(micro_Attribute('\x00\x00', False, False, True, Attribute=micro_Model(), attributes=micro_Model()), '', False, False, False, Attribute=micro_Model(), attributes=micro_Model()) == None


from python_code import micro_API
from python_code import micro_Command
from python_code import micro_Info
from python_code import micro_Step

def test_micro_Command___init__():
    assert micro_Command.__init__(micro_Command('', False, Command=micro_API(), commands=micro_API(), micro_Command42=micro_Step(), micro_Command=micro_Info()), '', False, Command=micro_API(), commands=micro_API(), micro_Command42=micro_Step(), micro_Command=micro_Info()) == None


from python_code import micro_NamedElement

def test_micro_NamedElement___init__():
    assert micro_NamedElement.__init__(micro_NamedElement(''), '') == None


from python_code import micro_Model
from python_code import micro_PrimitiveTypeAttribute

def test_micro_PrimitiveTypeAttribute___init__():
    assert micro_PrimitiveTypeAttribute.__init__(micro_PrimitiveTypeAttribute('', micro_PrimitiveTypeAttribute=micro_Model()), '', micro_PrimitiveTypeAttribute=micro_Model()) == None


from python_code import micro_MicroserviceArchitecture
from python_code import micro_Service

def test_micro_Service___init__():
    assert micro_Service.__init__(micro_Service('\x00\x00', '', '', 0, micro_Service=micro_MicroserviceArchitecture()), '', '', '', 0, micro_Service=micro_MicroserviceArchitecture()) == None

