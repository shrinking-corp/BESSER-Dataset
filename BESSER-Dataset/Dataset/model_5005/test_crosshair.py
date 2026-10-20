from python_code import systemmodel_Block
from python_code import systemmodel_Inport
from python_code import systemmodel_Outport
from python_code import systemmodel_SystemModel

def test_systemmodel_Block___init__():
    assert systemmodel_Block.__init__(systemmodel_Block(0, systemmodel_Block=systemmodel_SystemModel(), parentBlock=set(), parentBlock7=set(), Block=systemmodel_Inport(), Block17=systemmodel_Outport()), 0, systemmodel_Block=systemmodel_SystemModel(), parentBlock=set(), parentBlock7=set(), Block=systemmodel_Inport(), Block17=systemmodel_Outport()) == None


from python_code import systemmodel_DataType
from python_code import systemmodel_Port
from python_code import systemmodel_SystemModel

def test_systemmodel_DataType___init__():
    assert systemmodel_DataType.__init__(systemmodel_DataType('', systemmodel_DataType=systemmodel_SystemModel(), systemmodel_DataType19=systemmodel_Port()), '', systemmodel_DataType=systemmodel_SystemModel(), systemmodel_DataType19=systemmodel_Port()) == None


from python_code import systemmodel_GainBlock

def test_systemmodel_GainBlock___init__():
    assert systemmodel_GainBlock.__init__(systemmodel_GainBlock(''), '') == None


from python_code import systemmodel_MatrixType

def test_systemmodel_MatrixType___init__():
    assert systemmodel_MatrixType.__init__(systemmodel_MatrixType('', '\x00'), '\x00\x00', '') == None


from python_code import systemmodel_SMElement

def test_systemmodel_SMElement___init__():
    assert systemmodel_SMElement.__init__(systemmodel_SMElement(''), '') == None


from python_code import systemmodel_Saturation

def test_systemmodel_Saturation___init__():
    assert systemmodel_Saturation.__init__(systemmodel_Saturation('', '\x00'), '\x00\x00', '') == None


from python_code import systemmodel_UnitDelay

def test_systemmodel_UnitDelay___init__():
    assert systemmodel_UnitDelay.__init__(systemmodel_UnitDelay(''), '') == None


from python_code import systemmodel_VectorType

def test_systemmodel_VectorType___init__():
    assert systemmodel_VectorType.__init__(systemmodel_VectorType(''), '') == None

