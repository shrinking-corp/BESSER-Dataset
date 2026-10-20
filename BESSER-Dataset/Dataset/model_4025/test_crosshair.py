from python_code import uml2CD_DataType
from python_code import uml2CD_Parameter

def test_uml2CD_Parameter___init__():
    assert uml2CD_Parameter.__init__(uml2CD_Parameter('', '\x00', uml2CD_Parameter=uml2CD_DataType()), '\x00\x00', '', uml2CD_Parameter=uml2CD_DataType()) == None

