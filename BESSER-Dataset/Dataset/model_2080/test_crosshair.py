from python_code import ddsm_Port

def test_ddsm_Port___init__():
    assert ddsm_Port.__init__(ddsm_Port(False, '\x00'), False, '\x00') == None


from python_code import ddsm_ExecutionBinding
from python_code import ddsm_InternalComponent
from python_code import ddsm_MasterSlavePlatform
from python_code import ddsm_PeerToPeerPlatform
from python_code import ddsm_RequiredExecutionPlatform

def test_ddsm_RequiredExecutionPlatform___init__():
    assert ddsm_RequiredExecutionPlatform.__init__(ddsm_RequiredExecutionPlatform(True, ddsm_RequiredExecutionPlatform=ddsm_InternalComponent(), ddsm_RequiredExecutionPlatform38=ddsm_ExecutionBinding(), ddsm_RequiredExecutionPlatform60=ddsm_PeerToPeerPlatform(), ddsm_RequiredExecutionPlatform62=ddsm_MasterSlavePlatform(), ddsm_RequiredExecutionPlatform65=ddsm_MasterSlavePlatform()), False, ddsm_RequiredExecutionPlatform=ddsm_InternalComponent(), ddsm_RequiredExecutionPlatform38=ddsm_ExecutionBinding(), ddsm_RequiredExecutionPlatform60=ddsm_PeerToPeerPlatform(), ddsm_RequiredExecutionPlatform62=ddsm_MasterSlavePlatform(), ddsm_RequiredExecutionPlatform65=ddsm_MasterSlavePlatform()) == None


from python_code import ddsm_InternalComponent
from python_code import ddsm_Relationship
from python_code import ddsm_RequiredPort

def test_ddsm_RequiredPort___init__():
    assert ddsm_RequiredPort.__init__(ddsm_RequiredPort(True, ddsm_RequiredPort=ddsm_InternalComponent(), ddsm_RequiredPort36=ddsm_Relationship()), False, ddsm_RequiredPort=ddsm_InternalComponent(), ddsm_RequiredPort36=ddsm_Relationship()) == None


from python_code import ddsm_SparkCluster

def test_ddsm_SparkCluster___init__():
    assert ddsm_SparkCluster.__init__(ddsm_SparkCluster(0, 0, 0, 0, 0), 0, 0, 0, 0, 0) == None


from python_code import ddsm_StormCluster

def test_ddsm_StormCluster___init__():
    assert ddsm_StormCluster.__init__(ddsm_StormCluster(0, 0, 0, 0, 0, 0, 0, 0, 0, 0), 0, 0, 0, 0, 0, 0, 0, 0, 0, 0) == None


from python_code import ddsm_VM

def test_ddsm_VM___init__():
    assert ddsm_VM.__init__(ddsm_VM('\x00', '', '', '', '', '', '', '', '', '', '', '', '', '', '', 0, 0), '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', 0, 0) == None


from python_code import ddsm_ZookeeperCluster

def test_ddsm_ZookeeperCluster___init__():
    assert ddsm_ZookeeperCluster.__init__(ddsm_ZookeeperCluster(0, 0, 0), 0, 0, 0) == None

