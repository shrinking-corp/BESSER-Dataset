from python_code import arduino_BinaryBooleanExpression

def test_arduino_BinaryBooleanExpression___init__():
    assert arduino_BinaryBooleanExpression.__init__(arduino_BinaryBooleanExpression(''), '') == None


from python_code import arduino_BinaryIntegerExpression

def test_arduino_BinaryIntegerExpression___init__():
    assert arduino_BinaryIntegerExpression.__init__(arduino_BinaryIntegerExpression(''), '') == None


from python_code import arduino_BooleanConstant

def test_arduino_BooleanConstant___init__():
    assert arduino_BooleanConstant.__init__(arduino_BooleanConstant(True), False) == None


from python_code import arduino_BooleanVariable

def test_arduino_BooleanVariable___init__():
    assert arduino_BooleanVariable.__init__(arduino_BooleanVariable(True), False) == None


from python_code import arduino_Delay

def test_arduino_Delay___init__():
    assert arduino_Delay.__init__(arduino_Delay('', 0), '', 0) == None


from python_code import arduino_IntegerConstant

def test_arduino_IntegerConstant___init__():
    assert arduino_IntegerConstant.__init__(arduino_IntegerConstant(0), 0) == None


from python_code import arduino_IntegerVariable

def test_arduino_IntegerVariable___init__():
    assert arduino_IntegerVariable.__init__(arduino_IntegerVariable(0), 0) == None


from python_code import arduino_Connector
from python_code import arduino_Hardware
from python_code import arduino_Module
from python_code import arduino_ModuleGet
from python_code import arduino_ModuleInstruction
from python_code import arduino_Project

def test_arduino_Module___init__():
    assert arduino_Module.__init__(arduino_Module('\x00\x00', '', False, '', arduino_Module=arduino_Hardware(), arduino_Module17=arduino_Project(), arduino_Module41=arduino_Connector(), arduino_Module43=arduino_ModuleGet(), arduino_Module34=arduino_ModuleInstruction()), '', '', False, '', arduino_Module=arduino_Hardware(), arduino_Module17=arduino_Project(), arduino_Module41=arduino_Connector(), arduino_Module43=arduino_ModuleGet(), arduino_Module34=arduino_ModuleInstruction()) == None


from python_code import arduino_NamedElement

def test_arduino_NamedElement___init__():
    assert arduino_NamedElement.__init__(arduino_NamedElement(''), '') == None


from python_code import arduino_Connector
from python_code import arduino_Pin

def test_arduino_Pin___init__():
    assert arduino_Pin.__init__(arduino_Pin(0, 0, arduino_Pin=arduino_Connector()), 0, 0, arduino_Pin=arduino_Connector()) == None


from python_code import arduino_Hardware
from python_code import arduino_Platform
from python_code import arduino_Project

def test_arduino_Platform___init__():
    assert arduino_Platform.__init__(arduino_Platform('', arduino_Platform=arduino_Hardware(), arduino_Platform6=set(), arduino_Platform8=set(), arduino_Platform20=arduino_Project()), '', arduino_Platform=arduino_Hardware(), arduino_Platform6=set(), arduino_Platform8=set(), arduino_Platform20=arduino_Project()) == None


from python_code import arduino_Repeat

def test_arduino_Repeat___init__():
    assert arduino_Repeat.__init__(arduino_Repeat(0), 0) == None


from python_code import arduino_UnaryBooleanExpression

def test_arduino_UnaryBooleanExpression___init__():
    assert arduino_UnaryBooleanExpression.__init__(arduino_UnaryBooleanExpression(''), '') == None


from python_code import arduino_UnaryIntegerExpression

def test_arduino_UnaryIntegerExpression___init__():
    assert arduino_UnaryIntegerExpression.__init__(arduino_UnaryIntegerExpression(''), '') == None

