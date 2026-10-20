from python_code import cloudml_core_CloudMLElement

def test_cloudml_core_CloudMLElement___init__():
    assert cloudml_core_CloudMLElement.__init__(cloudml_core_CloudMLElement(''), '') == None


from python_code import cloudml_core_CloudMLElementWithProperties
from python_code import cloudml_core_DockerResource
from python_code import cloudml_core_Relationship

def test_cloudml_core_DockerResource___init__():
    assert cloudml_core_DockerResource.__init__(cloudml_core_DockerResource('', '\x00', Resource56=cloudml_core_Relationship(), Resource=cloudml_core_CloudMLElementWithProperties(), Resource53=cloudml_core_Relationship()), '\x00\x00', '', Resource56=cloudml_core_Relationship(), Resource=cloudml_core_CloudMLElementWithProperties(), Resource53=cloudml_core_Relationship()) == None


from python_code import Component
from python_code import Provider
from python_code import cloudml_core_CloudMLModel
from python_code import cloudml_core_ComponentInstance
from python_code import cloudml_core_ExecutionPlatform
from python_code import cloudml_core_ExternalComponent
from python_code import cloudml_core_Port

def test_cloudml_core_ExternalComponent___init__():
    assert cloudml_core_ExternalComponent.__init__(cloudml_core_ExternalComponent('', '', '', '', '', '', cloudml_core_ExternalComponent=Provider(), cloudml_core_ExternalComponent86=set(), Component91=cloudml_core_ExecutionPlatform(), Component45=cloudml_core_Port(False, 0, cloudml_core_Port=Component()), Component65=cloudml_core_ComponentInstance(), Component=cloudml_core_CloudMLModel()), '', '', '', '', '', '', cloudml_core_ExternalComponent=Provider(), cloudml_core_ExternalComponent86=set(), Component91=cloudml_core_ExecutionPlatform(), Component45=cloudml_core_Port(False, 0, cloudml_core_Port=Component()), Component65=cloudml_core_ComponentInstance(), Component=cloudml_core_CloudMLModel()) == None


from python_code import cloudml_core_CloudMLModel
from python_code import cloudml_core_ExecutionPlatformInstance
from python_code import cloudml_core_ExternalComponentInstance
from python_code import cloudml_core_PortInstance

def test_cloudml_core_ExternalComponentInstance___init__():
    assert cloudml_core_ExternalComponentInstance.__init__(cloudml_core_ExternalComponentInstance('', cloudml_core_ExternalComponentInstance=set(), ComponentInstance74=cloudml_core_PortInstance(), ComponentInstance=cloudml_core_CloudMLModel(), ComponentInstance93=cloudml_core_ExecutionPlatformInstance()), '', cloudml_core_ExternalComponentInstance=set(), ComponentInstance74=cloudml_core_PortInstance(), ComponentInstance=cloudml_core_CloudMLModel(), ComponentInstance93=cloudml_core_ExecutionPlatformInstance()) == None


from python_code import Component
from python_code import cloudml_core_Port

def test_cloudml_core_Port___init__():
    assert cloudml_core_Port.__init__(cloudml_core_Port(False, 0, cloudml_core_Port=Component()), False, 0, cloudml_core_Port=Component()) == None


from python_code import cloudml_core_Property

def test_cloudml_core_Property___init__():
    assert cloudml_core_Property.__init__(cloudml_core_Property(''), '') == None


from python_code import cloudml_core_Provider

def test_cloudml_core_Provider___init__():
    assert cloudml_core_Provider.__init__(cloudml_core_Provider('', '', '\x00\x00'), '', '', '') == None


from python_code import cloudml_core_CloudMLElementWithProperties
from python_code import cloudml_core_PuppetResource
from python_code import cloudml_core_Relationship

def test_cloudml_core_PuppetResource___init__():
    assert cloudml_core_PuppetResource.__init__(cloudml_core_PuppetResource('', '', '', '', '', '', '', Resource56=cloudml_core_Relationship(), Resource=cloudml_core_CloudMLElementWithProperties(), Resource53=cloudml_core_Relationship()), '', '\x00', '', '', '', '', '', Resource56=cloudml_core_Relationship(), Resource=cloudml_core_CloudMLElementWithProperties(), Resource53=cloudml_core_Relationship()) == None


from python_code import cloudml_core_PortInstance
from python_code import cloudml_core_RequiredPort

def test_cloudml_core_RequiredPort___init__():
    assert cloudml_core_RequiredPort.__init__(cloudml_core_RequiredPort(True, Port=cloudml_core_PortInstance()), False, Port=cloudml_core_PortInstance()) == None


from python_code import cloudml_core_Resource

def test_cloudml_core_Resource___init__():
    assert cloudml_core_Resource.__init__(cloudml_core_Resource('', '', '', '', '', '', False, False), '', '', '', '', '', '', False, False) == None


from python_code import cloudml_core_ResourcesPool

def test_cloudml_core_ResourcesPool___init__():
    assert cloudml_core_ResourcesPool.__init__(cloudml_core_ResourcesPool(0, 0, 0, '', cloudml_core_ResourcesPool=set(), cloudml_core_ResourcesPool108=set()), 0, 0, 0, '', cloudml_core_ResourcesPool=set(), cloudml_core_ResourcesPool108=set()) == None


from python_code import cloudml_core_CloudMLModel
from python_code import cloudml_core_VM

def test_cloudml_core_VM___init__():
    assert cloudml_core_VM.__init__(cloudml_core_VM(0, 0, 0, 0, 0, 0, '', False, '', '', '', '', '', '', cloudml_core_VM=set(), ExternalComponent=cloudml_core_CloudMLModel()), 0, 0, 0, 0, 0, 0, '', False, '', '\x00', '', '', '', '', cloudml_core_VM=set(), ExternalComponent=cloudml_core_CloudMLModel()) == None


from python_code import cloudml_core_CloudMLModel
from python_code import cloudml_core_VMInstance

def test_cloudml_core_VMInstance___init__():
    assert cloudml_core_VMInstance.__init__(cloudml_core_VMInstance('\x00\x00', '', cloudml_core_VMInstance=set(), ExternalComponentInstance=cloudml_core_CloudMLModel()), '', '', cloudml_core_VMInstance=set(), ExternalComponentInstance=cloudml_core_CloudMLModel()) == None

