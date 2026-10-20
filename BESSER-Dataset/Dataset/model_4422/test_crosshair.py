from python_code import ArduinoMetamodel_Analog
from python_code import ArduinoMetamodel_ArduinoBoardUNO

def test_ArduinoMetamodel_Analog___init__():
    assert ArduinoMetamodel_Analog.__init__(ArduinoMetamodel_Analog('', ArduinoMetamodel_Analog=ArduinoMetamodel_ArduinoBoardUNO()), '', ArduinoMetamodel_Analog=ArduinoMetamodel_ArduinoBoardUNO()) == None


from python_code import ArduinoMetamodel_ArduinoBoardUNO
from python_code import ArduinoMetamodel_Digital

def test_ArduinoMetamodel_Digital___init__():
    assert ArduinoMetamodel_Digital.__init__(ArduinoMetamodel_Digital('', ArduinoMetamodel_Digital=ArduinoMetamodel_ArduinoBoardUNO()), '', ArduinoMetamodel_Digital=ArduinoMetamodel_ArduinoBoardUNO()) == None


from python_code import ArduinoMetamodel_Metodo
from python_code import ArduinoMetamodel_Project

def test_ArduinoMetamodel_Metodo___init__():
    assert ArduinoMetamodel_Metodo.__init__(ArduinoMetamodel_Metodo('\x00', ArduinoMetamodel_Metodo=ArduinoMetamodel_Project(), ArduinoMetamodel_Metodo10=set()), '', ArduinoMetamodel_Metodo=ArduinoMetamodel_Project(), ArduinoMetamodel_Metodo10=set()) == None


from python_code import ArduinoMetamodel_Pin

def test_ArduinoMetamodel_Pin___init__():
    assert ArduinoMetamodel_Pin.__init__(ArduinoMetamodel_Pin('', '\x00'), '\x00\x00', '') == None


from python_code import ArduinoMetamodel_FiniteStateMachine
from python_code import ArduinoMetamodel_State
from python_code import ArduinoMetamodel_Transition

def test_ArduinoMetamodel_State___init__():
    assert ArduinoMetamodel_State.__init__(ArduinoMetamodel_State('', False, State=ArduinoMetamodel_Transition(), State17=ArduinoMetamodel_Transition(), ArduinoMetamodel_State=ArduinoMetamodel_FiniteStateMachine(), target=set(), source=set()), '', True, State=ArduinoMetamodel_Transition(), State17=ArduinoMetamodel_Transition(), ArduinoMetamodel_State=ArduinoMetamodel_FiniteStateMachine(), target=set(), source=set()) == None

