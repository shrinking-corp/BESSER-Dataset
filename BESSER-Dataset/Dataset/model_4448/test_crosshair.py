from python_code import pycom_Board
from python_code import pycom_Function
from python_code import pycom_System

def test_pycom_Board___init__():
    assert pycom_Board.__init__(pycom_Board('', pycom_Board=pycom_System(), pycom_Board10=set(), pycom_Board43=pycom_Function()), '', pycom_Board=pycom_System(), pycom_Board10=set(), pycom_Board43=pycom_Function()) == None


from python_code import pycom_Boolean
from python_code import pycom_LogicExp

def test_pycom_Boolean___init__():
    assert pycom_Boolean.__init__(pycom_Boolean('', pycom_Boolean=pycom_LogicExp()), '', pycom_Boolean=pycom_LogicExp()) == None


from python_code import pycom_Communication

def test_pycom_Communication___init__():
    assert pycom_Communication.__init__(pycom_Communication(''), '') == None


from python_code import pycom_Function
from python_code import pycom_FunctionName

def test_pycom_FunctionName___init__():
    assert pycom_FunctionName.__init__(pycom_FunctionName('', pycom_FunctionName=pycom_Function()), '', pycom_FunctionName=pycom_Function()) == None


from python_code import pycom_Actuator
from python_code import pycom_ModuleFunction
from python_code import pycom_ModuleType
from python_code import pycom_Pin
from python_code import pycom_Sensor

def test_pycom_ModuleType___init__():
    assert pycom_ModuleType.__init__(pycom_ModuleType('', '\x00', pycom_ModuleType=pycom_Sensor(), pycom_ModuleType17=pycom_Actuator(), pycom_ModuleType19=pycom_Pin(), pycom_ModuleType47=pycom_ModuleFunction()), '\x00\x00', '', pycom_ModuleType=pycom_Sensor(), pycom_ModuleType17=pycom_Actuator(), pycom_ModuleType19=pycom_Pin(), pycom_ModuleType47=pycom_ModuleFunction()) == None


from python_code import pycom_Pin
from python_code import pycom_PinName

def test_pycom_PinName___init__():
    assert pycom_PinName.__init__(pycom_PinName('', pycom_PinName=pycom_Pin(), pycom_PinName24=pycom_Pin()), '', pycom_PinName=pycom_Pin(), pycom_PinName24=pycom_Pin()) == None

