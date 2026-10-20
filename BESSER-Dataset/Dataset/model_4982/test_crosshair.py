from python_code import cloudml_CloudMLElement

def test_cloudml_CloudMLElement___init__():
    assert cloudml_CloudMLElement.__init__(cloudml_CloudMLElement(''), '') == None


from python_code import cloudml_CloudMLModel
from python_code import cloudml_ExternalComponentInstance

def test_cloudml_ExternalComponentInstance___init__():
    assert cloudml_ExternalComponentInstance.__init__(cloudml_ExternalComponentInstance('', cloudml_ExternalComponentInstance97=set(), cloudml_ExternalComponentInstance=cloudml_CloudMLModel()), '', cloudml_ExternalComponentInstance97=set(), cloudml_ExternalComponentInstance=cloudml_CloudMLModel()) == None


from python_code import cloudml_Component
from python_code import cloudml_Port
from python_code import cloudml_PortInstance

def test_cloudml_Port___init__():
    assert cloudml_Port.__init__(cloudml_Port(False, 0, cloudml_Port=cloudml_Component(), cloudml_Port77=cloudml_PortInstance()), False, 0, cloudml_Port=cloudml_Component(), cloudml_Port77=cloudml_PortInstance()) == None


from python_code import cloudml_CloudMLElementWithProperties
from python_code import cloudml_Property
from python_code import cloudml_ProvidedExecutionPlatform
from python_code import cloudml_RequiredExecutionPlatform

def test_cloudml_Property___init__():
    assert cloudml_Property.__init__(cloudml_Property('', cloudml_Property=cloudml_CloudMLElementWithProperties(), cloudml_Property111=cloudml_RequiredExecutionPlatform(), cloudml_Property108=cloudml_ProvidedExecutionPlatform()), '', cloudml_Property=cloudml_CloudMLElementWithProperties(), cloudml_Property111=cloudml_RequiredExecutionPlatform(), cloudml_Property108=cloudml_ProvidedExecutionPlatform()) == None


from python_code import cloudml_CloudMLElementWithProperties
from python_code import cloudml_PuppetResource

def test_cloudml_PuppetResource___init__():
    assert cloudml_PuppetResource.__init__(cloudml_PuppetResource('', '', '', '', '', '', '', cloudml_PuppetResource=cloudml_CloudMLElementWithProperties()), '', '\x00', '', '', '', '', '', cloudml_PuppetResource=cloudml_CloudMLElementWithProperties()) == None


from python_code import cloudml_InternalComponent
from python_code import cloudml_Relationship
from python_code import cloudml_RequiredPort

def test_cloudml_RequiredPort___init__():
    assert cloudml_RequiredPort.__init__(cloudml_RequiredPort(True, cloudml_RequiredPort=cloudml_InternalComponent(), cloudml_RequiredPort47=cloudml_Relationship()), False, cloudml_RequiredPort=cloudml_InternalComponent(), cloudml_RequiredPort47=cloudml_Relationship()) == None


from python_code import cloudml_CloudMLElementWithProperties
from python_code import cloudml_Relationship
from python_code import cloudml_Resource

def test_cloudml_Resource___init__():
    assert cloudml_Resource.__init__(cloudml_Resource('', '', '', '', '', '', False, False, cloudml_Resource=cloudml_CloudMLElementWithProperties(), cloudml_Resource53=cloudml_Relationship(), cloudml_Resource56=cloudml_Relationship()), '', '', '', '', '', '', False, False, cloudml_Resource=cloudml_CloudMLElementWithProperties(), cloudml_Resource53=cloudml_Relationship(), cloudml_Resource56=cloudml_Relationship()) == None


from python_code import cloudml_CloudMLModel
from python_code import cloudml_VM

def test_cloudml_VM___init__():
    assert cloudml_VM.__init__(cloudml_VM(0, 0, 0, 0, 0, 0, '', False, '', '', '', '', '', '', cloudml_VM31=set(), cloudml_VM=cloudml_CloudMLModel()), 0, 0, 0, 0, 0, 0, '', False, '', '\x00', '', '', '', '', cloudml_VM31=set(), cloudml_VM=cloudml_CloudMLModel()) == None


from python_code import cloudml_Cloud
from python_code import cloudml_CloudMLModel
from python_code import cloudml_VMInstance

def test_cloudml_VMInstance___init__():
    assert cloudml_VMInstance.__init__(cloudml_VMInstance('\x00\x00', '', cloudml_VMInstance=cloudml_CloudMLModel(), cloudml_VMInstance59=cloudml_Cloud(), cloudml_VMInstance61=set()), '', '', cloudml_VMInstance=cloudml_CloudMLModel(), cloudml_VMInstance59=cloudml_Cloud(), cloudml_VMInstance61=set()) == None

