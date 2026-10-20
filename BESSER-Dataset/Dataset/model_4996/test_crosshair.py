from python_code import ddsm_ChefResource

def test_ddsm_ChefResource___init__():
    assert ddsm_ChefResource.__init__(ddsm_ChefResource(''), '') == None


from python_code import ddsm_ClientNode

def test_ddsm_ClientNode___init__():
    assert ddsm_ClientNode.__init__(ddsm_ClientNode('', '', '\x00\x00'), '', '', '') == None


from python_code import ddsm_Port

def test_ddsm_Port___init__():
    assert ddsm_Port.__init__(ddsm_Port(False, '\x00'), False, '\x00') == None


from python_code import ddsm_ExecutionBinding
from python_code import ddsm_InternalComponent
from python_code import ddsm_RequiredExecutionPlatform

def test_ddsm_RequiredExecutionPlatform___init__():
    assert ddsm_RequiredExecutionPlatform.__init__(ddsm_RequiredExecutionPlatform(True, ddsm_RequiredExecutionPlatform24=ddsm_ExecutionBinding(), ddsm_RequiredExecutionPlatform=ddsm_InternalComponent()), False, ddsm_RequiredExecutionPlatform24=ddsm_ExecutionBinding(), ddsm_RequiredExecutionPlatform=ddsm_InternalComponent()) == None


from python_code import ddsm_InternalComponent
from python_code import ddsm_Relationship
from python_code import ddsm_RequiredPort

def test_ddsm_RequiredPort___init__():
    assert ddsm_RequiredPort.__init__(ddsm_RequiredPort(True, ddsm_RequiredPort22=ddsm_Relationship(), ddsm_RequiredPort=ddsm_InternalComponent()), False, ddsm_RequiredPort22=ddsm_Relationship(), ddsm_RequiredPort=ddsm_InternalComponent()) == None


from python_code import ddsm_StormCluster

def test_ddsm_StormCluster___init__():
    assert ddsm_StormCluster.__init__(ddsm_StormCluster(''), '') == None


from python_code import ddsm_StormNimbus

def test_ddsm_StormNimbus___init__():
    assert ddsm_StormNimbus.__init__(ddsm_StormNimbus('', '', '', '', '', ''), '', '', '', '', '\x00', '') == None


from python_code import ddsm_StormSupervisor

def test_ddsm_StormSupervisor___init__():
    assert ddsm_StormSupervisor.__init__(ddsm_StormSupervisor('\x00\x00', '', '', ''), '', '', '', '') == None


from python_code import ddsm_Cluster
from python_code import ddsm_VM

def test_ddsm_VM___init__():
    assert ddsm_VM.__init__(ddsm_VM('\x00', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '\x00', ddsm_VM=ddsm_Cluster()), '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ddsm_VM=ddsm_Cluster()) == None


from python_code import ddsm_Zookeeper

def test_ddsm_Zookeeper___init__():
    assert ddsm_Zookeeper.__init__(ddsm_Zookeeper('', '', '\x00\x00'), '', '', '') == None

