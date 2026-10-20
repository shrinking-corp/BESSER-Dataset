from python_code import simulink_ActionEntry
from python_code import simulink_ActionTable

def test_simulink_ActionEntry___init__():
    assert simulink_ActionEntry.__init__(simulink_ActionEntry('', '', '\x00\x00', simulink_ActionEntry=simulink_ActionTable()), '', '', '', simulink_ActionEntry=simulink_ActionTable()) == None


from python_code import simulink_Chart

def test_simulink_Chart___init__():
    assert simulink_Chart.__init__(simulink_Chart(''), '') == None


from python_code import simulink_ConditionTable
from python_code import simulink_Decision

def test_simulink_Decision___init__():
    assert simulink_Decision.__init__(simulink_Decision('', 0, simulink_Decision56=set(), simulink_Decision=simulink_ConditionTable()), '', 0, simulink_Decision56=set(), simulink_Decision=simulink_ConditionTable()) == None


from python_code import simulink_Function

def test_simulink_Function___init__():
    assert simulink_Function.__init__(simulink_Function(''), '') == None


from python_code import simulink_LocalData

def test_simulink_LocalData___init__():
    assert simulink_LocalData.__init__(simulink_LocalData(''), '') == None


from python_code import simulink_ModelReference

def test_simulink_ModelReference___init__():
    assert simulink_ModelReference.__init__(simulink_ModelReference(''), '') == None


from python_code import simulink_SimulinkElement

def test_simulink_SimulinkElement___init__():
    assert simulink_SimulinkElement.__init__(simulink_SimulinkElement('', '\x00'), '\x00\x00', '') == None


from python_code import simulink_SimulinkModel

def test_simulink_SimulinkModel___init__():
    assert simulink_SimulinkModel.__init__(simulink_SimulinkModel('', False), '', False) == None


from python_code import simulink_StateflowElement

def test_simulink_StateflowElement___init__():
    assert simulink_StateflowElement.__init__(simulink_StateflowElement('', 0), '', 0) == None

