from python_code import arduino_Delay

def test_arduino_Delay___init__():
    assert arduino_Delay.__init__(arduino_Delay('', 0), '', 0) == None


from python_code import arduino_Function
from python_code import arduino_FunctionCall
from python_code import arduino_Sketch

def test_arduino_Function___init__():
    assert arduino_Function.__init__(arduino_Function('', arduino_Function=arduino_Sketch(), arduino_Function57=set(), arduino_Function59=set(), arduino_Function64=arduino_FunctionCall()), '', arduino_Function=arduino_Sketch(), arduino_Function57=set(), arduino_Function59=set(), arduino_Function64=arduino_FunctionCall()) == None


from python_code import arduino_Connector
from python_code import arduino_Hardware
from python_code import arduino_Module
from python_code import arduino_ModuleInstruction
from python_code import arduino_Project

def test_arduino_Module___init__():
    assert arduino_Module.__init__(arduino_Module('\x00\x00', '', '', True, arduino_Module=arduino_Hardware(), arduino_Module35=arduino_ModuleInstruction(), arduino_Module22=arduino_Project(), arduino_Module42=arduino_Connector()), '', '', '', False, arduino_Module=arduino_Hardware(), arduino_Module35=arduino_ModuleInstruction(), arduino_Module22=arduino_Project(), arduino_Module42=arduino_Connector()) == None


from python_code import arduino_NamedElement

def test_arduino_NamedElement___init__():
    assert arduino_NamedElement.__init__(arduino_NamedElement(''), '') == None


from python_code import arduino_Connector
from python_code import arduino_Pin

def test_arduino_Pin___init__():
    assert arduino_Pin.__init__(arduino_Pin(0, arduino_Pin=arduino_Connector()), 0, arduino_Pin=arduino_Connector()) == None


from python_code import arduino_Hardware
from python_code import arduino_Platform
from python_code import arduino_Project

def test_arduino_Platform___init__():
    assert arduino_Platform.__init__(arduino_Platform('', arduino_Platform=arduino_Hardware(), arduino_Platform6=set(), arduino_Platform8=set(), arduino_Platform25=arduino_Project()), '', arduino_Platform=arduino_Hardware(), arduino_Platform6=set(), arduino_Platform8=set(), arduino_Platform25=arduino_Project()) == None


from python_code import arduino_Repeat

def test_arduino_Repeat___init__():
    assert arduino_Repeat.__init__(arduino_Repeat(0), 0) == None


from python_code import arduino_Sensor
from python_code import arduino_Status

def test_arduino_Status___init__():
    assert arduino_Status.__init__(arduino_Status(True, Status=arduino_Sensor(), status=arduino_Sensor()), False, Status=arduino_Sensor(), status=arduino_Sensor()) == None


from python_code import arduino_Set
from python_code import arduino_Variable

def test_arduino_Variable___init__():
    assert arduino_Variable.__init__(arduino_Variable('', arduino_Variable=arduino_Set()), '', arduino_Variable=arduino_Set()) == None

