from python_code import simulink_Connection
from python_code import simulink_OutPort

def test_simulink_Connection___init__():
    assert simulink_Connection.__init__(simulink_Connection('', Connection=simulink_OutPort(), connection=simulink_OutPort()), '', Connection=simulink_OutPort(), connection=simulink_OutPort()) == None


from python_code import simulink_Block
from python_code import simulink_Enable

def test_simulink_Enable___init__():
    assert simulink_Enable.__init__(simulink_Enable('', simulink_Enable=simulink_Block()), '', simulink_Enable=simulink_Block()) == None


from python_code import simulink_From
from python_code import simulink_Goto
from python_code import simulink_GotoTagVisibility

def test_simulink_Goto___init__():
    assert simulink_Goto.__init__(simulink_Goto('\x00\x00', '', Goto=simulink_From(), simulink_Goto=simulink_GotoTagVisibility(), gotoBlock=set()), '', '', Goto=simulink_From(), simulink_Goto=simulink_GotoTagVisibility(), gotoBlock=set()) == None


from python_code import simulink_Block
from python_code import simulink_LibraryLinkReference

def test_simulink_LibraryLinkReference___init__():
    assert simulink_LibraryLinkReference.__init__(simulink_LibraryLinkReference(True, simulink_LibraryLinkReference=simulink_Block()), False, simulink_LibraryLinkReference=simulink_Block()) == None


from python_code import simulink_Block
from python_code import simulink_Parameter
from python_code import simulink_Port

def test_simulink_Parameter___init__():
    assert simulink_Parameter.__init__(simulink_Parameter('\x00\x00', '', '', True, simulink_Parameter=simulink_Block(), simulink_Parameter20=simulink_Port()), '', '', '', False, simulink_Parameter=simulink_Block(), simulink_Parameter20=simulink_Port()) == None


from python_code import simulink_ModelReference
from python_code import simulink_SimulinkModel

def test_simulink_SimulinkModel___init__():
    assert simulink_SimulinkModel.__init__(simulink_SimulinkModel('', '', False, simulink_SimulinkModel=set(), simulink_SimulinkModel44=simulink_ModelReference()), '', '', True, simulink_SimulinkModel=set(), simulink_SimulinkModel44=simulink_ModelReference()) == None


from python_code import simulink_Block
from python_code import simulink_SubSystem

def test_simulink_SubSystem___init__():
    assert simulink_SubSystem.__init__(simulink_SubSystem('', parent41=set(), SubSystem=simulink_Block()), '', parent41=set(), SubSystem=simulink_Block()) == None


from python_code import simulink_Block
from python_code import simulink_Trigger

def test_simulink_Trigger___init__():
    assert simulink_Trigger.__init__(simulink_Trigger('', '\x00', simulink_Trigger=simulink_Block()), '\x00\x00', '', simulink_Trigger=simulink_Block()) == None

