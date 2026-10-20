from python_code import pycom_Board
from python_code import pycom_Function
from python_code import pycom_System

def test_pycom_Board___init__():
    assert pycom_Board.__init__(pycom_Board('', '', 0, pycom_Board67=pycom_Function(), pycom_Board=pycom_System(), pycom_Board19=set(), pycom_Board22=set()), '', '', 0, pycom_Board67=pycom_Function(), pycom_Board=pycom_System(), pycom_Board19=set(), pycom_Board22=set()) == None


from python_code import pycom_Boolean
from python_code import pycom_LogicExp

def test_pycom_Boolean___init__():
    assert pycom_Boolean.__init__(pycom_Boolean('', pycom_Boolean=pycom_LogicExp()), '', pycom_Boolean=pycom_LogicExp()) == None


from python_code import pycom_Communication
from python_code import pycom_CommunicationType

def test_pycom_CommunicationType___init__():
    assert pycom_CommunicationType.__init__(pycom_CommunicationType('', '', '\x00\x00', pycom_CommunicationType=pycom_Communication()), '', '', '', pycom_CommunicationType=pycom_Communication()) == None


from python_code import pycom_Actuator
from python_code import pycom_ModuleName
from python_code import pycom_Sensor

def test_pycom_ModuleName___init__():
    assert pycom_ModuleName.__init__(pycom_ModuleName('', pycom_ModuleName=pycom_Sensor(), pycom_ModuleName39=pycom_Actuator()), '', pycom_ModuleName=pycom_Sensor(), pycom_ModuleName39=pycom_Actuator()) == None


from python_code import pycom_Actuator
from python_code import pycom_ModuleType
from python_code import pycom_Sensor

def test_pycom_ModuleType___init__():
    assert pycom_ModuleType.__init__(pycom_ModuleType('', pycom_ModuleType=pycom_Sensor(), pycom_ModuleType36=pycom_Actuator()), '', pycom_ModuleType=pycom_Sensor(), pycom_ModuleType36=pycom_Actuator()) == None


from python_code import pycom_Pin
from python_code import pycom_PinName

def test_pycom_PinName___init__():
    assert pycom_PinName.__init__(pycom_PinName('', pycom_PinName=pycom_Pin(), pycom_PinName48=pycom_Pin()), '', pycom_PinName=pycom_Pin(), pycom_PinName48=pycom_Pin()) == None

