from python_code import co2_BooleanLiteral

def test_co2_BooleanLiteral___init__():
    assert co2_BooleanLiteral.__init__(co2_BooleanLiteral(''), '') == None


from python_code import co2_Comparison
from python_code import co2_Expression

def test_co2_Comparison___init__():
    assert co2_Comparison.__init__(co2_Comparison('', co2_Comparison=co2_Expression(), co2_Comparison156=co2_Expression()), '', co2_Comparison=co2_Expression(), co2_Comparison156=co2_Expression()) == None


from python_code import co2_Contract
from python_code import co2_ContractDefinition
from python_code import co2_ContractReference
from python_code import co2_ContractsAndProcessesDeclaration
from python_code import co2_Session
from python_code import co2_Tell

def test_co2_ContractDefinition___init__():
    assert co2_ContractDefinition.__init__(co2_ContractDefinition('', co2_ContractDefinition=co2_ContractsAndProcessesDeclaration(), co2_ContractDefinition44=co2_Tell(), co2_ContractDefinition129=co2_Session(), co2_ContractDefinition131=co2_Contract(), co2_ContractDefinition185=co2_ContractReference()), '', co2_ContractDefinition=co2_ContractsAndProcessesDeclaration(), co2_ContractDefinition44=co2_Tell(), co2_ContractDefinition129=co2_Session(), co2_ContractDefinition131=co2_Contract(), co2_ContractDefinition185=co2_ContractReference()) == None


from python_code import co2_EmptyContract

def test_co2_EmptyContract___init__():
    assert co2_EmptyContract.__init__(co2_EmptyContract(''), '') == None


from python_code import co2_EmptyProcess

def test_co2_EmptyProcess___init__():
    assert co2_EmptyProcess.__init__(co2_EmptyProcess(''), '') == None


from python_code import co2_Equals
from python_code import co2_Expression

def test_co2_Equals___init__():
    assert co2_Equals.__init__(co2_Equals('', co2_Equals=co2_Expression(), co2_Equals161=co2_Expression()), '', co2_Equals=co2_Expression(), co2_Equals161=co2_Expression()) == None


from python_code import co2_Import

def test_co2_Import___init__():
    assert co2_Import.__init__(co2_Import(''), '') == None


from python_code import co2_Expression
from python_code import co2_MultiOrDiv

def test_co2_MultiOrDiv___init__():
    assert co2_MultiOrDiv.__init__(co2_MultiOrDiv('', co2_MultiOrDiv=co2_Expression(), co2_MultiOrDiv176=co2_Expression()), '', co2_MultiOrDiv=co2_Expression(), co2_MultiOrDiv176=co2_Expression()) == None


from python_code import co2_NumberLiteral

def test_co2_NumberLiteral___init__():
    assert co2_NumberLiteral.__init__(co2_NumberLiteral(0), 0) == None


from python_code import co2_CO2System
from python_code import co2_PackageDeclaration

def test_co2_PackageDeclaration___init__():
    assert co2_PackageDeclaration.__init__(co2_PackageDeclaration(False, '\x00', co2_PackageDeclaration=co2_CO2System()), False, '\x00', co2_PackageDeclaration=co2_CO2System()) == None


from python_code import co2_ContractsAndProcessesDeclaration
from python_code import co2_HonestyDeclaration
from python_code import co2_ParallelProcesses
from python_code import co2_ProcessCall
from python_code import co2_ProcessDefinition

def test_co2_ProcessDefinition___init__():
    assert co2_ProcessDefinition.__init__(co2_ProcessDefinition(False, '\x00', co2_ProcessDefinition32=co2_ProcessCall(), co2_ProcessDefinition=co2_HonestyDeclaration(), co2_ProcessDefinition11=co2_ContractsAndProcessesDeclaration(), co2_ProcessDefinition13=set(), co2_ProcessDefinition15=co2_ParallelProcesses()), False, '', co2_ProcessDefinition32=co2_ProcessCall(), co2_ProcessDefinition=co2_HonestyDeclaration(), co2_ProcessDefinition11=co2_ContractsAndProcessesDeclaration(), co2_ProcessDefinition13=set(), co2_ProcessDefinition15=co2_ParallelProcesses()) == None


from python_code import co2_Receive
from python_code import co2_TimeoutProcess

def test_co2_Receive___init__():
    assert co2_Receive.__init__(co2_Receive(False, co2_Receive=set(), co2_Receive93=co2_TimeoutProcess()), False, co2_Receive=set(), co2_Receive93=co2_TimeoutProcess()) == None


from python_code import co2_StringLiteral

def test_co2_StringLiteral___init__():
    assert co2_StringLiteral.__init__(co2_StringLiteral(''), '') == None


from python_code import co2_Expression
from python_code import co2_Process
from python_code import co2_SwitchCase

def test_co2_SwitchCase___init__():
    assert co2_SwitchCase.__init__(co2_SwitchCase(False, co2_SwitchCase=co2_Expression(), co2_SwitchCase110=set(), co2_SwitchCase112=co2_Process()), False, co2_SwitchCase=co2_Expression(), co2_SwitchCase110=set(), co2_SwitchCase112=co2_Process()) == None


from python_code import co2_Process
from python_code import co2_Session
from python_code import co2_TellAndWait
from python_code import co2_TimeoutProcess

def test_co2_TellAndWait___init__():
    assert co2_TellAndWait.__init__(co2_TellAndWait(True, co2_TellAndWait73=co2_TimeoutProcess(), co2_TellAndWait=co2_Session(), co2_TellAndWait70=co2_Process()), False, co2_TellAndWait73=co2_TimeoutProcess(), co2_TellAndWait=co2_Session(), co2_TellAndWait70=co2_Process()) == None


from python_code import co2_Placeholder
from python_code import co2_Type
from python_code import co2_Variable

def test_co2_Type___init__():
    assert co2_Type.__init__(co2_Type('', co2_Type=co2_Placeholder(), co2_Type123=co2_Variable()), '', co2_Type=co2_Placeholder(), co2_Type123=co2_Variable()) == None

